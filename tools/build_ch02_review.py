"""Build the chapter-2 pilot with chapter 1 included for working prerequisite links."""
from pathlib import Path
import json
import os
import re
import subprocess
from review_artifacts import check_build_inputs, hashes, source_hashes

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / 'build/review_ch02'
OUT = ROOT / 'dist'
STEM = '综合数学_第二章起步审阅版'
SOURCE = ROOT / 'manuscript/review_ch02/chapter.md'
SOURCE_LINK = re.compile(r'\.\./review_ch01/(?:part_opening|chapter)\.md#source-(sec-[\w-]+)')


def inputs():
    return {**source_hashes(), **hashes([SOURCE, Path(__file__), OUT / '综合数学_第一章审阅版.md'])}


def main():
    check_build_inputs()
    BUILD.mkdir(parents=True, exist_ok=True)
    os.environ['XDG_CACHE_HOME'] = str(BUILD / 'fontcache')
    body = SOURCE_LINK.sub(r'#\1', SOURCE.read_text())
    assert '../review_ch01/' not in body
    prior = (OUT / '综合数学_第一章审阅版.md').read_text()
    marker = '# 附录一 本章课后题参考答案'
    assert prior.count(marker) == 1
    combined = prior.replace(marker, body + '\n\n' + marker, 1)
    combined = combined.replace('正文仅包含第一部分开篇和第1章（00Axx）',
                                '包含第一部分开篇、第1章及第2章起步草稿', 1)
    combined = combined.replace('第2章起步草稿另供审阅。',
                                '第2章仅写第24节，其余九节待写。第1章保留在本稿中供先修回查，文件总页数不是第2章正文页数。', 1)
    combined = combined.replace('其起步导读另供审阅。', '本稿收录其起步导读。', 1)
    md = OUT / (STEM + '.md')
    md.write_text(combined)
    header = (ROOT / 'build/review_ch01/header.tex').read_text().replace('第一章审阅稿', '第二章起步审阅稿')
    (BUILD / 'header.tex').write_text(header)
    command = ['pandoc', str(md), '--standalone', '--toc', '--toc-depth=2',
               '--resource-path=.:dist', '--pdf-engine=xelatex', '-H', str(BUILD / 'header.tex'),
               '-V', 'mainfont=Noto Serif CJK SC', '-V', 'sansfont=Noto Sans CJK SC',
               '-V', 'monofont=Noto Sans Mono CJK SC', '-V', 'monofontoptions=AutoFakeSlant=0.15',
               '-V', 'geometry:margin=22mm', '-V', 'fontsize=11pt',
               '-V', 'colorlinks=true', '-V', 'linkcolor=blue', '-o', str(OUT / (STEM + '.pdf'))]
    with (BUILD / 'build.log').open('w') as log:
        subprocess.run(command, cwd=ROOT, stderr=log, check=True)
    subprocess.run(['pandoc', str(md), '--standalone', '--toc', '--toc-depth=2',
                    '--resource-path=.:dist', '--mathml', '--embed-resources',
                    '--css=dist/style.css', '-o', str(OUT / (STEM + '.html'))], cwd=ROOT, check=True)
    (BUILD / 'build_inputs.json').write_text(json.dumps(inputs(), ensure_ascii=False, indent=2)+'\n')


if __name__ == '__main__':
    main()
