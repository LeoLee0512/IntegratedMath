# B2.13—B2.14 最终PDF独立视觉审查：后半范围

审查者：pedagogy_visual。实际查看后证据核算时间：2026-10-29T18:37:19.196531+00:00。

## 结论与版本绑定

在下述实际打开的范围和尺度内，未发现阻断性的正文裁切、公式重叠、图文遮挡、表格出界或代码行越过页面边界。后半387页的33张联系表及4张单页通过本次视觉检查。此结论不是全书逐字放大校对，不代替数学审读、运行测试、PDF链接点击或用户验收，也不把第528章、97H20或任何部分标成完成。

本次先按主编要求等待新版自动验证及截图生成完成，收到明确READY后才开始打开图片，没有把旧截图当作本轮证据。实际读取 `data/production/batch_validation.json`：状态 `automated_checks_passed`，`validated_at` 为 `2026-10-29T18:34:29.983841+00:00`，含152份源文件、41份产物、641张截图的哈希记录。审查者独立计算下列四PDF、四份冻结书稿和37张实际打开截图的SHA-256，逐一与该QA记录一致。

读取时QA文件SHA-256：`30bab7ea6f62fa57a25806e72d0d9d18f126d35f8e8353925ca481e3bd118cac`。该哈希绑定本次读到的自动检查记录；主编后续补录人工视觉字段可能改变JSON字节，本报告仍以下列PDF和截图哈希绑定已看版本。没有修改或宣布全局QA验收。

## 实际打开的范围与尺度

实际通过 `view_image` 打开33张 `batch-contact` 联系表，起始页依次为157、169、181、193、205、217、229、241、253、265、277、289、301、313、325、337、349、361、373、385、397、409、421、433、445、457、469、481、493、505、517、529、541。连续覆盖审阅版PDF物理页157—543，共387页；前32张各12页、尺寸1200×1760像素，最后一张为541—543三页、尺寸1200×440像素。每个缩略页约313×405像素，主要检查版心、分页、图表位置及明显重叠、截断，不能据此声称每个字形、分数或上下标都已读清。

另外实际打开765×990像素单页：PDF300（书内页298，系数记录图及图注）、PDF541（书内页539，附录二十说明及报告路径）、PDF542（书内页540，代码上半）、PDF543（书内页541，代码末尾）。页码均优先按PDF物理页记录，避免与页脚页码混淆。

本报告未打开审阅版1—156页，也未打开其他三PDF的页面截图；其他PDF仅作同轮构建哈希绑定。新正文和新答案没有全部逐页放大；主编的其他视觉工作不计作本审查者的实际查看范围。检查前完整阅读四份冻结多项式书稿及既有教学报告，未发现新的文本内容阻断；该准备阅读不扩大本报告的视觉覆盖。

## 实际观察

157—278页：有理数后续、函数、方程、不等式及坐标内容在联系表尺度下保持版心；图表、题号、蓝色链接与正文可区分，未见明显重叠。PDF183、184、200等章或部分切换页下方留白较多，仍有内容和页码，接续页排版正常，列为非阻断分页密度现象。

279—313页：幂与有限和以及本批两单元正文、例题、习题连续，分步公式没有可见横向越界。PDF300单页中，五个索引列从0至4排列清楚：原记录1、0、2、0、0；规范记录前三实框及后两虚框；另一多项式前两实框1、2及后面补零虚框。索引一处不同系数着色可辨，实框与虚框的解释没有被裁切。图题、图14图注与下方正式定义段落间距正常，整图、图注及随后正文均在版心内。

314—492页：完整答案区域的题号、返回链接、说明段与公式在联系表尺度下连续。新记录答案从PDF479接入，线性运算答案从PDF485接入，最后零边界在PDF492结束；未见异常空白断页或覆盖页脚。PDF313只有末两题及大量下部留白，PDF492只有答案余段及下部留白，均为相邻内容接续中的非阻断分页现象；没有据此声称读清所有答案。

493—543页：插图索引、来源记录、说明及源码附录全部实际看过联系表。较密来源页和表格未见明显越界；代码缩进与语法配色清楚。PDF509、512、515等代码尾页留白较大，符合短尾段及下一附录另页开始的版式。没有把缩略代码可见性当作实现正确性或测试通过的证明。

PDF541单页确认附录二十的标题、系数分段式、求值式、运算系数式和解释均完整；报告目录 `research/production/` 与文件名 `rational_polynomial_basic_validation.json` 分行显示，两行都在版心内，没有长路径越过右边界。最后一段仍在页脚上方。PDF542能看见record、normalize、coefficient、same_polynomial、degree、evaluate及add开头的代码，异常字符串与右侧行尾完整；add余段正常接到PDF543。PDF543的terms生成、返回、scale及subtract全部可见，之后大块留白属于源代码结束后的余白，未见被截断的函数尾部。

未发现需要退回修改的视觉阻断。联系表不能可靠排除细微字距、单字缺字、所有细小分数或脚注问题；四张单页也仅达到现有765×990截图尺度，没有另行生成更高分辨率截图。

## 同轮PDF哈希

| 文件 | 页数 | SHA-256 |
| --- | ---: | --- |
| `dist/综合数学.pdf` | 758 | `ce03c5b1932c972bb570398feedcb12d1ab5f162d0d876de66903fa6b09c5553` |
| `dist/综合数学_基础续写审阅版.pdf` | 543 | `e82caf15a299323ad26a68a8907fbc52193faac87b3e2004612d06ed449c1f6c` |
| `dist/综合数学_完整数学目录.pdf` | 218 | `6cb12ea75b3c38217ab3e6a86004fc07400cae1bac31236355b3be9766881b55` |
| `dist/综合数学_第一章审阅版.pdf` | 31 | `53254c1d606eb037eb1dba3b856d254924debec51c3fe56283f5c9f4a606d1bd` |

## 四份冻结书稿绑定

以下四稿用于视觉准备和本轮版本核对，均与既有教学审查报告所列版本一致。

| 文件 | SHA-256 |
| --- | --- |
| `manuscript/foundations/polynomial_records.md` | `d243e9a7e7231f121182494b32a38f7799fd897beb4d3bd5f67431438846a8c5` |
| `manuscript/foundations/polynomial_records_answers.md` | `81a61101bd3382311ec4a460f6b9153279adc08c8f58e947589131c93a3783be` |
| `manuscript/foundations/polynomial_linear_operations.md` | `c7836f2dcb0684865109f3c44dc58eaea5ba434d9fd058f3e49b6686ad6a23f5` |
| `manuscript/foundations/polynomial_linear_operations_answers.md` | `e374e4b3051009476f113b4cf460cfddf7b335d20bf66668a08fb55799041427` |

## 实际打开截图的哈希

下列37张均位于 `build/learning_batch/screenshots/`。只列真正通过view_image打开并观察的图片，不把仅生成或仅计算哈希的图片计作已看。

| 文件 | 像素尺寸 | SHA-256 |
| --- | --- | --- |
| `batch-contact-157.png` | 1200×1760 | `9440859cfad58539305a51bab71d7490bfe635143d702c25c15286d839d87ba3` |
| `batch-contact-169.png` | 1200×1760 | `306e9aa870497943b50f4e1e16d6a82b52f93010ab0554a06c4179d523379811` |
| `batch-contact-181.png` | 1200×1760 | `176cfa1a9a1f531c66fa77056d819763300e650d733733379ddc5feb60936444` |
| `batch-contact-193.png` | 1200×1760 | `b358a92414846d769df311a74c57e0f2bdca59b8227ae881ab7d8ad99259a537` |
| `batch-contact-205.png` | 1200×1760 | `1695eff62ed23758acfdb32606ea18aab6106becce20ec034bc338920f689663` |
| `batch-contact-217.png` | 1200×1760 | `ccbbbf435cadae42401d75c5bebff3f6a32fbb681d5b151c624a07e3038be64a` |
| `batch-contact-229.png` | 1200×1760 | `5773160393ab4305fafbab96ca918f5bbf40da15f9c4b024b75b0b6b7f2920cc` |
| `batch-contact-241.png` | 1200×1760 | `fe627997c5c56c051803be510a0b8efe38f9e11a4eee7864881aa3cf1c48b4eb` |
| `batch-contact-253.png` | 1200×1760 | `35e14a6500ec9e6c99d6ed2f0b37ea45c734bf3d18d7b32f6c0c243eb045f1a5` |
| `batch-contact-265.png` | 1200×1760 | `f1c36d51e72a907a9eafcd1585f628d55566aaae4c3ac74d9abdcb8110e5d052` |
| `batch-contact-277.png` | 1200×1760 | `1e6a83e2aa5c71677af5f5289a59298566636528ae269e24c13f199edc39e0a2` |
| `batch-contact-289.png` | 1200×1760 | `71b5da3d115aeb730434c290c5047177f09f029edf7f93e955c3999a2b6f5bad` |
| `batch-contact-301.png` | 1200×1760 | `71dabdf675c2d02d3772376cd17078c8a44b3d076456cdee3cfb9321660b4ff6` |
| `batch-contact-313.png` | 1200×1760 | `2e2a52858f2adbec098302b82c2b2e0183bc530981b8dab302e2f7891ea12eea` |
| `batch-contact-325.png` | 1200×1760 | `2a2f3368c451038b6ae82db2457bb8d2e47190e0c81ea810d5dbe8f62719ec17` |
| `batch-contact-337.png` | 1200×1760 | `6bbc8d168688ce0c44013596e6e2a7b24a5e5d11381ae4f0c2dc00b3436dad4b` |
| `batch-contact-349.png` | 1200×1760 | `011cc905c297b563db4b32a2797f373552846cbb8e6a0f9d459cf72220e5c509` |
| `batch-contact-361.png` | 1200×1760 | `ab2ad329dd1a7e0e5242d3236a360a367d84729a5cd72292968296a1feb8028b` |
| `batch-contact-373.png` | 1200×1760 | `eac6b902c1b1a6586fd05ffc9f06bde4a47d5afec0c0bc1baa138c9b8a8807ba` |
| `batch-contact-385.png` | 1200×1760 | `054b77f1e0fba50023ea9b3da54d8b100915f20f1cb344052e3e7ed5204bdc47` |
| `batch-contact-397.png` | 1200×1760 | `4888775558bba5bb0183c5dab4d1013263c3a29b7edf1609262bb093a87f0aed` |
| `batch-contact-409.png` | 1200×1760 | `6952565f8d9168abf6ddf82de96ff0bd3dc21d964d745e34ec7a6e3aa4585386` |
| `batch-contact-421.png` | 1200×1760 | `24b7acd0da76d3b9f8aaadf4c8c6cbc5fa08c76acf63a8eefdb5a39680e4b565` |
| `batch-contact-433.png` | 1200×1760 | `90a84d3b8968dc40d6f02228ba67bfde5d5f433112f68cc4d59016edd0df2895` |
| `batch-contact-445.png` | 1200×1760 | `ac3142bcb8f1aa28ea9d1d04cf24d5b2a4597368914676b62c12c542baa91ea2` |
| `batch-contact-457.png` | 1200×1760 | `95392fc5bc8aca7b7ebc6afd948f44ec83cc125bea960576c1b09becb9cdd1a0` |
| `batch-contact-469.png` | 1200×1760 | `73079ad4e8fc586f0fd48f6054ea8e5caf4883000d3a860d6083f13dea969414` |
| `batch-contact-481.png` | 1200×1760 | `5f2ca15b6b278dcfbb88545086562c43a9f0329eee77cb558fd92586f96e30e5` |
| `batch-contact-493.png` | 1200×1760 | `a6956be7480ee92fb22db7f62c3799277a2e6819fa8fdbc6d52ff4e05f4950c2` |
| `batch-contact-505.png` | 1200×1760 | `c62590a261df6e28fb614fd73efdc47b0fcfc138d960234723a1bc216a1d0a30` |
| `batch-contact-517.png` | 1200×1760 | `0bdcd201d2bbde744da338e0b96778441c4cc7eb35d8b81ac575dff4bee57bfa` |
| `batch-contact-529.png` | 1200×1760 | `6c10688561811cb9967c29cfdbb2970d1adebc6bc5902d269230b5610444b850` |
| `batch-contact-541.png` | 1200×440 | `91be7b23948cf5f28c92a32d86fd7d7370242f35b0a48db771f5869a424eee4d` |
| `batch-page-300.png` | 765×990 | `399c5ea69986a0dfb48f9a42b37a1da78d245221628f01b1258ec0a90e21310a` |
| `batch-page-541.png` | 765×990 | `3bdb30daaf0eb44e160e5d27df11acbc0b1b10973ffb16852b07f8cd77ff04ff` |
| `batch-page-542.png` | 765×990 | `46c230418f01f011d4384aec0ce6f6271d5be178a0a9b1c684b7ffd5085aadde` |
| `batch-page-543.png` | 765×990 | `c4ecdcd9cf6f1e8386804862d9134d0a7f0a61afa529ba325cd63eed60e464cc` |

审查者只写本报告与临时证据清单，没有修改书稿、图片、PDF、截图、构建脚本、QA或台账，没有重跑构建或验证，没有提交、发布或推送。
