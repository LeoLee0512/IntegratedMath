"""Validate all translated headings, source identity, notation and selected qualifiers."""
from pathlib import Path
from collections import Counter
import hashlib
import json
import re
from manuscript_format import reader_title

ROOT=Path(__file__).resolve().parents[1]
# These are mathematical object/type names or variables, not English prose.
SYMBOLS={'BCK','BCI','o','GL','Tor','Ext','D','PROP','NK','Nil','T','I','A','DF','LB','LF','m','n'}
QUALIFIERS={r'nonlinear':r'非线性',r'noncommutative':r'非交换',r'nonassociative':r'非结合',
            r'nonselfadjoint':r'非自伴',r'nonarchimedean':r'非阿基米德',
            r'(?<![A-Za-z])finite-dimensional':r'有限维',r'infinite-dimensional':r'无穷维|无限维',r'cohomolog':r'上.?同调',
            r'homotopy':r'同伦',r'symplectic':r'辛',r'sheaf|sheaves':r'层'}
data=json.loads((ROOT/'data/catalog_titles_zh.json').read_text())
rows=data['entries']
assert len(rows)==len({r['code'] for r in rows})==6603
assert Counter(r['level'] for r in rows)=={'major':63,'intermediate':534,'general_leaf':503,'subject_leaf':5503}
original={r['code']:r['title_markdown'] for r in json.loads((ROOT/'data/catalog_titles.json').read_text())['entries']}
assert data['source_title_cache_sha256']==hashlib.sha256((ROOT/'data/catalog_titles.json').read_bytes()).hexdigest()
notation=[]; qualifier_count=0
for row in rows:
    code=row['code'];en=row['title_en'];zh=row['title_zh']
    assert en==original[code]
    assert re.search('[\u4e00-\u9fff]',zh),code
    assert re.findall(r'\$[^$]+\$',en)==re.findall(r'\$[^$]+\$',zh),code
    prose=re.sub(r'\$[^$]+\$','',zh)
    prose=re.sub(r'\d{2}(?:[A-Z](?:xx|\d{2})|-XX)','',prose)
    tokens=set(re.findall('[A-Za-z]+',prose))
    assert tokens<=SYMBOLS,(code,tokens-SYMBOLS,zh)
    if tokens:notation.append({'code':code,'mathematical_labels':sorted(tokens)})
    for term,pattern in QUALIFIERS.items():
        if re.search(term,en,re.I):
            qualifier_count+=1
            assert re.search(pattern,zh),(code,term,zh)
catalog=(ROOT/'dist/综合数学_完整数学目录.md').read_text()
headings=re.findall(r'^(#{1,3}) 第(\d+)(部分|章|节) (.+)$',catalog,re.M)
assert len(headings)==6603
lookup={row['code']:row for row in rows}
title_lookup={row['code']:row['title_zh'] for row in rows}
taxonomy=json.loads((ROOT/'data/msc_taxonomy.json').read_text())['entries']
assert len(taxonomy)==len(headings)
for (level,num,kind,title), record in zip(headings,taxonomy):
    code=record['code']
    expected='绪论：一般与综合专题' if code=='00Axx' else reader_title(lookup[code]['title_zh'], title_lookup)
    assert title==expected,(code,title,expected)
assert Counter(h[2] for h in headings)=={'部分':63,'章':534,'节':6006}
report={'status':'passed','translated_heading_count':6603,'parts':63,'chapters':534,'sections':6006,
        'all_source_codes_and_hierarchy_preserved':True,'all_original_math_fragments_preserved':True,
        'untranslated_english_prose_titles':0,'retained_mathematical_labels':notation,
        'selected_qualifier_checks':qualifier_count,
        'translation_sha256':hashlib.sha256((ROOT/'data/catalog_titles_zh.json').read_bytes()).hexdigest(),
        'limits':'Every heading has a per-code translation. Code/formula checks are exhaustive; independent semantic second review is sampled. Chinese terminology is this book\'s translation, not an official Chinese MSC edition.'}
(ROOT/'data/catalog_chinese_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='retained_mathematical_labels'},ensure_ascii=False,indent=2))
