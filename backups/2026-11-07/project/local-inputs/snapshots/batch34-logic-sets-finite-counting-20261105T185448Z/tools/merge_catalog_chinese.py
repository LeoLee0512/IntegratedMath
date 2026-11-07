"""Merge per-code reviewed translations; never fall back to untranslated headings."""
from pathlib import Path
from collections import Counter
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
CHUNKS = ROOT / 'research/catalog_zh_chunks'
SCOPE_ZH = dict(line.split('\t') for line in '''00	数学总论
01	数学史与人物传记
03	数理逻辑与数学基础
05	组合数学
06	有序结构
08	一般代数系统
11	数论
12	域论
13	交换代数
14	代数几何
15	线性代数
16	结合环与结合代数
17	非结合环与非结合代数
18	范畴论
19	$K$理论
20	群论
22	拓扑群
26	实函数
28	测度与积分
30	单复变函数
31	位势论
32	多复变函数与解析空间
33	特殊函数
34	常微分方程
35	偏微分方程
37	动力系统与遍历论
39	差分方程与函数方程
40	序列、级数与可和性
41	逼近与展开
42	欧氏空间上的调和分析
43	抽象调和分析
44	积分变换
45	积分方程
46	泛函分析
47	算子理论
49	变分法与最优控制
51	几何学
52	凸几何与离散几何
53	微分几何
54	一般拓扑学
55	代数拓扑学
57	流形与胞腔复形
58	整体分析
60	概率论
62	统计学
65	数值分析
68	计算机科学
70	质点与系统力学
74	可变形固体力学
76	流体力学
78	光学与电磁理论
80	经典热力学
81	量子理论
82	统计力学
83	相对论与引力理论
85	天文学与天体物理学
86	地球物理学
90	运筹学与数学规划
91	博弈论、经济学与金融
92	生物学
93	系统理论与控制理论
94	信息论与通信理论
97	数学教育'''.splitlines())

# Translate exact recurring phrases as a whole, preserving all qualifiers.
GENERAL = {
 '00': ('General reference works (handbooks, dictionaries, bibliographies, etc.) pertaining to ',
        '{scope}的一般参考工具（手册、词典、书目等）'),
 '01': ('Introductory exposition (textbooks, tutorial papers, etc.) pertaining to ',
        '{scope}的入门阐述（教材、教程性论文等）'),
 '02': ('Research exposition (monographs, survey articles) pertaining to ',
        '{scope}的研究性阐述（专著、综述文章）'),
 '03': ('History of ', '{scope}史'),
 '04': ('Software, source code, etc. for problems pertaining to ', '{scope}问题的软件、源代码等'),
 '05': ('Experimental work for problems pertaining to ', '{scope}问题的实验研究'),
 '06': ('Proceedings, conferences, collections, etc. pertaining to ', '{scope}的论文集、会议、文集等'),
 '08': ('Computational methods for problems pertaining to ', '{scope}问题的计算方法'),
 '10': ('Mathematical modeling or simulation for problems pertaining to ', '{scope}问题的数学建模或模拟'),
 '11': ('Research data for problems pertaining to ', '{scope}问题的研究数据'),
}
AGENTS = ['algebra_logic','msc_frontier','analysis','geometry_history','applications','sources_basic']


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    taxonomy = json.loads((ROOT/'data/msc_taxonomy.json').read_text())['entries']
    cache = json.loads((ROOT/'data/catalog_titles.json').read_text())
    english = {e['code']:e['title_markdown'] for e in cache['entries']}
    translations = {}; provenance = {}; files = {}
    root = {}
    for line in (CHUNKS/'root.tsv').read_text().splitlines():
        code,title = line.split('\t',1)
        assert code not in root
        root[code] = title
    (CHUNKS/'root.json').write_text(json.dumps(root,ensure_ascii=False,indent=2)+'\n')
    for group in ['root']+AGENTS:
        path=CHUNKS/(group+'.json')
        entries=json.loads(path.read_text())
        expected={e['code'] for e in taxonomy
                  if e['level'] in ['subject_leaf','intermediate'] and not e['code'].endswith('99')}
        assert set(entries)<=expected,group
        assert not (set(entries)&set(translations)),group
        translations.update(entries)
        provenance.update({code:group for code in entries})
        files[str(path.relative_to(ROOT))]=digest(path)
    # Each major class uses the already accepted Chinese domain name.
    for row in taxonomy:
        code=row['code']
        if row['level']=='major':
            translations[code]=row['title_zh'].replace('K理论','$K$理论')
            provenance[code]='existing_chinese_major_name'
        elif code.endswith('99'):
            assert english[code]=='None of the above, but in this section'
            translations[code]='本章中未列入以上各节的其他主题'
            provenance[code]='exact_recurring_phrase'
        elif row['level']=='general_leaf':
            prefix,template=GENERAL[code[-2:]]
            assert english[code].startswith(prefix),(code,english[code])
            scope_en=english[code][len(prefix):]
            scope_reference=english[code[:2]+'-01'].split('pertaining to ',1)[1]
            assert scope_en==scope_reference,(code,scope_en,scope_reference)
            translations[code]=template.format(scope=SCOPE_ZH[code[:2]])
            provenance[code]='verified_recurring_phrase_and_domain'
    assert set(translations)==set(english), sorted(set(english)-set(translations))
    for code,title in translations.items():
        assert isinstance(title,str) and re.search('[\u4e00-\u9fff]',title),code
        assert '\n' not in title and title.count('$')%2==0,code
        assert re.findall(r'\$[^$]+\$',english[code])==re.findall(r'\$[^$]+\$',title),(code,english[code],title)
    payload={
        'schema_version':1,
        'source_title_cache_sha256':digest(ROOT/'data/catalog_titles.json'),
        'source_pdf_sha256':cache['source_pdf_sha256'],
        'translation_scope':'All MSC heading names translated for this book; not an official Chinese MSC edition. Original code, hierarchy, qualifiers and mathematical notation retained. No source PDF or source prose redistributed.',
        'chapter_00Axx_display_title':'绪论：一般与综合专题',
        'translation_files_sha256':files,
        'entries':[{'code':row['code'],'level':row['level'],'parent_code':row['parent_code'],
                    'title_en':english[row['code']],'title_zh':translations[row['code']],
                    'translation_method':provenance[row['code']]} for row in taxonomy],
    }
    target=ROOT/'data/catalog_titles_zh.json'
    target.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'entries':len(translations),'methods':dict(Counter(provenance.values())),
                      'output':str(target)},ensure_ascii=False))


if __name__=='__main__':
    main()
