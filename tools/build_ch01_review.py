"""Build the author-requested first chapter, keeping the full MSC catalogue separate."""
from pathlib import Path
import json
import os
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'manuscript/review_ch01'
OUT = ROOT / 'dist'
BUILD = ROOT / 'build/review_ch01'


def run(args):
    subprocess.run(args, cwd=ROOT, check=True)


def compact_catalog(source):
    lines = []
    for line in source.splitlines():
        if line in ['**《综合数学》完整数学目录**', '**著作人：Leo Lee**']:
            continue
        if line.startswith('# 第'):
            line = '#' + line
        elif line.startswith('## 第'):
            line = '#' + line
        elif line.startswith('### 第'):
            line = '- ' + line[4:]
        lines.append(line)
    return '# 全书目录：63部分、534章、6006节\n\n' + '\n'.join(lines) + '\n\n'


def main():
    BUILD.mkdir(parents=True, exist_ok=True)
    os.environ['XDG_CACHE_HOME'] = str(BUILD / 'fontcache')
    (BUILD / 'fontcache').mkdir(exist_ok=True)
    (OUT / 'figures').mkdir(exist_ok=True)
    run(['python', 'tools/build_full_catalog.py'])
    run(['python', 'tools/draw_ch01_figures.py'])
    for p in (ROOT / 'figures').glob('ch01_*.png'):
        shutil.copy2(p, OUT / 'figures' / p.name)
    metadata = '---\ntitle: 综合数学\nauthor: Leo Lee\nlang: zh-CN\n---\n\n'
    notice = ('本稿供逐章审阅，正文仅包含第一部分开篇和第1章（00Axx）。'
              '全书仍以63部分、534章、6006节为编写范围；本次不写第2章。'
              '节号沿用完整目录：第1、2节直属部分，第3—23节属于第1章。\n\n')
    body = '\n\n'.join((SRC / n).read_text() for n in
                          ['part_opening.md', 'chapter.md', 'answers.md'])
    first_heading, remainder = body.split('\n', 1)
    body = first_heading + '\n\n' + notice + remainder
    body += '\n\n' + (SRC / 'appendices.md').read_text()
    body += '\n\n```python\n' + (ROOT / 'tools/ch01_simulation.py').read_text() + '```\n'
    catalog = compact_catalog((OUT / '综合数学_完整数学目录.md').read_text())
    main_text = metadata + catalog + body
    review_text = metadata + body
    (OUT / '综合数学.md').write_text(main_text)
    (OUT / '综合数学_第一章审阅版.md').write_text(review_text)
    (BUILD / 'catalog-print.md').write_text(metadata + catalog)
    header = (ROOT / 'tools/pdf_header.tex').read_text().replace('第一批工作稿', '第一章审阅稿')
    header += '\n\\usepackage{float}\n\\floatplacement{figure}{H}\n\\postdisplaypenalty=10000\n'
    (BUILD / 'header.tex').write_text(header)
    (BUILD / 'catalog-header.tex').write_text(header.split('\\renewcommand{\\maketitle}', 1)[0])
    common = ['pandoc', '--standalone', '--resource-path=.:dist',
              '--pdf-engine=xelatex', '-V', 'mainfont=Noto Serif CJK SC',
              '-V', 'sansfont=Noto Sans CJK SC', '-V', 'monofont=Noto Sans Mono CJK SC',
              '-V', 'monofontoptions=AutoFakeSlant=0.15', '-V', 'geometry:margin=22mm',
              '-V', 'fontsize=11pt', '-V', 'colorlinks=true', '-V', 'linkcolor=blue']
    jobs = [('综合数学', OUT / '综合数学.md', 1),
            ('综合数学_第一章审阅版', OUT / '综合数学_第一章审阅版.md', 2),
            ('综合数学_完整数学目录', BUILD / 'catalog-print.md', None)]
    for name, path, depth in jobs:
        args = common + [str(path), '-o', str(OUT / (name + '.pdf'))]
        args += ['-H', str(BUILD / ('header.tex' if depth else 'catalog-header.tex'))]
        if depth:
            args += ['--toc', '--toc-depth=' + str(depth)]
        with (BUILD / (name + '.log')).open('w') as log:
            subprocess.run(args, cwd=ROOT, check=True, stderr=log)
    run(['pandoc', str(OUT / '综合数学_第一章审阅版.md'), '--standalone', '--toc',
         '--toc-depth=2', '--resource-path=.:dist', '--mathml', '--embed-resources',
         '--css=dist/style.css', '-o', str(OUT / '综合数学_第一章审阅版.html')])
    # Replace the former main HTML too, so its chapter state is never stale.
    run(['pandoc', str(OUT / '综合数学.md'), '--standalone', '--toc', '--toc-depth=1',
         '--resource-path=.:dist', '--mathml', '--embed-resources', '--css=dist/style.css',
         '-o', str(OUT / '综合数学.html')])
    for html_name in ['综合数学.html', '综合数学_第一章审阅版.html']:
        html_path = OUT / html_name
        html_path.write_text('\n'.join(line.rstrip() if line.startswith('code span.') else line
                                       for line in html_path.read_text().splitlines()) + '\n')
    from ch01_simulation import simulate
    (ROOT / 'data/ch01_simulation.json').write_text(json.dumps(simulate(), indent=2)+'\n')


if __name__ == '__main__':
    main()
