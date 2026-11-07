# 第23批非负分割乘法：前半及其他版本实际视觉审读

审阅者：`/root/visual21_front`。开始时间（UTC）：`2026-10-30T02:30:56.323884+00:00`；完成时间：`2026-10-30T02:33:23.430489+00:00`。

结论：已实际用图像查看工具查看本次指定的 40 张当前 PNG；在下述尺度及范围内未发现明显裁切、重叠、异常空白、表格或插图缺失等阻断。此结论限于实际查看范围，不表示四份 PDF 全页逐字审校通过，也不替代本批新增正文、答案与长公式的放大检查。

## 版本绑定

读取当前 `data/production/batch_validation.json`，其 `validated_at` 为 `2026-10-30T02:28:30.719880+00:00`，读取时状态为 `automated_checks_passed`；SHA-256 为 `6bd9d4b079ec9f6dd57326a7405a946e69871bae1b32ce9dd3cad556ca0784dd`。与 `/tmp/recover23_hashes.json` 的审阅 PDF、完整 PDF 和 QA 哈希相符。

| PDF（仓库相对路径） | 页数 | SHA-256 |
| --- | ---: | --- |
| `dist/综合数学.pdf` | 926 | `263fa832ad3c7cfc1a7a46e0223dce6011ccdd7e0c7bcf6af95c03dc315a960a` |
| `dist/综合数学_基础续写审阅版.pdf` | 712 | `21beb4a4a6f462ced257796159590270f84ad9456bfb4b76e45c8b9c71557504` |
| `dist/综合数学_完整数学目录.pdf` | 218 | `6cb12ea75b3c38217ab3e6a86004fc07400cae1bac31236355b3be9766881b55` |
| `dist/综合数学_第一章审阅版.pdf` | 31 | `53254c1d606eb037eb1dba3b856d254924debec51c3fe56283f5c9f4a606d1bd` |

截图先与当前 QA 的 `screenshot_sha256` 逐项核对；四份 PDF 与 `artifact_sha256` 一致。实际查看之后再次计算本次 40 张 PNG、四份 PDF 及 QA 的哈希，全部与开始前快照相同。未沿用第21或22批截图作为当前证据。记录见 `/tmp/nonnegative_front_visual_snapshot.json`。

## 实际查看范围与观察

1. 审阅 PDF 的 1–336 页：逐张打开 `batch-contact-001.png` 至 `batch-contact-325.png`，步长 12，共 28 张，每张 12 个连续物理页缩略图；所有 336 页均在联系表尺度被看到。正文块、标题、页码与图表位置保持一致；没有发现明显被页边截断、相互覆盖或缺页式异常空白。章节转换页和最后一题的短续页有较大留白，但可见内容与分页结构相符。
2. 审阅 PDF 物理第 3、4、5、6 页：另用 original 细节模式逐张打开单页 PNG。目录中文字、点线与页码列分离清楚，未见长条目撞入页码或行间重叠。第4页清楚列出 B2.25/B2.26，印刷页码 382/389；第5页对应答案 632/637；第6页显示非负分割乘积参考资料入口 656。物理页与印刷页相差 2，未将两者混记。
3. 完整 PDF：实际打开现存全部六张 `full-contact-001/013/025/037/049/061.png`，覆盖 66 个既定选页。查看到封面、目录、基础单元、答案、插图表及计算附录，包括本批非负乘积正文入口与答案选页；未见联系表尺度的明显裁切或重叠。66 个选页不等于完整 PDF 全页覆盖。
4. 第一章审阅 PDF：打开 `ch01-contact-001.png`，查看物理页 1、2、16、31；封面、献词、图示及代码页布局未见明显异常。
5. 完整数学目录 PDF：打开 `catalog-contact-001.png`，查看物理页 1、2、110、218；标题层级、列表和末页留白未见明显异常。

## 检查限度

联系表适合判断整页布局、块状重叠与大幅越界，不能保证每个细小数学字符、分数线、上下标都正确。本次仅目录 3–6 页按单页原图检查，其余页面没有宣称逐字或逐公式放大审读。审阅 PDF 第337–712页不在本报告覆盖范围；其他三份 PDF 仅覆盖上述既定选页。PDF 内部链接的点击跳转并未在本次图像工具中验证，不能由点线排版或蓝色文字外观推出链接有效。

本次未修改稿件、QA、验收状态或构建产物；报告及快照只写入 `/tmp`。

## 40 张实际查看图像的哈希清单

全部文件位于 `build/learning_batch/screenshots/`。

| 图像 | SHA-256 |
| --- | --- |
| `batch-contact-001.png` | `5de9085ed2ca9ab850b83d5ae262c219eac8516bdc335004bdcfa2f59d713dc3` |
| `batch-contact-013.png` | `ab224cab814badefac492fefbcfb90e0029c764f78b718424dcb3bc37d6f1cf9` |
| `batch-contact-025.png` | `b775357e7fa2b94641545aeb2426c91dc0b65e140aea1476ff40f53e6acccc59` |
| `batch-contact-037.png` | `7720a529b3cb54166792513c823977bece5f95b0af2344dce86324b0ddd9527a` |
| `batch-contact-049.png` | `9ce6945222de2f0805e968fab470ef10cf3fc4f78ffb6be3179ac78f2faa59c6` |
| `batch-contact-061.png` | `63b2fe0c9f11ca38ba4c063aa2a9778230b30486abdf2751541a454bfbec642c` |
| `batch-contact-073.png` | `5b338ebf3279b492a9c20bae8c0c65fc669254714b73e2d5a215d679aad37eef` |
| `batch-contact-085.png` | `21ea2c1059ae4a1f56c08a9c5bfed5d60bdf923140532ecdd17505e3026c8772` |
| `batch-contact-097.png` | `1fb674142c503b84e0457385602011d6f40aa077cddcc46dedd1aec5db579015` |
| `batch-contact-109.png` | `310e0d4721d007a44a90d6d9adb6baac22888ad83ebf481652c0ecd4649cba6a` |
| `batch-contact-121.png` | `83c82021d61fcc32d5fd86ad6144a066c03503a7535c5b92d45575d04fa64e73` |
| `batch-contact-133.png` | `e07abfdb8ece075ce3273e49dba94c71785cd8a0456e201d4c2882d4d7f0cfb8` |
| `batch-contact-145.png` | `25ed63a2881987ac9e519f5de919ae9852908a014a357d56b0bbf5283361199b` |
| `batch-contact-157.png` | `31c80b7c66a7607aa20cbf3ca79e5f513b9e75f6ccccd7146a32206b8a0de2d2` |
| `batch-contact-169.png` | `6ca231b5c48b860a967a707295f69e09142200c3978eb5ec1d5560412578ccf2` |
| `batch-contact-181.png` | `aa72320a5e1b63fdadf0f0b100f572598db5e95b8406953364defc974ff36842` |
| `batch-contact-193.png` | `d2dda57e2d2acb4c885129ae201ddb3621164f83ac46d0db563e5127099d0155` |
| `batch-contact-205.png` | `8db17d1990ff9cf40f5f75bf1ab34b7251edf310e402824e2820c02bc74386f7` |
| `batch-contact-217.png` | `a5a40a4a44ef0160a231b574ec743840cfb5a8f66ad77eec15d4048240cc7434` |
| `batch-contact-229.png` | `aff57657fe09236ca28416fda8241da57ba2fc1a02eee90f72c7b8abe912946c` |
| `batch-contact-241.png` | `5a81534b4389a12ff9578ceccb36cf9ab6da1b572403ae45271b66ae23e44419` |
| `batch-contact-253.png` | `552fbc1a3a09faea80c8bcec2380b4922fabfc64c01b79f51d06bee007861916` |
| `batch-contact-265.png` | `6b006aca9a0f164c6d872e97550c35adf545bcf981ea285bc5d055eb8abce3a1` |
| `batch-contact-277.png` | `3f16fb56441f363b8f98db3eeb857b9a1ef74f9230df2c0db37cc08aec80ccf9` |
| `batch-contact-289.png` | `625eefe27ec25d15d96562e692b29eb1702d50a876ac836cf915fea6ba380a1b` |
| `batch-contact-301.png` | `13acdcac0696159a2920ef712a5a6d93d21ce86120359369cf5e1f9874f27d10` |
| `batch-contact-313.png` | `cffa8881ec8713497587ba07963552aee1d9cf1cda9d4c99125141f42be3c03d` |
| `batch-contact-325.png` | `cc637116bdc83b91573c505044409bb85869abce061ef45e6140a98f7bc5e70d` |
| `catalog-contact-001.png` | `1855dd0fa8213f41a22c7d4963a6eb12d30a6ba5f3c662a14752d1a23697b833` |
| `ch01-contact-001.png` | `7951d2f2fe656285214fcad14c8939f8a79424d08b4a34f5963722a57603547d` |
| `full-contact-001.png` | `ad023ec207c75a82cdb2ffeb6b4bb6a42b8330095d16e8faa61805e7a47acc00` |
| `full-contact-013.png` | `e65573eb553d2b44fb37c79f4fb97c3e4053c1e503ce48cb50affbd57ab045cb` |
| `full-contact-025.png` | `3659cefd071d77e8e912720022ed38b03ce67ae589448ab1fe06063309fdd1bc` |
| `full-contact-037.png` | `eddf7cb872a40b76eef32a85c79ab52bf952ca0f612939ccb11889207424ab6a` |
| `full-contact-049.png` | `66ad7cf57964f7ddbd5df468b19381ec5cca35b0df0270fda82772d53381a5be` |
| `full-contact-061.png` | `14ba1dacdd86c808ec394208a0683471dd82e1489748a32d6736686f60ae7f98` |
| `batch-page-003.png` | `da556c12589dc379f1a121838473dd5cb59cce8eb7cf31ff1d39d7355559c15a` |
| `batch-page-004.png` | `72ae81c71517fcbdf8d084841bdcaad72da0ba327f4201785ded0b51229dac67` |
| `batch-page-005.png` | `762a0db41d6eff0c908210a59cbfc1fe0b3c62599591990b89888426925ba5fb` |
| `batch-page-006.png` | `a15af169c5d65b3e756c87ec1713ddb3aa5ef07c1cd8e4625b1f38313108eb25` |
