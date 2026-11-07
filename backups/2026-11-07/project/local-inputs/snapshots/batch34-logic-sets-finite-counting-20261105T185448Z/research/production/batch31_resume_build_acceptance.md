# 第31批恢复：构建与限定范围验收报告

正式执行 `python tools/build_learning_batch.py` 与 `python tools/validate_learning_batch.py`，均退出0。当前245项构建输入、51项输出哈希逐项匹配；531组题答与实际PDF双向跳转、公式MathML、21张内嵌图、内部链接、图片重生成一致性、页边界、缺字及TeX溢出检查通过。

PDF实页数：基础审阅959、全目录主书1173、第一章41、完整分类目录218。三份真实视觉报告合并后，基础审阅959页全部通过contact逐页检查；主书仅99个抽检页、第一章与目录各4个抽检页。不得将后三者写为全页人工通过，也不把contact检查夸大为逐字放大审校。非阻塞观察包括章节收尾留白、较密导语，以及基础审阅908页单行代码续页。

视觉聚合已写入 `data/production/batch_validation.json`；原自动收据原样保存为 `build/learning_batch/automated_validation_before_visual.json`，使独立报告所引用的旧收据哈希仍可核验。伴随JSON绑定当前四PDF、清单、聚合收据、三段报告和真实页码。

本轮构建范围为63个基础单元，加第一章20题及第二章7题，共531题；完整分类保持63部分、534章、6006节。第一部分14个G节的专题来源仍pending；通过构建和视觉门不等于来源完整或整书完成。

包中另有三份未注册单元及其答案，仅作为草稿源文件收录；见 `batch31_resume_package_drafts.md/json` 的六文件明确清单。它们不计入63单元，不进入本轮PDF，不因出现在ZIP中而视为已验收。

此报告在ZIP生成前冻结。ZIP内容与散列另由既有打包器逐文件复核，最终结果保存 `data/production/package_validation.json`，版本副本及精确清单保存在本地snapshot；这样不在包内制造自引用哈希。没有提交、推送或网络发布。

最终生产账已重建：63单元的 `stages.build-verified` 全部passed，正文覆盖总阶段按既有政策仍为draft，不能混作整章完成。第一部分仍partial_draft、完整范围验收pending；来源计数4个G已核实、14个G待核实、15个T/S原创另审。B4.5—B4.7未登记进这63单元。五份最终账的哈希见伴随JSON，随最终ZIP及snapshot保存。
