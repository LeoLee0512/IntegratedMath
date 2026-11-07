# 第十九批前半卷与其他 PDF 选页实际视觉复核

自动 QA 时间：2026-10-29T19:20:53.442564+00:00。人工记录：2026-10-29T19:24:38.205045+00:00。

绑定 `data/production/batch_validation.json` 的自动通过版本，SHA-256：`2630831372ae3acc90e46268a1f45a67c4a7fa60fb5ea17c52de2a87c6d83a6a`。当前页数：基础续写审阅版 604、完整版 818、第一章审阅版 31、完整数学目录 218。

实际通过图像查看工具逐张打开本批 13 张审阅版联系表，覆盖 PDF 页 1–156；打开目录页 3、4、5 原尺寸截图，并因目录已延至第 6 页而额外打开该页原图；另打开其余三份 PDF 的全部 6 张生成选页联系表（完整版 4 张，第一章与完整数学目录各 1 张）。共实际打开 23 张图像，没有以旧批次观察替代本批检查，也没有修改任何截图、PDF、正式源码或 QA。以下已看范围未发现阻断性裁切、重叠、缺图或明显可见乱码。

## 实际观察与尺度限制

- 审阅版前 156 页：封面、献词、章节入口、练习、公式、表格与已有插图均有正常内容，联系表尺度未见明显越界、重叠或丢失图像。第一页码变动后，第一章末题在 PDF 第 25 页、部分入口在第 26 页，页面留白仍呈连续分页，不据留白推断缺页。
- 目录原尺寸页 3–6：第 4 页把 B2.17“一次除式的商余与综合除法”和 B2.18“因式定理、不同根数界与恒等识别”接在第 528 章续写下，章节层级、点线、页码和缩进可读。第 5 页含 B2.17/B2.18 答案及一次除式来源条目。目录现有四页，第 6 页为附录十八至二十二五项续表，存在较多页末留白，但五项标题与页码完整，并非空页或内容截断。实际还比较这四张单页按联系表规则缩小后的像素与联系表对应区域，均一致。
- 完整版全部 48 个生成选页：封面、目录、分类列表、原章与续章入口、教学与答案入口均存在。PDF 第 544/551 页可见 B2.17/B2.18 教学入口，第 751/756 页可见两单元答案入口；第 763 页插图来源表正常，仍列 15 图。第 817 页附录二十二说明、分行公式、不变式和分开的报告目录/文件名可见，第 818 页为完整短模块代码且正常结束。这里只按联系表尺度判断布局，不声称逐字验完代码或全部微小字形。
- 第一章选页：封面、献词、分数插图与末页模拟代码存在。完整数学目录选页中的标题、编号列表及末页条目可见，未发现明显重叠或越界。
- 12 页联系表为 1200 × 1760 像素，每页缩略图约 313 × 405 像素；第一章及分类目录 4 页联系表高 880。目录单页按 765 × 990 原图打开。联系表检查适合整体分页与明显布局问题，不能替代全部单页原尺寸的细小字形、上下标、数学证明或链接目的页检查。未打开的其余 PDF 页不在本报告范围；本报告未复看引用修复页 557，主编另记该页复核。

## 绑定的四份 PDF

- `dist/综合数学_基础续写审阅版.pdf`：`00e6637eb2ee4bb360a5a21e7b0848e7cc17d30959c8fcf5ea23603f0d4e051a`
- `dist/综合数学.pdf`：`44a42aeb215bf904d9a440217046afe5889f97ce7f1ddf9be651f0be9467a787`
- `dist/综合数学_第一章审阅版.pdf`：`53254c1d606eb037eb1dba3b856d254924debec51c3fe56283f5c9f4a606d1bd`
- `dist/综合数学_完整数学目录.pdf`：`6cb12ea75b3c38217ab3e6a86004fc07400cae1bac31236355b3be9766881b55`

## 已打开的联系表与覆盖页

- `build/learning_batch/screenshots/batch-contact-001.png`；PDF 页 1–12；SHA-256 `99e9d0e5e268b8008bb9002ec59ccac89e3d266914022ae41b71b60fdb614ca5`。
- `build/learning_batch/screenshots/batch-contact-013.png`；PDF 页 13–24；SHA-256 `ab224cab814badefac492fefbcfb90e0029c764f78b718424dcb3bc37d6f1cf9`。
- `build/learning_batch/screenshots/batch-contact-025.png`；PDF 页 25–36；SHA-256 `b775357e7fa2b94641545aeb2426c91dc0b65e140aea1476ff40f53e6acccc59`。
- `build/learning_batch/screenshots/batch-contact-037.png`；PDF 页 37–48；SHA-256 `7720a529b3cb54166792513c823977bece5f95b0af2344dce86324b0ddd9527a`。
- `build/learning_batch/screenshots/batch-contact-049.png`；PDF 页 49–60；SHA-256 `9ce6945222de2f0805e968fab470ef10cf3fc4f78ffb6be3179ac78f2faa59c6`。
- `build/learning_batch/screenshots/batch-contact-061.png`；PDF 页 61–72；SHA-256 `63b2fe0c9f11ca38ba4c063aa2a9778230b30486abdf2751541a454bfbec642c`。
- `build/learning_batch/screenshots/batch-contact-073.png`；PDF 页 73–84；SHA-256 `5b338ebf3279b492a9c20bae8c0c65fc669254714b73e2d5a215d679aad37eef`。
- `build/learning_batch/screenshots/batch-contact-085.png`；PDF 页 85–96；SHA-256 `21ea2c1059ae4a1f56c08a9c5bfed5d60bdf923140532ecdd17505e3026c8772`。
- `build/learning_batch/screenshots/batch-contact-097.png`；PDF 页 97–108；SHA-256 `1fb674142c503b84e0457385602011d6f40aa077cddcc46dedd1aec5db579015`。
- `build/learning_batch/screenshots/batch-contact-109.png`；PDF 页 109–120；SHA-256 `310e0d4721d007a44a90d6d9adb6baac22888ad83ebf481652c0ecd4649cba6a`。
- `build/learning_batch/screenshots/batch-contact-121.png`；PDF 页 121–132；SHA-256 `83c82021d61fcc32d5fd86ad6144a066c03503a7535c5b92d45575d04fa64e73`。
- `build/learning_batch/screenshots/batch-contact-133.png`；PDF 页 133–144；SHA-256 `e07abfdb8ece075ce3273e49dba94c71785cd8a0456e201d4c2882d4d7f0cfb8`。
- `build/learning_batch/screenshots/batch-contact-145.png`；PDF 页 145–156；SHA-256 `25ed63a2881987ac9e519f5de919ae9852908a014a357d56b0bbf5283361199b`。
- `build/learning_batch/screenshots/full-contact-001.png`；PDF 页 1、2、3、18、217、218、241、250、400、408、410、416；SHA-256 `7c4384e569dde163c94355f095ab4e732938abc4cccc89338106cffb02883367`。
- `build/learning_batch/screenshots/full-contact-013.png`；PDF 页 426、432、439、447、455、461、470、477、485、494、501、511；SHA-256 `627ee87345805c7ee7f5d5939f1b668218f92609ed2b4791be0f749d788bd28c`。
- `build/learning_batch/screenshots/full-contact-025.png`；PDF 页 520、528、536、544、551、559、649、658、713、724、737、743；SHA-256 `1963317e2baa2fb7a16090873d4f6317017126b5b023b16628e9ebdd347d3a94`。
- `build/learning_batch/screenshots/full-contact-037.png`；PDF 页 751、756、763、798、800、803、806、809、812、815、817、818；SHA-256 `0d502e3f46915d09909cd473fd713f6c61fb039e704fa611c199f11b59823f1f`。
- `build/learning_batch/screenshots/ch01-contact-001.png`；PDF 页 1、2、16、31；SHA-256 `7951d2f2fe656285214fcad14c8939f8a79424d08b4a34f5963722a57603547d`。
- `build/learning_batch/screenshots/catalog-contact-001.png`；PDF 页 1、2、110、218；SHA-256 `1855dd0fa8213f41a22c7d4963a6eb12d30a6ba5f3c662a14752d1a23697b833`。

## 已打开的目录单页

- `build/learning_batch/screenshots/batch-page-003.png`：`da556c12589dc379f1a121838473dd5cb59cce8eb7cf31ff1d39d7355559c15a`
- `build/learning_batch/screenshots/batch-page-004.png`：`1b85680da643038e13bc23c2bdc6b0d6ee7cb3532fda23581bf1436d237f1ae4`
- `build/learning_batch/screenshots/batch-page-005.png`：`165ba0cb76615642b7caa986a467ddf2a1e829344fa67eeaa9c0b88109090272`
- `build/learning_batch/screenshots/batch-page-006.png`：`20d6755497fcc9258732322ee99ca955bb0f75161b1f1406c0a2ebc07cc83333`

落盘前独立重新计算四份 PDF 与全部 23 张已看截图的 SHA-256，并与各图打开前快照逐项比较，均一致；四份 PDF 哈希也与同一自动 QA 报告一致。QA 仍为上述自动通过时间。本报告只认证实际打开范围的视觉观察，不作为整章完成、形式证明或发布批准。
