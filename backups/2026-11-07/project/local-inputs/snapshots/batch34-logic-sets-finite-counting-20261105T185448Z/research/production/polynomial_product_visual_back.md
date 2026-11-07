# 第十八批多项式乘法：审阅版后段实际视觉复核

## 结论与实际范围

在主代理明确发出第十八批 READY 后，独立视觉复核者实际打开本次生成的 35 张接触表及 3 张单页图，共 38 张图。接触表覆盖《综合数学_基础续写审阅版》PDF 物理页 157–576，共 420 页；单页放大检查为物理页 317、575、576。所见范围没有阻断性交叠、裁切、越界或图文遮挡问题。这里的页码全部指 PDF 物理页，非页脚印刷页码。

这是本代理的限定范围视觉结论，不是整书验收声明，也不修改全局 QA 状态。页 1–156 以及主代理另外打开的单页不计入本报告的实际打开范围。其余三份 PDF 仅核对文件哈希与页数，不据此声称实际逐页阅读。

## QA 快照与版本绑定

本次图片读取在 READY 后进行；没有把此前批次或 QA 完成前的图片冒充本轮证据。读取及复核使用以下 QA 快照：

- 路径：`data/production/batch_validation.json`
- `validated_at`：`2026-10-29T18:52:22.601744+00:00`
- 快照状态：`automated_checks_passed`
- 快照 SHA-256：`08f7176fecc824747606dcb3b8ff5b5bc1f5aa3694eaa46363865cd51657d266`
- 快照记录规模：160 个源文件、43 个构建产物、681 张截图。

逐个重新计算下列四份 PDF 与 38 张实际打开图片的 SHA-256，全部与该快照相符。该快照哈希绑定的是本次复核时读取的 QA 文件；后续若增加独立审阅记录，不能用新 QA 文件的哈希倒替此处历史绑定。

| PDF | 页数 | SHA-256 |
|---|---:|---|
| `dist/综合数学.pdf` | 791 | `822fe9bcd5bc88b7b9c3ef85b475804635d4fda6e7b96c9eeb7d8450c4f2008e` |
| `dist/综合数学_基础续写审阅版.pdf` | 576 | `f975faf1801b6c7767d533c8cb3cbe838783ac73fa9ac1cde113634f34bc795c` |
| `dist/综合数学_完整数学目录.pdf` | 218 | `6cb12ea75b3c38217ab3e6a86004fc07400cae1bac31236355b3be9766881b55` |
| `dist/综合数学_第一章审阅版.pdf` | 31 | `53254c1d606eb037eb1dba3b856d254924debec51c3fe56283f5c9f4a606d1bd` |

## 所见情况

- 页 157–312：接触表所示的正文、公式、表格与既有插图排布正常，未见可辨识的越界、文字互压或页脚遮挡。页 183、184、200 等章节转换页下方有较大留白，但仍有正常内容与页码；本次不把留白判成缺页。
- 页 313–329：新乘法及乘积结构单元的正文、证明、练习和来源提示均可在接触表中定位，公式块与正文分隔正常。页 319 顶部有短小的跨页延续行；本代理只在接触表尺度观察该页，未将其当成标题或正文被裁掉，视为非阻断的分页观感问题。页 329 结束本单元后留白，页 330 转入答案部分。
- 页 330–522：答案区在接触表尺度未见排版阻断；新增乘法答案从页 508 开始，乘积结构答案从页 514 开始。页 522 为答案尾页，下方留白明显，所见最后公式与段落完整。
- 页 523–576：索引、来源及程序附录在接触表尺度未见越界。代码尾页（如 540、543、546、562、574）可有较大余白；可见文本不是在页边被截断。
- 单页 317（页脚 315）：新卷积配对图居中，行系数 1、−1、2 与列系数 0、3、六个格内乘积 0、3、0、−3、0、6 及索引和均能辨识；按 k=0、1、2、3 汇总的 0、3、−3、6 清楚。第五项为零的说明可见。图中标注没有重叠或裁切，图题及下方说明均处于页边距内；上方计算与结果记录也完整可见。
- 单页 575（页脚 573）：附录二十一的标题、说明、移位及卷积公式、次数公式、验证记录路径与末尾说明均在页内。目录路径与 JSON 文件名分行显示，没有向右越界。视觉检查不等同于执行这些接口或验证脚本。
- 单页 576（页脚 574）：短源文件从文档字符串、导入、移位函数至乘法双循环及最后的 `return normalize(coefficients)` 完整显示，缩进与右侧行尾清楚；源码结束后的较大留白没有遮掉后续可见代码。

## 实际打开的图片及哈希

接触表每张 1200×1760，含连续 12 页缩略图；35 张依次覆盖 157–576，无间隙。单页图每张 765×990。本表中的每一张均实际调用图像查看工具打开，不以路径列表、文字提取或哈希匹配替代视觉查看。

| 图片 | 尺寸 | SHA-256 |
|---|---|---|
| `build/learning_batch/screenshots/batch-contact-157.png` | 1200×1760 | `9440859cfad58539305a51bab71d7490bfe635143d702c25c15286d839d87ba3` |
| `build/learning_batch/screenshots/batch-contact-169.png` | 1200×1760 | `306e9aa870497943b50f4e1e16d6a82b52f93010ab0554a06c4179d523379811` |
| `build/learning_batch/screenshots/batch-contact-181.png` | 1200×1760 | `176cfa1a9a1f531c66fa77056d819763300e650d733733379ddc5feb60936444` |
| `build/learning_batch/screenshots/batch-contact-193.png` | 1200×1760 | `b358a92414846d769df311a74c57e0f2bdca59b8227ae881ab7d8ad99259a537` |
| `build/learning_batch/screenshots/batch-contact-205.png` | 1200×1760 | `1695eff62ed23758acfdb32606ea18aab6106becce20ec034bc338920f689663` |
| `build/learning_batch/screenshots/batch-contact-217.png` | 1200×1760 | `ccbbbf435cadae42401d75c5bebff3f6a32fbb681d5b151c624a07e3038be64a` |
| `build/learning_batch/screenshots/batch-contact-229.png` | 1200×1760 | `5773160393ab4305fafbab96ca918f5bbf40da15f9c4b024b75b0b6b7f2920cc` |
| `build/learning_batch/screenshots/batch-contact-241.png` | 1200×1760 | `fe627997c5c56c051803be510a0b8efe38f9e11a4eee7864881aa3cf1c48b4eb` |
| `build/learning_batch/screenshots/batch-contact-253.png` | 1200×1760 | `35e14a6500ec9e6c99d6ed2f0b37ea45c734bf3d18d7b32f6c0c243eb045f1a5` |
| `build/learning_batch/screenshots/batch-contact-265.png` | 1200×1760 | `f1c36d51e72a907a9eafcd1585f628d55566aaae4c3ac74d9abdcb8110e5d052` |
| `build/learning_batch/screenshots/batch-contact-277.png` | 1200×1760 | `3413bfb2fb0817f96e46a866669f79ee7d76a68b474e73d6075c5ba58e5dd7cf` |
| `build/learning_batch/screenshots/batch-contact-289.png` | 1200×1760 | `71b5da3d115aeb730434c290c5047177f09f029edf7f93e955c3999a2b6f5bad` |
| `build/learning_batch/screenshots/batch-contact-301.png` | 1200×1760 | `71dabdf675c2d02d3772376cd17078c8a44b3d076456cdee3cfb9321660b4ff6` |
| `build/learning_batch/screenshots/batch-contact-313.png` | 1200×1760 | `1d2e968c64cfed3721d56aa1b7b1127663e81260fbf7e38e0d56941d13737e5a` |
| `build/learning_batch/screenshots/batch-contact-325.png` | 1200×1760 | `fabb2a250b9b9ac1d76771b087892e9988ac30d13b1314813b4c0063332cdb92` |
| `build/learning_batch/screenshots/batch-contact-337.png` | 1200×1760 | `33d2ec08937d9d529b8c0f6946e931645d3a1b8a9ad4400236c5452f0178aad1` |
| `build/learning_batch/screenshots/batch-contact-349.png` | 1200×1760 | `7813202d54a932df390f013c07a62679cd89de1eae3863af0db269047698fefd` |
| `build/learning_batch/screenshots/batch-contact-361.png` | 1200×1760 | `2b3e6b21e176dfdd0f078959e49a5d30b59813dd73deaa4bd4e576ecca7d80ea` |
| `build/learning_batch/screenshots/batch-contact-373.png` | 1200×1760 | `aff049676e405fe797341688aee8d90a116a6fc679fb8b77818bdbc4c5ebf12d` |
| `build/learning_batch/screenshots/batch-contact-385.png` | 1200×1760 | `c3c8d8fbc6c73ac2191e476c93e1d1adfbff227d6055af46c4c51a7c45dacd51` |
| `build/learning_batch/screenshots/batch-contact-397.png` | 1200×1760 | `2a7f42a10b560105f84c0383373f24ae2f0b2583748cff434392710a24ee86a2` |
| `build/learning_batch/screenshots/batch-contact-409.png` | 1200×1760 | `3c0962977fe463a6c99cfd64fb2ed91e4e59a7863a31d39c21e97f20bd5467ef` |
| `build/learning_batch/screenshots/batch-contact-421.png` | 1200×1760 | `1e61068af49fbf417c70a83f9768b28740c208929265dae4f73c3701d92d3fa5` |
| `build/learning_batch/screenshots/batch-contact-433.png` | 1200×1760 | `03a53c210658fb87243df71ca228d3717ad5083167519ad3872fdad29bd987c9` |
| `build/learning_batch/screenshots/batch-contact-445.png` | 1200×1760 | `f8640eee20130e15845d7d84956d873f397b06e72b31f58a9c5b10ece68a4349` |
| `build/learning_batch/screenshots/batch-contact-457.png` | 1200×1760 | `bc04fb10d42fea0765ada52654fa102abb99950b440d95edf6807ed25a09335f` |
| `build/learning_batch/screenshots/batch-contact-469.png` | 1200×1760 | `8d006b6116f6d94e1e07fce34548f4784b4053120f1cd9024527ed1f294f7ab9` |
| `build/learning_batch/screenshots/batch-contact-481.png` | 1200×1760 | `d7d1383b370df3fee176477a31535904107ee74bac44e079ef3a7f03e56a0049` |
| `build/learning_batch/screenshots/batch-contact-493.png` | 1200×1760 | `e076a3714a1e133cee7cbdf0511f5edabfafda8949b4e573ed5526fc2e36335c` |
| `build/learning_batch/screenshots/batch-contact-505.png` | 1200×1760 | `f42653dbcf31895a8c6b6c40362bcbd3543c854a44d163d93a7df8212adab7ce` |
| `build/learning_batch/screenshots/batch-contact-517.png` | 1200×1760 | `4bb62c6ade8fd06bc35c2e54f0c6d35f5c6c4239423e295cfe58bc30da6ad186` |
| `build/learning_batch/screenshots/batch-contact-529.png` | 1200×1760 | `447f62cb2d761656ce45695b8c955b4c89f3c021cccaa6c53ea687083f39d45d` |
| `build/learning_batch/screenshots/batch-contact-541.png` | 1200×1760 | `92627a2112a58dd577fb39fa796d1acaa4644919c5786d42a5da4112fd004038` |
| `build/learning_batch/screenshots/batch-contact-553.png` | 1200×1760 | `436027b76522b15de533f9165a0244355c6a8de9075c404a4d6bff6b5e7e86b4` |
| `build/learning_batch/screenshots/batch-contact-565.png` | 1200×1760 | `55c9151282d9354979036fd41d1ab76e14e6c081b7e4cc702456893beb9fe74b` |
| `build/learning_batch/screenshots/batch-page-317.png` | 765×990 | `07dc791a819fa96e002fd44921b3a087a034512791cf395445c23147a83c6f4e` |
| `build/learning_batch/screenshots/batch-page-575.png` | 765×990 | `b0b7417ed85e94be52d7bee86f4e47c9477020757b78e2f7d1fb12b044a528a8` |
| `build/learning_batch/screenshots/batch-page-576.png` | 765×990 | `cbc6fce79f5f919d7a0e5268911444116f393ba273c7873f05e53aa1e57c0d7b` |

## 检查边界

接触表适合检查页面整体结构、明显溢出与图文位置，不能支持“每个字、每个公式符号都在实际显示尺寸重新读过”的结论。页 317、575、576 才进行了此次指定的单页放大检查；没有另称其他页已被本代理放大逐读。数学内容与完整 16 道答案的独立通读结论另见 `research/production/polynomial_product_pedagogy_review.md`，不由此处缩略图检查替代。

本轮没有执行附录 API、Lean 或数学测试，没有点击 PDF 链接，没有重新抓取外部来源，也没有实际读者试用。四份 PDF 的字节绑定、自动 QA 的既有结果和本报告实际看到的视觉范围分别陈述，不相互扩大为额外验证声明。
