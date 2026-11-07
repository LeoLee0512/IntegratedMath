#!/usr/bin/env python3
"""Build the complete first part in isolated directories, without changing older editions."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'dist/part1'
BUILD = ROOT / 'build/part1'
CATALOG = ROOT / 'dist/综合数学_完整数学目录.md'
FULL = '综合数学_第一部分完整目录版'
REVIEW = '综合数学_第一部分审阅版'
CAT = '综合数学_完整数学目录'
STEMS = (FULL, REVIEW, CAT)
PLAN = ROOT / 'research/production/part1_scope_plan.json'
ZIP = OUT / '综合数学_第一部分伴生文件.zip'
MANUSCRIPTS = [ROOT / 'manuscript' / directory / name for directory, name in [
    ('review_ch01', 'part_opening.md'), ('review_ch01', 'chapter.md'),
    ('review_ch02', 'chapter.md'), ('review_ch01', 'answers.md'),
    ('review_ch02', 'answers.md'), ('review_ch01', 'appendices.md')]]
METADATA = '---\ntitle: 综合数学\nauthor: Leo Lee\nlang: zh-CN\n---\n\n'


def hashes(paths):
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(set(paths))}


def image_sources():
    paths = []
    for manuscript in MANUSCRIPTS:
        if not manuscript.exists():
            continue
        for reference in re.findall(r'!\[[^\]]*\]\(([^)]+)\)', manuscript.read_text()):
            path = Path(reference)
            if path.is_absolute() or '..' in path.parts:
                raise ValueError('Image must have a safe relative path: ' + reference)
            candidates = [ROOT / path, ROOT / 'dist' / path, manuscript.parent / path]
            source = next((p for p in candidates if p.is_file()), None)
            if source is None:
                raise FileNotFoundError('Missing image: ' + reference)
            paths.append((reference, source))
    return paths


def source_hashes(plan_path=PLAN):
    names = ['tools/build_part1_review.py', 'tools/validate_part1_review.py',
             'tools/ch01_simulation.py', 'tools/draw_ch01_figures.py', 'tools/pdf_header.tex', 'tools/style.css',
             'data/msc_taxonomy.json', 'data/catalog_titles.json',
             'data/catalog_titles_zh.json']
    plan_inputs = []
    if plan_path.is_file():
        plan_inputs = [plan_path] + [ROOT / p for p in json.loads(plan_path.read_text())['source_files']]
    return hashes(MANUSCRIPTS + [CATALOG] + [ROOT / n for n in names]
                  + [p for _, p in image_sources()] + plan_inputs)


def artifact_hashes():
    return hashes(p for p in OUT.rglob('*') if p.is_file() and p != ZIP)


def protected_hashes():
    return hashes(p for p in (ROOT / 'dist').rglob('*')
                  if p.is_file() and not p.is_relative_to(OUT))


def check_dependencies():
    missing = [name for name in ('pandoc', 'xelatex') if not shutil.which(name)]
    missing += [name for name in ('fitz', 'PIL') if importlib.util.find_spec(name) is None]
    if missing:
        raise SystemExit('Missing local dependencies (nothing installed): ' + ', '.join(missing))
    return {name: subprocess.check_output([name, '--version'], text=True).splitlines()[0]
            for name in ('pandoc', 'xelatex')}


def compact_catalog(source):
    lines = []
    for line in source.splitlines():
        if line in ('**《综合数学》完整数学目录**', '**著作人：Leo Lee**'):
            continue
        if line.startswith('# 第') or line.startswith('## 第'):
            line = '#' + line
        elif line.startswith('### 第'):
            line = '- ' + line[4:]
        lines.append(line)
    return '# 全书目录：63部分、534章、6006节 {#full-catalog}\n\n' + '\n'.join(lines)


def answers_section(source, chapter):
    lines = source.strip().splitlines()
    if not lines or not lines[0].startswith('# '):
        raise ValueError('Answer source must start with one top-level heading')
    anchor = re.search(r'\{#([^}]+)\}', lines[0])
    identifier = anchor.group(1) if anchor else f'answers-ch{chapter:02}'
    if identifier == 'answers':
        identifier = 'answers-ch01'
    lines[0] = f'## 第{chapter}章参考答案 {{#{identifier}}}'
    for i in range(1, len(lines)):
        if re.match(r'^#{1,5} ', lines[i]):
            lines[i] = '#' + lines[i]
    return '\n'.join(lines)


def compose_body():
    texts = [p.read_text() for p in MANUSCRIPTS]
    body = '\n\n'.join(texts[:3])
    body += '\n\n# 第一部分课后题参考答案 {#answers}\n\n'
    body += '\n\n'.join(answers_section(texts[3+i], i+1) for i in range(2))
    body += '\n\n' + texts[5].rstrip()
    body += '\n\n```python\n' + (ROOT / 'tools/ch01_simulation.py').read_text().rstrip() + '\n```\n'
    return body


def check_build_inputs():
    manifest = json.loads((BUILD / 'manifest.json').read_text())
    if manifest['input_sha256'] != source_hashes(ROOT / manifest['scope_plan']):
        raise ValueError('Build inputs changed; rebuild before validating')
    if manifest['artifact_sha256'] != artifact_hashes():
        raise ValueError('Built outputs changed; rebuild before validating')
    if manifest['protected_sha256'] != protected_hashes():
        raise ValueError('An older dist artifact changed since this build started')
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-deps', action='store_true', help='check only; never install')
    parser.add_argument('--plan', type=Path, default=PLAN, help='scope-plan JSON included in build input hashes')
    args = parser.parse_args()
    plan_path = args.plan.resolve()
    if not plan_path.is_relative_to(ROOT):
        raise SystemExit('Scope plan must be inside the repository')
    versions = check_dependencies()
    if args.check_deps:
        print(json.dumps(versions, ensure_ascii=False, indent=2))
        return
    missing = [str(p.relative_to(ROOT)) for p in MANUSCRIPTS if not p.is_file()]
    if missing:
        raise SystemExit('Manuscripts not ready; no artifacts written: ' + ', '.join(missing))
    inputs = source_hashes(plan_path)
    protected = protected_hashes()
    body = compose_body()
    OUT.mkdir(parents=True, exist_ok=True)
    BUILD.mkdir(parents=True, exist_ok=True)
    # Invalidate previous automated acceptance before any output changes.
    (BUILD / 'validation.json').unlink(missing_ok=True)
    (BUILD / 'manifest.json').unlink(missing_ok=True)
    (BUILD / 'part1_build_review.json').unlink(missing_ok=True)
    ZIP.unlink(missing_ok=True)
    env = dict(os.environ, XDG_CACHE_HOME=str(BUILD / 'fontcache'))
    (BUILD / 'fontcache').mkdir(exist_ok=True)
    shutil.copy2(ROOT / 'tools/style.css', OUT / 'style.css')
    for reference, source in image_sources():
        destination = OUT / reference
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
    compact = compact_catalog(CATALOG.read_text())
    texts = {FULL: METADATA + compact + '\n\n' + body,
             REVIEW: METADATA + body, CAT: METADATA + CATALOG.read_text()}
    for name, text in texts.items():
        (OUT / (name + '.md')).write_text(text)
    (BUILD / 'catalog-print.md').write_text(METADATA + compact)
    header = (ROOT / 'tools/pdf_header.tex').read_text().replace('第一批工作稿', '第一部分审阅稿')
    header += '\n\\usepackage{float}\n\\floatplacement{figure}{H}\n\\postdisplaypenalty=10000\n'
    (BUILD / 'header.tex').write_text(header)
    (BUILD / 'catalog-header.tex').write_text(header.split('\\renewcommand{\\maketitle}', 1)[0])
    resources = f'--resource-path={OUT}:{ROOT}'
    common = ['pandoc', '--standalone', resources, '--pdf-engine=xelatex',
              '-V', 'mainfont=Noto Serif CJK SC', '-V', 'sansfont=Noto Sans CJK SC',
              '-V', 'monofont=Noto Sans Mono CJK SC', '-V', 'monofontoptions=AutoFakeSlant=0.15',
              '-V', 'geometry:margin=22mm', '-V', 'fontsize=11pt',
              '-V', 'colorlinks=true', '-V', 'linkcolor=blue']
    for name in STEMS:
        source = BUILD / 'catalog-print.md' if name == CAT else OUT / (name + '.md')
        args = common + [str(source), '-o', str(OUT / (name + '.pdf')), '-H',
                         str(BUILD / ('catalog-header.tex' if name == CAT else 'header.tex'))]
        if name != CAT:
            args += ['--toc', '--toc-depth=' + ('1' if name == FULL else '2')]
        print('Building PDF:', name, flush=True)
        with (BUILD / (name + '.pdf.log')).open('w') as log:
            subprocess.run(args, cwd=ROOT, env=env, check=True, stdout=log, stderr=log)
        args = ['pandoc', str(OUT / (name + '.md')), '--standalone', resources,
                '--mathml', '--embed-resources', '--css=' + str(OUT / 'style.css'),
                '-o', str(OUT / (name + '.html'))]
        if name != CAT:
            args += ['--toc', '--toc-depth=' + ('1' if name == FULL else '2')]
        with (BUILD / (name + '.html.log')).open('w') as log:
            subprocess.run(args, cwd=ROOT, env=env, check=True, stdout=log, stderr=log)
        html_path = OUT / (name + '.html')
        html_path.write_text('\n'.join(line.rstrip() for line in html_path.read_text().splitlines()) + '\n')
    if inputs != source_hashes(plan_path):
        raise SystemExit('Inputs changed during build; rerun against stable manuscripts')
    if protected != protected_hashes():
        raise SystemExit('Older dist artifacts changed during build; investigate before accepting')
    manifest = {'input_sha256': inputs, 'artifact_sha256': artifact_hashes(),
                'protected_sha256': protected, 'tool_versions': versions,
                'scope_plan': str(plan_path.relative_to(ROOT)),
                'python_version': sys.version, 'visual_review': 'pending_actual_image_inspection'}
    (BUILD / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    print('Built isolated first-part artifacts; run python tools/validate_part1_review.py')


if __name__ == '__main__':
    main()
