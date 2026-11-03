"""Check the pilot's actual dependency destinations in Markdown, HTML and PDF."""
from collections import Counter
from html.parser import HTMLParser
import json
import re
import unicodedata
import fitz
from build_ch02_review import BUILD, OUT, ROOT, SOURCE, SOURCE_LINK, STEM, inputs
from review_artifacts import hashes

assert json.loads((BUILD / 'build_inputs.json').read_text()) == inputs(), 'Rebuild chapter 2 after source changes'
source = SOURCE.read_text()
dependencies = re.findall(r'\[先修：([^]]+)\]\(([^)]+)\)', source)
assert [code for code, path in dependencies] == ['00-02', '00A15', '00A17']
for code, target in dependencies:
    path, anchor = target.split('#')
    prerequisite = (SOURCE.parent / path).resolve().read_text()
    assert f'id="{anchor}"' in prerequisite, target  # GitHub source-page anchor
    assert '{#sec-' + code + '}' in prerequisite, target  # Pandoc destination
assert re.findall(r'^## 第(\d+)节 .+（([^）]+)）', source, re.M) == [('24', '00B05')]
taxonomy = json.loads((ROOT / 'data/msc_taxonomy.json').read_text())['entries']
children = [r['code'] for r in taxonomy if r['parent_code'] == '00Bxx']
assert children == ['00B05', '00B10', '00B15', '00B20', '00B25', '00B30', '00B50', '00B55', '00B60', '00B99']
plan = json.loads((ROOT / 'data/editorial_plan.json').read_text())
assert Counter(r['depth'] for r in plan['sections']) == {'T': 2, 'S': 13, 'G': 9}
assert len(plan['sections']) + len(plan['planned_sections']) + plan['unlisted_sections']['count'] == 6006
assert [r['code'] for r in plan['planned_sections']] == children[1:]


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = Counter()
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids[attrs['id']] += 1
        if tag == 'a' and 'href' in attrs:
            self.links.append(attrs['href'])


html = Links()
html.feed((OUT / (STEM + '.html')).read_text())
for code, target in dependencies:
    assert html.ids['sec-' + code] == 1
    assert SOURCE_LINK.sub(r'#\1', target) in html.links
assert all(html.ids[target[1:]] == 1 for target in html.links if target.startswith('#'))

pdf = fitz.open(OUT / (STEM + '.pdf'))
toc = pdf.get_toc(simple=False)
destinations = {code:next(row[3] for row in toc if f'（{code}）' in row[1])
                for code, target in dependencies}
texts = [p.get_text() for p in pdf]
start = next(row[2]-1 for row in toc if row[1].startswith('第2章 '))
end = next(i for i in range(start, len(pdf))
           if '而不必等文献分类全部读完' in ''.join(texts[i].split()))
assert start <= end <= next(row[2]-1 for row in toc if row[1].startswith('附录一 '))
checked = []
for index in range(start, end + 1):
    for link in pdf[index].get_links():
        label = unicodedata.normalize('NFKC', ''.join(pdf[index].get_textbox(link['from']).split()))
        label = label.replace('\u2010', '-').replace('\u2011', '-')
        found = re.search(r'先修:(\d\d(?:-\d\d|[A-Z]\d\d))', label)
        if not found:
            continue
        code = found.group(1)
        assert code in dict(dependencies), label
        expected = destinations[code]
        assert link['kind'] in [fitz.LINK_GOTO, fitz.LINK_NAMED]
        assert link['page'] == expected['page'] < start
        assert abs(link['to'].y - expected['to'].y) < 2, (label, link, expected)
        checked.append({'code':code, 'from_page':index+1, 'to_page':link['page']+1})
assert Counter(r['code'] for r in checked) == Counter(code for code, target in dependencies)
exercise_links = Counter()
for page in pdf:
    for link in page.get_links():
        label = ''.join(page.get_textbox(link['from']).split())
        if label not in ['参考答案', '返回题目']:
            continue
        target = link.get('page', -1)
        assert 0 <= target < len(pdf)
        assert ('返回题目' if label == '参考答案' else '参考答案') in texts[target]
        exercise_links[label] += 1
assert exercise_links == {'参考答案': 14, '返回题目': 14}
assert not any('Missing character' in line for line in (BUILD / 'build.log').read_text().splitlines())
for page in pdf:
    for x0,y0,x1,y1,word,*_ in page.get_text('words'):
        assert x0>=8 and y0>=8 and x1<=page.rect.width-8 and y1<=page.rect.height-8, word
screen = BUILD / 'screenshots'
screen.mkdir(exist_ok=True)
for old in screen.glob('page-*.png'):
    old.unlink()
pages = sorted({start, end, *(r['to_page']-1 for r in checked), *range(start,end+1)})
for index in pages:
    pdf[index].get_pixmap(matrix=fitz.Matrix(1.25,1.25)).save(screen / f'page-{index+1:03}.png')
report = {'status':'automated_checks_passed', 'pages':len(pdf),
          'chapter_02_pages':list(range(start+1,end+2)), 'chapter_02_written_sections':['00B05'],
          'chapter_02_unwritten_sections':children[1:], 'prerequisite_links':checked,
          'question_answer_links':exercise_links['参考答案'],
          'answer_question_links':exercise_links['返回题目'],
          'artifact_sha256':hashes([OUT/(STEM+ext) for ext in ['.md','.html','.pdf']]),
          'visual_review':'pending_actual_image_inspection',
          'limits':'Chapter 1 is included for offline cross-chapter navigation; the total PDF length is not the chapter-2 body length. Only section 24 is drafted.'}
(BUILD / 'validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
