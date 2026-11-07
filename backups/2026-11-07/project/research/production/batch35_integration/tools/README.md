# 第35批75单元builder/validator候选（未应用、未构建）

基于正式第34批工具：builder `efa3639ac6753e7b6fa45a5f3778121ce67b07962bc70f82329c7adbdb80efb1`，validator `14a36b325d52d9d1d8f3e3e597734aea399fa5f2969dd84cb8be85b14756ebaf`。后者已包括root的HTTP(S) `.md#`引用判断修复，本候选完整保留。配套登记来自`/tmp/frc-rfs-flc75-registration`，不是仍冻结的正式72项。

## 装配与真实分类

旧72篇教学正文及其顺序不改；尾部按约定FRC→RFS→FLC追加，学习号由导读映射B4.L1/B2.39/B4.L2，不改冻结稿标题。三段分别为：

| 单元 | 部分/章 | 部分锚 | 章段锚 |
|---|---|---|---|
| FRC，第73项 | 第11部分15-XX／第84章15Axx／15A03 | part-15 | chapter-84 |
| RFS，第74项 | 第63部分97-XX续／第528章97Hxx／97H20 | part-97-real-sums-continuation | chapter-528-rfs-continuation |
| FLC，第75项 | 第11部分15-XX续／第84章15Axx续／15A03 | part-15-combinations-continuation | chapter-84-combinations-continuation |

RFS前实际生成返回数学教育部分的标题，FLC前再返回线性代数部分；不把RFS放在线性代数标题下，也不为少标题换主分类。续写锚各唯一，不新增MSC部分/章/节。准确声明RFS不依赖FRC但FLC依赖二者；第84章及三个单元所属模块仍未完成。

同步75单元、627题答、21图与“七十五个基础桥接单元”。来源仍8G verified/10G pending/15原创，未改第一部分状态或稿源。目录总数仍63部分、534章、6006节。三篇正文已有frc-sources/rfs-sources/flc-sources，加入来源唯一锚检查；不复制外部正文或另造附录。

## 依赖与启动检查

source_hashes保留全部旧路径及其生成规则，再纳入三单元计划、来源及六份真实math/ped报告（作者记录仅为来源身份，不当独立签）；稿源两两随UNITS自动纳入。忽略缓存和preservation JSON不作为出版依赖、不收入分发。现有登记工具本身仍在输入哈希中。

启动函数改名check_batch35_prerequisites，builder与validator同步调用，位置仍在产物修改之前。要求75项与实际UNIT_SPECS顺序一致，旧B3三项及新三项的学习号/主章/主叶一致，新三项另外核part_code。原00B05核读及8/10/15计数、当前scope和八稿hash绑定检查保持。

本启动检查不是整部验收，也不替代真实文字审签载入；root应同步应用75登记/150审签并保全当前34批历史。当前正式72登记会被新guard拒绝，不能只覆盖两工具后开始构建。

## 保留检查及已实际执行的有限检查

AST比较：builder仅改source_hashes/compose_body/main并对原guard作有限更新及改名；validator仅改main/render_contacts；其余函数AST不变，旧分类表和21图不变。旧302个require调用中仅3条数量/章顺/部分顺断言更新；另加1条新段“部分→章→单元”包含关系，当前303条。所有旧scope披露、旧来源锚、算法复算、哈希、题答、目录、附录和视觉规则保留；正文接触图筛选增加新章和新题名。

`isolated_checks.json`实际运行原样提取的启动函数及两段章节位置检查（没有调用完整main/compose_body/build/validator/render）：75候选+实际8/10来源账通过；正式72、互换FRC/RFS、RFS错误part_code均拒。用候选中新导读原文和三篇真实稿件核84→528→84及11→63→11位置通过；故意把返回第63部分标题移到RFS后会被拒。24对题答及三个来源锚均实查。

这不是完整构建、样式、PDF分页、截图或视觉通过。当前未生成任何新书稿产物。`checks.json`为静态完整性，`isolated_checks.json`为上述有限执行范围，完整diff已逐段读过。

## root下一步

先封存当前34批，再依baseline核对正式版本。若当前工具又变，须按差异重新合并，不能覆盖新修复。应用75登记/审签及两工具后，旧75候选之外的其他草稿不得混入。是否能复用legacy第一章/目录只由既有严格增量输入/产物门槛判断；这里不预先宣布复用可行或验收通过。下一批须实际重建、核完整627题答、所有章节/部分回访、链接/图/字体/源哈希，并按新PDF哈希重新完成视觉审阅。
