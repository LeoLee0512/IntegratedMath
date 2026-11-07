"""Exhaustive small finite-table checks, not a proof about infinite functions."""
from pathlib import Path
from itertools import product, combinations
import datetime, hashlib, json
from finite_functions import FiniteFunction, identity, restrict, compose

ROOT=Path(__file__).resolve().parents[1]


def subsets(a):
    return [frozenset(c) for n in range(len(a)+1) for c in combinations(sorted(a), n)]


def rejects(fn, *args):
    try:
        fn(*args)
    except ValueError:
        return
    raise AssertionError((fn, args))


def encode(f):
    return dict(domain=sorted(f.domain), codomain=sorted(f.codomain), graph=sorted(f.graph))


def main():
    sets=[frozenset(),frozenset({0}),frozenset({0,1})]
    fs=[]
    for a,b in product(sets,repeat=2):
        for outputs in product(sorted(b), repeat=len(a)):
            fs.append(FiniteFunction(a,b,list(zip(sorted(a),outputs))))
    counts=dict(functions=len(fs), evaluations=0, equality_pairs=0, restrictions=0,
                nested_restrictions=0, identity_laws=0, compositions=0,
                mismatched_compositions=0, associative_triples=0,
                composition_restrictions=0, invalid_rejections=0)
    for f in fs:
        oracle=dict(f.graph)
        assert f.image()==frozenset(oracle.values())<=f.codomain
        assert FiniteFunction(list(f.domain),list(f.codomain),list(f.graph)*2)==f
        for x in f.domain:
            assert f(x)==oracle[x];counts['evaluations']+=1
        assert compose(identity(f.codomain),f)==f
        assert compose(f,identity(f.domain))==f
        counts['identity_laws']+=2
        for d in subsets(f.domain):
            r=restrict(f,d)
            assert r.domain==d and r.codomain==f.codomain
            assert dict(r.graph)=={x:oracle[x] for x in d}
            counts['restrictions']+=1
            for e in subsets(d):
                assert restrict(r,e)==restrict(f,e)
                counts['nested_restrictions']+=1
    for f,g in product(fs,repeat=2):
        expected=(f.domain==g.domain and f.codomain==g.codomain and dict(f.graph)==dict(g.graph))
        assert (f==g)==expected;counts['equality_pairs']+=1
        if f.codomain!=g.domain:
            rejects(compose,g,f);counts['mismatched_compositions']+=1
            continue
        c=compose(g,f);fo,go=dict(f.graph),dict(g.graph)
        assert c.domain==f.domain and c.codomain==g.codomain
        assert dict(c.graph)=={x:go[fo[x]] for x in f.domain}
        counts['compositions']+=1
        for d in subsets(f.domain):
            assert restrict(c,d)==compose(g,restrict(f,d))
            counts['composition_restrictions']+=1
        for h in fs:
            if g.codomain==h.domain:
                assert compose(h,c)==compose(compose(h,g),f)
                counts['associative_triples']+=1
    invalid=[([0],[0],[]),([0],[0],[(1,0)]),([0],[0],[(0,1)]),
             ([0],[0,1],[(0,0),(0,1)]),([True],[0],[(True,0)]),
             ([0],[False],[(0,False)]),([0],[0],[(0,True)]),
             ([0],[0],[(0,)]),([0],[0],[(0,0,0)]),
             ('0',[0],[(0,0)]),([0],[0],None),([0],[0],[('0',0)]),
             ([0],[0],[(0,0.0)]),([0.0],[0],[(0,0)])]
    for args in invalid:
        rejects(FiniteFunction,*args);counts['invalid_rejections']+=1
    f=identity([0,1])
    for x in [2,True,0.0,'0']:
        rejects(f,x);counts['invalid_rejections']+=1
    for d in [[2],[True],'0']:
        rejects(restrict,f,d);counts['invalid_rejections']+=1
    for fn,args in [(restrict,(None,[])),(compose,(None,f)),(compose,(f,None)),(identity,([True],))]:
        rejects(fn,*args);counts['invalid_rejections']+=1
    domain=[0,1];codomain=[0,1];graph=[[0,0],[1,1]]
    f=FiniteFunction(domain,codomain,graph)
    domain.append(2);codomain.append(2);graph[0][1]=1
    assert f==identity([0,1])
    square=FiniteFunction([0,1,2],[0,1,4,9],[(0,0),(1,1),(2,4)])
    assert square.image()==frozenset({0,1,4})
    empty_a=FiniteFunction([],[],[]);empty_b=FiniteFunction([],[0],[])
    assert empty_a!=empty_b
    a=identity([0,1]);s=frozenset({0});assert restrict(a,s)!=identity(s)
    wide=FiniteFunction([0],[0,1],[(0,0)]);narrow=identity([0])
    rejects(compose,narrow,wide)
    first=FiniteFunction([0,1],[2,3,4],[(0,2),(1,3)])
    second=FiniteFunction([2,3,4],[5,6],[(2,5),(3,5),(4,6)])
    combined=compose(second,first)
    assert combined==FiniteFunction([0,1],[5,6],[(0,5),(1,5)])
    assert combined.image()==frozenset({5})
    rejects(compose,first,second)
    examples=[dict(label='finite square diagram',function=encode(square),image=sorted(square.image())),
              dict(label='empty domain, distinct codomains',left=encode(empty_a),right=encode(empty_b),equal=False),
              dict(label='restricted identity retains old codomain',left=encode(restrict(a,s)),right=encode(identity(s)),equal=False),
              dict(label='image fits but strict middle sets differ',first=encode(wide),second=encode(narrow),composition='rejected by this declared interface'),
              dict(label='input mutation does not change stored function',function=encode(f)),
              dict(label='exercise finite composition',first=encode(first),second=encode(second),result=encode(combined),image=sorted(combined.image()),reverse='rejected')]
    paths=['tools/finite_functions.py','tools/validate_finite_functions.py']
    report=dict(status='passed',validated_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
                scope=dict(set_family=[[],[0],[0,1]],labels='exact Python integers; bool rejected',enumeration='all maps between each ordered pair of declared sets'),counts=counts,examples=examples,
                independent_model='Plain Python dictionaries for graph values and explicit domain/codomain equality.',
                limits='Finite integer-labelled graphs only. Does not construct infinite Q-domain functions, prove general theorems, represent real continuity or implement more general image-compatible composition.')
    (ROOT/'research/production/finite_functions_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(status='passed',counts=counts,examples=len(examples)),indent=2))

if __name__=='__main__':main()
