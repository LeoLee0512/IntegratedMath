# B2.9—B2.10 后半卷实际视觉复核

复核时间：2026-10-29T17:37:25.237935+00:00。复核者：`/root/astra_build`。
绑定自动QA：`2026-10-29T17:34:04.864330+00:00`，`automated_checks_passed`。本轮审阅版478页、全书693页、第一章审阅版31页、目录218页；QA文件检查时SHA-256为 `bc2a85068be849abea365a0f018b9aaa857c776d1cdc9d6f7884102452f0d4dc`。

## 实际查看与结论

通过图像查看工具逐张实际打开本轮27张联系表：batch-contact-157、169起每12页一张，直到batch-contact-469。最后一张覆盖469—478页，连续覆盖审阅版PDF物理页157—478，共322页。另以原始截图尺度实际打开276页新图与476页附录十八。未复用上批视觉结论代替本轮打开，也未把生成截图或提取文本算作看图。

视觉复核结果：本范围通过，未发现阻断性的裁切、文字重叠、公式出界、缺图或明显缺字方框。当前4份PDF及29张已看截图的哈希在查看前后核对一致，并与本轮QA记录相符。本报告只确认下面列出的实际查看范围，不单独授予全书总验收。

## 具体观察

- 157—261页此前有理数、比例、函数、方程与不等式正文在本轮重新打开，图表与版心未见明显重叠或遮挡。旧单元收尾与部分标题页留白可辨，未误作丢页。
- 262页实际显示第529章“续”标题及B2.9；270页接B2.10，标题层级可辨，续写说明与新正文衔接清楚。279页开始统一答案，未把新单元参考答案混入正文。此范围不包括卷前目录，故不声称检查了目录页的孤行。
- 276页原始尺度查看：蓝圈对应f(x)=2x−1，橙叉对应g(x)=−x+2，各五个样本；(0,−1)、(1/2,0)、(0,2)、(2,0)的标签与点位置正确，(1,1)处圈叉重叠，表示同一个共同点。标签、图例及轴刻度清晰，未见覆盖关键标记。图只画样本，没有用连接线冒充完整函数图；图注明确空心圈表示样本而非删去点。上方代入计算及下方图注完整可见。
- 新B2.9参考答案从421页开始，B2.10答案从427页开始，延续至433页；434页图源表包含第12图，下方另有Fraction精确计算与浮点渲染边界说明。440—441页新来源引用正常接续；441页引用收尾后的留白不遮挡内容。
- 476页原始尺度查看：附录十八标题、六个API说明、两点差商公式与两图交点有序对均完整可读。相同横坐标拒绝、截点与截距、整横轴与全Q²、有限图存在且唯一及目标集合责任均有文字说明。未见公式跨边或段落覆盖。477—478页源码在联系表尺度未见截断，478页有限图检查尾部及return可见。
- 450、453等旧代码末页有较大空白，属于模块收尾分页；476页附录说明最后一段在477页继续，未见重复标题或内容叠印。

## 尺度与范围限制

联系表宽1200像素，每张最多12页，适用于页面连续性、版心、图表存在和明显排版异常检查；缩略图不能充分核对全部细小上下标与每一步证明。276与476页单页图为765×990像素并以原始尺度打开，用于更细查看新图与新公式；这仍不是印刷级逐字校样。未实际打开本轮1—156页，也未打开其他三份PDF的图像；四PDF哈希记录同一次构建身份，不能理解为本复核者看过它们的全部页。数学审阅、来源审计和程序有限验算属于另行证据，视觉通过不替代这些责任。

## 当前PDF绑定

| 路径 | SHA-256 |
| --- | --- |
| `dist/综合数学.pdf` | `75ef79dae3a20c2ebb9012bdbde45ccf8b02f3b4b6d472f8c0fa975c97cf7251` |
| `dist/综合数学_基础续写审阅版.pdf` | `248feef685387dfb074d375cea25b4a75599a666f4ee9af6d356cfcbe3da931c` |
| `dist/综合数学_完整数学目录.pdf` | `6cb12ea75b3c38217ab3e6a86004fc07400cae1bac31236355b3be9766881b55` |
| `dist/综合数学_第一章审阅版.pdf` | `53254c1d606eb037eb1dba3b856d254924debec51c3fe56283f5c9f4a606d1bd` |

## 已实际打开的联系表

| 截图路径 | PDF物理页 | 像素 | SHA-256 |
| --- | --- | --- | --- |
| `build/learning_batch/screenshots/batch-contact-157.png` | 157—168 | 1200×1760 | `9440859cfad58539305a51bab71d7490bfe635143d702c25c15286d839d87ba3` |
| `build/learning_batch/screenshots/batch-contact-169.png` | 169—180 | 1200×1760 | `306e9aa870497943b50f4e1e16d6a82b52f93010ab0554a06c4179d523379811` |
| `build/learning_batch/screenshots/batch-contact-181.png` | 181—192 | 1200×1760 | `176cfa1a9a1f531c66fa77056d819763300e650d733733379ddc5feb60936444` |
| `build/learning_batch/screenshots/batch-contact-193.png` | 193—204 | 1200×1760 | `b358a92414846d769df311a74c57e0f2bdca59b8227ae881ab7d8ad99259a537` |
| `build/learning_batch/screenshots/batch-contact-205.png` | 205—216 | 1200×1760 | `1695eff62ed23758acfdb32606ea18aab6106becce20ec034bc338920f689663` |
| `build/learning_batch/screenshots/batch-contact-217.png` | 217—228 | 1200×1760 | `ccbbbf435cadae42401d75c5bebff3f6a32fbb681d5b151c624a07e3038be64a` |
| `build/learning_batch/screenshots/batch-contact-229.png` | 229—240 | 1200×1760 | `5773160393ab4305fafbab96ca918f5bbf40da15f9c4b024b75b0b6b7f2920cc` |
| `build/learning_batch/screenshots/batch-contact-241.png` | 241—252 | 1200×1760 | `fe627997c5c56c051803be510a0b8efe38f9e11a4eee7864881aa3cf1c48b4eb` |
| `build/learning_batch/screenshots/batch-contact-253.png` | 253—264 | 1200×1760 | `35e14a6500ec9e6c99d6ed2f0b37ea45c734bf3d18d7b32f6c0c243eb045f1a5` |
| `build/learning_batch/screenshots/batch-contact-265.png` | 265—276 | 1200×1760 | `f1c36d51e72a907a9eafcd1585f628d55566aaae4c3ac74d9abdcb8110e5d052` |
| `build/learning_batch/screenshots/batch-contact-277.png` | 277—288 | 1200×1760 | `c18942209af2390ed0a61e9739b1228b9d87d6ebd6e8ba97a71bd4ee0f0d6ba2` |
| `build/learning_batch/screenshots/batch-contact-289.png` | 289—300 | 1200×1760 | `9c497e0a9aaac3c23e9ac1fa5814104f2803c224a9b12f9f20cf998814ce6737` |
| `build/learning_batch/screenshots/batch-contact-301.png` | 301—312 | 1200×1760 | `e85dd1a4ec45f59c7be381fd276bebaf9a96e64d4c41e94633012602647240e2` |
| `build/learning_batch/screenshots/batch-contact-313.png` | 313—324 | 1200×1760 | `548bd1b16c042c4f0b4ed68605774252705cb5a4b99b35bbae0269bc63789609` |
| `build/learning_batch/screenshots/batch-contact-325.png` | 325—336 | 1200×1760 | `e9767a7858fb8d273d06b90f13d09d7352fe8ab7834c0b6a2ca91d325c772e71` |
| `build/learning_batch/screenshots/batch-contact-337.png` | 337—348 | 1200×1760 | `bfffe911a8e2e7ac5c2d22d47203be6f54f4769363711e48fae25231d695b420` |
| `build/learning_batch/screenshots/batch-contact-349.png` | 349—360 | 1200×1760 | `a98d611ff246725ab213de7c6003f54222c2f42ecc1ef6c64e1067b81886a73e` |
| `build/learning_batch/screenshots/batch-contact-361.png` | 361—372 | 1200×1760 | `177464039382883f5331931b5e2f85b12b9ec1e776707ed293b43c8c835766bc` |
| `build/learning_batch/screenshots/batch-contact-373.png` | 373—384 | 1200×1760 | `1bd2eec5f253842be6826a7ec72eac18ee62964a85560034ae0ca133bddbc3ce` |
| `build/learning_batch/screenshots/batch-contact-385.png` | 385—396 | 1200×1760 | `e4ba08baf264dfbe4aa63894424e837d439493ef6eba156f8206da30317a08e5` |
| `build/learning_batch/screenshots/batch-contact-397.png` | 397—408 | 1200×1760 | `55ee59c3cdc3ff706a007b2c658acb49495726d3c7867733e291fc66415b52b6` |
| `build/learning_batch/screenshots/batch-contact-409.png` | 409—420 | 1200×1760 | `3e0b16ecc3c17b56c1365e2e3471b8ca9a64815669ac547253384e06cca8fea8` |
| `build/learning_batch/screenshots/batch-contact-421.png` | 421—432 | 1200×1760 | `44c76e652aca001fa030649cabccdf7c05d49b1f2d8bb47af2c5d482b98a5ece` |
| `build/learning_batch/screenshots/batch-contact-433.png` | 433—444 | 1200×1760 | `4d90065fac85750c66d290219ebd02f6fbdd79a2e0c9f272d4236ae0c57296d4` |
| `build/learning_batch/screenshots/batch-contact-445.png` | 445—456 | 1200×1760 | `1596da5ed2ec41691bcb4727259379be2abe50bfba81df11849e657f14222cc9` |
| `build/learning_batch/screenshots/batch-contact-457.png` | 457—468 | 1200×1760 | `a4adaaf314ce5c404ac266d7aaed1f0eb83f7eeb086cb071de4a70982c8abf01` |
| `build/learning_batch/screenshots/batch-contact-469.png` | 469—478 | 1200×1760 | `f8bebc9573e043d34bb17a9964182b27974ebb0d4ad2803e22463a8895923dc0` |

## 已实际打开的单页

| 截图路径 | PDF物理页 | 像素 | SHA-256 |
| --- | --- | --- | --- |
| `build/learning_batch/screenshots/batch-page-276.png` | 276 | 765×990 | `af112b189abe0e9d38c71b43c7fadd637cfd9b7d7e2023610bac88343e113b91` |
| `build/learning_batch/screenshots/batch-page-476.png` | 476 | 765×990 | `31f553396418f0c178f2a75df6abb92a105800676b4717cacd68bbfc3e4ffeea` |
