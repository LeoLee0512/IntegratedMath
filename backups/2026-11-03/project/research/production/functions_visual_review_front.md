# B2.1—B2.2 批次独立前半视觉审查

记录编号：VIS-FUNCTIONS-FRONT-2026-10-29。审查者：geometry_history。实际审阅日期：2026-10-29（UTC）。仅在最终 QA 完成通知后实际打开本轮图片，未复用旧批截图代替查看。

所依据的 `data/production/batch_validation.json`：`validated_at=2026-10-29T15:58:59.961055+00:00`，状态 `automated_checks_passed`。下列四份 PDF 与二十张图片均独立计算 SHA-256，并与本次 QA 记录逐项匹配。

## 实际查看范围

所有页码均指 PDF 物理页码。

- 基础续写审阅版：13 张联系表 `batch-contact-001`、`013`、`025`、`037`、`049`、`061`、`073`、`085`、`097`、`109`、`121`、`133`、`145`，覆盖第 1—156 页；另打开第 3、4、5 页单页截图放大检查目录。
- 综合版：本轮全部两张选页联系表 `full-contact-001`、`full-contact-013`；所含页为 1、2、3、18、217、218、241、250、288、400、408、416、426、433、523、532、544、575。
- 第一章审阅版：`ch01-contact-001`，页 1、2、16、31。
- 完整数学目录：`catalog-contact-001`，页 1、2、110、218。

总计实际打开 17 张联系表及 3 张放大单页截图。审阅版第 157—360 页由主编另行审阅，不计入本报告的独立查看范围。

## 观察及结论

指定前半页面在联系表尺度内未见明显裁切、重叠、破损图片占位或裸露公式源代码。计数、集合重叠、分拍、方格与位值图均完整；表格、陈列式和题答入口保持在版心内。封面及献词留白符合该页用途。其余三份 PDF 的实际选页中，目录层级、正文、答案、图源表及代码块未见明显版面异常。

放大目录后，物理第 3、4 页的条目、引导点和页码可辨，对齐正常，没有压字或页脚覆盖。物理第 5 页只有“附录十二 有理数比较、绝对值与距离”“附录十三 比、比例与单位数值换算”“附录十四 有限函数表、限制与复合”三项，页下大幅留白。这是非阻断的分页疏松，三项文字与页码完整；本报告不建议为消除留白而继续压缩字号。此轮目录确为三页，不沿用上一批“两页目录”的结论。

结论：在实际分配范围和查看尺度内，未发现阻断交付的明显视觉缺陷；保留上述目录尾页留白观察。

## 局限

联系表检查针对整体布局，不能保证每个微小字形、上下标或公式内容逐字无误。只有目录三页在本审查中单页放大；本报告不将前半及选页抽查授予整本 PDF 全面认证，不替代数学、教学、许可及程序审查。新增函数正文、对应图、答案和代码的后半细节由主编另行记录，本报告不代认其查看结果。未更改正文或重跑构建。

## PDF 快照

| 文件 | 总页数 | SHA-256 |
|---|---:|---|
| `dist/综合数学_基础续写审阅版.pdf` | 360 | `809e4ecafecfc730244ec75b39b792bc5bf459af56d2ab2a6c3754214d6f3dc9` |
| `dist/综合数学.pdf` | 575 | `bb195f194864cacecbafd215081ea9be390b77380a6288f9a2874670c24cf408` |
| `dist/综合数学_第一章审阅版.pdf` | 31 | `53254c1d606eb037eb1dba3b856d254924debec51c3fe56283f5c9f4a606d1bd` |
| `dist/综合数学_完整数学目录.pdf` | 218 | `6cb12ea75b3c38217ab3e6a86004fc07400cae1bac31236355b3be9766881b55` |

## 实际打开的图片快照

以下路径均相对于 `build/learning_batch/screenshots/`。

| 图片文件 | SHA-256 |
|---|---|
| `batch-contact-001.png` | `7b4442b08f04df15f229237a5739365f6914034caa1b50720fea2eaf81a08100` |
| `batch-contact-013.png` | `66a120558c7c20a59281e28892bb59a6b7e651d614fdd62d2c9178ab2943470c` |
| `batch-contact-025.png` | `9a54992e1135074b33323059a32b60b123766df97a0c268f6ed6a0ed536b8fe1` |
| `batch-contact-037.png` | `4dbb2c2cc32cbc006ff223ce113d2d9b003cf788573dab71a8262c47ca7b31b8` |
| `batch-contact-049.png` | `7c635238a67fc94ddcac9f57256c88c875a303b05bd0489a02134f49f4f297a1` |
| `batch-contact-061.png` | `e0434767b148e6c96821c582145a825c441ae2d5533bad9bb86ba9f3380ab63f` |
| `batch-contact-073.png` | `c71967fa136cf3b193473f5f015c642502a4d21b4c1d04b89e6630ad8620f6a8` |
| `batch-contact-085.png` | `1e9a0d167ccd8dde58b507f59ff27582412ac80ed056f0256a7f12e952bcef1e` |
| `batch-contact-097.png` | `384b33fb399602d1aee3bc9e2ce126f0b59656e3d80eecf6513c40e8532350cf` |
| `batch-contact-109.png` | `46f7c465cde31053bea40cad0c6dbb0cba37e3da3e26f773ff0a47ebb9ff6214` |
| `batch-contact-121.png` | `dcf006949d9e01c60d4debd0f786e98740083c046b1e3363956c5d51c6233bad` |
| `batch-contact-133.png` | `c2cad88f455d9cd73435a5ed73840820fd6d87f8d4e923285c0b3bd13a1d49c9` |
| `batch-contact-145.png` | `78a8c26d1edf933357c1e855e09773d7e7a41ed4ed3b3ae0fcc31d279bf3767d` |
| `full-contact-001.png` | `42a567cf88d0f18b2a359470845fa944484873791386f2f1ca735484a90f72fa` |
| `full-contact-013.png` | `36b94564b2c6bae7ee3865c59c92344b9eb3902baf89d9cf61d7592f9258ea18` |
| `ch01-contact-001.png` | `7951d2f2fe656285214fcad14c8939f8a79424d08b4a34f5963722a57603547d` |
| `catalog-contact-001.png` | `1855dd0fa8213f41a22c7d4963a6eb12d30a6ba5f3c662a14752d1a23697b833` |
| `batch-page-003.png` | `357602d550b3a7b49780fe9d08284e1ae7619d9787b4a9a5758d9fe480905651` |
| `batch-page-004.png` | `866246a4a38025426f37b9b8eff0144af9ec20fd1c58d21142b5f4cdd528576d` |
| `batch-page-005.png` | `e4842acedc431d5807df7db7b3564e878eb05a453e6ce8fcfc57284e0ba56c2d` |
