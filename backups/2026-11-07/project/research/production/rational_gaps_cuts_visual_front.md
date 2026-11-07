# 第二十一批前半卷与其他 PDF 选页实际视觉复核

自动 QA 时间（validated_at）：2026-10-30T01:51:08.575929+00:00。实际视觉记录：2026-10-30T01:54:19.681879+00:00。

绑定 `data/production/batch_validation.json` 的自动通过版本，SHA-256：`ace18d636f4812de1f271ffe8b9f8c3855fb33dba3b1138c03dbdb63a90b3af7`。当前页数：基础续写审阅版 660、完整版 874、第一章审阅版 31、完整数学目录 218；该 QA 绑定 183 份源文件、47 份产物及 788 张截图。

本次通过图像查看工具实际打开 43 张当前图像：审阅版 28 张联系表连续覆盖 PDF 页 1–336，目录单页 3–6，代表性正文单页 207、259、318、335，以及其余三份 PDF 的全部 7 张生成选页联系表。完整版联系表覆盖 58 个选页，第一章和完整数学目录各覆盖 4 个选页。没有以旧批次记录、文本抽取或自动 QA 代替本次实际看图。

## 实际观察与边界

- 审阅版 PDF 页 1–336：封面、献词、目录、章节入口、练习、推导、表格和已有图示整体排布完整；在联系表尺度未发现阻断性的裁切、重叠、缺图或明显乱码。第 25 页只有章节末题，第 26 页为下一部分入口；第 184 页为末题、第 185 页为数学教育部分入口，其留白属于可见章节结构，未将其记为渲染空白故障。
- 目录 PDF 第 3–6 页按 765 × 990 原图逐页打开。标题层级、点线及右侧页码均可辨认；第 4 页新增 B2.21“有理数的稠密、界与平方缺口”和 B2.22“戴德金分割、次序与上确界”分别列印刷页码 356、362；第 5 页两单元答案列 584、589，参考资料中有“有理数缺口与戴德金分割次序参考资料”；第 6 页附录二十四“有理缺口的有限见证绘图”列页码 657。目录末页下部留白，所有可见条目完整。
- 代表性原尺寸正文：PDF 第 207 页的有限函数对应图，集合轮廓、三个箭头、未命中元素 9、图注与正文没有碰撞；第 259 页绝对值范围示意的实心和空心端点、左右箭头、三种关系及图注明确；第 318 页乘积系数图的行列标签、彩色方框、输出系数与公式排列完整；第 335 页逐步除法表、两组计算例与后续公式均在页内，没有截断或表格重叠。以上四页是代表性既有内容，不冒称为本批新单元正文放大检查。
- 完整版 58 个生成选页：封面、总目录、分类目录、续写教学与答案入口、图源表和代码附录整体呈现正常。联系表中 PDF 第 572 页含 B2.21 入口，第 578 页含 B2.22 入口；第 800、805 页分别可见两单元答案入口；第 811 页图源表包含第 17 图；第 873–874 页为新附录的说明、公式和代码，未见明显越界。仅做这些页面的联系表尺度观察，不宣称逐字验证附录代码或全部数学字形。
- 第一章选页 1、2、16、31 显示封面、献词、分数节奏图与模拟代码；完整数学目录选页 1、2、110、218 显示标题、总目录说明及分类条目，未见明显裁切或重叠。
- 12 页联系表为 1200 × 1760，每页缩略图约 313 × 405 像素；完整版末张含 10 页、尺寸同为 1200 × 1760；第一章及目录 4 页联系表为 1200 × 880。单页图为 765 × 990。联系表只适合整体版式、分页与明显异常；不能替代全部单页放大后的细小字形、上下标、证明正确性、链接目标或可访问性检查。审阅版第 337–660 页以及其他 PDF 未列出的页不属于本报告实际已看范围。

## 绑定的四份 PDF

- `dist/综合数学_基础续写审阅版.pdf`：`6ee14b1b683b04975d1cb3e475d697ce4e0267d7f9c9836072e058e877c665ca`。
- `dist/综合数学.pdf`：`33a0a4f1bf63b780b4608af85fba4e0187a49b2e0f105b8e0bc75f5674b604be`。
- `dist/综合数学_第一章审阅版.pdf`：`53254c1d606eb037eb1dba3b856d254924debec51c3fe56283f5c9f4a606d1bd`。
- `dist/综合数学_完整数学目录.pdf`：`6cb12ea75b3c38217ab3e6a86004fc07400cae1bac31236355b3be9766881b55`。

## 实际打开的联系表与覆盖页

- `build/learning_batch/screenshots/batch-contact-001.png`；PDF 页 1–12；SHA-256 `efde2210bb21e96ad783ff5afbc5ebc834bf197fd67ef059dcce12621954407d`。
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
- `build/learning_batch/screenshots/batch-contact-157.png`；PDF 页 157–168；SHA-256 `31c80b7c66a7607aa20cbf3ca79e5f513b9e75f6ccccd7146a32206b8a0de2d2`。
- `build/learning_batch/screenshots/batch-contact-169.png`；PDF 页 169–180；SHA-256 `6ca231b5c48b860a967a707295f69e09142200c3978eb5ec1d5560412578ccf2`。
- `build/learning_batch/screenshots/batch-contact-181.png`；PDF 页 181–192；SHA-256 `aa72320a5e1b63fdadf0f0b100f572598db5e95b8406953364defc974ff36842`。
- `build/learning_batch/screenshots/batch-contact-193.png`；PDF 页 193–204；SHA-256 `d2dda57e2d2acb4c885129ae201ddb3621164f83ac46d0db563e5127099d0155`。
- `build/learning_batch/screenshots/batch-contact-205.png`；PDF 页 205–216；SHA-256 `8db17d1990ff9cf40f5f75bf1ab34b7251edf310e402824e2820c02bc74386f7`。
- `build/learning_batch/screenshots/batch-contact-217.png`；PDF 页 217–228；SHA-256 `a5a40a4a44ef0160a231b574ec743840cfb5a8f66ad77eec15d4048240cc7434`。
- `build/learning_batch/screenshots/batch-contact-229.png`；PDF 页 229–240；SHA-256 `aff57657fe09236ca28416fda8241da57ba2fc1a02eee90f72c7b8abe912946c`。
- `build/learning_batch/screenshots/batch-contact-241.png`；PDF 页 241–252；SHA-256 `5a81534b4389a12ff9578ceccb36cf9ab6da1b572403ae45271b66ae23e44419`。
- `build/learning_batch/screenshots/batch-contact-253.png`；PDF 页 253–264；SHA-256 `552fbc1a3a09faea80c8bcec2380b4922fabfc64c01b79f51d06bee007861916`。
- `build/learning_batch/screenshots/batch-contact-265.png`；PDF 页 265–276；SHA-256 `6b006aca9a0f164c6d872e97550c35adf545bcf981ea285bc5d055eb8abce3a1`。
- `build/learning_batch/screenshots/batch-contact-277.png`；PDF 页 277–288；SHA-256 `3f16fb56441f363b8f98db3eeb857b9a1ef74f9230df2c0db37cc08aec80ccf9`。
- `build/learning_batch/screenshots/batch-contact-289.png`；PDF 页 289–300；SHA-256 `625eefe27ec25d15d96562e692b29eb1702d50a876ac836cf915fea6ba380a1b`。
- `build/learning_batch/screenshots/batch-contact-301.png`；PDF 页 301–312；SHA-256 `13acdcac0696159a2920ef712a5a6d93d21ce86120359369cf5e1f9874f27d10`。
- `build/learning_batch/screenshots/batch-contact-313.png`；PDF 页 313–324；SHA-256 `cffa8881ec8713497587ba07963552aee1d9cf1cda9d4c99125141f42be3c03d`。
- `build/learning_batch/screenshots/batch-contact-325.png`；PDF 页 325–336；SHA-256 `cc637116bdc83b91573c505044409bb85869abce061ef45e6140a98f7bc5e70d`。
- `build/learning_batch/screenshots/full-contact-001.png`；PDF 页 1、2、3、18、217、218、241、250、400、408、416、426；SHA-256 `2dc4098e7904e45aa487784349a6e7fc1eb91fb52f6078e7138f4504d9cceac1`。
- `build/learning_batch/screenshots/full-contact-013.png`；PDF 页 432、438、439、447、455、461、470、477、485、494、501、511；SHA-256 `561ca6b765e95cfd1b49535ac6b51d67ad4defa0058a2f24594fe70ff31b9e22`。
- `build/learning_batch/screenshots/full-contact-025.png`；PDF 页 520、528、536、544、551、558、564、572、578、586、676、685；SHA-256 `c25c0a82db40a067a5c5cbeab15480afb3a4c1a9cb8c8d9a8cd78c9f9d08c391`。
- `build/learning_batch/screenshots/full-contact-037.png`；PDF 页 740、751、764、770、778、783、789、794、800、805、811、849；SHA-256 `5e851a890d3d1bb6f316d619d788a1658e3d17edd0f82f7853734746d0226f99`。
- `build/learning_batch/screenshots/full-contact-049.png`；PDF 页 851、854、857、860、863、866、868、870、873、874；SHA-256 `cda2b7369b5561793c38066f95d5ae2c439423bf894ebcfe928e9ca3daa6f6a8`。
- `build/learning_batch/screenshots/ch01-contact-001.png`；PDF 页 1、2、16、31；SHA-256 `7951d2f2fe656285214fcad14c8939f8a79424d08b4a34f5963722a57603547d`。
- `build/learning_batch/screenshots/catalog-contact-001.png`；PDF 页 1、2、110、218；SHA-256 `1855dd0fa8213f41a22c7d4963a6eb12d30a6ba5f3c662a14752d1a23697b833`。

## 实际打开的原尺寸单页

- `build/learning_batch/screenshots/batch-page-003.png`：`da556c12589dc379f1a121838473dd5cb59cce8eb7cf31ff1d39d7355559c15a`。
- `build/learning_batch/screenshots/batch-page-004.png`：`35aebb7b38469ee87baf9b9fdf6e3b47a5524e58147d29f5a80b2cf8783ddd72`。
- `build/learning_batch/screenshots/batch-page-005.png`：`1d5f2415853e2c1e2a0e9738cd0b4760f1ba7ef927b99cd1cd0fb2b3fd640e20`。
- `build/learning_batch/screenshots/batch-page-006.png`：`30d206bd9246bd8de0d6448b2e5108bfdd7f626b358d1d9264f5775a902a2ccb`。
- `build/learning_batch/screenshots/batch-page-207.png`：`582c8e359d2298fa2505632993bf494bd794c4133340af517afa8ea4bbc565ac`。
- `build/learning_batch/screenshots/batch-page-259.png`：`3915a01d197877c2c32d26eabd2e5e16c54ee0cd2a238d965774e47bd229768a`。
- `build/learning_batch/screenshots/batch-page-318.png`：`0add6179e7bb4a6a6e1869196734672df86b894270dac5c34f6c43d8fe503d4d`。
- `build/learning_batch/screenshots/batch-page-335.png`：`3ca9e75bce26ec562ed18e9d9145019ce4e69363b3500ccd447769c217164a39`。

落盘前重新计算四份 PDF 与全部 43 张已看截图的 SHA-256，均与打开前快照及上述同一自动 QA 的哈希逐项一致。报告只记录已看范围的视觉观察，不构成整章完成、数学证明或发布批准；未修改任何 accepted 状态、自动 QA、PDF、截图或正式源码。本文件作为本轮未注册的补充视觉报告单独交回主编。
