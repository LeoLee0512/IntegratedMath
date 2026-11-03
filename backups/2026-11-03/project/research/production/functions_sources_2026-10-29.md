# 函数定义、限制与复合：公开来源核验

核验日期：2026-10-29 UTC。11次公开请求全部HTTP200；两个独立系列。源码只做阅读交叉核验，没有运行Lean验证书稿。

B2.1 集合、笛卡尔积、三数据函数、空集与像；B2.2 同类型函数相等、限制定义域、严格类型复合、恒等与结合、限制相容。

## 网络与使用边界

继承代理与TLS验证，只读公开文件，未绕限制；第三方完整响应仅在/tmp，仓库只收原创审计和来源元数据。

实际环境observations_current为true，网络状态enforced；本机restricted允许github.com和raw.githubusercontent.com。使用正常代理与TLS验证，无登录或绕过。

## [FUN-JUDSON] Abstract Algebra: Theory and Applications

Annual Edition 2026，前言August 4, 2026；commit 3069910e3ded72ff5e18837a97a0e810c92790e2

作者：Thomas W. Judson。

许可：GFDL-1.3-or-later为本次核到的共同可用范围。COPYING写1.3或以后；前言写1.2或以后。共同范围1.3或以后；均无不变章节、封面文本要求。

- **src/sets.xml，sets-subsection-cartesian-products，行615–684**：笛卡尔积定义为有序对集；函数表述为f⊆A×B的特殊关系，每个a∈A恰有一个b∈B；像f(A)⊆B。未明确将(A,B,G)三元组作为对象本身。
- **src/sets.xml，行758–764**：正式复合条件为f:A→B、g:B→C，值为g(f(x))。前导散文说range作为下一个domain，但前文range已定义为f(A)，且可严格小于B；不采用那句模糊表述。
- **src/sets.xml，行883–941**：正式给f:A→B,g:B→C,h:C→D的结合律，并实际逐点展开h(g(f(a)))证明。本书还须核两侧定义域/目标集合相同才能由逐点相等推出三数据相等。
- **src/sets.xml，行354–356、635–645**：包含空集及与空集的积说明；本次未取得其完整空函数分类定理，书稿需自证固定目标唯一性。

## [FUN-LEAN-MATHLIB] Lean 4 function primitives and mathlib function, restriction, image APIs

Lean4 v4.24.0；mathlib4 v4.24.0

各文件作者：

- `lean_function`：Leonardo de Moura、Mario Carneiro。
- `mathlib_function_defs`：Leonardo de Moura、Jeremy Avigad、Haitao Zhang。
- `mathlib_function`：Johannes Hölzl、Mario Carneiro。
- `mathlib_restrict`：Jeremy Avigad、Andrew Zipperer、Haitao Zhang、Minchao Wu、Yury Kudryashov。
- `mathlib_image`：Jeremy Avigad、Leonardo de Moura。

许可：Lean与mathlib源码均为Apache-2.0，已读版本对应LICENSE及源文件声明。

- **Lean src/Init/Prelude.lean，id行38、Function.comp行41–49**：恒等类型α→α；复合g:α→β后接f:β→δ，返回α→δ。类型化函数，与本书集合三元组编码不同。
- **Mathlib/Logic/Function/Defs.lean，Function.comp_assoc行48–49；Mathlib/Logic/Function/Basic.lean，hfunext行50起**：结合律对匹配的中间类型成立，证明为rfl。普通函数相等同一类型，跨类型需要额外的异质相等处理；不把Lean类型等同于集合目标三数据的现成构造。
- **Mathlib/Data/Set/Restrict.lean，Set.restrict、restrict_eq、restrict_id、restrict_eq_iff，行27–43**：限制定义域以子类型实现，目标不变；restrict_id为Subtype.val即包含映射，而不是类型不同的子集恒等。限制相等仍按共同子类型逐点检查。
- **Mathlib/Data/Set/Restrict.lean，restrict₂、restrict₂_comp_restrict、restrict₂_comp_restrict₂，行100–112**：子集s⊆t与t⊆u的嵌套限制相容性有明确声明与rfl证明；本书集合限制需展开相同逻辑，不省目标集合。
- **Mathlib/Data/Set/Restrict.lean，range_restrict行49–50；Mathlib/Data/Set/Image.lean，image_comp行216、image_empty行243**：限制后的全像等于原函数对子集的像；复合像为逐次像；空集像为空集。这些源码只交叉核条件与结论。

## 本书约定与独立条件核对

- 明确采用函数三数据(A,B,G)，G⊆A×B，对每个a恰有一个输出。相等必须A=A′、B=B′、G=G′；共同域目标下逐点相等才等价于函数相等。Judson图式定义不直接替本书证明这条约定。
- 同一图G={(0,0)}可配目标{0}或{0,1}；按本书约定这两个函数不同。像是{0}，不应混作两种目标。
- 固定B时∅→B唯一，图只能为空且全称唯一条件空真；B改变时三数据改变。若A非空而B为空，任选a∈A将不存在输出。
- 限制f|S=(S,B,{(x,y)∈G:x∈S})；S⊆A保障每输入唯一值，目标B保持不变，故(id_A)|S:S→A是包含映射，若S不等于A就不能与id_S直接相等。
- 严格类型复合只先定义f:A→B和g:B→C。即使f(A)⊆D，若后函数定义域D不同于B，不能直接使用本批这一复合定义；可后续显式改目标或加入包含映射。
- 复合的每输入输出由f的存在唯一性和g的存在唯一性连续给出；图定义为{(a,c)∈A×C:存在b∈B,(a,b)∈Gf且(b,c)∈Gg}。不借选择公理为任意一族选择多个非唯一值。
- 恒等id_A=(A,A,{(a,a):a∈A})；复合左右单位及结合律先核相同域/目标，再逐点展开。空域时仍适用。
- (g∘f)|S=g∘(f|S)，S⊆A，双方S→C；嵌套限制(f|S)|T=f|T，T⊆S⊆A，目标仍B。
- 像f(S)={b∈B:存在a∈S使(a,b)∈G}需S⊆A；由无见证得f(∅)=∅，从每个输入有输出得f(A)=∅当且仅当A=∅。不涉及实数或完备性。

## 分类定位

B2.1、B2.2的单元顺序号为22、23，主挂第63部分97-XX、第529章97Ixx的97I20“映射与函数（教育方面）”。97E60、03E20只作交叉定位，不在其所属章重复登记正文完成度。26A03实际涵盖极限及直线初等拓扑，不用于本批入口。

## 请求证据

字节数与SHA-256按本次响应原始字节计算；精确UTC时间和最终URL见JSON。

- `judson_copying`：HTTP 200，427字节；SHA-256 `b7d47749512a424173f6a20daeea7b00f36b9f5ef95c25930fdbc3bd549b8983`。
  https://raw.githubusercontent.com/twjudson/aata/3069910e3ded72ff5e18837a97a0e810c92790e2/COPYING
- `judson_front`：HTTP 200，12931字节；SHA-256 `addf82ea52f863a28a6cf9372e7a42945c77cf36448ed99ce709a53dab6cfa23`。
  https://raw.githubusercontent.com/twjudson/aata/3069910e3ded72ff5e18837a97a0e810c92790e2/src/frontmatter.xml
- `judson_sets`：HTTP 200，97708字节；SHA-256 `fa1d972edf851618fd869a7a1e5ff1dbcf7a9e5135f603087aff4bc418131b15`。
  https://raw.githubusercontent.com/twjudson/aata/3069910e3ded72ff5e18837a97a0e810c92790e2/src/sets.xml
- `lean_function`：HTTP 200，223109字节；SHA-256 `a590e5b64fdaf40d4a4cc5cc123b4056bd152330ff608072de27e54094609632`。
  https://raw.githubusercontent.com/leanprover/lean4/v4.24.0/src/Init/Prelude.lean
- `lean_license`：HTTP 200，9160字节；SHA-256 `8b28515ffffc5c0fe2807d8ae3735b00b324d9b7ce807dd63ff6ac8922fbce7e`。
  https://raw.githubusercontent.com/leanprover/lean4/v4.24.0/LICENSE
- `mathlib_function`：HTTP 200，48376字节；SHA-256 `7d75d2a6f0510469afcaab5f9809e9ec2c2811b8db1a13dbd43a5b37f53616f3`。
  https://raw.githubusercontent.com/leanprover-community/mathlib4/v4.24.0/Mathlib/Logic/Function/Basic.lean
- `mathlib_function_defs`：HTTP 200，3378字节；SHA-256 `3295d86ee02840f55476323ab75de7b230f7f963e8ea9c4aba6c951c9df7aa6b`。
  https://raw.githubusercontent.com/leanprover-community/mathlib4/v4.24.0/Mathlib/Logic/Function/Defs.lean
- `mathlib_image`：HTTP 200，54229字节；SHA-256 `eb705a539daba1e0dce45498e637d64c9e48d292e57ee0e279ffceba01b4b629`。
  https://raw.githubusercontent.com/leanprover-community/mathlib4/v4.24.0/Mathlib/Data/Set/Image.lean
- `mathlib_license`：HTTP 200，11357字节；SHA-256 `b40930bbcf80744c86c46a12bc9da056641d722716c378f5659b9e555ef833e1`。
  https://raw.githubusercontent.com/leanprover-community/mathlib4/v4.24.0/LICENSE
- `mathlib_restrict`：HTTP 200，11231字节；SHA-256 `da98c61fa2df86265538163caeb957d0e663a8275cc8910f0e77f0df5f8e4593`。
  https://raw.githubusercontent.com/leanprover-community/mathlib4/v4.24.0/Mathlib/Data/Set/Restrict.lean
- `mathlib_set_function`：HTTP 200，54997字节；SHA-256 `19b9a1f32b200d8c84102f87ed77422fc49729067279bad6e2cdae040d2b36b8`。
  https://raw.githubusercontent.com/leanprover-community/mathlib4/v4.24.0/Mathlib/Data/Set/Function.lean

## 未核事项

- 不把图式函数与三元数据函数两种约定混用。
- 没有运行Lean或形式验证书稿。
- 没有从先修单元声称严格集合论公理与有序对集合论构造已经完成，正文需明示采用的朴素集合背景。

不分发教材正文、题干、图或第三方源码。仅本审计原创摘要、URL、许可短摘、版本与响应哈希入库。
