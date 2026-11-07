# 单射、满射、双射与逆函数来源审计（2026-10-29）

本记录核验公开来源的条件、证明链和许可；不是正文审稿通过证明，不授予第529章或97I20完成状态。范围为B2.3、B2.4，正文来源锚为 `inverse-functions-sources`。

读取云环境运行与网络指引、受限网络策略后，独立查询得到 current / enforced / running。通过继承代理和正常TLS验证，对以下固定版本公开文件实际发出13次请求，均HTTP 200；不需登录、未碰凭据。完整第三方响应仅存 `/tmp`。逐请求UTC时间、URL、字节数及SHA-256见同名JSON。

## 两个独立来源系列

### INV-JUDSON：Abstract Algebra: Theory and Applications

Annual Edition 2026；前言August 4, 2026；commit 3069910e3ded72ff5e18837a97a0e810c92790e2。

Thomas W. Judson 著。COPYING为GFDL 1.3或以后，frontmatter.xml行60为1.2或以后；共同范围采用GFDL-1.3-or-later，两处均无不变章节或封面文本要求。

- [sets-subsection-cartesian-products：三种映射性质](https://github.com/twjudson/aata/blob/3069910e3ded72ff5e18837a97a0e810c92790e2/src/sets.xml#L732)（src/sets.xml，行732–745）：满射量词对每个目标元素要求至少一个原像；单射从相同输出推出相同输入；双射兼具两者。
- [无编号XML theorem：复合的四条性质](https://github.com/twjudson/aata/blob/3069910e3ded72ff5e18837a97a0e810c92790e2/src/sets.xml#L883)（src/sets.xml，行883–954）：单射、满射、双射在匹配域目标的复合下保持。实际证明只展开结合与满射，单射部分留作练习；本书不能把该处当已读到全部证明。
- [双侧逆定义](https://github.com/twjudson/aata/blob/3069910e3ded72ff5e18837a97a0e810c92790e2/src/sets.xml#L958)（src/sets.xml，行958–979）：逆函数g:B→A须同时满足g∘f=id_A及f∘g=id_B。
- [无编号XML theorem：invertible iff one-to-one and onto](https://github.com/twjudson/aata/blob/3069910e3ded72ff5e18837a97a0e810c92790e2/src/sets.xml#L1090)（src/sets.xml，行1090–1124）：逆存在推出单射与满射；反向由满射给存在、单射给唯一，再定义每个b的唯一原像。书稿还需按三数据记录证明逆图合法及两复合等式。

### INV-LEAN-MATHLIB：Lean 4 function primitives and mathlib function, equivalence and preimage APIs

Lean4 v4.24.0；mathlib4 v4.24.0。

Lean核心文件作者Kim Morrison；mathlib各文件作者见JSON和文件头。两库许可均为Apache-2.0。

- [Function.Injective / Surjective / Injective.comp / Surjective.comp](https://github.com/leanprover/lean4/blob/v4.24.0/src/Init/Data/Function.lean#L53)（src/Init/Data/Function.lean，行53–68）：逐量词定义与复合保性证明均读到，满射复合逐次消去两个存在量词，不需为整族选择非唯一原像。
- [Function.LeftInverse / RightInverse / LeftInverse.injective / RightInverse.surjective](https://github.com/leanprover/lean4/blob/v4.24.0/src/Init/Data/Function.lean#L71)（src/Init/Data/Function.lean，行71–103）：左右逆按两个不同的逐点恒等式定义；左逆推出原函数单射，右逆推出原函数满射。
- [Function.Bijective / Bijective.comp / bijective_id](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Logic/Function/Defs.lean#L51)（Mathlib/Logic/Function/Defs.lean，行51–59）：双射定义为单射与满射的合取；复合与恒等保持双射。
- [LeftInverse.comp_eq_id / RightInverse.comp_eq_id / LeftInverse.eq_rightInverse](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Logic/Function/Basic.lean#L284)（Mathlib/Logic/Function/Basic.lean，行284–337）：同类型逐点式转为函数等式；任一左逆与任一右逆相等，证明利用结合与双单位律。
- [InvFun section / injective_iff_hasLeftInverse](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Logic/Function/Basic.lean#L365)（Mathlib/Logic/Function/Basic.lean，行365–409）：该段有[Nonempty α]前提，invFun使用Classical.choose与任意默认元素。不得删去非空条件，∅→非空集合单射却无反向函数。
- [surjInv / Surjective.hasRightInverse / bijective_iff_has_inverse](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Logic/Function/Basic.lean#L417)（Mathlib/Logic/Function/Basic.lean，行417–443）：surjInv为noncomputable并显式调用Classical.choose；双射逆判据可对照结论，但这里的实现不能用来宣称已在不采用选择公理的集合背景中证明任意满射有右逆。
- [Equiv.symm / left_inv' / right_inv'](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Logic/Equiv/Defs.lean#L148)（Mathlib/Logic/Equiv/Defs.lean，行148–158）：交换正反函数和两侧恒等证据定义逆等价，不需额外非空条件。
- [apply_symm_apply / symm_apply_apply / symm_trans_apply / symm_symm_apply](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Logic/Equiv/Defs.lean#L249)（Mathlib/Logic/Equiv/Defs.lean，行249–276）：双侧恒等、逆的逆以及复合逆的反序公式；trans方向按先f后g核查。
- [Set.preimage_comp / preimage_comp_eq / preimage_preimage](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Data/Set/Image.lean#L135)（Mathlib/Data/Set/Image.lean，行135–148）：原像的复合反序对任意类型匹配函数成立，不需双射。
- [image_preimage_subset / subset_preimage_image / preimage_image_eq / image_preimage_eq](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Data/Set/Image.lean#L393)（Mathlib/Data/Set/Image.lean，行393–409）：一般只含包含关系；单射支持原像像等式，满射支持像原像等式；不可省略相应条件。

## 按本书约定独立复核的推理边界

1. 沿用f=(A,B,G)。定义域、目标与图均是函数数据；Judson图式对象与Lean类型化函数不能直接替代本书三数据证明。单射只看同一图中输出的碰撞；满射还依赖所声明目标集合。
2. 固定B时空函数∅→B总单射；满射当且仅当B=∅，故双射也当且仅当B=∅。A≠∅时A→∅不存在，不能对不存在函数讨论性质。空集合上的恒等与逆仍合法。
3. 对f:A→B，翻转图H={(b,a)∈B×A:(a,b)∈G}：每个b有至少一个输出恰是f满射；每个b至多一个输出恰是f单射。因此(B,A,H)为函数当且仅当f双射，不从非唯一纤维任意选择。
4. 若g∘f=id_A，则f(a)=f(a′)经g得到a=a′。若f∘g=id_B，则每个b以g(b)为原像。若l是左逆而r是右逆，则l=l∘id_B=l∘(f∘r)=(l∘f)∘r=id_A∘r=r，所有中间类型明确。
5. 若f:A→B及g:B→C均双射，则f⁻¹∘g⁻¹:C→A；代入两侧分别得id_C与id_A，再用唯一性得(g∘f)⁻¹=f⁻¹∘g⁻¹。不能保持原函数顺序。
6. 任意f:A→B和T⊆B的原像是{x∈A:f(x)∈T}，不要求可逆。双射时它等于逆函数对T的像；f⁻¹(b)为元素、f⁻¹[T]为集合，不混用，亦不等于数的倒数1/f(b)。
7. 任意f:A→B、g:B→C、T⊆C，x∈(g∘f)⁻¹[T] iff g(f(x))∈T iff f(x)∈g⁻¹[T] iff x∈f⁻¹[g⁻¹[T]]。这是逐成员等价，无双射前提。
8. 改变目标为像f(A)可使新三数据函数满射，却不消除原有碰撞；例如{0,1}→{0}的常值函数仍非单射。单射限制到任意子集仍单射；满射限制可能失去原像。
9. 逻辑边界：已给定右逆推出满射没有选择需求；从任意满射同时挑选所有非唯一原像是另一原则。本书不把其普遍成立列作本批已证结果；双射的唯一原像图构造不要求这种选择。

## 使用方式与尚未完成事项

只核对数学事实、条件和证明结构；不复制教材的行文、图、例题、题干或源码。新正文、证明组织及16题题答由作者单元独立撰写，答案与正文分离。Judson图式函数、Lean类型化函数与本书(A,B,G)三数据约定分别记录，不假装不同对象模型完全相同。

没有运行Lean或对本书进行形式化证明；没有证明选择公理或从集合论公理重新构造全部对象。有限实现检查不能代替一般证明。来源审计、独立数学审稿、教学审稿、实际构建和视觉验收是不同证据。

分类只登记第63部分97-XX、第529章97Ixx的97I20；03E20/97E60仅交叉索引。新增第24、25单元后，若全部题答实际存在，则为25单元、200基础题加绪论14题，共214题；这些计数由正式构建验证，不在本来源审计中授予完成状态。
