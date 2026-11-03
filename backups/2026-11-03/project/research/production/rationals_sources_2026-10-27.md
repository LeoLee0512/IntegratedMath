# 有理数构造与加法：公开来源核查

核查日期：2026-10-27。范围仅为B1.14–B1.15的构造、嵌入、加法和相反数，不收录外部题目或连续正文。

## 方法与表示边界

已读云运行技能、网络参考与启动策略，并查询当前运行状态。网络策略为restricted且raw.githubusercontent.com在启动允许列表；运行时策略状态为unknown，不声称执行状态已验证。全部读取经原代理并保留TLS验证。9次公开请求全部HTTP 200。

两类独立来源为Judson教材及Lean/mathlib形式化资料；后两者有关联。Judson允许整域中任意非零分母，Lean存互素正分母规范结构，本书须明确自己采用的整数对与等价类范围。

## [RAT-JUDSON] Abstract Algebra: Theory and Applications

作者：Thomas W. Judson。

版本：Annual Edition 2026；前言日期 August 4, 2026；本次固定提交 3069910e3ded72ff5e18837a97a0e810c92790e2。

公开入口：https://github.com/twjudson/aata

许可：GNU Free Documentation License；共同可用范围 GFDL-1.3-or-later。

许可短摘：`Version 1.3 or any later version; no Invariant Sections`。

根COPYING为1.3或以后版本，活动前言为1.2或以后版本；两者共同允许1.3或以后版本，均无不变章节和封面文字要求。不隐去版本差异。

- **等价关系与等价类的对象层次**：明确关系的自反、对称、传递条件以及等价类、划分框架；用于检查先建立关系再形成类的次序，不替代本书集合形成的采用声明。 定位：src/sets.xml：sets-subsection-equivalence-relations，行1125–1157、1270–1329。
- **分母非零与交叉乘积关系**：对整域D取有序对(a,b)，b≠0，以ad=bc定义关系。传递证明利用中间分母非零和整域的非零因子消去。本书可在已证整数性质下独立特化，不应突然要求读者先学完整整域理论。 定位：src/domains.xml：domains-section-field-of-fractions，行64–102。
- **等价类加法与良定义**：定义加法代表元为(ad+bc,bd)，并确实展开两输入同时更换代表元后的交叉乘积等式。这是对本书加法良定义证明义务的直接参照。分母积仍须非零；若书稿从正分母开始，须用整数乘法正性说明新分母为正。 定位：src/domains.xml：domains-section-field-of-fractions，行106–157。
- **加法零元、相反数及证明边界**：正文把[0,1]作为加法零元并展开计算，给出[-a,b]为相反数；但将加法构成阿贝尔群的完整核查留给读者，不可宣称本次教材已逐步证明每条加法律。 定位：src/domains.xml：domains-lemma-field-of-fractions，行160–191。
- **整数嵌入及单射**：以a映到[a,1]嵌入，并给出同加兼容及单射的理由。本书当前只采用相应整数嵌入与加法部分，不引入来源随后讨论的有理数乘法、域或倒数结论。 定位：src/domains.xml：domains-theorem-field-of-quotients，行226–240。
- **与书稿表示范围的差别**：来源允许任意非零分母，且对一般整域讨论；若书稿限定正整数分母，这是适用于整数的进一步选定，需自证负分母变号可归入该范围，不能把两个定义域说成字面相同。 定位：src/domains.xml：domains-section-field-of-fractions。

只核对事实、假设与证明结构并引用；不收录或改编原题、解答、插图或连续段落。第三方全文不写入仓库和最终分发包。

## [RAT-LEAN] Lean 4 core: Init.Data.Rat.Basic and Init.Data.Rat.Lemmas

作者：Mario Carneiro；Johannes Hölzl；Robin Arnez。

版本：Lean v4.24.0 固定发布标签。

公开入口：https://github.com/leanprover/lean4/tree/v4.24.0/src/Init/Data/Rat

许可：Apache-2.0。

许可短摘：`Released under Apache 2.0 license as described in the file LICENSE.`。

文件作者：

- `Init/Data/Rat/Basic.lean`：Mario Carneiro。
- `Init/Data/Rat/Lemmas.lean`：Mario Carneiro；Johannes Hölzl；Robin Arnez。

- **规范对表示不是等价类定义**：实际结构存储整数num、自然数den及den≠0、num绝对值与den互素的证明。其对象已处于规范形式，不是直接把任意整数对的等价类作为数据类型。书稿等价类与这种规范记录的对应需由规范代表存在唯一性建立。 定位：Basic.lean：structure Rat（23–34）、Rat.den_pos（45）。
- **约分构造与零分母边界**：normalize要求非零自然数分母，并通过gcd约分；便捷构造器mkRat对零分母返回零，是程序全函数约定。此行为不能当作本书允许零分母的依据，书稿及配套构造器应按其定义拒绝零分母。 定位：Basic.lean：Rat.normalize（84）、mkRat（95–96）。
- **规范表示相等与零**：两个输入分母各自非零时，规范结果相同当且仅当交叉乘积相等；非零分母下结果为零当且仅当分子为零。前提不能因源码中另有全函数构造器而删去。 定位：Lemmas.lean：normalize_eq_iff（77）、normalize_eq_zero（100）。
- **加法实现与数学公式的连接**：实现利用分母gcd先消公因子并规范化，未机械地保存未经约分的乘积分母；add_def实际证明它等于对(ad+bc,bd)作规范化。故本书可采用直接整数交叉和公式，再独立规范化，不能声称算法每个中间量与Lean一致。 定位：Basic.lean：Rat.add（249–263）；Lemmas.lean：add_def（277）、add_def'（292）、normalize_add_normalize（300）。
- **加法律与相反数的已读证明**：相反数保持分母、将分子取负；源码给出零元、交换、结合、逆元及加法消去证明。所读结合律证明展开整数交叉和并用整数运算律，消去证明在两边加相反数，不要求引入有理数乘法或序。 定位：Basic.lean：Rat.neg（268）；Lemmas.lean：add_zero/zero_add（296/298）、add_comm（321）、add_assoc（324）、neg_add_cancel（348）、add_neg_cancel（351）、add_right_cancel（354）。

仅阅读指定源码声明和证明结构；未运行Lean编译、形式验证或比较本书程序与库的逐步执行轨迹。

## [RAT-MATHLIB] mathlib: Mathlib.Data.Rat.Defs

作者：Johannes Hölzl；Mario Carneiro。

版本：mathlib4 v4.24.0 固定发布标签。

公开入口：https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Data/Rat/Defs.lean

许可：Apache-2.0。

许可短摘：`Released under Apache 2.0 license as described in the file LICENSE.`。

- **整数嵌入单射**：通过分子映射核对整数嵌入是单射；所用有理数仍是Lean的规范结构。 定位：Mathlib/Data/Rat/Defs.lean：intCast_injective（48）。
- **规范有理数的交叉乘积判定**：两个已构造的规范有理数相等当且仅当各自分子分母的交叉乘积相等；分母非零由类型内证据提供。这不能跳过本书原始对关系的传递证明。 定位：Mathlib/Data/Rat/Defs.lean：eq_iff_mul_eq_mul（207–213）。
- **相反数及零的规范分量**：取负不改变分母，分子变号；零的规范分量为(0,1)。不据此引入有理数次序、乘法或倒数。 定位：Mathlib/Data/Rat/Defs.lean：den_neg_eq_den（216）、num_neg_eq_neg_num（220）、num_zero（224）、den_zero（228）。

未运行mathlib；与Lean源码存在依赖，属于同一形式化资料系列，不能另外算作独立数学证明。

## 本项目独立数学核对

以下为原创核对笔记，不是外部原文；依赖书内已经建立的整数运算、消去、gcd约分和规范对唯一性，不借用待定义的有理数乘法或除法。

### RC01 关系的传递性和定义域

对整数a,c,e及正整数b,d,f，若ad=bc且cf=de，则adf=bcf=bde，重排得(af)d=(be)d。因为d>0所以d≠0，使用整数非零乘法消去得af=be。这一步只用整数乘法；不能先用尚未构造的有理数除法约去d。

### RC02 加法代表元无关

设ab'=a'b、cd'=c'd，四个分母均正。新的两个分母bd、b'd'均正。待证(ad+bc)b'd'=(a'd'+b'c')bd；左边以整数分配律展开为(ab')dd'+bb'(cd')，代入两项假设并重排即得右边。因此同时换两个代表元不改变和的类。

### RC03 相反数、零与加法律

若ab'=a'b，则(-a)b'=(-a')b，故取负代表无关。相反数相加得到分子0、分母b²的代表，它与(0,1)交叉相等。交换律由整数交换律；三项结合律先将两种分组统一展开为分子adf+bcf+bde与分母bdf，再用整数运算律。这里涉及的所有乘法都是整数分量乘法，不是尚未定义的有理数乘法。

### RC04 等价类与规范记录的桥梁

每个正分母整数对先提取正gcd得到互素且分母仍正的记录；B1.13的交叉乘积唯一性保证每类至多一份规范记录，约分构造保证至少一份。由此可用规范对存储等价类，但两者是经证明对应的表示方式，不应直接把程序字段等同于集合定义。

### RC05 配套代码核验边界

候选构造接口必须明确接受正分母，或接受非零有符号分母并先统一为正；两者都拒绝零分母。加法结果的规范对须与原始(ad+bc,bd)交叉相等，取负结果须与(-a,b)交叉相等。规范零为(0,1)。本次仅给数学接口约束，未核验root尚在编写的具体函数名、代码或输出，不报告API已经对齐。

## 简短引用建议

- 构造与代表元无关性使用 [RAT-JUDSON] 的 domains-section-field-of-fractions；同时写清书稿限定的整数与分母范围。
- 规范记录与程序表示使用 [RAT-LEAN] 的 Rat结构、normalize_eq_iff；明确它与等价类构造不同。
- 加法与相反数公式使用 [RAT-LEAN] 的 add_def、add_assoc、neg_add_cancel；源码核对不能替代书稿逐步证明。
- 整数嵌入及交叉乘积比较可使用 [RAT-MATHLIB] 的 intCast_injective、eq_iff_mul_eq_mul。
- 不引用mkRat的零分母回退行为作为数学规则；配套API应另行核对输入检查与表示不变量。

## 实际访问与哈希

行号是实际固定源码的行号，不是出版页码。

### judson_domains

https://raw.githubusercontent.com/twjudson/aata/3069910e3ded72ff5e18837a97a0e810c92790e2/src/domains.xml

访问：2026-10-27T15:57:44.026009+00:00；HTTP 200；verified_http_200。

字节数：80443；SHA-256：`cdadd1a266f58008c8ae025c76cf8dfcdeaa821f985253d348c58114715fdd04`。

### judson_sets

https://raw.githubusercontent.com/twjudson/aata/3069910e3ded72ff5e18837a97a0e810c92790e2/src/sets.xml

访问：2026-10-27T15:57:44.026501+00:00；HTTP 200；verified_http_200。

字节数：97708；SHA-256：`fa1d972edf851618fd869a7a1e5ff1dbcf7a9e5135f603087aff4bc418131b15`。

### judson_front

https://raw.githubusercontent.com/twjudson/aata/3069910e3ded72ff5e18837a97a0e810c92790e2/src/frontmatter.xml

访问：2026-10-27T15:57:44.027274+00:00；HTTP 200；verified_http_200。

字节数：12931；SHA-256：`addf82ea52f863a28a6cf9372e7a42945c77cf36448ed99ce709a53dab6cfa23`。

### judson_copying

https://raw.githubusercontent.com/twjudson/aata/3069910e3ded72ff5e18837a97a0e810c92790e2/COPYING

访问：2026-10-27T15:57:44.027944+00:00；HTTP 200；verified_http_200。

字节数：427；SHA-256：`b7d47749512a424173f6a20daeea7b00f36b9f5ef95c25930fdbc3bd549b8983`。

### lean_rat_basic

https://raw.githubusercontent.com/leanprover/lean4/v4.24.0/src/Init/Data/Rat/Basic.lean

访问：2026-10-27T15:57:44.339523+00:00；HTTP 200；verified_http_200。

字节数：12914；SHA-256：`f92a643905d91f93d10026264553362081b328b8755f9d7ff2f770bc3bdf0755`。

### lean_license

https://raw.githubusercontent.com/leanprover/lean4/v4.24.0/LICENSE

访问：2026-10-27T15:57:44.347676+00:00；HTTP 200；verified_http_200。

字节数：9160；SHA-256：`8b28515ffffc5c0fe2807d8ae3735b00b324d9b7ce807dd63ff6ac8922fbce7e`。

### mathlib_rat_defs

https://raw.githubusercontent.com/leanprover-community/mathlib4/v4.24.0/Mathlib/Data/Rat/Defs.lean

访问：2026-10-27T15:57:44.434777+00:00；HTTP 200；verified_http_200。

字节数：10985；SHA-256：`1308b329af093a43fcf6254a912ac90106aa7b9740999deedfd2fa57bed0fb41`。

### mathlib_license

https://raw.githubusercontent.com/leanprover-community/mathlib4/v4.24.0/LICENSE

访问：2026-10-27T15:57:44.440626+00:00；HTTP 200；verified_http_200。

字节数：11357；SHA-256：`b40930bbcf80744c86c46a12bc9da056641d722716c378f5659b9e555ef833e1`。

### lean_rat_lemmas

https://raw.githubusercontent.com/leanprover/lean4/v4.24.0/src/Init/Data/Rat/Lemmas.lean

访问：2026-10-27T15:59:34.566860+00:00；HTTP 200；verified_http_200。

字节数：45941；SHA-256：`79f153962f148a08747db7d5c142a9d1990e90aec7dd7d8a228788f2c8bcd2d5`。

## 核查限制

- 未运行Lean/mathlib形式验证，未声称本书已获机器证明。
- Judson整域分式域与本书正分母整数对的构造范围不同；其阿贝尔群加法性质留作读者验证。
- Lean Rat为规范数据结构，与书稿等价类之间须用规范代表唯一性连接。
- mkRat零分母返回零属于程序约定，本书不得据此允许零分母。
- 来源文件还含乘法、序或倒数内容，本次未将这些结论登记为本批书稿已写或已审。
- 未取得排版PDF；不猜页码，只定位固定源码标识、声明名和实际行号。
- 具体配套代码API及其输出尚未在本次来源核查中验证。

第三方文本仅暂存/tmp/integratedmath-rationals-audit供核查；仓库永久产物仅本JSON和配套Markdown元数据、许可短摘与原创摘要。
