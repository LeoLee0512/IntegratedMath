# B2.12 有限和与求和规则：独立数学复核

审阅者：Astra/high独立数学代理。日期：2026-10-29。结论：本单元正文与8题完整答案数学通过，无待解决数学阻断。已实际读完同批四稿与16全解；两作者确认冻结。

## 定义、SUM1—SUM5与索引

I_n按自然索引j<n定义，I_0为空；I_(n+1)恰由I_n和新索引n组成，使用后继比较与严格/非严格比较的联系，不给0−1赋值。长度n表为I_n→Q的函数，空表无a_0；有理序列为N→Q，定义域无限不意味着进行无限求和。

实际定义先取固定状态范围N×Q与初态(0,0)，更新T(k,s)=(k+1,s+u_k)在整个状态范围处处定义且唯一。B1.1递归给出F后，先归纳首分量为n，才从第二分量推出Σ_0=0、Σ_(n+1)=Σ_n+u_n。独立唯一性证明核同域同目标再逐点相等，没有把索引依赖的s↦s+u_n误当成固定T。含端点上界k的求和定义为Σ_(k+1)，因此上界零是一项，不是空和。

SUM1归纳性质保留任意u,v量词，后继前提分为前n项一致和第n项一致；不要求表外相等。有限表零延拓两支互斥且覆盖所有自然索引，第一支仅在合法域内读取a_j；SUM1保证任何合法延拓给同一表和，空表无须读取不存在的a_0，也未使用选择原则。

SUM2逐项加法与缩放分别归纳。加法明确交换累计值Σ_n(v)与新增项u_n，缩放仅用分配律，允许常数零或负数。相反序列和差序列先逐项定义，再用已证公式；未从函数符号直接套用数值运算。SUM3用明确嵌入η(n)作有理系数，空和基例、η(n+1)=η(n)+1和分配律给全部项数；和为零不反推空表。

SUM4固定u,m对后段长度n归纳，移位第零项是u_m。有限表拼接先核前后段合法且不相交；每个i≥m的合法后段索引才取j=i−m，O8反映比较保证j<n，消去保证唯一。前段/后段覆盖I_(m+n)后才定义拼接表，通过SUM1识别两个表和；m=0、n=0仍成立。SUM5从拼接及常量零和推出尾补零不改值，保持不同表长是不同函数记录的事实。

带幂例只讨论固定x下的有限有理表，使用x^0=1包含x=0而保留常数项。旧自然数表和兼容性从非空一项表归纳，保加嵌入使每步相容，准确承认旧B1.5没有定义空自然数表之和。

## 八题完整答案

| 题 | 实际逐项核验 |
| --- | --- |
| 1 | 四项累计0,1/2,−1/2,1,3；空范围和0、上端点0的一项和1/2区分，非空零和反例合法。 |
| 2 | 序列η(j)+1给状态(1,1),(2,3),(3,6)；固定T条件、首分量归纳和部分和唯一性完整，存在性另依递归。 |
| 3 | 前缀一致归纳量词及后继前提正确；(2,0,−1)和1，索引3及以后不计入，空表延拓独立明确。 |
| 4 | 一般加法证明指出交换Σ_n(v)和u_n；具体逐项(5/6,0,3/2)和7/3，原和3/2与5/6之和同值。 |
| 5 | 任意c缩放独立归纳；c=−2/3给(−1,2,0)和1，原和−3/2乘c也1；c=0,n=0不排除，不除以c。 |
| 6 | 常量和η(n)c归纳正确，四个5/4和5；相反/差序列定义后推导，两式空和边界分别0=−0、0=0−0。 |
| 7 | 后段归纳与自然索引相加正确；五项总和3，前二项−1、后三项4；错从u0重读给1，空两段均覆盖。 |
| 8 | 先依据已证索引合法拼接，再用零表和；两项/四项带幂表同为2−x，x=0分别(2,0)/(2,0,0,0)，不同域使两表不同。 |

## 修订闭环

预备审读指出B1.5旧求和只覆盖非空自然表；作者正式正文第9节已从一项起归纳兼容，未补造旧空和。实际首轮正文发现图alt含“七分之二”及纠错残留，已改为正确的“二分之七”，公式7/2始终正确。答案4“前零、一、二三个索引”已简化为“索引零、一、二”并读回。额外先修链接、开篇通分6分母计算与定义后的三步状态演算均已逐项复核；SUM一般证明未被数值例替代。无剩余数学阻断。

## 实际依赖与范围

已完整读取本批四份实际稿件及16题完整答案，核对最终修订；批准只绑定下列最终哈希，不把预备计划或其他代理的意见视为全文证据。实际检查的既有接口包括B1.1归纳/固定更新递归、自然数后继比较及加法保序反映、条件减法、旧位值自然幂与非空自然数和、有理加乘/零乘积/非零除法、两层嵌入及三数据函数的逐点相等与严格复合。B1.1原则是书中公开采用的基础，没有被说成已完成集合论构造。有限表仍是固定域I_n、固定目标Q的函数；不同长度表即使同和值也不因而相等。

本批只涵盖Q底数的自然指数与有理有限前缀和。没有负/分数/实指数、无限和及收敛、一般有限置换、双三重求和换序、卷积或正式多项式对象；当前两单元不能视为97H20或第528章全部完成。

## 实现与主验证器

已全文读取tools/rational_powers_sums.py与validate_rational_powers_sums.py，核对主JSON记录的源码哈希。rational复用既有精确输入检查，只接受exact int/Fraction，拒bool和float。power先验证底数和exact int非负指数，再从Fraction(1)连乘；即使指数0也先拒非法底数。partial_sums先验证整张list/tuple表，再输出长度n+1的不可变元组(S0,…,Sn)，S0为Fraction(0)。finite_sum取最后累计值，空表为0。segment_sum先验证整张表，再核0≤start≤len、count≥0、start+count≤len；末端空段合法，段外非法项仍拒。Fraction(2)作为指数被拒属于API表示约定，不是在数学上否定该数为自然数；任意迭代器和回调不属于API输入。

主验证器以Fraction内置整数幂、对独立切片的标准精确sum作oracle。实际JSON记录：50次幂，245次指数加法、245次幂的幂、175次乘积幂，781张表、3711前缀、10791连续段、3711分割、3124尾补零、3905缩放、16276逐项加、68非法输入拒绝与781输入不变性检查，另有六个明确示例。本审阅读取了该实际记录与程序，没有冒称重新执行该次主验证器运行。

## 独立有限oracle

本审阅实际执行独立脚本：幂的预期用整数分子、分母各自二分求幂，未调用Fraction幂；求和预期先取所有分母的乘积，再在整数中累计通分后的分子，最后仅构造一次Fraction，不照抄被测逐项有理累加过程。七个底数、指数0…12共91次幂；另1029次三条指数律检查。五值项集合、长度0…5给3906张表；22461前缀、76416合法连续段、22461拼接、11718缩放、16276逐项加全部一致。68次非法输入拒绝涵盖bool/float、非法自然指数、容器与段边界，并明确测试空段之外的坏项也被拒。

完整可重放代码与实际输出附于finite_sums_math_review.md，脚本SHA-256为124ce52897eed02df3478ceddbdf35879388b098c37ac592ad2ed0c98c9f7ade。该独立脚本不另声称覆盖主验证器的尾补零与输入不变性计数。所有有限枚举只支持实现与边界检查，不是一般数学命题的证明；一般结论来自本批逐步归纳与逐题证明。

## 来源与批准边界

已全文读取本地powers_sums_sources_2026-10-29.md和JSON，不重新联网。审计保留20次真实访问（19次HTTP200、一次候选多项式路径404及后续正确路径），并明确区分当前幂/有限和与未来多项式预读。OpenStax固定提交、CC-BY-NC-SA-4.0；mathlib v4.24.0、Apache-2.0。OpenStax的零指数条款要求非零底数，不被冒用为本书0^0约定依据；mathlib自然幂提供相应离散语境，但只是源码阅读，没有Lean编译或本书形式验证。来源预备诊断计数不是本模块测试计数，未混用。

本报告不批准最终PDF逐页视觉效果、发布、合并或推送。图注中数学值与含义已读，图和版式验收仍属另一个环节；冻结稿改变须按差异重新绑定。

最终稿行数依次为幂正文422、幂答案319、有限和正文467、有限和答案322。四稿题答互链与先修引用已检查，唯一不在manuscript目录内的来源锚powers-sums-sources由构建程序提供。来源最后登记POW1—5/SUM1—5及η接口已读回；常量和的mathlib nsmul与本书η(n)c区别得到明确，不把库的一般标量作用当作本书先修。

最终构建后追加复核：有限和图注把纯文本S_n、n、S_0改成数学模式 $S_n$、$n$、$S_0$。已实际读回，并将该处反向还原后得到上一冻结正文哈希e8ed699b9cd3b8428e9286b3f18cf4c90720fcc55c5b2b6c93aad071df4359b0，证实没有其他正文差异；图注的数学定义与数值未改变。此处只复核源文本，不授予PDF视觉批准。

## 四稿最终哈希

| 文件 | SHA-256 |
| --- | --- |
| `manuscript/foundations/rational_powers.md` | `581010522535b41a771d0dd920531b37669b379ea64ce6001028620988bb3ee2` |
| `manuscript/foundations/rational_powers_answers.md` | `fe64ec1b757dedb07583460db31afe240c9a1c0845c78a10603787ba2acef102` |
| `manuscript/foundations/finite_sums.md` | `ea736adc9c09e27a9443cd24a11af4c3a1f1fcad72824a8f7430b3a4b670ea23` |
| `manuscript/foundations/finite_sums_answers.md` | `127a6dd135315f2ccf2f9e4931e0e0c5f8c3a4adfb511b4f962cd70f552b4704` |

## 依赖、代码与来源审计绑定

| 文件 | SHA-256 |
| --- | --- |
| `manuscript/foundations/functions_composition.md` | `806b32944f8253b2e2af3b2a551a25cc0ce6bf17ce51cc6b50216cf28e58a94a` |
| `manuscript/foundations/functions_definition.md` | `1dee6ffb8bada53f6f09ea4ad908c0a03fd06c937fb685538566175cb9655650` |
| `manuscript/foundations/integers_addition_order.md` | `bd18f2b22e9a8b2ef116c5835140eb79beacc4499e489dbfc8e6a38c89778672` |
| `manuscript/foundations/integers_multiplication.md` | `4bc038ace8d4fe782843098e3f171cf1e2b78b3e79a8169baea9d4bbdfa52bba` |
| `manuscript/foundations/natural_numbers.md` | `709c9ebf1f580c8bf7af17b494ecd07505dd33f65ccfe49482675fe7712880f3` |
| `manuscript/foundations/natural_order.md` | `4ad8e874bedda7f4c15739fd47344903ec71bd9a5b538c71bde0f9827b091435` |
| `manuscript/foundations/natural_subtraction.md` | `92d1ac5e3cf6c07f61afd8f84e1e96d0556bf62d752e1d2a854121b66c412247` |
| `manuscript/foundations/place_value.md` | `93c1182d304b216a0a3b73cf4e4b2fd23dd370f31a9db8ffcd85c08eadf0fb45` |
| `manuscript/foundations/positional_representation.md` | `d1967565dd6e58c8980da21d33ba071dba401e8621141d5f15b9074153f82c09` |
| `manuscript/foundations/rationals_addition.md` | `9b349aec9a9df0c7c45c9d33e7d0cfa483dc22432f0250baa23ab2a6d02b417b` |
| `manuscript/foundations/rationals_construction.md` | `0833130ad2bd8f24598a8c8fdfd3ce38e03874036fceac57b019d6d9c7da45a0` |
| `manuscript/foundations/rationals_division.md` | `b2adb43e3d4b0fbe5c57dd6b745cfa1550f050321a2208df618a666ca8ecfc64` |
| `manuscript/foundations/rationals_multiplication.md` | `033ed077c363d91143247bebedb790d4c444b5574c5085509a2b6c207d0b9c20` |
| `tools/linear_equation_solvers.py` | `c3ec0ab4a892397d3d0af59a1acd367bf1f1cfea80e3e14bd6b2b6cd790b74c9` |
| `tools/rational_powers_sums.py` | `fad8cf2a22151b4d584ba09ea3464526668cf34d2737afdf0374f241f16cfda4` |
| `tools/validate_rational_powers_sums.py` | `9318a2df81bf07d952cc8e5db1f6dd4f41b05a3ad67384719200267eec88ce0e` |
| `research/production/rational_powers_sums_validation.json` | `9e845a9d8b0d9253178a6dd222297c7da6d7ec290fdf3de78dbdb786997ab121` |
| `research/production/powers_sums_sources_2026-10-29.md` | `bb77d0334f86315d1cb34a725d0e86470be8fe8f427eb386e22c7f93a2546b79` |
| `research/production/powers_sums_sources_2026-10-29.json` | `e3758d928704f77b435e1f581d2a4c1ddafdd5bc6a2d92dd96131baa0843a03d` |

## 独立oracle完整脚本与实际输出

实际命令：`python -B /tmp/powers_sums_astra_oracle.py`。代码可原样保存重放，ROOT仅指定本地仓库。脚本SHA-256：`124ce52897eed02df3478ceddbdf35879388b098c37ac592ad2ed0c98c9f7ade`。

```python
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import sys
ROOT=Path('/workspace/IntegratedMath-book')
sys.path.insert(0,str(ROOT/'tools'))
from rational_powers_sums import power,partial_sums,finite_sum,segment_sum
counts=dict(powers=0,power_laws=0,records=0,prefixes=0,segments=0,
            concatenations=0,scalings=0,termwise_additions=0,rejected=0)

def integer_power(a,n):
    """Independent binary powering in integers, no Fraction power call."""
    value=1
    while n:
        if n%2:
            value*=a
        a*=a
        n//=2
    return value

def expected_power(a,n):
    a=F(a)
    return F(integer_power(a.numerator,n),integer_power(a.denominator,n))

def expected_sum(values):
    """One common denominator; integer accumulation, not rational prefix addition."""
    denominator=1
    for value in values:
        denominator*=value.denominator
    numerator=0
    for value in values:
        numerator+=value.numerator*(denominator//value.denominator)
    return F(numerator,denominator)

bases=(F(-3),F(-1),F(-1,2),F(0),F(1,2),F(1),F(3))
for a in bases:
    for n in range(13):
        actual=power(a,n)
        assert type(actual) is F and actual==expected_power(a,n)
        assert (actual==0)==(a==0 and n>0)
        counts['powers']+=1
    for m,n in product(range(7),repeat=2):
        assert power(a,m+n)==power(a,m)*power(a,n)
        assert power(power(a,m),n)==power(a,m*n)
        counts['power_laws']+=2
for a,b,n in product(bases,bases,range(7)):
    assert power(a*b,n)==power(a,n)*power(b,n)
    counts['power_laws']+=1

values=(F(-3,2),F(-1,3),F(0),F(1,2),F(2))
for length in range(6):
    for record in product(values,repeat=length):
        prefixes=partial_sums(record)
        assert type(prefixes) is tuple and len(prefixes)==length+1
        assert all(type(x) is F for x in prefixes)
        assert finite_sum(list(record))==expected_sum(record)
        counts['records']+=1
        for stop in range(length+1):
            assert prefixes[stop]==expected_sum(record[:stop])
            counts['prefixes']+=1
        for start in range(length+1):
            for size in range(length-start+1):
                actual=segment_sum(record,start,size)
                assert type(actual) is F and actual==expected_sum(record[start:start+size])
                counts['segments']+=1
            assert finite_sum(record)==finite_sum(record[:start])+finite_sum(record[start:])
            counts['concatenations']+=1
        for scalar in (F(-2),F(0),F(3,2)):
            assert finite_sum([scalar*x for x in record])==scalar*expected_sum(record)
            counts['scalings']+=1
for length in range(4):
    records=tuple(product(values,repeat=length))
    for left,right in product(records,repeat=2):
        together=[x+y for x,y in zip(left,right)]
        assert finite_sum(together)==expected_sum(left)+expected_sum(right)
        counts['termwise_additions']+=1

def reject(fn,*args):
    try:
        fn(*args)
    except ValueError:
        counts['rejected']+=1
    else:
        raise AssertionError(('invalid input accepted',fn.__name__,args))
for bad in (None,True,False,0.5,'1/2',(1,2)):
    reject(power,bad,0)
    for fn in (finite_sum,partial_sums):
        reject(fn,[F(1),bad])
    reject(segment_sum,[F(1),bad],0,0)
for bad in (-1,None,True,False,2.0,'2',F(2)):
    reject(power,0,bad)
    reject(segment_sum,[F(1)],bad,0)
    reject(segment_sum,[F(1)],0,bad)
for bad in (None,{F(1)},frozenset({F(1)}),'12',iter([F(1)]),lambda n:F(n)):
    reject(finite_sum,bad)
    reject(partial_sums,bad)
    reject(segment_sum,bad,0,0)
for record,start,size in [([],1,0),([],0,1),([F(1)],2,0),([F(1)],1,1),([F(1)],0,2)]:
    reject(segment_sum,record,start,size)
assert power(0,0)==F(1)
assert partial_sums([])==(F(0),)
assert segment_sum([F(1)],1,0)==F(0)
print(json.dumps(counts,sort_keys=True,indent=2))
```

实际标准输出：

```text
{
  "concatenations": 22461,
  "power_laws": 1029,
  "powers": 91,
  "prefixes": 22461,
  "records": 3906,
  "rejected": 68,
  "scalings": 11718,
  "segments": 76416,
  "termwise_additions": 16276
}
```
