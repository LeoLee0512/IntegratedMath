# 第28批前半与其余版本选页实际视觉检查

审阅者：`/root/visual21_front`。
实际检查时间：2026-10-30T04:14:52.777060+00:00 至 2026-10-30T04:17:47.152221+00:00。
绑定 QA validated_at：`2026-10-30T04:13:50.710049+00:00`；QA SHA256：`3b2615b11359f5742f8dff709ecc54a5c4c7994b80ca03d968cddf490c68ea2c`。

本报告仅记录本人实际打开图片所见。当前 QA 状态为 automated_checks_passed；未修改 QA、正式稿或总验收状态。

## 实际范围与观察

- 审阅版物理页 1–336：逐张实际打开 batch-contact-001、013、…、325 共 28 张联系表，连续覆盖全部 336 页。检查页面布局、公式块、表格、图像、页边界及页号；此缩放不支持逐字逐符号校对。
- 其余三 PDF 的全部现有选页联系表：full-contact-001 至 085 共 8 张，覆盖 86 个选页；catalog-contact-001 覆盖 1、2、110、218；ch01-contact-001 覆盖 1、2、16、31。不是通读这些 PDF 的所有页。
- 目录物理页 3、4、5、6、7 实际按 original 打开；第 7 页虽超原 3–6 指派范围，因目录继续而补看。目录字行、引导点和右端页码分离正常。B2.35/B2.36 正文条目为印刷页 452/458，答案为 769/776；几何来源及附录二十六条目可见。
- 额外实际按 original 打开审阅版物理页 468（印刷页 466），检查本批两栏坐标图在 PDF 中的缩放：左右标题、坐标刻度、P/M/Q 与 O/A/B 标签、蓝/棕线和图下注释清楚，无明显碰撞、裁切或拉伸；图注与其后练习没有重叠。没有把独立 PNG 的外观当作 PDF 中外观。

所看图片范围未发现阻断性排版问题。标题页与题献有意留白；审阅目录物理页 7 仅五条附录、合订目录物理页 4 仅三条附录而留白较多，是可见的非阻断分页现象，未擅改版式。正文有跨页延续及短尾页，但所看联系表未见文字越界、公式覆盖正文、表格截断或空白代替图片。新图的有限坐标实例与“示意图不代替证明”说明在放大页可读。

本人没有查看审阅物理页 337–859 的全部联系表（除上述 468 放大页）；这部分由其他审阅者负责。没有独立逐字复核 470 题，也没有以自动零警告替代图片查看；未做 PDF 阅读器点击链接测试。本报告不能单独作为整套书的全部视觉验收。

## 文件绑定

| PDF | SHA256 |
|---|---|
| `dist/综合数学.pdf` | `6995363bd9a014978285d8578677a19344be0e92eff9abbefcd2e136b9a5426a` |
| `dist/综合数学_基础续写审阅版.pdf` | `309b4466315ac8dd99c0404ce7f5544417107c3f286cabb75189024056c28d4e` |
| `dist/综合数学_完整数学目录.pdf` | `6cb12ea75b3c38217ab3e6a86004fc07400cae1bac31236355b3be9766881b55` |
| `dist/综合数学_第一章审阅版.pdf` | `53254c1d606eb037eb1dba3b856d254924debec51c3fe56283f5c9f4a606d1bd` |

共实际查看 44 个 PNG：28 前半联系表、10 其他版本联系表、5 目录原图和 1 新图 PDF 页面原图。当前整批 QA 登记 1035 个 PNG，未声称本人全部查看。QA、4 PDF 及全部所看 PNG 于收尾重新计算散列，与起始快照及 QA 的文件散列一致。

逐图绑定如下（路径相对正式仓库；只读取未修改）：

| PNG | SHA256 |
|---|---|
| `build/learning_batch/screenshots/batch-contact-001.png` | `cb5394cf82f8dfce4e46255dc1accff779e9dede01ad27d817759cd9b3e12fe2` |
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
| `build/learning_batch/screenshots/full-contact-001.png` | `181ca519ac1bcfac970fd635345fbbeaa8a20c118a026e5a66b6b2e5023c301a` |
| `build/learning_batch/screenshots/full-contact-013.png` | `25b5444c3812b21a8b959e8e1d7824e6a232250e713b5fdfec6b0bc92fb15946` |
| `build/learning_batch/screenshots/full-contact-025.png` | `c26bd00fa3126eaba52d8c12a31c9b614b2fe27200848126bbf1618e0e7455b5` |
| `build/learning_batch/screenshots/full-contact-037.png` | `2ad79a361df178061209c0d02bb48312128824ccb3c131e02ffe5ba77810aa69` |
| `build/learning_batch/screenshots/full-contact-049.png` | `6d46fa04b42f6c8448e7da99048759c857fbf99a264fd0892324d815988639d2` |
| `build/learning_batch/screenshots/full-contact-061.png` | `5ccf3feae0053c2b7021cd0e8cf2aca04e419be251be9094ad8218d918114e63` |
| `build/learning_batch/screenshots/full-contact-073.png` | `0aee9919604719843277bd998dda284fa8b84004a31d99082ae7f0705cdec8b7` |
| `build/learning_batch/screenshots/full-contact-085.png` | `127aabdff6e0a90c6d20cefa13a6c6bae88e7bd3c65cf460352c335f406d524e` |
| `build/learning_batch/screenshots/batch-page-003.png` | `ba81bf0ae4d2bb11241a19ea86a5d728f5da28884c3935f78287d2d20ae56ffe` |
| `build/learning_batch/screenshots/batch-page-004.png` | `39caac5bca86797110953c5ed23c0f4c88b6c101c7458ed0a877328b9bcdd393` |
| `build/learning_batch/screenshots/batch-page-005.png` | `1f956e2ddeec010c9e9c39a7bdd18ba82949315495934daebc027e0ffd62c95a` |
| `build/learning_batch/screenshots/batch-page-006.png` | `e12e949202127a059f74d9e676ef7f7445de9f4e4ec861dffade40b689d1257d` |
| `build/learning_batch/screenshots/batch-page-007.png` | `7fcc4854f542a1a9e336849bbc791ead90bdd2dc3ac47e52584aa36f98a35f89` |
| `build/learning_batch/screenshots/batch-page-468.png` | `03d20db0033fe6d4d5384a8b37d692abe38f1b20c81f6fcf9dd6dbf2edfbb76b` |

机器快照：`/tmp/real_plane_metric_front_visual_snapshot.json`，SHA256 `ed059185aa1e9d89007e5702eadb40f1cd7c6f96a31bb08d611b00204a77f399`。
