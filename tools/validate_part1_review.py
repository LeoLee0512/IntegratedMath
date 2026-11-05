#!/usr/bin/env python3
"""Validate current first-part artifacts and render every review PDF page for inspection."""
from __future__ import annotations

from collections import Counter
import argparse
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import json
import re
import shlex
import subprocess
import zipfile

import fitz
from PIL import Image, ImageDraw

from build_part1_review import (ROOT, OUT, BUILD, FULL, REVIEW, CAT, STEMS, PLAN, ZIP,
                               hashes, check_build_inputs, check_dependencies)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def nodes(node, kind):
    if isinstance(node, dict):
        if node.get('t') == kind:
            yield node
        for value in node.values():
            yield from nodes(value, kind)
    elif isinstance(node, list):
        for value in node:
            yield from nodes(value, kind)


class OfflineHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.images = 0
        self.math = 0
        self.remote_resources = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'a' and attrs.get('href', '').startswith('#'):
            self.links.append(attrs['href'][1:])
        if tag == 'math':
            self.math += 1
        if tag == 'img':
            self.images += 1
            require(attrs.get('src', '').startswith('data:image/'), 'HTML image is not embedded')
        if tag in ('script', 'iframe'):
            self.remote_resources.append((tag, attrs))
        if tag in ('img', 'source', 'video', 'audio', 'link'):
            resource = attrs.get('src', attrs.get('href', ''))
            if resource and not resource.startswith(('data:', '#')):
                self.remote_resources.append((tag, resource))


def check_catalog():
    text = (OUT / (CAT + '.md')).read_text()
    headings = re.findall(r'^(#{1,3}) 第(\d+)(部分|章|节) (.+)（(?:MSC )?([0-9A-Zx-]+)）$', text, re.M)
    require(Counter(h[2] for h in headings) == {'部分': 63, '章': 534, '节': 6006},
            'Full Chinese catalog counts differ')
    taxonomy = json.loads((ROOT / 'data/msc_taxonomy.json').read_text())['entries']
    titles = {r['code']: r for r in json.loads((ROOT / 'data/catalog_titles_zh.json').read_text())['entries']}
    require([h[4] for h in headings] == [r['code'] for r in taxonomy], 'Catalog order/codes changed')
    part = chapter = None
    for (level, number, kind, title, code), entry in zip(headings, taxonomy):
        expected_title = '绪论：一般与综合专题' if code == '00Axx' else titles[code]['title_zh']
        require(title == expected_title and re.search('[\u4e00-\u9fff]', title), 'Wrong Chinese title: ' + code)
        if kind == '部分':
            part, chapter = code, None
        elif kind == '章':
            require(entry['parent_code'] == part, 'Wrong catalog chapter parent: ' + code)
            chapter = code
        else:
            expected_parent = part if entry['level'] == 'general_leaf' else chapter
            require(entry['parent_code'] == expected_parent, 'Wrong catalog section parent: ' + code)
    return taxonomy


def check_scope(md, taxonomy):
    sections = re.findall(r'^## 第(\d+)节 .+（([^）]+)）', md, re.M)
    expected = [r['code'] for r in taxonomy if r['level'] in ('general_leaf', 'subject_leaf')
                and r['parent_code'] in ('00-XX', '00Axx', '00Bxx')]
    require([int(n) for n, _ in sections] == list(range(1, 34)), 'Expected sections 1 through 33')
    require([code for _, code in sections] == expected, 'First-part classification codes changed')
    chapter = None
    lookup = {r['code']: r for r in taxonomy}
    for line in md.splitlines():
        match = re.match(r'^# 第(\d+)章 .+（([^）]+)）', line)
        if match:
            chapter = match[2]
        match = re.match(r'^## 第\d+节 .+（([^）]+)）', line)
        if match:
            entry = lookup[match[1]]
            require(entry['parent_code'] == (chapter or '00-XX'), 'Section moved between original parents')
    require(len(re.findall(r'^# 第\d+章 ', md, re.M)) == 2, 'Expected exactly two chapters')
    require(md.index('# 第2章 ') < md.index('# 第一部分课后题参考答案 '), 'Answers must follow both chapters')
    require(not re.search(r'第2章正文仍待编写|本次不写第2章|正文仅包含.*第1章', md), 'Stale chapter-one scope notice')


def main():
    arguments = argparse.ArgumentParser(description=__doc__)
    arguments.add_argument('--package', action='store_true', help='create verified ZIP and acceptance build record')
    args = arguments.parse_args()
    check_dependencies()
    manifest = check_build_inputs()
    (BUILD / 'validation.json').unlink(missing_ok=True)
    (BUILD / 'part1_build_review.json').unlink(missing_ok=True)
    taxonomy = check_catalog()
    md = (OUT / (REVIEW + '.md')).read_text()
    check_scope(md, taxonomy)
    full = (OUT / (FULL + '.md')).read_text()
    require(len(re.findall(r'^## 第\d+部分 ', full, re.M)) == 63, 'Full version lacks catalog parts')
    require(len(re.findall(r'^### 第\d+章 ', full, re.M)) == 534, 'Full version lacks catalog chapters')
    require(len(re.findall(r'^- 第\d+节 ', full, re.M)) == 6006, 'Full version lacks catalog sections')
    ast = json.loads(subprocess.check_output(['pandoc', str(OUT / (REVIEW + '.md')), '-t', 'json']))
    anchors = re.findall(r'\{#([^}\s]+)\}', md)
    require(len(anchors) == len(set(anchors)), 'Duplicate manuscript anchor')
    links = list(nodes(ast, 'Link'))
    fragments = [n['c'][2][0][1:] for n in links if n['c'][2][0].startswith('#')]
    require(set(fragments) <= set(anchors), 'Broken manuscript fragment: ' + str(set(fragments) - set(anchors)))
    questions = {a for a in anchors if re.search(r'(?:^|-)question-', a)}
    answers = {a for a in anchors if re.search(r'(?:^|-)answer-', a)}
    require(len(questions) == len(answers) and len(questions) > 14, 'Missing chapter-two questions/answers')
    require({q.replace('question-', 'answer-') for q in questions} == answers, 'Question/answer identifiers differ')
    require(all(fragments.count(a) == 1 for a in answers), 'Every answer requires one question link')
    require(all(fragments.count(q) == 1 for q in questions), 'Every question requires one return link')
    for identifier in questions | answers:
        suffix = md.split('{#' + identifier + '}', 1)[1]
        destination = re.search(r'\[(参考答案|返回题目)\]\(#([^)]*)\)', suffix)
        counterpart = (identifier.replace('question-', 'answer-') if identifier in questions
                       else identifier.replace('answer-', 'question-'))
        require(destination is not None and destination[2] == counterpart,
                'Question/answer points to the wrong counterpart: ' + identifier)
    answer_start = md.index('# 第一部分课后题参考答案 ')
    require(all(md.index('{#' + q + '}') < answer_start for q in questions), 'Question found in answer appendix')
    require(all(md.index('{#' + a + '}') > answer_start for a in answers), 'Answer found before separate appendix')
    images = list(nodes(ast, 'Image'))
    require(len(images) >= 4, 'Expected the four chapter-one illustrations')
    for image in images:
        require((OUT / image['c'][2][0]).is_file(), 'Missing output illustration')
    math_count = len(list(nodes(ast, 'Math')))
    require(math_count > 100, 'Mathematical content was not parsed as math')
    html_reports = {}
    for name in STEMS:
        html = (OUT / (name + '.html')).read_text()
        parser = OfflineHTML()
        parser.feed(html)
        require(len(parser.ids) == len(set(parser.ids)), name + ': duplicate HTML IDs')
        require(set(parser.links) <= set(parser.ids), name + ': broken HTML fragments')
        require(not parser.remote_resources, name + ': HTML requires nonembedded runtime resources')
        require(not re.search(r'@import|url\(\s*[\"\']?https?://', html), name + ': remote CSS resource')
        if name != CAT:
            require(parser.math == math_count if name == REVIEW else parser.math >= math_count,
                    name + ': missing MathML')
            require(parser.images == len(images), name + ': missing embedded illustrations')
        html_reports[name] = {'mathml_elements': parser.math, 'embedded_images': parser.images,
                              'offline_runtime_resources': True, 'fragment_links_valid': True}
    warnings = [line for p in BUILD.glob('*.log') for line in p.read_text().splitlines()
                if any(token in line for token in ('Missing character', 'Could not convert TeX math',
                                                   'Could not fetch resource', 'Undefined control sequence'))]
    require(not warnings, 'Rendering warnings: ' + str(warnings))
    rendered = []
    contact_index = []
    pdf_reports = {}
    for name in STEMS:
        screen = BUILD / 'screenshots' / name
        contact = BUILD / 'contacts' / name
        screen.mkdir(parents=True, exist_ok=True)
        contact.mkdir(parents=True, exist_ok=True)
        for old in list(screen.glob('page-*.png')) + list(contact.glob('contact-*.png')):
            old.unlink()
        with fitz.open(OUT / (name + '.pdf')) as pdf:
            texts = [page.get_text() for page in pdf]
            require('Leo Lee' in '\n'.join(texts), name + ': missing author')
            require(not any('$$' in t or '\ufffd' in t for t in texts), name + ': unrendered/invalid text')
            overflow = []
            forwards, backwards = [], []
            for i, page in enumerate(pdf):
                for word in page.get_text('words'):
                    if word[0] < 8 or word[2] > page.rect.width - 8 or word[1] < 8 or word[3] > page.rect.height - 8:
                        overflow.append({'page': i+1, 'text': word[4]})
                if name != CAT:
                    for link in page.get_links():
                        label = ''.join(page.get_textbox(link['from']).split())
                        if label not in ('参考答案', '返回题目'):
                            continue
                        destination = link.get('page', -1)
                        require(0 <= destination < len(pdf), name + ': invalid PDF answer destination')
                        opposite = '返回题目' if label == '参考答案' else '参考答案'
                        require(opposite in texts[destination], name + ': wrong PDF question/answer destination')
                        (forwards if label == '参考答案' else backwards).append([i+1, destination+1])
                page.get_pixmap(matrix=fitz.Matrix(1.25, 1.25)).save(screen / f'page-{i+1:03}.png')
            require(not overflow, name + ': text outside page bounds: ' + str(overflow))
            if name != CAT:
                require(len(forwards) == len(backwards) == len(questions), name + ': wrong PDF exercise-link count')
            pdf_reports[name] = {'pages': len(pdf), 'page_boundary_overflow': overflow,
                                 'question_answer_links': forwards, 'answer_question_links': backwards,
                                 'embedded_image_count': sum(len(p.get_images()) for p in pdf)}
            if name == REVIEW:
                require(pdf_reports[name]['embedded_image_count'] >= len(images), 'PDF illustrations missing')
            for start in range(0, len(pdf), 12):
                count = min(12, len(pdf)-start)
                sheet = Image.new('RGB', (1200, 440*((count+2)//3)), '#dfe6ec')
                for j in range(count):
                    with Image.open(screen / f'page-{start+j+1:03}.png') as source:
                        im = source.convert('RGB')
                    im.thumbnail((380, 405))
                    x, y = j % 3 * 400, j // 3 * 440
                    sheet.paste(im, (x+(400-im.width)//2, y+5))
                    ImageDraw.Draw(sheet).text((x+12, y+419), f'PDF page {start+j+1}', fill='black')
                destination = contact / f'contact-{start+1:03}.png'
                sheet.save(destination)
                contact_index.append({'pdf': str((OUT / (name + '.pdf')).relative_to(ROOT)),
                                      'pages': list(range(start+1, start+count+1)),
                                      'path': str(destination.relative_to(ROOT)),
                                      'sha256': hashlib.sha256(destination.read_bytes()).hexdigest(),
                                      'inspected': False})
            rendered += list(screen.glob('page-*.png')) + list(contact.glob('contact-*.png'))
            pdf_reports[name]['all_pages_rendered'] = True
    check_build_inputs()
    report = {'status': 'automated_checks_passed', 'scope': {'parts': 1, 'chapters': 2, 'sections': 33},
              'catalog_counts': {'parts': 63, 'chapters': 534, 'sections': 6006},
              'exercises': len(questions), 'figures': len(images), 'math_nodes': math_count,
              'input_sha256': manifest['input_sha256'], 'artifact_sha256': manifest['artifact_sha256'],
              'protected_outputs_unchanged': True, 'rendered_sha256': hashes(rendered),
              'contact_index': contact_index,
              'pdfs': pdf_reports, 'html': html_reports, 'render_warnings': warnings,
              'visual_review': 'pending_actual_image_inspection',
              'limits': 'Automated structural checks do not establish mathematical correctness or visual acceptance.'}
    (BUILD / 'validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    if args.package:
        create_package(manifest, report, rendered)
    print(json.dumps({'status': report['status'], 'exercises': len(questions), 'math_nodes': math_count,
                      'pdf_pages': {n: r['pages'] for n, r in pdf_reports.items()},
                      'all_review_pages_rendered': True, 'visual_review': report['visual_review'],
                      'report': str(BUILD / 'validation.json')}, ensure_ascii=False, indent=2))


def create_package(manifest, report, rendered):
    plan_path = ROOT / manifest['scope_plan']
    require(plan_path.is_file(), 'Scope plan is required for an acceptance build record')
    plan = json.loads(plan_path.read_text())
    source_sha256 = hashes(ROOT / p for p in plan['source_files'])
    require(set(source_sha256) <= set(manifest['input_sha256']), 'Rebuild with all scope-plan sources')
    evidence = [BUILD / 'validation.json', BUILD / 'manifest.json']
    # Independent written reviews are available before visual acceptance; never bundle a stale acceptance.
    reviews = [p for p in (ROOT / 'research/production').glob('part1_*')
               if p.is_file() and not any(word in p.name for word in ('build_review', 'visual_review', 'acceptance.json'))]
    files = [ROOT / p for p in manifest['input_sha256']]
    files += [ROOT / p for p in manifest['artifact_sha256']] + evidence + rendered + reviews
    members = hashes(files)
    with zipfile.ZipFile(ZIP, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for path in sorted(members):
            archive.write(ROOT / path, path)
        archive.writestr('PACKAGE_SHA256.json', json.dumps(members, ensure_ascii=False, indent=2) + '\n')
    with zipfile.ZipFile(ZIP) as archive:
        require(archive.testzip() is None, 'ZIP CRC validation failed')
        for path, digest in members.items():
            require(hashlib.sha256(archive.read(path)).hexdigest() == digest, 'ZIP member changed: ' + path)
    artifact_sha256 = dict(manifest['artifact_sha256'], **hashes([ZIP]))
    build_review = {'schema_version': 1, 'target_type': 'part', 'target_id': '00-XX', 'scope': 'complete_part',
                    'status': 'automated_checks_passed',
                    'command': shlex.join(['python', 'tools/build_part1_review.py', '--plan', manifest['scope_plan']])
                               + ' && python tools/validate_part1_review.py --package',
                    'built_at': datetime.now(timezone.utc).isoformat(),
                    'plan_sha256': hashlib.sha256(plan_path.read_bytes()).hexdigest(),
                    'source_sha256': source_sha256, 'build_input_sha256': manifest['input_sha256'],
                    'section_codes': [s['code'] for s in plan['sections']], 'blocking_issues': [],
                    'artifact_sha256': artifact_sha256,
                    'pdf_page_counts': {str((OUT / (name+'.pdf')).relative_to(ROOT)): item['pages']
                                        for name, item in report['pdfs'].items()},
                    'checks': {key: True for key in ('scope_33_sections', 'formula_rendering', 'images',
                               'cross_references', 'exercise_answer_pairs', 'offline_html', 'source_bundle', 'page_boundaries')},
                    'evidence': [{'path': p, 'sha256': digest} for p, digest in hashes(evidence).items()]}
    check_build_inputs()
    (BUILD / 'part1_build_review.json').write_text(json.dumps(build_review, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    main()
