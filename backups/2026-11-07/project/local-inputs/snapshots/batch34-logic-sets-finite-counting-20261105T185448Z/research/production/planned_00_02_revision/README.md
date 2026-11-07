# 00-02 后续修订方案存档：未应用

这里保存先前 `/tmp/part1-00-02-independent-review/` 的独立阅读评估、最小重新绑定方案、只读模拟脚本与结果，防止临时工作区恢复时丢失。

**当前正式状态仍为 G 来源已核4项、pending 14项、原创 T/S 独立审阅15项。** 单项映射正例仅说明未来按方案完成绑定后可将 00-02 来源需求核为 verified，不是当前正式来源账、完整第一部分或构建通过。其余13个G缺口不受该提案支持。

当前第32批 B4.5—B4.7 产物保持独立冻结；本目录没有修改第一部分正文、附录、scope、来源账、数学/教学/构建/视觉签署或收据。第32批封存后，才可按主代理授权实施独立修订、差异审查、重新构建与实际看图。

- `assessment_and_rebinding_plan.md`：实际读取范围、充分性结论、精确签署失配和重建顺序。
- `check_gate_impact.py`：只读真实验收器，内存模拟改源或改计划后的旧签失效；不修改仓库源、状态或receipt。
- `gate_checks.json`：当时输入hash与正反例结果，不是完整部分验收收据。
- `proposal_review.json`：对来源代理提案的独立核验及原文件未变记录。
- `preservation_manifest.json`：从临时目录保存的文件hash。

脚本和历史说明中的绝对路径记录当时工作区；迁移后需明确调整工作区根再运行，不能据旧路径的存在与否伪造新验证。历史报告引用的 `/tmp/part1_00-02_minimal_revision_proposal.*` 属来源代理另存的提案，不将其当作已应用变更。

未来 B4.8—B4.9 的注册元数据另保存在 `research/production/next_b48_b49_registration.json`，status 为 `metadata_proposal_only_not_registered`。其中67/68是拟用编号，当前正式台账仍66单元，不授予新稿构建或视觉通过。
