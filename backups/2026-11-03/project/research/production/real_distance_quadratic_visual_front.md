# 第 27 批前半独立视觉复核

审阅者：`/root/visual21_front`。
开始：`2026-10-30T03:52:26.994870+00:00`；完成及最终字节复核：`2026-10-30T03:55:19.033404+00:00`。
QA validated_at：`2026-10-30T03:51:16.569489+00:00`，状态 `automated_checks_passed`。

结论：在以下实际查看范围和尺度内未发现阻断性的可见排版问题。目录末页单条目形成较多留白，作为非阻断版式观察记录。本报告不修改总验收或代替其他审阅。

## 实际查看

- 审阅版物理 1–336 页：逐张实际查看 28 张联系图，编号 001、013、…、325，每张连续 12 页。
- 其他三个版本当前生成的全部 9 张选页联系图：完整书 7 张共 80 选页（末张 8 页），第一章 1 张含 1、2、16、31 页，完整目录 1 张含 1、2、110、218 页。完整书末张是 1024、1027、1030、1032、1034、1037、1039、1040 页。
- 审阅版目录物理 3–6 页逐张以 original 模式实际查看；发现目录本批延续至物理 7 页后，也额外打开第 7 页原图。共 42 个实际查看 PNG，未使用旧批次图替代。

## 观察

联系图尺度上正文、公式块、证明、练习、表格及图示排列正常，未见明显越界、裁切、叠字或无内容的异常整页。章首、献辞和短段落的留白符合所示内容。其他版本选页的表格、代码和末页续代码仍在版心内。

目录 3–6 页原图的层级、引导点和页码清楚。新增 B2.33/B2.34 正文条目对应印刷页码 436/445，答案条目为 738/746；这些是实际可见目录读数，不作为目标页链接逐项核验。物理第 7 页只有“附录二十五 分割网格的有限见证绘图”条目和页码 823，留白明显，但该条目完整，没有文字被截掉。完整书物理第 4 页同样仅延续最后附录条目；按当前冻结版式记录此分页，不自行缩字或改源。

## 边界

联系图支持整页布局和明显缺陷检查，不能证明全部小字号、上下标、数学符号或链接都正确。除目录 3–7 页外，本次没有逐页放大前半正文；未独立查看审阅版 337–826 页，这部分和新内容放大页由主审另行记录。完整书 1040 页、目录 218 页、第一章 31 页在本报告中仅检查指定选页。文本教学审、自动检查和过去批次视觉不代替此次实际图像查看。

## 字节绑定

查看前后重算 QA、四份 PDF 及开始记录的 41 PNG，46 个文件 SHA 全部不变。额外查看的第 7 页原图另算 SHA 并匹配同一未变 QA。全部 42 PNG 都与当前 screenshot_sha256 逐项一致。下列路径相对于 `/workspace/IntegratedMath-book`。

| 文件 | PDF 页数 | SHA-256 |
|---|---:|---|
| `data/production/batch_validation.json` | — | `1e0d96b8f79d95aebccef5c68a4b3331be01a5bf4a72d5029294863f5acee9f8` |
| `dist/综合数学.pdf` | 1040 | `de58ea8b3f453764fc98a0a071bb0bdaebfb5c53ee62879f548dbf1957114ede` |
| `dist/综合数学_基础续写审阅版.pdf` | 826 | `9f7258274fe84bd8d54d532100213f5a2007030765c398a198df5acbf5bdde56` |
| `dist/综合数学_完整数学目录.pdf` | 218 | `6cb12ea75b3c38217ab3e6a86004fc07400cae1bac31236355b3be9766881b55` |
| `dist/综合数学_第一章审阅版.pdf` | 31 | `53254c1d606eb037eb1dba3b856d254924debec51c3fe56283f5c9f4a606d1bd` |
| `build/learning_batch/screenshots/batch-contact-001.png` | — | `844172db342a3aa2186407f64bc9e6b9de3a0677f032dd296c149fefb3783445` |
| `build/learning_batch/screenshots/batch-contact-013.png` | — | `d82ff7dab75d69b892de57aafbf1ae3f39b0e75ef02210cc9b8042f996a6fe90` |
| `build/learning_batch/screenshots/batch-contact-025.png` | — | `1d1603665c59c7b5fa8bceaf5a430c03dd02776035601cd525b5a5189ccd7659` |
| `build/learning_batch/screenshots/batch-contact-037.png` | — | `c9243df7b2f338f284b12618948852746464ce5e24cfe4c0810704312f5c9d1f` |
| `build/learning_batch/screenshots/batch-contact-049.png` | — | `8f49752c0cd6b73ae57264244db6722f54ade31ae7241b8d7519ac0cbc4a05e9` |
| `build/learning_batch/screenshots/batch-contact-061.png` | — | `1012b6cd7233fbdf4ab28d24305b99ebd7f01851632ed5f1b4ee6fb8f5d360cc` |
| `build/learning_batch/screenshots/batch-contact-073.png` | — | `a9116c9fd728d38e4b8e01a12b1daef9da31dfab837341e1ba08eafbcaf7bc4b` |
| `build/learning_batch/screenshots/batch-contact-085.png` | — | `29663e2735d200e9542fc1ead901575022ea5383a89b3c8737d1d071311e996e` |
| `build/learning_batch/screenshots/batch-contact-097.png` | — | `edb2944cd16526b5ca377b76e2265b63279c3cbe95001175146b6246b2554e40` |
| `build/learning_batch/screenshots/batch-contact-109.png` | — | `6209caea72fd900a1d802a2047115a6a9d2b3a4d1a5119522520583c9c6d4e80` |
| `build/learning_batch/screenshots/batch-contact-121.png` | — | `e2421f6a1c7f9888c5cf730a5e5cef83becd02ff53f6051f0d59c79a59e22747` |
| `build/learning_batch/screenshots/batch-contact-133.png` | — | `aa24a15cf1ee888214f59e935df54d11bb190ca1cf711ac4e6bc2975db6294f7` |
| `build/learning_batch/screenshots/batch-contact-145.png` | — | `de07fdc1a677b176c9fb74801534e112726a56db6aaa53e4d7bb55d48dd8f990` |
| `build/learning_batch/screenshots/batch-contact-157.png` | — | `f91558eeb4b312778d950bd63d1a322b30005b4f4ed81a855bbde83938de3832` |
| `build/learning_batch/screenshots/batch-contact-169.png` | — | `71d995fb42a5fa6264c46506663278ad12a5175eeb3e8d24aecdb455414471fc` |
| `build/learning_batch/screenshots/batch-contact-181.png` | — | `07234d637f5352d95a02305fd1b007e6329bde352873c4d9d46051ea27689288` |
| `build/learning_batch/screenshots/batch-contact-193.png` | — | `6c071b7d72f1f700b24abf8a1b77628d7fdd6c4b281dd4927f702b62e7c0c163` |
| `build/learning_batch/screenshots/batch-contact-205.png` | — | `bc51fdc4b4bb93e5585c692d6fb4a2229541dbf494dfb515bf18a4f90de6c3ad` |
| `build/learning_batch/screenshots/batch-contact-217.png` | — | `17d90f66bbc850b382a154cd7da07d51878aed5644e60cd73d847c01a6a10e52` |
| `build/learning_batch/screenshots/batch-contact-229.png` | — | `ccf4908a6b88e933f852866271aed4b593d616b8becea374c90f10e122043f34` |
| `build/learning_batch/screenshots/batch-contact-241.png` | — | `04289bded7bbd458125b7af412addd1c68b1ab7d8d8a65e078695884e322c4ec` |
| `build/learning_batch/screenshots/batch-contact-253.png` | — | `3f12093953d41c2bab98dabb9b96955d07388b65c5a5236dd35e4a4d5185f734` |
| `build/learning_batch/screenshots/batch-contact-265.png` | — | `283489cf923e786ab692f0efbdf216b69aabb2bdabb30a4680787c4763d12b4f` |
| `build/learning_batch/screenshots/batch-contact-277.png` | — | `30bc4087e322626479c09d7903a4bd295f106505510774fe2aa1a2cf83392349` |
| `build/learning_batch/screenshots/batch-contact-289.png` | — | `d48506f76b02417943225d71a350a229dcb0ee4a73976e9f393560f93f32e2a7` |
| `build/learning_batch/screenshots/batch-contact-301.png` | — | `d16d1f4d7077641103c38970b8cdc35dc9b68a377a73f6c2b4de373945e367d7` |
| `build/learning_batch/screenshots/batch-contact-313.png` | — | `b73a48afdeab9d4de4e834887d430ab7ff073ee292d0a74e7b5d638607c2689b` |
| `build/learning_batch/screenshots/batch-contact-325.png` | — | `578936e349ac3c372af4c5bcb8063b33a973b1affbda61a6ea7a4471aa80d2ec` |
| `build/learning_batch/screenshots/catalog-contact-001.png` | — | `1855dd0fa8213f41a22c7d4963a6eb12d30a6ba5f3c662a14752d1a23697b833` |
| `build/learning_batch/screenshots/ch01-contact-001.png` | — | `7951d2f2fe656285214fcad14c8939f8a79424d08b4a34f5963722a57603547d` |
| `build/learning_batch/screenshots/full-contact-001.png` | — | `07f0de4b05633e7d3516c762fe20c5658f13d0ee0da9aff8847968d8d70bc96e` |
| `build/learning_batch/screenshots/full-contact-013.png` | — | `25b5444c3812b21a8b959e8e1d7824e6a232250e713b5fdfec6b0bc92fb15946` |
| `build/learning_batch/screenshots/full-contact-025.png` | — | `e624c14e96d49af062d867b4b7daa668431a5b010e72eaf18fec40dd5a49f2d0` |
| `build/learning_batch/screenshots/full-contact-037.png` | — | `e70a4b2f1cb9d6989be57803ab59f0af81548fdb526432835c942a91424fe0c6` |
| `build/learning_batch/screenshots/full-contact-049.png` | — | `7eed95d1c22bf3f71027f341651f0233c6ef1d6d8c303446cb8ad2b1fd4d30f0` |
| `build/learning_batch/screenshots/full-contact-061.png` | — | `116cdd98ae89e078acb587f561f046702b44993421ec836eba3ef86db58733a5` |
| `build/learning_batch/screenshots/full-contact-073.png` | — | `d341353de81b5b9f2c1f196c972048ad1907a77245f3374163d741185282f3fd` |
| `build/learning_batch/screenshots/batch-page-003.png` | — | `ba81bf0ae4d2bb11241a19ea86a5d728f5da28884c3935f78287d2d20ae56ffe` |
| `build/learning_batch/screenshots/batch-page-004.png` | — | `8cfa413c340a5c2f8bb681e99ceb4cfbbdb838e9b6b284ab630106229af84eb0` |
| `build/learning_batch/screenshots/batch-page-005.png` | — | `521e64831143c999e8510959760012b13ebc6912c8f3842306b673982fa98e92` |
| `build/learning_batch/screenshots/batch-page-006.png` | — | `d68ffa0f77fe5730afd99662ff04c8ccfb2c6495bbd5055aa4655c791e173eff` |
| `build/learning_batch/screenshots/batch-page-007.png` | — | `71344d7ff88858b79c05bc76ef742cf89d225101a9711d5a178682f4d3f45355` |

只在 `/tmp` 写入报告和证据快照；未改稿件、截图、PDF、QA 或 aggregate 状态。
