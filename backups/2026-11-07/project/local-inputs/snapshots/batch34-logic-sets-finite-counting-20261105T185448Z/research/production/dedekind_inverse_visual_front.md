# 第 25 批前半实际视觉审阅

审阅者：`/root/visual21_front`。

结论：本次实际重新打开并查看当前冻结构建的 40 张 PNG，在下述范围与缩放尺度内未发现视觉阻断。没有用上一批截图或相同哈希代替实际查看。

开始时间（UTC）：`2026-10-30T03:05:48.296642+00:00`；完成时间：`2026-10-30T03:08:29.660315+00:00`。QA `validated_at`：`2026-10-30T03:04:40.471787+00:00`；QA SHA-256：`5a52b3fc53377bcb1a5ee42428f2255f0b93906b8706d4687b1a34fd0e986993`。读取时状态为 `automated_checks_passed`，本审阅者未修改 QA 或总验收状态。

## 实际范围与发现

- 审阅版物理第 1–336 页：`batch-contact-001` 至 `batch-contact-325`，步长 12，共 28 张联系图。逐张查看页面边缘、正文/公式整体位置、表格与插图边界、分页、页脚及明显空白；未见明显越界、重叠、缺页或意外空白。章节开头和题尾的留白有可见内容与结构依据，不能仅凭稀疏版面判为故障。
- 其他三个 PDF 的全部现有联系图共 8 张：`catalog-contact-001`（物理 1、2、110、218 页），`ch01-contact-001`（1、2、16、31 页），以及 `full-contact-001/013/025/037/049/061`（共 72 个选页）。全部实际查看；标题、正文、表格、公式与代码区在联系图尺度内未见明显裁切或碰撞。这里是完整版本的选页查看，不是逐页覆盖其 979 页。
- 审阅版物理 3、4、5、6 页另用 `detail=original` 原图实际打开。目录文字、点线和页码分栏清楚；B2.29/B2.30 正文印刷页码为 409/414，答案 683/688，新来源项 709。长条目没有与右侧页码碰撞，也没有被边界截断。

审阅版 765 页、完整 PDF 979 页、第一章版 31 页、完整目录版 218 页。本报告仅覆盖本人上述实际查看范围；审阅版 337–765 页及新内容重点放大检查由 root 另行负责，本报告不代签。联系图用于发现整体排版问题，不能排除微小字形或单个数学符号错误；除目录四页外没有逐页原尺寸细读，也不替代数学审稿和 PDF 链接功能检查。

## 文件绑定

以下路径均相对 `/workspace/IntegratedMath-book`。查看前快照、查看后再次计算确认全部 40 张 PNG、4 个 PDF 和 QA 文件保持不变；全部 40 张 PNG 哈希与当前 QA 的 `screenshot_sha256` 一致。机器可读完整快照保存于 `/tmp/inverse_front_visual_snapshot.json`。

| 文件 | SHA-256 |
| --- | --- |
| `data/production/batch_validation.json` | `5a52b3fc53377bcb1a5ee42428f2255f0b93906b8706d4687b1a34fd0e986993` |
| `dist/综合数学.pdf` | `3f720d5fffa96fa1298785c284f492845b5fc51bd2335339b0a3c60e60a939c3` |
| `dist/综合数学_基础续写审阅版.pdf` | `dc7d0bf566d7542d8d9b81547afb862b68dde6cb080a2d2c03bba96cd0c008a9` |
| `dist/综合数学_完整数学目录.pdf` | `6cb12ea75b3c38217ab3e6a86004fc07400cae1bac31236355b3be9766881b55` |
| `dist/综合数学_第一章审阅版.pdf` | `53254c1d606eb037eb1dba3b856d254924debec51c3fe56283f5c9f4a606d1bd` |
| `build/learning_batch/screenshots/batch-contact-001.png` | `834a631374549e2e4752aff1af528171714a7a60df98922b05c998617261baba` |
| `build/learning_batch/screenshots/batch-contact-013.png` | `ab224cab814badefac492fefbcfb90e0029c764f78b718424dcb3bc37d6f1cf9` |
| `build/learning_batch/screenshots/batch-contact-025.png` | `b775357e7fa2b94641545aeb2426c91dc0b65e140aea1476ff40f53e6acccc59` |
| `build/learning_batch/screenshots/batch-contact-037.png` | `7720a529b3cb54166792513c823977bece5f95b0af2344dce86324b0ddd9527a` |
| `build/learning_batch/screenshots/batch-contact-049.png` | `9ce6945222de2f0805e968fab470ef10cf3fc4f78ffb6be3179ac78f2faa59c6` |
| `build/learning_batch/screenshots/batch-contact-061.png` | `63b2fe0c9f11ca38ba4c063aa2a9778230b30486abdf2751541a454bfbec642c` |
| `build/learning_batch/screenshots/batch-contact-073.png` | `5b338ebf3279b492a9c20bae8c0c65fc669254714b73e2d5a215d679aad37eef` |
| `build/learning_batch/screenshots/batch-contact-085.png` | `21ea2c1059ae4a1f56c08a9c5bfed5d60bdf923140532ecdd17505e3026c8772` |
| `build/learning_batch/screenshots/batch-contact-097.png` | `1fb674142c503b84e0457385602011d6f40aa077cddcc46dedd1aec5db579015` |
| `build/learning_batch/screenshots/batch-contact-109.png` | `310e0d4721d007a44a90d6d9adb6baac22888ad83ebf481652c0ecd4649cba6a` |
| `build/learning_batch/screenshots/batch-contact-121.png` | `83c82021d61fcc32d5fd86ad6144a066c03503a7535c5b92d45575d04fa64e73` |
| `build/learning_batch/screenshots/batch-contact-133.png` | `e07abfdb8ece075ce3273e49dba94c71785cd8a0456e201d4c2882d4d7f0cfb8` |
| `build/learning_batch/screenshots/batch-contact-145.png` | `25ed63a2881987ac9e519f5de919ae9852908a014a357d56b0bbf5283361199b` |
| `build/learning_batch/screenshots/batch-contact-157.png` | `31c80b7c66a7607aa20cbf3ca79e5f513b9e75f6ccccd7146a32206b8a0de2d2` |
| `build/learning_batch/screenshots/batch-contact-169.png` | `6ca231b5c48b860a967a707295f69e09142200c3978eb5ec1d5560412578ccf2` |
| `build/learning_batch/screenshots/batch-contact-181.png` | `aa72320a5e1b63fdadf0f0b100f572598db5e95b8406953364defc974ff36842` |
| `build/learning_batch/screenshots/batch-contact-193.png` | `d2dda57e2d2acb4c885129ae201ddb3621164f83ac46d0db563e5127099d0155` |
| `build/learning_batch/screenshots/batch-contact-205.png` | `8db17d1990ff9cf40f5f75bf1ab34b7251edf310e402824e2820c02bc74386f7` |
| `build/learning_batch/screenshots/batch-contact-217.png` | `a5a40a4a44ef0160a231b574ec743840cfb5a8f66ad77eec15d4048240cc7434` |
| `build/learning_batch/screenshots/batch-contact-229.png` | `aff57657fe09236ca28416fda8241da57ba2fc1a02eee90f72c7b8abe912946c` |
| `build/learning_batch/screenshots/batch-contact-241.png` | `5a81534b4389a12ff9578ceccb36cf9ab6da1b572403ae45271b66ae23e44419` |
| `build/learning_batch/screenshots/batch-contact-253.png` | `552fbc1a3a09faea80c8bcec2380b4922fabfc64c01b79f51d06bee007861916` |
| `build/learning_batch/screenshots/batch-contact-265.png` | `6b006aca9a0f164c6d872e97550c35adf545bcf981ea285bc5d055eb8abce3a1` |
| `build/learning_batch/screenshots/batch-contact-277.png` | `3f16fb56441f363b8f98db3eeb857b9a1ef74f9230df2c0db37cc08aec80ccf9` |
| `build/learning_batch/screenshots/batch-contact-289.png` | `625eefe27ec25d15d96562e692b29eb1702d50a876ac836cf915fea6ba380a1b` |
| `build/learning_batch/screenshots/batch-contact-301.png` | `13acdcac0696159a2920ef712a5a6d93d21ce86120359369cf5e1f9874f27d10` |
| `build/learning_batch/screenshots/batch-contact-313.png` | `cffa8881ec8713497587ba07963552aee1d9cf1cda9d4c99125141f42be3c03d` |
| `build/learning_batch/screenshots/batch-contact-325.png` | `cc637116bdc83b91573c505044409bb85869abce061ef45e6140a98f7bc5e70d` |
| `build/learning_batch/screenshots/catalog-contact-001.png` | `1855dd0fa8213f41a22c7d4963a6eb12d30a6ba5f3c662a14752d1a23697b833` |
| `build/learning_batch/screenshots/ch01-contact-001.png` | `7951d2f2fe656285214fcad14c8939f8a79424d08b4a34f5963722a57603547d` |
| `build/learning_batch/screenshots/full-contact-001.png` | `c218ae78e1ea185105a9419f6a6d28aea27e7ae23649a7c12ba69913c9eb091e` |
| `build/learning_batch/screenshots/full-contact-013.png` | `89466b7d5c31f0ab164369cf557f5cb1f7fb2a8c7dde13b9e994c508ba2087b1` |
| `build/learning_batch/screenshots/full-contact-025.png` | `e354e0c3ac766d553f7670f80e74d14f3254bf02cc5f413339e794cee25fd9f2` |
| `build/learning_batch/screenshots/full-contact-037.png` | `14482d94252ad2d04524f05d15b4ddb012b80a8cd669178485e779320cbd87a5` |
| `build/learning_batch/screenshots/full-contact-049.png` | `c481326a17f46be079dd98ec299d237dad9d914a2dbfa04d063e1c13f7791291` |
| `build/learning_batch/screenshots/full-contact-061.png` | `914870e7b1bde97687a8c1e5a099e0f73fe384aae602298f8d1a2b156692455b` |
| `build/learning_batch/screenshots/batch-page-003.png` | `da556c12589dc379f1a121838473dd5cb59cce8eb7cf31ff1d39d7355559c15a` |
| `build/learning_batch/screenshots/batch-page-004.png` | `044fe1d04a49d43f632942764002af93b19883fa6283c92ca653eaeaba4db62f` |
| `build/learning_batch/screenshots/batch-page-005.png` | `d7c1d29094c81598865313b32eec861646a16efac839d01d8d0557efd63ed707` |
| `build/learning_batch/screenshots/batch-page-006.png` | `6a616db874b3d4cfae516a41a08adf31b10bf9e2fff78c0edfe35776b8a24856` |

未修改正式稿件、构建产物、QA、审阅登记或批次状态；仅写本报告与 /tmp 快照。

最终自动验收时间：2026-10-30T03:04:40.471787+00:00。原报告SHA-256 `ea0c789dc63adca09a2478425a40ac5de5540d6dec108b5273cb4019c9713d28`。
