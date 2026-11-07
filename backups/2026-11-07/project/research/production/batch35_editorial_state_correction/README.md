# 编辑计划当前状态修正候选（当前8/10，未应用）

本目录仅准备 `data/editorial_plan.json` 的修正候选，不修改正式 repo，不引入未来 00B15 的 9/9 方案。

- `editorial_plan.json`：拟替换内容。
- `base_editorial_plan.json`：原文件逐字快照。
- `editorial_plan.diff`：完整差异。
- `checks.json`：精确 base/new/diff hash、正式 scope/source/review 绑定及 327 输入排除证据。
- `prepare.py`：只写本 /tmp 目录的准备程序；读取当前正式状态生成，不做正式应用。

逐33节检查了代码、深度、原目标和源锚，均与正式 scope 对应；来源状态逐项与 scope 和 source ledger 一致。仅 00-02、00A30、00A64、00B05 的旧 pending 改为当前 verified；00B15 仍 pending。合计8已核G、10待核G、15原创T/S；27题、全部作者pending、完整部分pending及0完成不变。

旧 completion_note/current_part（包括4/14、旧页数和旧绑定）完整保存到 editorial_state_history，并明确不适用于当前稿；原更早 de08a8a 历史记录不变。当前 math/pedagogy 报告精确匹配正式计划和八源，因此保留已审阶段；独立Part1 build/visual 报告仍绑定较早计划和源稿，标 pending_current_revision，不把现有基础续写批次验收代替独立Part1。未重新认证旧产物或审核全部外部证据。

5973只是6006减去本文件33节的“本文件未列出”数量，不再称全书未规划/未写。全书当前规划/覆盖权威明确指根目录 data/production 的 parts/chapters/sections/units；仅核parts当前completed_parts为0，不在此复制或冻结全书单位数量。

本轮实际调用当前 builder 的只读 source_hashes 函数：共327项，与 build/learning_batch/build_inputs.json 完全一致，不含 data/editorial_plan.json；没有执行 builder.main、validator 或构建。该 JSON 会被 package_learning_batch 的既有显式名单装入 ZIP，因此 root 若在封包前应用此单文件修正，不会因它改变327项渲染输入；但仍需按最终文件生成/核查包内清单。若包已生成，则不能只改文件而沿用旧包哈希，需重包。

应用前先核 checks.json 中 base hash、正式 scope/ledger及四审签 hash仍一致，再由root审diff并决定复制候选到正式；本代理没有应用。若根改变了任何对应状态，必须先刷新候选，不能盲用旧current绑定。正式源账、scope、正文、工具、35/36候选均未改。
