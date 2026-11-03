# 第十八批前半卷与其他 PDF 选页实际视觉复核

自动 QA 时间：2026-10-29T18:52:22.601744+00:00。人工记录：2026-10-29T18:54:57.038495+00:00。

绑定 `data/production/batch_validation.json` 的自动通过版本，SHA-256：`08f7176fecc824747606dcb3b8ff5b5bc1f5aa3694eaa46363865cd51657d266`。当前页数：基础续写审阅版 576、完整版 791、第一章审阅版 31、完整数学目录 218。

实际通过图像查看工具重新逐张打开本批 13 张审阅版联系表，覆盖 PDF 页 1–156；另打开目录页 3、4、5 原尺寸截图，以及其余三份 PDF 的全部 6 张生成选页联系表（完整版 4 张、第一章及完整数学目录各 1 张）。共实际打开 22 张图像，没有把前批查看记录当作本批观察，也没有生成或修改截图、PDF、稿件或 QA。以下已看范围未发现阻断性裁切、重叠、缺图或明显可见乱码。

## 实际观察与尺度限制

- 审阅版前 156 页：封面、献词、章节入口、练习、公式、表格与已有插图均有正常内容；联系表尺度未见明显越界、重叠或丢失图像。第 24 页第一章末题之后和第 25 页部分入口之后的留白属于连续分页，不据留白推断缺页。
- 目录原尺寸页 3–5：点线、页码和缩进可读。第 4 页把 B2.11–B2.16 一起列在第 528 章续写标题下，新增 B2.15“移位、有限倒序与多项式乘法”及 B2.16“多项式乘法的结合、求值与次数”的标题未互相挤压。第 529 章的续写标记也保留。第 5 页从 B2.8 答案接续到 B2.16，再列来源和附录二至二十一；新多项式乘法来源、两单元答案和附录二十一入口完整，未另生孤立目录尾页。
- 完整版全部 43 个生成选页：封面、目录、分类列表、原章与续章入口、教学及答案入口均存在。PDF 第 528/536 页可见 B2.15/B2.16 入口，第 723/729 页可见相应答案入口；第 738 页插图来源表含新乘法图条目。第 790 页附录二十一说明、公式、分开的报告目录/文件名正常排列，第 791 页完整显示该模块代码并留有正常页末空白；未见明显代码截断。该观察仅为联系表尺度的布局核查，不宣称逐字验完程序。
- 第一章选页：封面、献词、分数插图和末页模拟代码存在。完整数学目录选页的标题、编号列表及末页条目可见，未发现明显重叠或越界。
- 12 页联系表为 1200 × 1760 像素，每页缩略图约 313 × 405 像素；完整版最后 7 页联系表高 1320，第一章及分类目录 4 页联系表高 880。目录单页按 765 × 990 原图打开。联系表可核整体分页和明显布局问题，不能替代全部单页原尺寸的细小字形、上下标、数学正确性或链接目的页检查。未打开的其余 PDF 页面不在本报告覆盖范围，相关数学审查与自动验收另记。

## 绑定的四份 PDF

- `dist/综合数学_基础续写审阅版.pdf`：`f975faf1801b6c7767d533c8cb3cbe838783ac73fa9ac1cde113634f34bc795c`
- `dist/综合数学.pdf`：`822fe9bcd5bc88b7b9c3ef85b475804635d4fda6e7b96c9eeb7d8450c4f2008e`
- `dist/综合数学_第一章审阅版.pdf`：`53254c1d606eb037eb1dba3b856d254924debec51c3fe56283f5c9f4a606d1bd`
- `dist/综合数学_完整数学目录.pdf`：`6cb12ea75b3c38217ab3e6a86004fc07400cae1bac31236355b3be9766881b55`

## 已打开的联系表与覆盖页

- `build/learning_batch/screenshots/batch-contact-001.png`；PDF 页 1–12；SHA-256 `db281f504044fc7da0d9664cea07197de6c554e8f1992a2ad57b820240e938e4`。
- `build/learning_batch/screenshots/batch-contact-013.png`；PDF 页 13–24；SHA-256 `66a120558c7c20a59281e28892bb59a6b7e651d614fdd62d2c9178ab2943470c`。
- `build/learning_batch/screenshots/batch-contact-025.png`；PDF 页 25–36；SHA-256 `9a54992e1135074b33323059a32b60b123766df97a0c268f6ed6a0ed536b8fe1`。
- `build/learning_batch/screenshots/batch-contact-037.png`；PDF 页 37–48；SHA-256 `4dbb2c2cc32cbc006ff223ce113d2d9b003cf788573dab71a8262c47ca7b31b8`。
- `build/learning_batch/screenshots/batch-contact-049.png`；PDF 页 49–60；SHA-256 `7c635238a67fc94ddcac9f57256c88c875a303b05bd0489a02134f49f4f297a1`。
- `build/learning_batch/screenshots/batch-contact-061.png`；PDF 页 61–72；SHA-256 `e0434767b148e6c96821c582145a825c441ae2d5533bad9bb86ba9f3380ab63f`。
- `build/learning_batch/screenshots/batch-contact-073.png`；PDF 页 73–84；SHA-256 `c71967fa136cf3b193473f5f015c642502a4d21b4c1d04b89e6630ad8620f6a8`。
- `build/learning_batch/screenshots/batch-contact-085.png`；PDF 页 85–96；SHA-256 `1e9a0d167ccd8dde58b507f59ff27582412ac80ed056f0256a7f12e952bcef1e`。
- `build/learning_batch/screenshots/batch-contact-097.png`；PDF 页 97–108；SHA-256 `384b33fb399602d1aee3bc9e2ce126f0b59656e3d80eecf6513c40e8532350cf`。
- `build/learning_batch/screenshots/batch-contact-109.png`；PDF 页 109–120；SHA-256 `46f7c465cde31053bea40cad0c6dbb0cba37e3da3e26f773ff0a47ebb9ff6214`。
- `build/learning_batch/screenshots/batch-contact-121.png`；PDF 页 121–132；SHA-256 `dcf006949d9e01c60d4debd0f786e98740083c046b1e3363956c5d51c6233bad`。
- `build/learning_batch/screenshots/batch-contact-133.png`；PDF 页 133–144；SHA-256 `c2cad88f455d9cd73435a5ed73840820fd6d87f8d4e923285c0b3bd13a1d49c9`。
- `build/learning_batch/screenshots/batch-contact-145.png`；PDF 页 145–156；SHA-256 `78a8c26d1edf933357c1e855e09773d7e7a41ed4ed3b3ae0fcc31d279bf3767d`。
- `build/learning_batch/screenshots/full-contact-001.png`；PDF 页 1、2、3、18、217、218、241、250、396、400、408、416；SHA-256 `1e6af0d5ad6600e7b5a014b99e35c1fb18edcbcdc2918856f7e01406caf4dbea`。
- `build/learning_batch/screenshots/full-contact-013.png`；PDF 页 426、432、439、447、455、461、470、477、485、494、501、511；SHA-256 `48c1eba04dc77a6502d6323b259d088c33af364d81ac926cf859b7d2b2865b70`。
- `build/learning_batch/screenshots/full-contact-025.png`；PDF 页 520、528、536、545、635、644、699、710、723、729、738、773；SHA-256 `5b172e4315eba24b4b5c38366414a03e8744b5520fffb34c8cbcaff57ea61376`。
- `build/learning_batch/screenshots/full-contact-037.png`；PDF 页 775、778、781、784、787、790、791；SHA-256 `71597730b3e01e1f7cb3c7bc039fde13780166c795c683b072a1479ed1ae6a2b`。
- `build/learning_batch/screenshots/ch01-contact-001.png`；PDF 页 1、2、16、31；SHA-256 `7951d2f2fe656285214fcad14c8939f8a79424d08b4a34f5963722a57603547d`。
- `build/learning_batch/screenshots/catalog-contact-001.png`；PDF 页 1、2、110、218；SHA-256 `1855dd0fa8213f41a22c7d4963a6eb12d30a6ba5f3c662a14752d1a23697b833`。

## 已打开的目录单页

- `build/learning_batch/screenshots/batch-page-003.png`：`357602d550b3a7b49780fe9d08284e1ae7619d9787b4a9a5758d9fe480905651`
- `build/learning_batch/screenshots/batch-page-004.png`：`0351515c0e28c2e40b2128ff0879a1eab55791c82942698293425b417a3cae13`
- `build/learning_batch/screenshots/batch-page-005.png`：`a4ed0f30dafb876409de9726463c4d7ae866705b2aaa07a2b275525d8edfa602`

落盘前独立重新计算四份 PDF 与全部 22 张已看截图的 SHA-256，并与打开前快照逐项比较，均一致；四份 PDF 哈希也与同一自动 QA 报告一致。QA 仍为上述自动通过时间。本报告只认证实际打开范围的视觉观察，不作为整章完成、形式证明或发布批准。
