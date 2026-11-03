from pathlib import Path
from hashlib import sha256
from math import gcd
from PIL import Image
import json
paths=['/tmp/dedekind_grid_figure.py','/tmp/b2_dedekind_grid.png','/tmp/dedekind_addition_sources.md','/tmp/dedekind_addition_sources.json']
manifest={p:sha256(Path(p).read_bytes()).hexdigest() for p in paths}
# Independent integer-pair arithmetic; do not import the drawing program.
points=[];inside=[]
for n in range(6):
    numerator,denominator=4+n,4
    common=gcd(numerator,denominator)
    points.append([numerator//common,denominator//common])
    inside.append(2*numerator<3*denominator)
assert points==[[1,1],[5,4],[3,2],[7,4],[2,1],[9,4]]
assert inside==[True,True,False,False,False,False]
# 2*(4+n)<12 iff n<2, so 0,1 are in and 2 is the first natural exit.
assert all(inside[n] for n in (0,1)) and not inside[2]
m=2;N=5
assert 5>4 # N*delta = 5/4 > b0-a0 = 1.
assert 9>8 # p_N = 9/4 > b0 = 2.
assert N!=m
u,v=points[1],points[2]
diff_num=v[0]*u[1]-u[0]*v[1];diff_den=v[1]*u[1]
assert diff_num>0 and 4*diff_num==diff_den
assert 2*diff_num<diff_den # v-u < epsilon=1/2.
# v equals the principal endpoint, which is excluded by strict membership.
assert 2*v[0]==3*v[1] and inside[2] is False
with Image.open('/tmp/b2_dedekind_grid.png') as im:metadata={'format':im.format,'size':list(im.size),'mode':im.mode}
assert all(sha256(Path(p).read_bytes()).hexdigest()==h for p,h in manifest.items())
print(json.dumps({'status':'passed','method':'integer-pair formulas and positive-denominator cross products; no drawing rerun or Fraction oracle','input_sha256':manifest,'image_metadata':metadata,'points':points,'inside':inside,'first_exit_index':m,'nonempty_exit_set_witness_index':N,'N_is_first_exit':False,'u':u,'v':v,'gap':'1/4','epsilon':'1/2','endpoint_is_outside':True,'scope':'six points for the specified decidable principal cut only; no general cut membership or exit-search algorithm'},ensure_ascii=False,indent=2))
