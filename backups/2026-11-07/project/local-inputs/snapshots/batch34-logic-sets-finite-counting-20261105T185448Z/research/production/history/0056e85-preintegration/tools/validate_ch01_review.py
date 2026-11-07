"""Check scope, mathematical computations, links and rendered chapter artifacts."""
from pathlib import Path
import hashlib
import itertools
import json
import re
import subprocess
import fitz
from PIL import Image, ImageDraw
from sympy import symbols, expand, solveset, S, FiniteSet
from ch01_simulation import simulate
from review_artifacts import artifact_hashes, check_build_inputs

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'dist'
BUILD = ROOT / 'build/review_ch01'
SCREEN = BUILD / 'screenshots'
SCREEN.mkdir(exist_ok=True)
check_build_inputs()
for old in list(SCREEN.glob('page-*.png')) + list(BUILD.glob('contact-*.png')):
    old.unlink()
md = (OUT / '综合数学_第一章审阅版.md').read_text()
full = (OUT / '综合数学.md').read_text()
catalog = json.loads((ROOT / 'data/catalog_validation.json').read_text())
assert catalog['catalog_checks']['heading_counts'] == {'部分':63, '章':534, '节':6006}
assert len(re.findall(r'^## 第\d+部分 ', full, re.M)) == 63
assert len(re.findall(r'^### 第\d+章 ', full, re.M)) == 534
assert len(re.findall(r'^- 第\d+节 ', full, re.M)) == 6006
assert len(re.findall(r'^# 第\d+章 ', md, re.M)) == 1
assert '第1章 绪论：一般与综合专题（00Axx）' in md
sections = re.findall(r'^## 第(\d+)节 .+（([^）]+)）', md, re.M)
assert [int(n) for n, c in sections] == list(range(1,24))
taxonomy = json.loads((ROOT / 'data/msc_taxonomy.json').read_text())['entries']
expected = [e['code'] for e in taxonomy if e['parent_code'] == '00-XX' and e['level']=='general_leaf']
expected += [e['code'] for e in taxonomy if e['parent_code'] == '00Axx']
assert [c for n,c in sections] == expected
assert len(re.findall(r'\{#question-\d+\}',md)) == 14
assert len(re.findall(r'\{#answer-\d+\}',md)) == 14
assert md.count('[参考答案](#answer-') == 14
assert md.count('[返回题目](#question-') == 14
images = re.findall(r'!\[([^\]]*)\]\(([^)]+)\)',md)
assert len(images) == 4
assert all('原创' not in label and (OUT/path).is_file() for label,path in images)

# Independent exact symbolic computations supplement (not replace) written proofs.
x,a,b = symbols('x a b', real=True)
assert expand((a+b)**2-(a*a+2*a*b+b*b)) == 0
assert solveset(x*(x-1),x,domain=S.Reals) == FiniteSet(0,1)
assert solveset(x*(x-2),x,domain=S.Reals) == FiniteSet(0,2)
perms = list(itertools.permutations([1,2,3]))
assert [p for p in perms if p[0]<p[2]] == [(1,2,3),(1,3,2),(2,1,3)]
assert [p for p in perms if p[0]>p[2]] == [(2,3,1),(3,1,2),(3,2,1)]
assert [r['volume_litres'] for r in simulate(4)] == [5,7,9,11,13]
assert len(simulate(0)) == 1
for bad in [-1,1.5,True,'3']:
    try:
        simulate(bad)
        raise AssertionError('invalid simulation input accepted')
    except ValueError:
        pass

ast = json.loads(subprocess.check_output(['pandoc',str(OUT/'综合数学_第一章审阅版.md'),'-t','json']))
counts = {}
def walk(node):
    if isinstance(node,dict):
        if 't' in node: counts[node['t']] = counts.get(node['t'],0)+1
        for v in node.values():walk(v)
    elif isinstance(node,list):
        for v in node:walk(v)
walk(ast)
assert counts.get('Math',0)>100 and counts.get('Image') == 4
html = (OUT/'综合数学_第一章审阅版.html').read_text()
assert '<math' in html and '<script' not in html
assert html.count('data:image/png;base64,') == 4
logs='\n'.join(p.read_text() for p in BUILD.glob('*.log'))
missing=[line for line in logs.splitlines() if 'Missing character' in line]
assert not missing, missing

reports={}
for name in ['综合数学_第一章审阅版','综合数学','综合数学_完整数学目录']:
    path=OUT/(name+'.pdf')
    pdf=fitz.open(path)
    texts=[page.get_text() for page in pdf]
    assert 'Leo Lee' in '\n'.join(texts)
    assert not any('$$' in t or '\ufffd' in t for t in texts)
    overflow=[]
    for i,page in enumerate(pdf):
        for w in page.get_text('words'):
            if w[0]<8 or w[2]>page.rect.width-8 or w[1]<8 or w[3]>page.rect.height-8:
                overflow.append({'page':i+1,'text':w[4]})
    assert not overflow, (name,overflow)
    report={'pages':len(pdf),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'page_boundary_overflow':overflow}
    if name!='综合数学_完整数学目录':
        forward=[];back=[]
        for i,page in enumerate(pdf):
            for link in page.get_links():
                label=''.join(page.get_textbox(link['from']).split())
                if label not in ['参考答案','返回题目']:continue
                dest=link.get('page',-1)
                assert 0<=dest<len(pdf),(name,label,link)
                if label=='参考答案':
                    assert '返回题目' in texts[dest]
                    forward.append([i+1,dest+1])
                else:
                    assert '参考答案' in texts[dest]
                    back.append([i+1,dest+1])
        assert len(forward)==len(back)==14,(name,forward,back)
        report['question_answer_links']=len(forward)
        report['answer_question_links']=len(back)
    if name=='综合数学_第一章审阅版':
        # Render every review page for a contact-sheet review; select full pages separately.
        for i,page in enumerate(pdf):
            page.get_pixmap(matrix=fitz.Matrix(1.25,1.25)).save(SCREEN/f'page-{i+1:03}.png')
        report['all_pages_rendered']=True
        for start in range(0,len(pdf),12):
            sheet=Image.new('RGB',(1200,440*min(4,(len(pdf)-start+2)//3)),'#dfe6ec')
            for j in range(min(12,len(pdf)-start)):
                im=Image.open(SCREEN/f'page-{start+j+1:03}.png').convert('RGB')
                im.thumbnail((380,405))
                xx=(j%3)*400;yy=(j//3)*440
                sheet.paste(im,(xx+(400-im.width)//2,yy+5))
                ImageDraw.Draw(sheet).text((xx+12,yy+419),f'PDF page {start+j+1}',fill='black')
            sheet.save(BUILD/f'contact-{start+1:03}.png')
    reports[name]=report
report={'status':'automated_checks_passed','catalog_counts':{'parts':63,'chapters':534,'sections':6006},
        'current_chapters':1,'part_general_items':2,'chapter_sections':21,'exercises':14,'figures':4,
        'math_nodes':counts['Math'],'exact_computation_checks':'passed','missing_glyph_warnings':missing,
        'artifact_sha256':artifact_hashes(),
        'artifacts':reports,'visual_review':'pending_actual_image_inspection',
        'limits':'Automated checks and independent manuscript review do not constitute formal proof verification.'}
(ROOT/'data/ch01_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
