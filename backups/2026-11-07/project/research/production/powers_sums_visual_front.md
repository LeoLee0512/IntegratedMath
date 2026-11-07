# 第十六批前半卷与其他 PDF 选页实际视觉复核

自动 QA 时间：2026-10-29T18:07:47.267548+00:00。人工记录：2026-10-29T18:13:47.344838+00:00。

绑定 `data/production/batch_validation.json` 的自动通过版本，SHA-256：`76294bcf11c87b2dd6805f788274c735e3a9af933b7f6baea4a061c9bd754c10`。当前页数：基础续写审阅版 510、完整版 725、第一章审阅版 31、完整数学目录 218。

实际通过图像查看工具逐张打开 13 张审阅版联系表，覆盖 PDF 页 1–156；另打开目录页 3、4、5 原尺寸截图，以及其余三份 PDF 的全部 5 张既有选页联系表。本次没有生成或修改截图、PDF、稿件或 QA。结论：以下已看范围未发现阻断性裁切、重叠、缺图或可见乱码。

## 实际观察与尺度限制

- 审阅版前 156 页：章标题、题目、公式、表格和已有插图整体排版连续；联系表中未见明显超出页界或互相覆盖。部分练习末尾留白属于现有分页，不构成缺页证据。
- 目录原尺寸页 3–5：第 529 章与第 528 章续写标题均标“续”，层级与原章一致，B2.11/B2.12 置于第 528 章续标题下。第 4 页答案目录接到第 5 页首行，之后继续附录二至十九，页面不是单独一条孤立目录页。点线、页码和缩进可读。
- 完整版选页：目录及正文的两次续章标题可见；新幂单元入口、有限和入口和新答案入口可见；图源表和附录十九首尾页面均有内容。第 725 页为连续代码尾页，剩余留白不表示截断。此处只作联系表尺度的排版检查，未据此声称逐字验完代码。
- 第一章选页：封面、献词、分数插图和末页代码存在；完整数学目录选页的标题、列表及末页条目正常。
- 联系表宽 1200 像素，每页缩略图约 313 × 405 像素；常规 12 页联系表为 1200 × 1760，4 页选页表为 1200 × 880。目录单页以 765 × 990 原图打开。联系表足以检查整体分页和明显布局问题，不足以逐字核对所有汉字、微小上下标或链接目标。未查看的其他 PDF 页不在本报告覆盖范围；数学证明、数值正确性和链接目的页依赖对应独立审稿及自动检查。

## 附带独立核查的验证器修正

`Image.c[1]` 替代文本中的 Math 节点按节点身份排除，Figure 可见 caption 和正文公式继续严格参与 HTML MathML 数量相等检查；同时记录 source_math_nodes 与 image_alt_math_nodes 以便审计。未将可见图注公式整体略过。“查看完整解答”加入现有合法标签识别，同目的页的断行标签可合并；目的页范围、答案/题目目的页判据及 278 对双向链接数量仍保留。未发现这两处修正放宽到跳过实际可见公式或取消链接检查。

## 绑定的四份 PDF

- `dist/综合数学.pdf`：`2e6098e9e867da90bcd3895ae7f92ddeeb8906f3c261c90b81a6c288c1c94d08`
- `dist/综合数学_基础续写审阅版.pdf`：`f9b152b7973e80b8eb14901cde42e7fb97199e2da68cdb0afece2858c0827abc`
- `dist/综合数学_完整数学目录.pdf`：`6cb12ea75b3c38217ab3e6a86004fc07400cae1bac31236355b3be9766881b55`
- `dist/综合数学_第一章审阅版.pdf`：`53254c1d606eb037eb1dba3b856d254924debec51c3fe56283f5c9f4a606d1bd`

## 已打开的联系表与覆盖页

- `build/learning_batch/screenshots/batch-contact-001.png`；审阅版 PDF 1–12；SHA-256 `1a5658bff7544fed1d76ee7ed2579e5fc9cfa46a0ab405239a4f06d9ba42a5ca`。
- `build/learning_batch/screenshots/batch-contact-013.png`；审阅版 PDF 13–24；SHA-256 `66a120558c7c20a59281e28892bb59a6b7e651d614fdd62d2c9178ab2943470c`。
- `build/learning_batch/screenshots/batch-contact-025.png`；审阅版 PDF 25–36；SHA-256 `9a54992e1135074b33323059a32b60b123766df97a0c268f6ed6a0ed536b8fe1`。
- `build/learning_batch/screenshots/batch-contact-037.png`；审阅版 PDF 37–48；SHA-256 `4dbb2c2cc32cbc006ff223ce113d2d9b003cf788573dab71a8262c47ca7b31b8`。
- `build/learning_batch/screenshots/batch-contact-049.png`；审阅版 PDF 49–60；SHA-256 `7c635238a67fc94ddcac9f57256c88c875a303b05bd0489a02134f49f4f297a1`。
- `build/learning_batch/screenshots/batch-contact-061.png`；审阅版 PDF 61–72；SHA-256 `e0434767b148e6c96821c582145a825c441ae2d5533bad9bb86ba9f3380ab63f`。
- `build/learning_batch/screenshots/batch-contact-073.png`；审阅版 PDF 73–84；SHA-256 `c71967fa136cf3b193473f5f015c642502a4d21b4c1d04b89e6630ad8620f6a8`。
- `build/learning_batch/screenshots/batch-contact-085.png`；审阅版 PDF 85–96；SHA-256 `1e9a0d167ccd8dde58b507f59ff27582412ac80ed056f0256a7f12e952bcef1e`。
- `build/learning_batch/screenshots/batch-contact-097.png`；审阅版 PDF 97–108；SHA-256 `384b33fb399602d1aee3bc9e2ce126f0b59656e3d80eecf6513c40e8532350cf`。
- `build/learning_batch/screenshots/batch-contact-109.png`；审阅版 PDF 109–120；SHA-256 `46f7c465cde31053bea40cad0c6dbb0cba37e3da3e26f773ff0a47ebb9ff6214`。
- `build/learning_batch/screenshots/batch-contact-121.png`；审阅版 PDF 121–132；SHA-256 `dcf006949d9e01c60d4debd0f786e98740083c046b1e3363956c5d51c6233bad`。
- `build/learning_batch/screenshots/batch-contact-133.png`；审阅版 PDF 133–144；SHA-256 `c2cad88f455d9cd73435a5ed73840820fd6d87f8d4e923285c0b3bd13a1d49c9`。
- `build/learning_batch/screenshots/batch-contact-145.png`；审阅版 PDF 145–156；SHA-256 `78a8c26d1edf933357c1e855e09773d7e7a41ed4ed3b3ae0fcc31d279bf3767d`。
- `build/learning_batch/screenshots/catalog-contact-001.png`；完整数学目录 PDF 1、2、110、218；SHA-256 `1855dd0fa8213f41a22c7d4963a6eb12d30a6ba5f3c662a14752d1a23697b833`。
- `build/learning_batch/screenshots/ch01-contact-001.png`；第一章审阅版 PDF 1、2、16、31；SHA-256 `7951d2f2fe656285214fcad14c8939f8a79424d08b4a34f5963722a57603547d`。
- `build/learning_batch/screenshots/full-contact-001.png`；完整版 PDF 1、2、3、18、217、218、241、250、363、400、408、416；SHA-256 `56fe995620f4fb22f13c9426b7a446955a671b3548b53e699b92753e7af6fd67`。
- `build/learning_batch/screenshots/full-contact-013.png`；完整版 PDF 426、432、439、447、455、461、470、477、485、494、501、512；SHA-256 `30a894c926fca11aa34c53f7361cfbd8c44d3e048d2df4a37a13dc01cbf1b785`。
- `build/learning_batch/screenshots/full-contact-025.png`；完整版 PDF 602、611、666、678、712、714、717、720、723、725；SHA-256 `77f78929edd8bf7a69d904bb3202071c2883936fc90f47812f1ea2391ac743d1`。

## 已打开的目录单页

- `build/learning_batch/screenshots/batch-page-003.png`：`357602d550b3a7b49780fe9d08284e1ae7619d9787b4a9a5758d9fe480905651`
- `build/learning_batch/screenshots/batch-page-004.png`：`a0b9e64c2715469e4b511c26131820e6b9dc325db0ea83c66b1bfb035ca9df74`
- `build/learning_batch/screenshots/batch-page-005.png`：`2bef848d040d4989241a980be65b62447e7dca992fb4e34634e2197311c6478c`

落盘前重新核对以上四份 PDF 与全部 21 张已看截图的 SHA-256，均与开始检查时快照一致；QA 仍为同一自动通过时间。
