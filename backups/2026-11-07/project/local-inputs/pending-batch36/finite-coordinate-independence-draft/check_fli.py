from pathlib import Path
from collections import defaultdict
from fractions import Fraction as Q
import re, json, hashlib
repo=Path('/workspace/IntegratedMath-book')
d=Path('/tmp/finite-coordinate-independence-draft')
files=list((repo/'manuscript').rglob('*.md'))
for extra in (Path('/tmp/finite-coordinate-subspaces-draft/finite_coordinate_subspaces.md'),d/'finite_coordinate_independence.md',d/'finite_coordinate_independence_answers.md'):
    if not any(p.name==extra.name for p in files): files.append(extra)
anchors=defaultdict(list)
for p in files:
    for a in re.findall(r'\{#([^}]+)\}',p.read_text()): anchors[a].append(str(p))
new=[d/'finite_coordinate_independence.md',d/'finite_coordinate_independence_answers.md']
links=set()
for p in new:
    text=p.read_text()
    assert text.count('$$')%2==0
    links.update(re.findall(r'\]\(#([^)]+)\)',text))
errors={a:anchors[a] for a in sorted(links) if len(anchors[a])!=1}
assert not errors,errors
for k in range(1,9):
    assert len(anchors[f'fli-q{k:02}'])==len(anchors[f'fli-a{k:02}'])==1
assert (d/'figures/fli_redundancy.png').exists()
def c(a,v):return tuple(sum(x*w[j] for x,w in zip(a,v)) for j in range(2))
v=[(1,0),(3,2),(0,1)]
assert c((-6,2,-4),v)==(0,0)
assert tuple(Q(-1,2)*x for x in (-6,-4))==(3,2)
assert c((3,2),[v[0],v[2]])==v[1]
assert c((-3,1,-2),v)==(0,0)
assert c((-2,0,1),[(1,0),(0,1),(2,0)])==(0,0)
result={'status':'author finite checks passed; not independent proof validation','unique_internal_targets':len(links),'question_answer_pairs':8,'numerical_checks':['q5 null relation, nonzero inverse coefficient, reconstructed item, reverse relation','q8 null relation'],'files':{p.name:{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'lines':len(p.read_text().splitlines())} for p in new}}
(d/'author_checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
