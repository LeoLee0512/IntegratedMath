# 第十七批前半卷与其他 PDF 选页实际视觉复核

自动 QA 时间：2026-10-29T18:34:29.983841+00:00。人工记录：2026-10-29T18:37:21.856319+00:00。

绑定 `data/production/batch_validation.json` 的自动通过版本，SHA-256：`30bab7ea6f62fa57a25806e72d0d9d18f126d35f8e8353925ca481e3bd118cac`。当前页数：基础续写审阅版 543、完整版 758、第一章审阅版 31、完整数学目录 218。

实际通过图像查看工具逐张打开 13 张审阅版联系表，覆盖 PDF 页 1–156；另打开目录页 3、4、5 原尺寸截图，以及其余三份 PDF 的全部 6 张选页联系表（完整版 4 张、第一章及完整数学目录各 1 张）。本次共实际打开 22 张图像，没有生成或修改截图、PDF、稿件或 QA。以下已看范围未发现阻断性裁切、重叠、缺图或明显可见乱码。

## 实际观察与尺度限制

- 审阅版前 156 页：封面、献词、章节入口、题目、公式、表格与已有插图均有正常内容；联系表尺度未见明显越界、重叠或丢失图像。第 24 页最后一道第一章练习后及第 25 页部分入口处的留白属于连续分页，不据留白推断缺页。
- 目录原尺寸页 3–5：点线、页码和缩进清楚。第 4 页将 B2.11–B2.14 放在第 528 章唯一的续写标题下；第 529 章续标题也保留“续”，无新增同级分类章号。第 5 页从 B2.10 答案继续列到 B2.14 答案，再列参考资料和附录二至二十；新多项式来源条目及附录二十入口均完整，没有单独产生仅一条目录的尾页。
- 完整版全部 38 个生成选页：封面、目录及分类列表、原章与续章标题、教学入口和答案入口均存在。新 B2.13/B2.14 入口分别在 PDF 第 511/520 页选页中可见；第 694 页含 B2.13 答案入口。第 708 页插图来源表可见新增系数记录图条目；第 756 页为附录二十说明、公式和分开的报告目录/文件名，第 758 页为代码末页并正常结束，未见被裁掉的代码。这里只按联系表尺度判断布局，未据此声称逐字核完程序。
- 第一章选页：封面、献词、分数插图与末页模拟代码正常存在。完整数学目录选页中的标题、编号列表和最后一页条目可见，未见明显重叠或越界。
- 常规联系表宽 1200 像素、12 页表高 1760 像素，每页缩略图约 313 × 405 像素；4 页选页表高 880，完整版最后 2 页联系表高 440。目录单页按 765 × 990 原图打开。联系表适合核整体分页及明显布局问题，不能替代每页原尺寸微小字形、上下标、数学证明或链接目的页检查。没有把未打开的其余 PDF 页计入本报告；这些边界与相应审稿及自动检查分别记录。

## 绑定的四份 PDF

- `dist/综合数学_基础续写审阅版.pdf`：`e82caf15a299323ad26a68a8907fbc52193faac87b3e2004612d06ed449c1f6c`
- `dist/综合数学.pdf`：`ce03c5b1932c972bb570398feedcb12d1ab5f162d0d876de66903fa6b09c5553`
- `dist/综合数学_第一章审阅版.pdf`：`53254c1d606eb037eb1dba3b856d254924debec51c3fe56283f5c9f4a606d1bd`
- `dist/综合数学_完整数学目录.pdf`：`6cb12ea75b3c38217ab3e6a86004fc07400cae1bac31236355b3be9766881b55`

## 已打开的联系表与覆盖页

- `build/learning_batch/screenshots/batch-contact-001.png`；PDF 页 1–12；SHA-256 `a502166f32625684be1a1af7385916d3f2f06de2377697e54e9783e822bb44aa`。
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
- `build/learning_batch/screenshots/full-contact-001.png`；PDF 页 1、2、3、18、217、218、241、250、380、400、408、416；SHA-256 `3e8cebe175e6434cc697f8ef7fded8ad5a058bbb20a3ce99cb77413dde929299`。
- `build/learning_batch/screenshots/full-contact-013.png`；PDF 页 426、432、439、447、455、461、470、477、485、494、501、511；SHA-256 `b8059217217cffd7e620c69bd877656135570fc7519eebedaa1e6dab675dfafd`。
- `build/learning_batch/screenshots/full-contact-025.png`；PDF 页 520、529、619、628、683、694、708、742、744、747、750、753；SHA-256 `9a5bd925820be0a4fb152c6cc01f26beb60a4f68a5cedec6409cf2d1b9aaab0a`。
- `build/learning_batch/screenshots/full-contact-037.png`；PDF 页 756、758；SHA-256 `f9f3d97094080fc74ba0fb8995bef81d8433c03e0cd9d0d36d49e90706217315`。
- `build/learning_batch/screenshots/ch01-contact-001.png`；PDF 页 1、2、16、31；SHA-256 `7951d2f2fe656285214fcad14c8939f8a79424d08b4a34f5963722a57603547d`。
- `build/learning_batch/screenshots/catalog-contact-001.png`；PDF 页 1、2、110、218；SHA-256 `1855dd0fa8213f41a22c7d4963a6eb12d30a6ba5f3c662a14752d1a23697b833`。

## 已打开的目录单页

- `build/learning_batch/screenshots/batch-page-003.png`：`357602d550b3a7b49780fe9d08284e1ae7619d9787b4a9a5758d9fe480905651`
- `build/learning_batch/screenshots/batch-page-004.png`：`820a8b79cd159f10c71195f19926cabffc4cf87e14c78f8744fa761de04cab06`
- `build/learning_batch/screenshots/batch-page-005.png`：`da583aabb8699f1f830a55bf0507b035a3f8a2fe2beeafb8425d2a826a01d7a8`

落盘前独立重新计算四份 PDF 与全部 22 张已看截图的 SHA-256，并与打开前快照逐项比较，均一致；四份 PDF 哈希也与同一自动 QA 报告一致。QA 仍为上述自动通过时间。该结论仅绑定本批实际查看范围，不作为整章完成、形式证明或发布批准。
