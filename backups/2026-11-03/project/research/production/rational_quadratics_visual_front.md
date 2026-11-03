# 第二十批前半卷与其他 PDF 选页实际视觉复核

自动 QA 时间：2026-10-29T20:01:09.623579+00:00。人工记录：2026-10-29T20:04:13.183248+00:00。

绑定 `data/production/batch_validation.json` 的自动通过版本，SHA-256：`1166d4b59cd5c777a09fc42e8d3ab44300dff99afcdb8f2c0e6420962465f8c4`。当前页数：基础续写审阅版 632、完整版 846、第一章审阅版 31、完整数学目录 218；该 QA 绑定 177 份源文件、46 份产物及 753 张截图。

实际通过图像查看工具逐张打开本批 13 张审阅版联系表，覆盖 PDF 页 1–156；打开目录第 3、4、5、6 页原尺寸截图；另打开其余三份 PDF 的全部 7 张生成选页联系表（完整版 5 张，第一章与完整数学目录各 1 张）。共实际打开 24 张图像。以下已看范围未发现阻断性裁切、重叠、缺图或明显可见乱码。没有用旧批次观察替代本批检查，没有修改截图、PDF、正式源码或 QA。

## 实际观察与尺度限制

- 审阅版前 156 页：封面、献词、章节入口、练习、分行公式、表格与已有插图正常呈现。联系表尺度未见明显越界、文字重叠或图像丢失。PDF 第 25 页为第一章末题，第 26 页为第 7 部分入口；这些页的较多留白与后续章节起页相接，不是空白图像。
- 目录原尺寸第 3–6 页：文字、点线、页码和层级缩进可读。第 4 页将 B2.19“有理平方与平方方程”和 B2.20“配方与有理二次方程”列于第 528 章续写下，印刷页码分别为 342、348。第 5 页列出两单元答案、相应来源条目，答案印刷页码为 559、564。第 6 页列出附录十五至二十三共九项；新附录印刷页码为 628，标题完整。该页下部较空，但续表内容完整可见。
- 完整版全部 53 个生成选页：封面、总目录、分类列表、原章与续章入口、教学与答案入口均存在。PDF 第 558/564 页可见 B2.19/B2.20 教学入口，第 775/780 页可见其答案入口；第 786 页插图来源表列出新图及总计 16 图。第 844 页附录二十三的整数平方界说明、分行不变式和证明段落正常排布；第 846 页为模块末段代码，行首缩进及末行均在页面内。仅按联系表尺度判断这些页面的整体布局，没有声称逐字验完代码或全部微小数学字形，也未把未选中的第 845 页视为本次已看。
- 第一章的四个选页显示封面、献词、分数插图与末页模拟代码。完整数学目录的四个选页显示标题、编号列表与末页分类条目，未见明显重叠或越界。
- 12 页联系表为 1200 × 1760 像素，每页缩略图约 313 × 405 像素；完整版最后五页联系表、第一章及目录四页联系表均为 1200 × 880。目录单页按 765 × 990 原图打开。联系表检查适合整体分页及明显布局问题，不能替代全部单页原尺寸的细小字形、上下标、数学证明或链接目的页检查。未打开的其余 PDF 页不在本报告范围；主编另行记录其放大页检查。

## 绑定的四份 PDF

- `dist/综合数学_基础续写审阅版.pdf`：`48631f7b35c352772ace00e6951d1ff1f23c1807d5c41efce11b1a4268f84694`
- `dist/综合数学.pdf`：`c632cd1d05d72d9bff486934c08f429703df89b51a6197ce10cb9316961ffc5c`
- `dist/综合数学_第一章审阅版.pdf`：`53254c1d606eb037eb1dba3b856d254924debec51c3fe56283f5c9f4a606d1bd`
- `dist/综合数学_完整数学目录.pdf`：`6cb12ea75b3c38217ab3e6a86004fc07400cae1bac31236355b3be9766881b55`

## 已打开的联系表与覆盖页

- `build/learning_batch/screenshots/batch-contact-001.png`；PDF 页 1–12；SHA-256 `e27abca99cf99e24715a1367534340119e4b599e6250614345556846757884f9`。
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
- `build/learning_batch/screenshots/full-contact-001.png`；PDF 页 1、2、3、18、217、218、241、250、400、408、416、424；SHA-256 `4f3b27c4925091cf2ba04e7c484699e3f17f9dc4a4141e5c6e861096ca14d61c`。
- `build/learning_batch/screenshots/full-contact-013.png`；PDF 页 426、432、439、447、455、461、470、477、485、494、501、511；SHA-256 `a7b9366167827e2425ef8b2fc22448539c9f1e29dc6d2e55733ee027723b9f2d`。
- `build/learning_batch/screenshots/full-contact-025.png`；PDF 页 520、528、536、544、551、558、564、572、662、671、726、737；SHA-256 `1a9ea0b10e1c2b550ad6bbf0c2011da3ece01dd87b9ba0c22dec27e5ee936b8c`。
- `build/learning_batch/screenshots/full-contact-037.png`；PDF 页 750、756、764、769、775、780、786、823、825、828、831、834；SHA-256 `ba59757f282894fdc32723966ff8f75cb3c16957916a7beb36821c008f464929`。
- `build/learning_batch/screenshots/full-contact-049.png`；PDF 页 837、840、842、844、846；SHA-256 `cbc6c17e9ef443a1cdf25b8426208214b27e7b1f9fea09841793cff543df749f`。
- `build/learning_batch/screenshots/ch01-contact-001.png`；PDF 页 1、2、16、31；SHA-256 `7951d2f2fe656285214fcad14c8939f8a79424d08b4a34f5963722a57603547d`。
- `build/learning_batch/screenshots/catalog-contact-001.png`；PDF 页 1、2、110、218；SHA-256 `1855dd0fa8213f41a22c7d4963a6eb12d30a6ba5f3c662a14752d1a23697b833`。

## 已打开的目录单页

- `build/learning_batch/screenshots/batch-page-003.png`：`da556c12589dc379f1a121838473dd5cb59cce8eb7cf31ff1d39d7355559c15a`
- `build/learning_batch/screenshots/batch-page-004.png`：`435c04cf0ec84ab5182d4976214cb8e5ec927f8022795659c311b17f80b3dcba`
- `build/learning_batch/screenshots/batch-page-005.png`：`af16e7cbdb0f005f872e81cdc124dcf866adf68e22cb8317cb267cc36b2cec7c`
- `build/learning_batch/screenshots/batch-page-006.png`：`21c0552369cbbfb0be5d65c678350204c09ca55300303aeddf4b64308e998ae4`

落盘前重新计算四份 PDF、自动 QA 与全部 24 张已看截图的 SHA-256，与打开前快照逐项比较，均一致；PDF 和截图哈希亦与同一自动 QA 报告一致。本报告只认证实际打开范围的视觉观察，不作为整章完成、形式证明或发布批准。
