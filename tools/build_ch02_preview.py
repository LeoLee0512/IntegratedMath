"""Build and check the single G-level section separately from chapter 1 releases."""
from collections import Counter
from pathlib import Path
import hashlib
import json
import os
import re
import subprocess
import zipfile

import fitz
from manuscript_format import pandoc_headings

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / 'build/review_ch02'
OUT = ROOT / 'dist'
SOURCE = ROOT / 'manuscript/review_ch02/chapter.md'
STEM = '综合数学_第二章单节导读'


def assemble():
    source = SOURCE.read_text()
    plan = json.loads((ROOT / 'data/editorial_plan.json').read_text())
    entry = next(s for s in plan['sections'] if s['code'] == '00B05')
    assert entry['depth'] == 'G' and entry['status'] == '待作者审阅'
    assert len(plan['sections']) + plan['unlisted_sections']['count'] == 6006
    assert Counter(s['depth'] for s in plan['sections']) == {'T': 2, 'S': 13, 'G': 9}
    assert re.findall(r'^## 第(\d+)节 ', source, re.M) == ['24']
    titles = json.loads((ROOT / 'data/catalog_titles_zh.json').read_text())['entries']
    title = next(e['title_zh'] for e in titles if e['code'] == '00B05')
    assert f'第24节 {title}' in source
    body = pandoc_headings(source)
    excerpts = []
    for link in entry['prerequisite_sources']:
        path, anchor = link.split('#')
        original = (ROOT / path).read_text()
        assert original.count(f'<a id="{anchor}"></a>') == 1, link
        relative = os.path.relpath(ROOT / path, SOURCE.parent) + '#' + anchor
        assert '](' + relative + ')' in source, link
        body = body.replace('](' + relative + ')', '](#' + anchor + ')')
        headings = re.split(r'(?=^## )', pandoc_headings(original), flags=re.M)
        excerpts.append(next(h for h in headings if '{#' + anchor + '}' in h.split('\n')[0]))
    body += '\n\n# 先修摘录（原文回看，不计入本节篇幅）\n\n'
    body += '以下摘录来自本次源码中的第一部分开篇及第1章，保留原节号；均待作者审阅。\n\n'
    body += '\n\n'.join(excerpts)
    return '---\ntitle: 综合数学\nauthor: Leo Lee\nlang: zh-CN\n---\n\n' + body, entry


def main():
    BUILD.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(exist_ok=True)
    for old in BUILD.glob('page-*.png'):
        old.unlink()
    text, entry = assemble()
    md, pdf, html = [OUT / (STEM + suffix) for suffix in ['.md', '.pdf', '.html']]
    md.write_text(text)
    header = BUILD / 'header.tex'
    header.write_text((ROOT / 'tools/pdf_header.tex').read_text().replace('第一批工作稿', '第二章单节导读草稿'))
    with (BUILD / 'build.log').open('w') as log:
        subprocess.run(['pandoc', str(md), '--standalone', '--pdf-engine=xelatex',
                        '-V', 'mainfont=Noto Serif CJK SC', '-V', 'sansfont=Noto Sans CJK SC',
                        '-V', 'monofont=Noto Sans Mono CJK SC', '-V', 'geometry:margin=22mm',
                        '-V', 'fontsize=11pt', '-V', 'colorlinks=true',
                        '-H', str(header), '-o', str(pdf)], cwd=ROOT, stderr=log, check=True)
    subprocess.run(['pandoc', str(md), '--standalone', '--mathml', '--embed-resources',
                    '--css', str(ROOT / 'tools/style.css'), '-o', str(html)], check=True)
    rendered = html.read_text()
    ids = re.findall(r'\bid="([^"]+)"', rendered)
    assert len(ids) == len(set(ids)), 'Duplicate HTML anchors'
    assert 'Missing character' not in (BUILD / 'build.log').read_text()
    for link in entry['prerequisite_sources']:
        anchor = link.split('#')[1]
        assert f'href="#{anchor}"' in rendered and anchor in ids
    doc = fitz.open(pdf)
    page_texts = [page.get_text() for page in doc]
    assert 'Leo Lee' in ''.join(page_texts)
    assert not any('\ufffd' in t for t in page_texts)
    destinations = set()
    for index, page in enumerate(doc):
        for word in page.get_text('words'):
            assert word[0] >= 8 and word[2] <= page.rect.width - 8, (index + 1, word)
            assert word[1] >= 8 and word[3] <= page.rect.height - 8, (index + 1, word)
        for link in page.get_links():
            if link.get('page', -1) >= 0:
                target = link['page']
                assert 0 <= target < len(doc)
                destinations.add(target)
        page.get_pixmap(matrix=fitz.Matrix(1.1, 1.1)).save(BUILD / f'page-{index+1:02}.png')
    for title in ['第2节数学总论的研究性阐述', '第8节数学总论书目', '第9节外部书评']:
        assert any(title in ''.join(page_texts[p].split()) for p in destinations), title
    section_page = next(i for i, t in enumerate(page_texts) if '第24节讲座摘要汇编' in ''.join(t.split()))
    appendix_page = next(i for i, t in enumerate(page_texts) if '先修摘录' in t)
    report = {'status': 'automated_checks_passed', 'pages': len(doc),
              'section_page_range': [section_page + 1, appendix_page],
              'section_body_pages': appendix_page - section_page,
              'prerequisite_sources': entry['prerequisite_sources'],
              'visual_review': {'status': 'pending'},
              'artifact_sha256': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                                  for p in [md, pdf, html]}}
    report_path = BUILD / 'validation.json'
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    # Preview bundle is explicitly not a release or an author-approved manuscript.
    paths = [SOURCE, md, pdf, html, report_path, ROOT / 'data/editorial_plan.json',
             ROOT / 'tools/build_ch02_preview.py', ROOT / 'tools/pdf_header.tex',
             ROOT / 'tools/manuscript_format.py',
             ROOT / 'tools/style.css', ROOT / 'requirements-build.txt',
             ROOT / 'data/catalog_titles_zh.json',
             ROOT / 'research/ch02_review.md']
    paths += [ROOT / p.split('#')[0] for p in entry['prerequisite_sources']]
    paths += list(BUILD.glob('page-*.png'))
    with zipfile.ZipFile(OUT / (STEM + '_伴生文件.zip'), 'w', zipfile.ZIP_DEFLATED) as bundle:
        for path in sorted(set(paths)):
            bundle.write(path, Path('IntegratedMath') / path.relative_to(ROOT))
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
