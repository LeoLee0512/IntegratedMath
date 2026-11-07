# 第21批有理缺口图：独立只读检查

结论：通过本图的数值、图面和限定范围检查。此次实际用图像查看工具打开 `/tmp/b2_rational_gap.png`，逐行读取绘图代码，并运行独立整数对核算。未执行或重绘原图程序，未改变源图、来源审计或第20批正式文件；这不是全稿或最终构建验收。

核验时间：2026-10-29T19:59:53.470113+00:00

## 实际图面

PNG 为 1781×792 像素，RGBA。已实际看到标题公式 `f(q)=(2q+2)/(q+2), q≥0`、两行各三个数框、四条带“应用 f”标签的箭头及六个平方比较。上行蓝色标题为“S 中更大的成员”，下行棕色标题为“更小的有理上界”；语义由文字和不等式同时表示，不只靠颜色。数字、正负比较方向及中文标签清楚，没有观察到截断、叠字或平方分数被遮挡。箭头表示应用公式的步骤，画面没有数轴刻度、连续曲线或平方根终点。

## 独立精确核算

独立程序没有导入绘图函数，也没有复用其 `Fraction` 计算。把输入表示为整数对 `(n,d)`，直接算 `f(n/d)=(2n+2d)/(n+2d)`，用整数 gcd 约分；平方及前后比较均使用正分母交叉乘积。

| 行 | 两次计算 | 六个平方比较中的本行三项 | 比较证据 |
|---|---|---|---|
| S 的成员 | 1 → 4/3 → 7/5 | 1<2；16/9<2；49/25<2 | 1<2；16<18；49<50 |
| 有理上界 | 2 → 3/2 → 10/7 | 4>2；9/4>2；100/49>2 | 4>2；9>8；100>98 |

前后差的交叉乘积分子上行为 1、1，下行为 −1、−1，分别严格增加、严格减小。四步还分别核了 QG3 的两条恒等式，清分母后的整数等式全部成立。下行数均正且平方大于二，故对任意 `s∈S`，非负平方比较给 `s<q`；这说明“上界”文字有数学依据，不能仅凭六个样本的比较断言全称结论。

## 图、正文与程序边界

`/tmp/rational_gaps_bounds.md` 第143—158行给出 QG3 的定义、两恒等式及两侧符号结论；第160行先核非负输入、正分子、正分母；第162—211行逐项展开。第209行明确是有限项恒等式，不引用连续性或极限。第251行是本 PNG 的插图引用；第253行明确每行只画两次计算、图不是数轴、没有声明迭代极限，全称的成员增大和上界减小依据 QG3/QG4；第297行再次限定有限实例不能替代无有理上确界证明。

绘图代码第13—20行的 `step` 是 `draw_rational_gap` 内部函数，实际只接收从 `Fraction(1)`、`Fraction(2)` 开始的各两步非负有理输入。第21—27行包含样本值、两恒等式和单调方向断言；第28—41行只是静态框、箭头和文字的绘图布局。代码没有定义分割、通用实数、实数算术、极限、分割判等或成员判定 API。绘图库使用的坐标只是页面布局坐标，不是已构造实数的数学实现。

## DC 历史两句核对

实际读取 `/tmp/dedekind_cuts_order.md`，SHA-256 恰为 `a244695551c88b167daac9ddf76c8becc5e70411ea5e30063af9cf8e7ce22ee4`。第27行同一段中的两句与已冻结来源一致：第一句将1872年《连续性与无理数》与有理数分割、两侧切分和端点分配相连；第二句明确本书使用现代单侧下集、把无最大元纳入定义，并不把四条件逐字归于原著。

对应来源为冻结审计的 `history_1872`（Dedekind TeX第1258—1266行，原作1872年自注）、`history_preface`（第399—417行，1872年3月20日前言）和 `historical_cuts`（第704—730行，§IV两侧切分及有理端点的两种归属）。此历史句不声称本书的 f 公式来自原著。没有新增网络请求。

## 输入字节绑定

```json
{
  "/tmp/rational_gap_figure.py": "057b33b5c518d498bdbe37f026048494cdc1887c5142e52de8b20f4622bbf278",
  "/tmp/b2_rational_gap.png": "d86ad3a6737614ac2ee439abf34c61913bb224220e4e48728783947002762667",
  "/tmp/rational_gaps_bounds.md": "20ab8bd8ee996a2b69f297020caf7138c533e8781ff35bc794c8fe6cad0f4ff3",
  "/tmp/dedekind_cuts_order.md": "a244695551c88b167daac9ddf76c8becc5e70411ea5e30063af9cf8e7ce22ee4",
  "/tmp/rational_gaps_cuts_sources.md": "a0640b04ff3e045250d55066fba58d8178d946ab13b92305cf6624a4ef6d9db3",
  "/tmp/rational_gaps_cuts_sources.json": "f3716babcc2017d5c0ba37899e85c118002c6413e5682d5b595a5e0e5bb69e27"
}
```

独立检查程序 SHA-256：`a3f08727c11cd9bd39c156b4535685f19d020c807696bc714b3269cc35a86e35`。
实际输出 SHA-256：`88ab8eed851e5990fb96ceb4ed816ebe9cf8f0d5efb53773492bc46330ab3e0c`。

## 完整独立检查代码

```python
from pathlib import Path
from hashlib import sha256
from math import gcd
import json
from PIL import Image
paths=['/tmp/rational_gap_figure.py','/tmp/b2_rational_gap.png','/tmp/rational_gaps_bounds.md','/tmp/dedekind_cuts_order.md','/tmp/rational_gaps_cuts_sources.md','/tmp/rational_gaps_cuts_sources.json']
manifest={p:sha256(Path(p).read_bytes()).hexdigest() for p in paths}
assert manifest['/tmp/dedekind_cuts_order.md']=='a244695551c88b167daac9ddf76c8becc5e70411ea5e30063af9cf8e7ce22ee4'
expected=[[(1,1),(4,3),(7,5)],[(2,1),(3,2),(10,7)]]
rows=[]
for k,chain in enumerate(expected):
 states=[];transitions=[]
 for n,d in chain:
  assert n>=0 and d>0 and gcd(n,d)==1
  residual=n*n-2*d*d
  assert residual<0 if k==0 else residual>0
  states.append({'q':[n,d],'square':[n*n,d*d],'square_minus_two_numerator':residual})
 for (n,d),(m,e) in zip(chain,chain[1:]):
  # f(n/d)=(2n+2d)/(n+2d), using integer pairs only.
  a,b=2*n+2*d,n+2*d;g=gcd(a,b)
  assert (a//g,b//g)==(m,e)
  difference=m*d-n*e
  assert difference>0 if k==0 else difference<0
  # f(q)-q=(2-q^2)/(q+2), cross multiplied.
  assert difference*(n+2*d)==e*(2*d*d-n*n)
  # f(q)^2-2=2(q^2-2)/(q+2)^2, cross multiplied.
  assert (m*m-2*e*e)*(n+2*d)**2==2*(n*n-2*d*d)*e*e
  transitions.append({'from':[n,d],'to':[m,e],'raw_f_pair':[a,b],'difference_cross_numerator':difference})
 rows.append({'states':states,'transitions':transitions})
with Image.open('/tmp/b2_rational_gap.png') as im: meta={'format':im.format,'size':list(im.size),'mode':im.mode}
assert all(sha256(Path(p).read_bytes()).hexdigest()==h for p,h in manifest.items())
print(json.dumps({'status':'passed','method':'independent integer-pair evaluation and cross multiplication; no drawing-code import or rerun','input_sha256':manifest,'image_metadata':meta,'rows':rows,'limitations':'Six finite samples and four transitions; no assertion of convergence, real-root existence, or universal cut API.'},ensure_ascii=False,indent=2))
```

## 完整实际输出

```json
{
  "status": "passed",
  "method": "independent integer-pair evaluation and cross multiplication; no drawing-code import or rerun",
  "input_sha256": {
    "/tmp/rational_gap_figure.py": "057b33b5c518d498bdbe37f026048494cdc1887c5142e52de8b20f4622bbf278",
    "/tmp/b2_rational_gap.png": "d86ad3a6737614ac2ee439abf34c61913bb224220e4e48728783947002762667",
    "/tmp/rational_gaps_bounds.md": "20ab8bd8ee996a2b69f297020caf7138c533e8781ff35bc794c8fe6cad0f4ff3",
    "/tmp/dedekind_cuts_order.md": "a244695551c88b167daac9ddf76c8becc5e70411ea5e30063af9cf8e7ce22ee4",
    "/tmp/rational_gaps_cuts_sources.md": "a0640b04ff3e045250d55066fba58d8178d946ab13b92305cf6624a4ef6d9db3",
    "/tmp/rational_gaps_cuts_sources.json": "f3716babcc2017d5c0ba37899e85c118002c6413e5682d5b595a5e0e5bb69e27"
  },
  "image_metadata": {
    "format": "PNG",
    "size": [
      1781,
      792
    ],
    "mode": "RGBA"
  },
  "rows": [
    {
      "states": [
        {
          "q": [
            1,
            1
          ],
          "square": [
            1,
            1
          ],
          "square_minus_two_numerator": -1
        },
        {
          "q": [
            4,
            3
          ],
          "square": [
            16,
            9
          ],
          "square_minus_two_numerator": -2
        },
        {
          "q": [
            7,
            5
          ],
          "square": [
            49,
            25
          ],
          "square_minus_two_numerator": -1
        }
      ],
      "transitions": [
        {
          "from": [
            1,
            1
          ],
          "to": [
            4,
            3
          ],
          "raw_f_pair": [
            4,
            3
          ],
          "difference_cross_numerator": 1
        },
        {
          "from": [
            4,
            3
          ],
          "to": [
            7,
            5
          ],
          "raw_f_pair": [
            14,
            10
          ],
          "difference_cross_numerator": 1
        }
      ]
    },
    {
      "states": [
        {
          "q": [
            2,
            1
          ],
          "square": [
            4,
            1
          ],
          "square_minus_two_numerator": 2
        },
        {
          "q": [
            3,
            2
          ],
          "square": [
            9,
            4
          ],
          "square_minus_two_numerator": 1
        },
        {
          "q": [
            10,
            7
          ],
          "square": [
            100,
            49
          ],
          "square_minus_two_numerator": 2
        }
      ],
      "transitions": [
        {
          "from": [
            2,
            1
          ],
          "to": [
            3,
            2
          ],
          "raw_f_pair": [
            6,
            4
          ],
          "difference_cross_numerator": -1
        },
        {
          "from": [
            3,
            2
          ],
          "to": [
            10,
            7
          ],
          "raw_f_pair": [
            10,
            7
          ],
          "difference_cross_numerator": -1
        }
      ]
    }
  ],
  "limitations": "Six finite samples and four transitions; no assertion of convergence, real-root existence, or universal cut API."
}
```

检查限于已打开的这张 PNG、冻结代码、所列正文位置、六个样本和四次转换，以及独立读到的历史表述。它不证明迭代收敛，不证明实数平方根存在，也不替代 QG/DC 全部证明与全书排版验收。
