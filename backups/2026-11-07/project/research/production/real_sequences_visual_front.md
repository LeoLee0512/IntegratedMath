# 第30批实数数列：前半及其他版本选页实际视觉记录

审阅者：`/root/visual21_front`。只在 `/tmp` 写记录，未修改稿件、PDF、截图、QA 或 aggregate。

开始绑定时间：2026-10-30T04:59:37.878309+00:00；查看完成并结束复核时间：2026-10-30T05:02:18.576452+00:00。
绑定本次 QA validated_at：2026-10-30T04:58:16.106398+00:00；状态 `automated_checks_passed`。
QA `data/production/batch_validation.json` SHA-256：`b061e0f29aa27bb302f2350ab3af4c98e733fb5c792c6cc9556b726d7ef91e73`。

## 版本、实际范围与结论

本次检查当前重建后的审阅版 919 页、合订版 1133 页、第一章版 31 页及目录版 218 页。没有沿用第29批 891 页 PDF 或旧截图的检查结论。查看前先计算当前 PDF 和选定 PNG 哈希并与本次 QA 对照。

通过 view_image 实际逐张打开并查看 44 张本次图像：审阅版物理 1–336 页全部 28 张联系表；合订版全部 8 张现有选页联系表（96 个选页）；目录与第一章版各 1 张联系表（各 4 个选页）；审阅版物理 3–7 页目录及物理 488 页新图的 6 张原图。目录版选页为 1、2、110、218；第一章版选页为 1、2、16、31。各联系表按图上的 PDF page 标记查看。

以上范围与尺度内未见阻断的明显裁切、文字/公式重叠、缺图、乱码或异常空白页。前半正文、表格、公式和原有插图均保持版心内布局；短尾页与部标题页留白有相应内容依据。其他版本选页包括新增数列单元、答案、图清单及末尾附录，联系表尺度未见明显越界。

目录 3–7 原图检查：中文标题、各层级、引导点及页码清楚；B4.1/B4.2 与数列新章已列入，答案及来源条目可读，附录二十八出现在目录末尾。物理 7 页和合订版物理 4 页下方的留白为目录自然结束，未作为缺页。

新图 21 所在物理第 488 页（印刷页码 486）已实际以原图查看。图中 ±ε 边界、零线、n=3 的空心边界点、n=4 阈值与尾部点、坐标标签和两份箭头说明可辨，未重叠或被裁掉。图下全尾估计、有限图不代替证明及只处理单个 ε 的说明可读；图注与正文衔接正常。显示式和上下文正确排出 ε=1/4、N=4，正文也显示 n=3 等于边界不满足严格条件。此处记录 PDF 实际视觉，不以绘图脚本曾运行替代。

## 复核与范围限制

结束时重新计算 QA、4 个 PDF 和本记录全部 44 张 PNG 的 SHA-256，均与开始快照一致，且逐项等于 QA artifact_sha256 / screenshot_sha256。QA 共生成 1110 张 PNG；本人实际查看其中 44 张，不声称全部 1110 张都逐张看过。

联系表仅用于整体布局与明显排版异常检查，不能替代每页原尺寸逐字校读。除目录 3–7 与新图 488 外，本报告未声称原尺寸审查。审阅版后半物理 337–919 的完整联系表与其他重点放大页由其他审阅者负责，本报告不代签其范围，也不代替数学、教学、链接、代码、来源或整批验收。

## PDF SHA-256

| 文件 | SHA-256 |
|---|---|
| `dist/综合数学.pdf` | `08d0290d7b0c5142172e86b8648d10612e3457c75488c5f43850ee3f030921c7` |
| `dist/综合数学_基础续写审阅版.pdf` | `63e80e2de25315277176d49ff8630fc68f2188048f61d7a569a05cabf2957f25` |
| `dist/综合数学_完整数学目录.pdf` | `6cb12ea75b3c38217ab3e6a86004fc07400cae1bac31236355b3be9766881b55` |
| `dist/综合数学_第一章审阅版.pdf` | `53254c1d606eb037eb1dba3b856d254924debec51c3fe56283f5c9f4a606d1bd` |

## 实际查看的全部 PNG SHA-256

以下相对路径根为 `/workspace/IntegratedMath-book`。

| 图像 | SHA-256 |
|---|---|
| `build/learning_batch/screenshots/batch-contact-001.png` | `5af9ed4451a6c7a79c99b293720f20f8291a3db4b6f2b29bed6307ea0b19e504` |
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
| `build/learning_batch/screenshots/full-contact-001.png` | `8fee2f564ad1f54af8ce4584548c0930782503047b11bf1a77c10c859a8768cb` |
| `build/learning_batch/screenshots/full-contact-013.png` | `25b5444c3812b21a8b959e8e1d7824e6a232250e713b5fdfec6b0bc92fb15946` |
| `build/learning_batch/screenshots/full-contact-025.png` | `368305770e8d2266f1fb3ea5e176c4be895485b73231c64dae0bb8f434268b29` |
| `build/learning_batch/screenshots/full-contact-037.png` | `eaaf2fb00c179764ceb6a808c8f070e758a6df8d4f9310a55324b374a4a43645` |
| `build/learning_batch/screenshots/full-contact-049.png` | `4c9deac631ba60ddf3fe9b7a204f67bce088782181e24498a70cb65c6890b4b4` |
| `build/learning_batch/screenshots/full-contact-061.png` | `e62add82922dfc24032484f282c3c6ffa12723237f0d5a8ab98a65e2689801f9` |
| `build/learning_batch/screenshots/full-contact-073.png` | `9d6ccb195f6c62fa5b403268ee25bdc25d5bb76c4c814a3fa3907c2a36b2411c` |
| `build/learning_batch/screenshots/full-contact-085.png` | `8b302d82c001cd1517622f442e9ae28729ad44c8b232e186aeb4fe70559a230d` |
| `build/learning_batch/screenshots/batch-page-003.png` | `ba81bf0ae4d2bb11241a19ea86a5d728f5da28884c3935f78287d2d20ae56ffe` |
| `build/learning_batch/screenshots/batch-page-004.png` | `024c676cbfea5ffd7183e55a8233ce226e31c6cae37d01f74a68cf3b817b9443` |
| `build/learning_batch/screenshots/batch-page-005.png` | `804b4c4ba5ca8b1bf26708a497de512d2872c43bc272b1d42f40c7abe4f290b0` |
| `build/learning_batch/screenshots/batch-page-006.png` | `50d3b182583bcadd4397c7eed9cfef8e1b92c16c6fde35838e217e1c2394f1bb` |
| `build/learning_batch/screenshots/batch-page-007.png` | `4d2646b40dd4c6b32cf23210dede2585b84502eea8f612e61d9ac7a9b331bd99` |
| `build/learning_batch/screenshots/batch-page-488.png` | `3baeeca5239f0d7d35790b653bf175af18e044d42dd6453b61866b26950a436c` |

开始快照：`/tmp/real_sequences_visual_front_snapshot.json`。范围内实际视觉未见阻断，未写总验收状态。
