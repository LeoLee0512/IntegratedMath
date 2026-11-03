# 第 26 批前半独立视觉复核

审阅者：`/root/visual21_front`。
实际查看开始：`2026-10-30T03:28:04.913335+00:00`；完成并复核字节：`2026-10-30T03:32:47.365467+00:00`。
绑定 QA：`2026-10-30T03:27:34.484916+00:00`，状态 `automated_checks_passed`。

结论：在下列实际查看范围和分辨率内，未发现需要阻断交付的可见版式问题。本报告只是独立视觉证据，不修改或替代总验收状态。

## 实际查看范围

- 审阅版物理第 1–336 页：逐张调用图像查看工具，实际查看 28 张联系图（001、013、…、325）。每张 12 页，连续无缺页。
- 其余三个 PDF 当前生成的全部 9 张选页联系图：完整书 7 张，共 76 个选页；第一章审阅版 1 张，物理 1、2、16、31 页；完整目录 1 张，物理 1、2、110、218 页。完整书末张实际含 1002、1005、1007、1008 页。
- 审阅版目录物理第 3、4、5、6 页：另逐张以 original 模式打开原图，共 4 张。合计实际查看 41 个 PNG 文件。

## 观察

前半正文、证明、练习、表格和图示在联系图尺度上排列正常，未见明显越界、裁切、叠字或异常整页空白。章首、献辞及短段落产生的留白与内容结构相符。其他三个版本的选页未见明显页面边界问题；完整书末页代码续页仍在版心内。

四张目录原图的标题层级、引导点和右侧页码均清楚，未见相互覆盖。B2.31、B2.32 条目及其答案条目完整可读，分别列于印刷页码 421、428、708、716；附录和参考资料条目连续。此处是可见排版观察，未把目录页码外观当作逐条目标链接验证。

## 限制

联系图只能支持整页布局和明显缺陷判断，不能证明所有小字号、上下标或每一数学符号均正确。本次未逐页放大审阅版第 7–336 页，亦未独立查看审阅版第 337–794 页；后半与新内容放大检查由主审另行记录。完整书 1008 页、目录 218 页及第一章 31 页在本报告中只按上述选页查看。没有把先前批次截图、文本教学审或自动检查替代本批实际视觉检查，也不声称完成数学全文验收。

## 冻结与哈希

查看前后重新计算 QA、四个 PDF 与全部 41 个实际查看 PNG 的 SHA-256，均与开始快照一致；全部 PNG 同时逐项匹配当前 QA 的 screenshot_sha256。以下路径相对于 `/workspace/IntegratedMath-book`。

| 文件 | 页数（PDF） | SHA-256 |
|---|---:|---|
| `data/production/batch_validation.json` | — | `5d2e35d9362554ca7cf3247a324e513a63ae3d39608c9747e9052d06eb8d2501` |
| `dist/综合数学.pdf` | 1008 | `a4ba277fa593402fc386fab901f5c50de4fe143d35e139cf575515184ff5b251` |
| `dist/综合数学_基础续写审阅版.pdf` | 794 | `41e2a2b7d9d26561c145accd816e4c2feab681109da6424cea88e0c4acaa592b` |
| `dist/综合数学_完整数学目录.pdf` | 218 | `6cb12ea75b3c38217ab3e6a86004fc07400cae1bac31236355b3be9766881b55` |
| `dist/综合数学_第一章审阅版.pdf` | 31 | `53254c1d606eb037eb1dba3b856d254924debec51c3fe56283f5c9f4a606d1bd` |
| `build/learning_batch/screenshots/batch-contact-001.png` | — | `64467e74009b90850f511665a901e0f04d9cbd91cbcdc6cc0f81864a60732a70` |
| `build/learning_batch/screenshots/batch-contact-013.png` | — | `ab224cab814badefac492fefbcfb90e0029c764f78b718424dcb3bc37d6f1cf9` |
| `build/learning_batch/screenshots/batch-contact-025.png` | — | `b775357e7fa2b94641545aeb2426c91dc0b65e140aea1476ff40f53e6acccc59` |
| `build/learning_batch/screenshots/batch-contact-037.png` | — | `7720a529b3cb54166792513c823977bece5f95b0af2344dce86324b0ddd9527a` |
| `build/learning_batch/screenshots/batch-contact-049.png` | — | `9ce6945222de2f0805e968fab470ef10cf3fc4f78ffb6be3179ac78f2faa59c6` |
| `build/learning_batch/screenshots/batch-contact-061.png` | — | `63b2fe0c9f11ca38ba4c063aa2a9778230b30486abdf2751541a454bfbec642c` |
| `build/learning_batch/screenshots/batch-contact-073.png` | — | `5b338ebf3279b492a9c20bae8c0c65fc669254714b73e2d5a215d679aad37eef` |
| `build/learning_batch/screenshots/batch-contact-085.png` | — | `21ea2c1059ae4a1f56c08a9c5bfed5d60bdf923140532ecdd17505e3026c8772` |
| `build/learning_batch/screenshots/batch-contact-097.png` | — | `1fb674142c503b84e0457385602011d6f40aa077cddcc46dedd1aec5db579015` |
| `build/learning_batch/screenshots/batch-contact-109.png` | — | `310e0d4721d007a44a90d6d9adb6baac22888ad83ebf481652c0ecd4649cba6a` |
| `build/learning_batch/screenshots/batch-contact-121.png` | — | `83c82021d61fcc32d5fd86ad6144a066c03503a7535c5b92d45575d04fa64e73` |
| `build/learning_batch/screenshots/batch-contact-133.png` | — | `e07abfdb8ece075ce3273e49dba94c71785cd8a0456e201d4c2882d4d7f0cfb8` |
| `build/learning_batch/screenshots/batch-contact-145.png` | — | `25ed63a2881987ac9e519f5de919ae9852908a014a357d56b0bbf5283361199b` |
| `build/learning_batch/screenshots/batch-contact-157.png` | — | `31c80b7c66a7607aa20cbf3ca79e5f513b9e75f6ccccd7146a32206b8a0de2d2` |
| `build/learning_batch/screenshots/batch-contact-169.png` | — | `6ca231b5c48b860a967a707295f69e09142200c3978eb5ec1d5560412578ccf2` |
| `build/learning_batch/screenshots/batch-contact-181.png` | — | `aa72320a5e1b63fdadf0f0b100f572598db5e95b8406953364defc974ff36842` |
| `build/learning_batch/screenshots/batch-contact-193.png` | — | `d2dda57e2d2acb4c885129ae201ddb3621164f83ac46d0db563e5127099d0155` |
| `build/learning_batch/screenshots/batch-contact-205.png` | — | `8db17d1990ff9cf40f5f75bf1ab34b7251edf310e402824e2820c02bc74386f7` |
| `build/learning_batch/screenshots/batch-contact-217.png` | — | `a5a40a4a44ef0160a231b574ec743840cfb5a8f66ad77eec15d4048240cc7434` |
| `build/learning_batch/screenshots/batch-contact-229.png` | — | `aff57657fe09236ca28416fda8241da57ba2fc1a02eee90f72c7b8abe912946c` |
| `build/learning_batch/screenshots/batch-contact-241.png` | — | `5a81534b4389a12ff9578ceccb36cf9ab6da1b572403ae45271b66ae23e44419` |
| `build/learning_batch/screenshots/batch-contact-253.png` | — | `552fbc1a3a09faea80c8bcec2380b4922fabfc64c01b79f51d06bee007861916` |
| `build/learning_batch/screenshots/batch-contact-265.png` | — | `6b006aca9a0f164c6d872e97550c35adf545bcf981ea285bc5d055eb8abce3a1` |
| `build/learning_batch/screenshots/batch-contact-277.png` | — | `3f16fb56441f363b8f98db3eeb857b9a1ef74f9230df2c0db37cc08aec80ccf9` |
| `build/learning_batch/screenshots/batch-contact-289.png` | — | `625eefe27ec25d15d96562e692b29eb1702d50a876ac836cf915fea6ba380a1b` |
| `build/learning_batch/screenshots/batch-contact-301.png` | — | `13acdcac0696159a2920ef712a5a6d93d21ce86120359369cf5e1f9874f27d10` |
| `build/learning_batch/screenshots/batch-contact-313.png` | — | `cffa8881ec8713497587ba07963552aee1d9cf1cda9d4c99125141f42be3c03d` |
| `build/learning_batch/screenshots/batch-contact-325.png` | — | `cc637116bdc83b91573c505044409bb85869abce061ef45e6140a98f7bc5e70d` |
| `build/learning_batch/screenshots/catalog-contact-001.png` | — | `1855dd0fa8213f41a22c7d4963a6eb12d30a6ba5f3c662a14752d1a23697b833` |
| `build/learning_batch/screenshots/ch01-contact-001.png` | — | `7951d2f2fe656285214fcad14c8939f8a79424d08b4a34f5963722a57603547d` |
| `build/learning_batch/screenshots/full-contact-001.png` | — | `394d37b63c94527f5fa15c17939b1663c7746d48411f42db7abba09e7ed09b7f` |
| `build/learning_batch/screenshots/full-contact-013.png` | — | `166e18fa4f83fc6813653daef39421113dc28cec714aca365788c31759dbf0c1` |
| `build/learning_batch/screenshots/full-contact-025.png` | — | `bd961cc514a1196fd057bef35a771d7e4364d2b5bf44e0165f7f8ee88f1e3d67` |
| `build/learning_batch/screenshots/full-contact-037.png` | — | `4503aa832b15f99163fc8bb0e650a3f7b84d0776cd12b874110808649a13df3e` |
| `build/learning_batch/screenshots/full-contact-049.png` | — | `a8d0e60dc5a282e6499b087327d672ab6c8bfb6f774a9fc61c830df17fd35a8a` |
| `build/learning_batch/screenshots/full-contact-061.png` | — | `61134510b39c170f88c26c146b32135be7651514be1e7b4c7e07f07c4eb52690` |
| `build/learning_batch/screenshots/full-contact-073.png` | — | `b69782edcb171ede841ba0a104a703bcccf77c5e2e3db60096533a3e837cd60d` |
| `build/learning_batch/screenshots/batch-page-003.png` | — | `da556c12589dc379f1a121838473dd5cb59cce8eb7cf31ff1d39d7355559c15a` |
| `build/learning_batch/screenshots/batch-page-004.png` | — | `8ba6379e64688b45d09768337ea6f21680208b9d7e00f4034c9fe93354ef97e7` |
| `build/learning_batch/screenshots/batch-page-005.png` | — | `6bedd5c627d0cf63758ef59cb55ba1af1a331581f9a5365270f0f0dd983ff144` |
| `build/learning_batch/screenshots/batch-page-006.png` | — | `bbfed606fe87368bbfd14a58f996874ddbdcac8936d89c443692bfc9b3ac209f` |

本报告及辅助快照仅写入 `/tmp`；未改动稿件、截图、PDF、QA 或总验收字段。
