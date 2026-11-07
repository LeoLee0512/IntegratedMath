# 第25批构建与倒数、除法重点公式实际页图复核

执行者 recover_build21；记录UTC时间：2026-10-30T03:01:13.995150+00:00。20张1.7倍页图实际打开在2026-10-30T03:00:23Z前完成。

收到明确READY25并确认ledger已结束后才构建。未改正式稿、工具、来源、图、台账或审阅；未提交，未接受aggregate visual；保留30e21b8与全部第24批快照。

## 实际构建和全页边界

`python tools/build_learning_batch.py --incremental` 实际退出0，日志/tmp/recover25-build.log。随后 `/tmp/recover25_pdf_precheck.py` 实际退出0。四份PDF逐页逐词按与validator相同的8pt纸张边界检查：审阅765页、合订979页、旧章31页、目录218页均零越界。页数与哈希见/tmp/recover25_pdf_precheck.json。

## 实际打开的二十页

本次指定内容跨页较多，为包含DQ2答案的非零和零系数两页，实际覆盖增加到两版各10页。PyMuPDF按1.7倍渲染，view_image逐张实际打开审阅物理413、415、418、419、421、687、689、691、692、695页，及合订物理627、629、632、633、635、901、903、905、906、909页。不是仅生成截图或读取文字层。

- 审阅413/合订627：IR2的ε=a0(1−q)、跨界间距、v>a0>0、u>qv≥0和中点b=(q/u+1/v)/2均清晰完整；正见证u、b及q<ub位于页末仍完整，未与页脚碰撞。
- 审阅415/合订629：逆元唯一性的五行Inv长式、零无逆、双倒数及取反倒数的公式完整；嵌套括号与上下标未裁切。
- 审阅418/合订632：DQ2的解集定义、非零系数候选、乘回与必要性Inv长链完整；零系数的两个分支（全体与空集）文字齐全，没有误漏页边。
- 审阅419/合订633：两次函数复合往返、仿射解集三支大括号的唯一解/全体/空集及各自条件完整可读，三行对应清楚。
- 审阅421/合订635：DQ4两列表有表头及七项性质，每项依据完整；表格未跨页，未发生行列重叠。后面的非空有上界条件、并集集合定义和上确界说明完整。
- 审阅687/合订901：IR答案的严格间距→u>qv正性→中点正见证完整，除以uv后的比较和最终成员关系显示清晰；下部双侧逆元公式可读。
- 审阅689/合订903：IR答案唯一性Inv五行链、零输入限制、IR4相容/双倒数/取反长式完整，无横向裁切。
- 审阅691/合订905及692/906：DQ2答案非零系数的存在性与唯一性计算在前页，零系数两支在后页开头，衔接完整；随后两次函数复合多行计算、恒等映射下标以及满射候选长式清晰。
- 审阅695/合订909：DQ4答案的域与有序域依据逐项文字、完整的上确界集合式，以及上方共同正因子Inv长链和反向比较式均完整。这里答案是文字逐项核对，未虚称答案另有同样两列表。

以上仅为所列20页的排版视觉检查，不替代独立数学审阅或整体人工视觉接受。自动预检生成的末页不计入本报告实际打开覆盖。

## 本次产物绑定

- 审阅PDF：dc7d0bf566d7542d8d9b81547afb862b68dde6cb080a2d2c03bba96cd0c008a9
- 合订PDF：3f720d5fffa96fa1298785c284f492845b5fc51bd2335339b0a3c60e60a939c3
- build manifest：ac957ecb5f379cd780ea0040c4a9369d643d5749dec0be22ea9a042f34c9ce87

四稿、来源及工具哈希见/tmp/recover25_hashes.json。

| 实际打开页图 | SHA256 |
| --- | --- |
| /tmp/recover25_formula_pages/full-627.png | ec2fd606969e2ebf94fce008ef48ded6502b1c95245b2fd14c81a3f32831f68b |
| /tmp/recover25_formula_pages/full-629.png | 42ff42fe9a30e3368872a32d368877d6020f2783e3e0499f140e03f7976ad17f |
| /tmp/recover25_formula_pages/full-632.png | f7a6c0debf11097959bb29d18f638e6813ea6c6190de35c6b82918d228a874e7 |
| /tmp/recover25_formula_pages/full-633.png | 222d597e318b1a1c25a1fa1110b074968ff15ffb2359b360720f5cadcab8dec2 |
| /tmp/recover25_formula_pages/full-635.png | 44c6b048df624b929bc50d7abc85d896a8c92a4cad5984498731c3acac4217e9 |
| /tmp/recover25_formula_pages/full-901.png | 6fa7b1af1b9b09f2fd9dedea6e6010ddeb9b2faa48c410435bbd8b4230ad95ac |
| /tmp/recover25_formula_pages/full-903.png | 05830987647b21cf570f5f81f08f5301941af0458b1b14cef19b1260fe7e1512 |
| /tmp/recover25_formula_pages/full-905.png | 2d4c34d9a89427d534df8bc8281da75dc627ed3a7c4e6c2e878d7d7e830e8a37 |
| /tmp/recover25_formula_pages/full-906.png | e0fb8657d6818e497df53c3e50638a214d89e7c2676b560979d6262cf6019813 |
| /tmp/recover25_formula_pages/full-909.png | 3103c16cbc0326c8953800ea834b0d411557e826077f554e1456506e357bfbde |
| /tmp/recover25_formula_pages/review-413.png | 5b858e504e1a2c076a4b378ab5a087d86eeb8a3a306acec4b93a2d5f730a819f |
| /tmp/recover25_formula_pages/review-415.png | 5735da82f04b80359716e0ac0570f29e3d001f6419301c9b6e7d709265ab5a1b |
| /tmp/recover25_formula_pages/review-418.png | 25996b0cfc08a87a8a32d072d0584a47849c9e8ba5b2d7307fc2c45015522812 |
| /tmp/recover25_formula_pages/review-419.png | 1fdaa572f31a819fa571e0147b365f1622ed68015827b1e3edc1fb403c87fa1e |
| /tmp/recover25_formula_pages/review-421.png | 7b67b157666e663571bcac1b9dbbd133abbfad53e8397818f0d041d1ddc2704f |
| /tmp/recover25_formula_pages/review-687.png | 5e7b13313f55f371fbcf644aa66e057276a7f28dd57a5f571dc8d921cfda8bc6 |
| /tmp/recover25_formula_pages/review-689.png | 3cae2ef1984e90b8b2fde7b19de4b4ece6a245e00ae21e3f6d6a4004c01f9b60 |
| /tmp/recover25_formula_pages/review-691.png | 56e9c59bd5f5aa90e78b41782d33311933cf75a2325fa95ff5e56bd9e0b2bd47 |
| /tmp/recover25_formula_pages/review-692.png | 0c403c06de41a03e10886dfccf29f739ee087c0bcb081e5e26dac9e48011e547 |
| /tmp/recover25_formula_pages/review-695.png | 3170e2f30da72c5cbca2547ef00677d68a37d4d944d3e400a88efc84ce2126b3 |

## 完整自动验收实际结果

在2026-10-30T03:04:56.183698+00:00实际读取完整验收结果。`python tools/validate_learning_batch.py` 退出码0，日志 `/tmp/recover25-qa.log`。正式报告 `data/production/batch_validation.json` 状态为 `automated_checks_passed`，SHA256为 `5a52b3fc53377bcb1a5ee42428f2255f0b93906b8706d4687b1a34fd0e986993`。范围51单元、422对题答、18图；四PDF页数765/979/31/218。完整公式/链接、既有有限计算、18图重生成、源码/产物绑定与全部PDF边界检查通过，零缺字及TeX越界警告，实际生成917张PNG。整体人工视觉仍为 `pending_actual_image_inspection`，未代root接受。

最终自动验收时间：2026-10-30T03:04:40.471787+00:00。原报告SHA-256 `9867df562257bdecf9dbe5f2c623c0c6bb394a676dafd9fdb3c874face65df6f`。
