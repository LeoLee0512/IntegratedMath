# 第29批前半与其他版本选页独立视觉记录

审阅者：`/root/visual21_front`。本记录由实际逐张查看图像后形成；只写入 `/tmp`，未修改正文、PDF、截图、QA 或总验收状态。

开始核绑定时间：2026-10-30T04:31:28.174335+00:00；实际查看完成及结束复核时间：2026-10-30T04:36:03.107209+00:00。
本批 QA `validated_at`：2026-10-30T04:30:27.090103+00:00；状态：`automated_checks_passed`。
QA 文件：`data/production/batch_validation.json`；SHA-256：`2925db3e10bf9df8ba19a3b2ca8fc5fd7de6b93e0d3abee45057e245710dd7f2`。

## 实际范围与结果

本次通过 `view_image` 实际打开并查看 44 张本批生成图像：审阅版物理第 1–336 页的全部 28 张联系表；合订版全部现有 8 张选页联系表（92 个选页）；目录版和第一章审阅版各 1 张联系表（各 4 个选页）；审阅版目录物理第 3–7 页及新投影图物理第 482 页的 6 张原图。目录版为物理 1、2、110、218 页；第一章版为物理 1、2、16、31 页。联系表覆盖范围按图上 PDF page 标记核对。没有把旧批次截图当作本批结果。

在上述范围及查看尺度内，未发现阻断交付的明显裁切、文字或公式重叠、缺图、乱码或异常空白页。前半联系表中的正文、题答、表格与原有图像保持版心内布局。合订版选页含新增单元、答案和附录二十七的首尾代码页；联系表尺度未见越界。

原图目录 3–6 页标题、层级、引导点与页码清楚；第 7 页为附录十八至二十七的目录尾页，下方留白属于目录自然结束，不按缺页处理。合订版目录第 4 页也有正常尾页留白。目录条目显示新增 B2.37、B2.38 及相应答案与参考资料。

物理第 482 页（印刷页码 480）的投影图已经原图放大检查：坐标、直线、P/X/H/Y 标注、u、距离标记及平方距离恒等式可读，中文图题、图注与正文不重叠；图注中的有限有理坐标实例和正文证明边界可读。图像未超出版心。

## 绑定与限制

审阅版 891 页，合订版 1105 页，目录版 218 页，第一章审阅版 31 页。QA 总共生成 1076 张 PNG；本审阅者实际查看其中 44 张，不声称逐张检查全部 1076 张。查看结束后重新计算当前 QA、4 个 PDF 及这 44 张 PNG 的 SHA-256，均与开始快照一致，并逐一与 QA 的 artifact_sha256 / screenshot_sha256 核对一致。

联系表适于检查整体布局与明显排版异常，不能替代逐页原尺寸逐字校读。除目录 3–7 与投影图 482 外，未在本记录中宣称原尺寸审查。审阅版第 337–891 页的完整联系表及其他放大页由其他审阅者负责；本记录不代签其检查，不替代数学、教学、链接、源代码或全书验收。自动 QA 结果仅作为所查看版本的绑定依据。

## 四个 PDF 的 SHA-256

| 文件 | SHA-256 |
|---|---|
| `dist/综合数学.pdf` | `30607eb40002c0da1111e28d479594904a57598c15bef00c98285859765421b1` |
| `dist/综合数学_基础续写审阅版.pdf` | `243e380dbda24458c643c81ce11a206c9c7275d06e24619d9f72bea4f4a61e87` |
| `dist/综合数学_完整数学目录.pdf` | `6cb12ea75b3c38217ab3e6a86004fc07400cae1bac31236355b3be9766881b55` |
| `dist/综合数学_第一章审阅版.pdf` | `53254c1d606eb037eb1dba3b856d254924debec51c3fe56283f5c9f4a606d1bd` |

## 实际查看的全部 PNG 与 SHA-256

目录均相对于 `/workspace/IntegratedMath-book`。

| 图像 | SHA-256 |
|---|---|
| `build/learning_batch/screenshots/batch-contact-001.png` | `141c2c2d2d7b5ae63cb4d6a974888beab7736eb264059241a08607e6fa48705e` |
| `build/learning_batch/screenshots/batch-contact-013.png` | `d82ff7dab75d69b892de57aafbf1ae3f39b0e75ef02210cc9b8042f996a6fe90` |
| `build/learning_batch/screenshots/batch-contact-025.png` | `1d1603665c59c7b5fa8bceaf5a430c03dd02776035601cd525b5a5189ccd7659` |
| `build/learning_batch/screenshots/batch-contact-037.png` | `c9243df7b2f338f284b12618948852746464ce5e24cfe4c0810704312f5c9d1f` |
| `build/learning_batch/screenshots/batch-contact-049.png` | `8f49752c0cd6b73ae57264244db6722f54ade31ae7241b8d7519ac0cbc4a05e9` |
| `build/learning_batch/screenshots/batch-contact-061.png` | `1012b6cd7233fbdf4ab28d24305b99ebd7f01851632ed5f1b4ee6fb8f5d360cc` |
| `build/learning_batch/screenshots/batch-contact-073.png` | `a9116c9fd728d38e4b8e01a12b1daef9da31dfab837341e1ba08eafbcaf7bc4b` |
| `build/learning_batch/screenshots/batch-contact-085.png` | `29663e2735d200e9542fc1ead901575022ea5383a89b3c8737d1d071311e996e` |
| `build/learning_batch/screenshots/batch-contact-097.png` | `edb2944cd16526b5ca377b76e2265b63279c3cbe95001175146b6246b2554e40` |
| `build/learning_batch/screenshots/batch-contact-109.png` | `6209caea72fd900a1d802a2047115a6a9d2b3a4d1a5119522520583c9c6d4e80` |
| `build/learning_batch/screenshots/batch-contact-121.png` | `e2421f6a1c7f9888c5cf730a5e5cef83becd02ff53f6051f0d59c79a59e22747` |
| `build/learning_batch/screenshots/batch-contact-133.png` | `aa24a15cf1ee888214f59e935df54d11bb190ca1cf711ac4e6bc2975db6294f7` |
| `build/learning_batch/screenshots/batch-contact-145.png` | `de07fdc1a677b176c9fb74801534e112726a56db6aaa53e4d7bb55d48dd8f990` |
| `build/learning_batch/screenshots/batch-contact-157.png` | `f91558eeb4b312778d950bd63d1a322b30005b4f4ed81a855bbde83938de3832` |
| `build/learning_batch/screenshots/batch-contact-169.png` | `71d995fb42a5fa6264c46506663278ad12a5175eeb3e8d24aecdb455414471fc` |
| `build/learning_batch/screenshots/batch-contact-181.png` | `07234d637f5352d95a02305fd1b007e6329bde352873c4d9d46051ea27689288` |
| `build/learning_batch/screenshots/batch-contact-193.png` | `6c071b7d72f1f700b24abf8a1b77628d7fdd6c4b281dd4927f702b62e7c0c163` |
| `build/learning_batch/screenshots/batch-contact-205.png` | `bc51fdc4b4bb93e5585c692d6fb4a2229541dbf494dfb515bf18a4f90de6c3ad` |
| `build/learning_batch/screenshots/batch-contact-217.png` | `17d90f66bbc850b382a154cd7da07d51878aed5644e60cd73d847c01a6a10e52` |
| `build/learning_batch/screenshots/batch-contact-229.png` | `ccf4908a6b88e933f852866271aed4b593d616b8becea374c90f10e122043f34` |
| `build/learning_batch/screenshots/batch-contact-241.png` | `04289bded7bbd458125b7af412addd1c68b1ab7d8d8a65e078695884e322c4ec` |
| `build/learning_batch/screenshots/batch-contact-253.png` | `3f12093953d41c2bab98dabb9b96955d07388b65c5a5236dd35e4a4d5185f734` |
| `build/learning_batch/screenshots/batch-contact-265.png` | `283489cf923e786ab692f0efbdf216b69aabb2bdabb30a4680787c4763d12b4f` |
| `build/learning_batch/screenshots/batch-contact-277.png` | `30bc4087e322626479c09d7903a4bd295f106505510774fe2aa1a2cf83392349` |
| `build/learning_batch/screenshots/batch-contact-289.png` | `d48506f76b02417943225d71a350a229dcb0ee4a73976e9f393560f93f32e2a7` |
| `build/learning_batch/screenshots/batch-contact-301.png` | `d16d1f4d7077641103c38970b8cdc35dc9b68a377a73f6c2b4de373945e367d7` |
| `build/learning_batch/screenshots/batch-contact-313.png` | `b73a48afdeab9d4de4e834887d430ab7ff073ee292d0a74e7b5d638607c2689b` |
| `build/learning_batch/screenshots/batch-contact-325.png` | `578936e349ac3c372af4c5bcb8063b33a973b1affbda61a6ea7a4471aa80d2ec` |
| `build/learning_batch/screenshots/catalog-contact-001.png` | `1855dd0fa8213f41a22c7d4963a6eb12d30a6ba5f3c662a14752d1a23697b833` |
| `build/learning_batch/screenshots/ch01-contact-001.png` | `7951d2f2fe656285214fcad14c8939f8a79424d08b4a34f5963722a57603547d` |
| `build/learning_batch/screenshots/full-contact-001.png` | `60b9b5e40b1580899fb39f90eb62af26eefd2e139e4ef41c53e4cf8c2ec7f479` |
| `build/learning_batch/screenshots/full-contact-013.png` | `25b5444c3812b21a8b959e8e1d7824e6a232250e713b5fdfec6b0bc92fb15946` |
| `build/learning_batch/screenshots/full-contact-025.png` | `92ed8a8f08241453c0a879e127cc557af81d87c33ca85429c19f6b438bf35a55` |
| `build/learning_batch/screenshots/full-contact-037.png` | `eaaf2fb00c179764ceb6a808c8f070e758a6df8d4f9310a55324b374a4a43645` |
| `build/learning_batch/screenshots/full-contact-049.png` | `118094af3e06b4470e3147328e4344f252063349aa2e08107351fa5c8f04ce3e` |
| `build/learning_batch/screenshots/full-contact-061.png` | `a1ceec844fe2592c443be4eb866631f8560450af3ba5ad13e1caa799846a67bb` |
| `build/learning_batch/screenshots/full-contact-073.png` | `d5417ebd6a72c3e9856479c21bc231078c55515e819cf11b4b91b7a09134b677` |
| `build/learning_batch/screenshots/full-contact-085.png` | `1bb7920ae71c6b80e313146366558e13fbad6fbfb961628406bdb2b38b7b66c0` |
| `build/learning_batch/screenshots/batch-page-003.png` | `ba81bf0ae4d2bb11241a19ea86a5d728f5da28884c3935f78287d2d20ae56ffe` |
| `build/learning_batch/screenshots/batch-page-004.png` | `e51552b6155483d679ef30f3042fc510c1cf072d819f5fd72f3e9c9fb1fa92e8` |
| `build/learning_batch/screenshots/batch-page-005.png` | `cd61822cac5b19b2b9fe3c9365d3b1d6e40845b92943159d4313129c435ab9ea` |
| `build/learning_batch/screenshots/batch-page-006.png` | `1a0aab4ea2c223998a9b48ed734b767b1c8daf92621d214b28435d9435d516b2` |
| `build/learning_batch/screenshots/batch-page-007.png` | `c47ac8348c9fa35908db588e7fe43921a3d389daff5317849134941a34c4c736` |
| `build/learning_batch/screenshots/batch-page-482.png` | `e8cc7b8cb364e6febcd46f31acc667710f6d7e791dd92cd5082a684fc12de798` |

开始快照：`/tmp/real_lines_projection_front_visual_snapshot.json`。本记录结论仅为以上明确范围内的视觉检查未见阻断。
