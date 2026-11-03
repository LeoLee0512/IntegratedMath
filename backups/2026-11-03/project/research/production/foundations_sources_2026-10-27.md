# 基础材料公开来源核验与教学审查准备

核验日期：2026-10-27。范围限于自然数归纳与递归、十进制位值、带余除法。先读取并沿用本仓库 `research/ch01_source_checks.json` 和 `.md` 的已知来源，再检查当前公开资料。实际请求元数据、时间和散列见同名 JSON。

本轮共发出 16 次公开 HTTPS 只读请求：13 次取得 HTTP 200，3 次是猜测源码文件路径的 HTTP 404。读取公开目录后找到了对应实际文件。没有绕过代理、登录墙或访问控制。环境状态中的网络策略状态为 `unknown`，不能写成已确认执行；可访问性只按每次实际响应记录。

## 可用于正文的来源

### FND-OPENSTAX：《Prealgebra 2e》

作者：Lynn Marecek、MaryAnne Anthony-Smith、Andrea Honeycutt Mathis。出版项目：OpenStax，Rice University。作者姓名由实际取得的[前言](https://raw.githubusercontent.com/openstax/osbooks-prealgebra-bundle/main/modules/m81241/index.cnxml)中 “About the Authors / Senior Contributing Authors” 核对，CNXML 标识为 `eip-653`。

[官方项目](https://github.com/openstax/osbooks-prealgebra-bundle)的[许可证](https://raw.githubusercontent.com/openstax/osbooks-prealgebra-bundle/main/LICENSE)与[本书集合元数据](https://raw.githubusercontent.com/openstax/osbooks-prealgebra-bundle/main/collections/prealgebra-2e.collection.xml)均已取得，声明 **CC BY-NC-SA 4.0**。不能把这个当前版本称为允许无条件商业再利用的资料。

实际数学定位：[Introduction to Whole Numbers，模块 m81243](https://raw.githubusercontent.com/openstax/osbooks-prealgebra-bundle/main/modules/m81243/index.cnxml)。

| 核对内容 | 活动正文定位 | 结果与限制 |
|---|---|---|
| 十进制位值 | “Identify the Place Value of a Digit”，`fs-id1883656` | 明确相邻数位左边单位值是右边的十倍。这里只核对位值意义，未据此认定任意底数表示的存在唯一性已被证明。 |
| 占位零 | “Use Place Value to Write Whole Numbers”，`fs-id1339359` | 明确在需要的位置写零；书稿须独立区分内部占位零与规范表示中的前导零。 |
| 自然数名称 | “Identify Counting Numbers and Whole Numbers”，`fs-id1830385` | 该书将 counting/natural numbers 从 1 起，将含零者称 whole numbers。本书若采用自然数含零的约定，必须明示，不能说所有教材约定相同。 |

英文教材按千、百万等三位分组读数，不能直接替代汉语按万、亿等单位组织的读法；中文例子需另外核查。

### FND-LEVIN：Oscar Levin，《Discrete Mathematics: An Open Introduction》

[官方项目](https://github.com/oscarlevin/discrete-book)。当前 [bookinfo](https://raw.githubusercontent.com/oscarlevin/discrete-book/master/source/bookinfo.ptx) 标识 `dmoi-4`，说明为 2024 年发行的第四版。[LICENSE](https://raw.githubusercontent.com/oscarlevin/discrete-book/master/LICENSE) 实际取得，明确第四版及以后的材料为 **CC BY-NC-SA 4.0**；已发行第三版及以前版本的 **CC BY-SA 4.0** 不能套用于当前活动源码。

1. [Proof by Induction](https://raw.githubusercontent.com/oscarlevin/discrete-book/master/source/sec_seq-induction.ptx)：其中 “Formalizing Proofs / Induction Proof Structure”，XML 标识 `subsec_induction-formproofs`，明确基例和对所有合适下标成立的归纳步；“Recursive Reasoning” 的标识为 `subsec_induction-recursion`。这些内容可作教学结构参考。多米诺式直观没有从更弱公理证明归纳原理；本书应说明把归纳原理作为哪一层基础规则采用。
2. [Describing Sequences](https://raw.githubusercontent.com/oscarlevin/discrete-book/master/source/sec_seq-basics.ptx)：根标识 `sec_seq_intro`，实际定义 “Recursive definition” 同时要求递推关系与初始条件。它没有给出适用于任意隐式或非线性递推的一般存在唯一性定理；不能把该入门说明扩大使用。
3. [Introduction to Number Theory](https://raw.githubusercontent.com/oscarlevin/discrete-book/master/source/sec_addtops-numbth.ptx)：“Divisibility / The Division Algorithm”，根标识 `sec_addtops-numbth`。**发现原文声明框有省略：给出带余分解及余数范围，却在“任意整数”的表述中未明确排除零除数，且该框没有陈述唯一性。** 因此不把它作为完整带余除法定理已经核对无误的依据。

本书自然数版必须写正除数；整数版必须说明除数条件与余数范围，独立证明存在性和唯一性。可信来源同样需要逐项检查，不能因为署名可信便照搬遗漏。

### FND-LEAN：Lean 4 核心自然数定义与除法源码

[官方项目](https://github.com/leanprover/lean4)。`Init.Prelude` 文件头署 Leonardo de Moura、Mario Carneiro；`Init.Data.Nat.Div.Basic` 文件头署 Leonardo de Moura。两份文件头均明确采用 **Apache 2.0**，与实际取得的[根许可证](https://raw.githubusercontent.com/leanprover/lean4/master/LICENSE)一致。

- [Init.Prelude](https://raw.githubusercontent.com/leanprover/lean4/master/src/Init/Prelude.lean)：本次读取第 1363–1385 行的 `inductive Nat` 明确零与后继构造；约第 1910、1931 行的 `Nat.add`、`Nat.mul` 给出沿第二变量的递归规则。这里只用作定义方向的另一视角核查，不要求零基础读者读程序。
- 同一文件第 2432 行的 `Nat.mod_lt` 显式要求除数为正，才给出余数严格小于除数。
- [Init.Data.Nat.Div.Basic](https://raw.githubusercontent.com/leanprover/lean4/master/src/Init/Data/Nat/Div/Basic.lean)：第 241 行 `Nat.div_add_mod` 给出商余分解恒等式；第 365 行 `Nat.div_eq_of_lt_le` 给出商的区间刻画。

**重要区别：**某个实现可以对零除数规定特殊返回值，使部分代数恒等式仍成立；这不意味着带余除法定理的正除数条件可以删去。书稿须以自己的数学定义为准。

上述行号仅定位本次下载、散列已记录的源码版本，不是印刷页码。只阅读了源码声明与实现，**没有运行 Lean 验证本书证明**，也没有验证整个源码项目可构建。

## 来源使用决定

所有资料仅用于核对标准概念、条件与教学安排，并作引用。正文证明、例题和练习独立编写；不把外部教材的题干、解答、图片或连续文段收入本书。公开可读与开放许可的再利用条件分别记录，不能混为一谈。临时取得的源码留在临时检查目录，报告只保存元数据、必要许可短语与独立摘要。

本轮未读取出版 PDF，不猜测页码；未完成一般集合论意义的自然数递归定理的证明。若本书暂采用该定理，须明确标注“采用的基础结论”，不能写成已在书内证明。

## 供作者使用的教学审查清单

- 入口从有限物品计数、逐个配对和“再加一个”开始；避免先用未定义的基数。
- 先说自然数含零的约定，再介绍后继、数字与数；加号、等号、字母、下标须在第一次使用时解释。
- 清楚分开采用的基础规则、定义、推导出的命题。后继单射、零不是后继、归纳原理不可隐身成为已证结论。
- 区分递归定义与归纳证明；初值和每一步的规则要完整，说明递归存在唯一性在哪里建立或被采用。
- 基例与归纳步下界一致，不能跳过从零到一；归纳假设只用于证明相邻一步的条件命题。
- 交换律、结合律、消去律、分配律的证明不得循环引用自身；引用前文时提供定位。
- 若用最小元或比较证明除法，先建立顺序与良序性质；不得暗中使用尚在证明的位值唯一性。
- 带余除法写明正除数，分别证明存在与唯一。算例和有限机器检查不能证明全部自然数的命题。
- 十进制说明数位、位权、占位零与前导零；规范表示不得带多余最高位零。
- 长除法既要解释每一步的公式，也要解释为什么结束。中文万、亿分组另行检查。

来源报告先交付；以下补记随后完成的教学审读，不改写作者正文。

## 随后完成的教学审读

已读取 `natural_numbers.md`、`natural_numbers_answers.md`、`place_value.md`、`place_value_answers.md`，共两个基础单元与16题答案。检查快照散列与时间见 JSON。

自然数加法 N1–N5、答案中的左消去律、乘法运算律依赖链和位值算例均未发现阻断数学错误；采用基础原则与书内已证结论区分清楚。未把这次阅读说成形式化验证。

已向主编提出以下可具体修订事项：

1. 将“函数括号表示输入范围”改为“括号中写本次输入的对象”，避免同定义域混淆。
2. 自然数题7现有反例只说明归纳基例不可省。若末句要断言两个任务都不可省，应另给“性质是该数等于零”的例子：基例真、零到一的传递失败、全称结论假。
3. 在位值单元首次正式算到六以前，补六为五的后继的命名；七至九也应明确命名，而不让数字的使用早于说明。
4. “归并”首次出现应作简明解释；复查时主编已经加入。

位值部分谨慎把203和23首先作为不同的位值表达讨论，而没有以这两个例子证明一般唯一性，这个边界应保留。最终插图生成、题解往返锚点、PDF公式及版面由合编环节检查；本组不提前宣称它们通过。
