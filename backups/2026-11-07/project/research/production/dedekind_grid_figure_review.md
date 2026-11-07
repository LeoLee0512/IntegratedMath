# 第22批有理网格图：独立只读检查

结论：通过此图的数值、成员关系、指标含义和代码范围检查。已实际使用图像查看工具打开 `/tmp/b2_dedekind_grid.png`，并逐行读取 `/tmp/dedekind_grid_figure.py`。另运行一个小型独立整数对检查程序，未导入或重跑原绘图程序，未重绘 PNG。

检查时间：2026-10-29T20:15:20.642160+00:00

## 实际图面

PNG 为1883×666像素、RGBA。实际看到标题 `A=i(3/2), ε=1/2, δ=ε/2=1/4`，六列指标0—5与六个有理数框逐一对齐。前两列有“在 A 内”文字，后四列均明确“不在 A 内”；颜色只是辅助，成员关系有文字支持。下方分别标明 u=5/4、v=3/2、b₀=2、N=5，以及 m=2、v−u=1/4<ε。没有观察到文字截断、框内数字遮挡或标签相互覆盖。

六列是该具体有理网格的有限示例。图没有画出无穷网格、未定义的实数运算或一个迭代极限；同一列上方的 n 是自然指标，下方的数是有理点。

## 六点、成员与两种指标

对本图，p_n=1+n/4=(4+n)/4，A={q∈Q:q<3/2}。

| n | p_n | 是否在 A 内 |
|---|---|---|
| 0 | 1 | 是：1<3/2 |
| 1 | 5/4 | 是：10<12 |
| 2 | 3/2 | 否：等于严格端点 |
| 3 | 7/4 | 否：14>12 |
| 4 | 2 | 否：2>3/2 |
| 5 | 9/4 | 否：18>12 |

正分母交叉比较给 p_n<3/2 当且仅当 2(4+n)<12，即 n<2。因此0、1在内，2在外，m=2确是自然指标中的首次退出，不是只在一组未排序样本中找出的外点。u=p₁=5/4、v=p₂=3/2，v−u=1/4，确有0<1/4<ε=1/2。v正好等于有理端点而不属于A，是严格主下段定义允许且需要标清的情形。

N=5承担另一项任务：Nδ=5/4>b₀−a₀=1，且p₅=9/4>b₀=2，故p₅在外，见证退出指标集合E非空。它不表示最小指标；m=2与N=5不能互换。图中这两个标签分别位于其对应处，数值与证明角色一致。

## 源码的枚举范围

函数只接收输出目录；第13行固定 endpoint=3/2、epsilon=1/2、a0=1、b0=2，第15行只生成 n=0,…,5 的六个精确 Fraction 点，第16行通过与已给有理端点的可判定比较构造成员布尔列表。第18行的 `next` 只在这份固定有限列表中找到第一项 False。第17行断言已明确该列表的成员结构，第20—21行核 m、外部见证、u/v和严格间距。

因此，本代码并未接收任意分割、成员谓词或实数对象；`next` 不构成对任意cut的通用首次退出算法。DA1一般证明中的非空自然索引集最小元，是依据已证良序结论取得的存在性见证。任意cut没有提供可执行成员判定，这一逻辑边界不因本图具体主下段可计算而改变。图上坐标只是布局，不是实数类型实现。

## 输入与检查证据

下列 SHA-256 绑定本次实际读取的源图、代码及保持未改的来源审计：

```json
{
  "/tmp/dedekind_grid_figure.py": "cd1e360adda174f42682309b3d3851fe99d3146eb0ab979dee09e06f13ac3b90",
  "/tmp/b2_dedekind_grid.png": "635c8f35e9dc1d6e91d69efbff36fa0815bbf51faea53ed2335d2b8f1b4926a1",
  "/tmp/dedekind_addition_sources.md": "9b35692eaee574bc5ccbc648a0af3f6305138741258426ba66886a0328c15856",
  "/tmp/dedekind_addition_sources.json": "9e741561321e14342b5b6919e2ac44da884d5a118562abfafe63ffa23d50377f"
}
```

独立检查采用整数分子分母及交叉乘积，没有复用原图的 Fraction 路线。检查代码 SHA-256：`02af536860e5dab5135ddb5d983885bc121a462eb850f6058abd777c6160a2aa`；实际输出 SHA-256：`7a5e959d4214d46f8a1bc59a09cfae30aaf4ba241704fd0ddecfa04367466f54`。

### 完整独立检查代码

```python
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
```

### 完整实际输出

```json
{
  "status": "passed",
  "method": "integer-pair formulas and positive-denominator cross products; no drawing rerun or Fraction oracle",
  "input_sha256": {
    "/tmp/dedekind_grid_figure.py": "cd1e360adda174f42682309b3d3851fe99d3146eb0ab979dee09e06f13ac3b90",
    "/tmp/b2_dedekind_grid.png": "635c8f35e9dc1d6e91d69efbff36fa0815bbf51faea53ed2335d2b8f1b4926a1",
    "/tmp/dedekind_addition_sources.md": "9b35692eaee574bc5ccbc648a0af3f6305138741258426ba66886a0328c15856",
    "/tmp/dedekind_addition_sources.json": "9e741561321e14342b5b6919e2ac44da884d5a118562abfafe63ffa23d50377f"
  },
  "image_metadata": {
    "format": "PNG",
    "size": [
      1883,
      666
    ],
    "mode": "RGBA"
  },
  "points": [
    [
      1,
      1
    ],
    [
      5,
      4
    ],
    [
      3,
      2
    ],
    [
      7,
      4
    ],
    [
      2,
      1
    ],
    [
      9,
      4
    ]
  ],
  "inside": [
    true,
    true,
    false,
    false,
    false,
    false
  ],
  "first_exit_index": 2,
  "nonempty_exit_set_witness_index": 5,
  "N_is_first_exit": false,
  "u": [
    5,
    4
  ],
  "v": [
    3,
    2
  ],
  "gap": "1/4",
  "epsilon": "1/2",
  "endpoint_is_outside": true,
  "scope": "six points for the specified decidable principal cut only; no general cut membership or exit-search algorithm"
}
```

本次没有修改已冻结第22批来源审计、源图、绘图代码或第21批正式文件。检查只覆盖这张实际打开的图及有限例子；不替代任意分割的DA1全称证明、两单元全文数学/教学审阅或最终PDF页图验收。


## 2026-10-30 主编续核（保留上次独立记录）

正文在已有负分割函数N之外使用自然指标M，图中N=5已更正为M=5；最小退出指标仍为m=2。其余代码仅分行，Python AST与旧版仅有该标签字符串之差。主编重跑绘图及已有整数对独立诊断，六个样本、成员条件、首次退出与间距检查通过，并实际打开新PNG核对M=5标签和布局。本次不声称重跑了外部来源抓取或一般分割算法。

- `/tmp/dedekind_grid_figure.py` SHA-256 `4a13641c2cc43d604b28b3930ff533810aba54fc547c3d6d09e8ae5f763a1673`
- `/tmp/b2_dedekind_grid.png` SHA-256 `d89c138785739d43eaef849703f4d13e2b9b8060bb02a315612bde7be848b85d`
