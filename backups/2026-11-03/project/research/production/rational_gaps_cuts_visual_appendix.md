# 第21批绘图代码附录修复与实际页图复核

执行者：recover_build21；日期：2026-10-30。

## 实际故障与修复

已读取 /tmp/integratedmath-gaps-cuts-qa.log。首次完整自动验收实际停在审阅PDF物理第660页，两行绘图代码超出页面边界。接手时前四处换行已经写入，绘图模块SHA256为8846e1d520f297b500809645dded848ac285f6e46327b058889c11e5b5947590；本次继续拆分三个长语句。无正文、答案或台账编辑。

完整Python模块AST在本次修复前后完全相等（忽略源码位置属性）；当前draw_rational_gap函数AST也与原/tmp/rational_gap_figure.py同名函数完全相等。实际运行当前函数，PNG与正式dist图逐字节相同，SHA256为d86ad3a6737614ac2ee439abf34c61913bb224220e4e48728783947002762667。更新来源记录中的绘图脚本哈希；教学报告末尾仅加入执行者绑定说明，明确不是原独立审阅者的新增教学审阅。accepted_reviews只重绑相关两条教学证据哈希，不改原审阅日期、审阅者、结论或范围。

## 构建及快速页面边界检查

实际执行python tools/build_learning_batch.py --incremental，退出码0，日志/tmp/recover21-build.log。只复用哈希验证的独立旧章/目录快照，新合订本与新审阅本重建。

实际扫描四份PDF的每页每词边界，条件与完整验收一致（距纸张边界8pt）：审阅660页、合订874页、旧章31页、目录218页均无越界。具体哈希和空溢出列表见/tmp/recover21_pdf_precheck.json。此项不代替完整自动验收。

## 实际放大打开的页面

将以下六页渲染为1.7倍页面图，并逐张通过view_image实际打开：审阅物理658、659、660页及合订物理872、873、874页。不是仅生成文件或仅读文字层。

- 审阅658/合订872：上一附录二次求解代码收尾；函数分支、返回值和页脚清晰，没有裁切或重叠。下半页留白来自下一附录另起页，不是缺字。
- 审阅659/合订873：附录二十四标题、三个公式、有限实例与一般证明的区别、输入依赖说明和函数开头均可读。公式分母/上下标、中文段落、链接和代码没有遮挡。代码在row.append后分页，下一页从chains.append继续，内容连续。
- 审阅660/合订874：完整函数余部、字体设置、保存图文件及调用入口完整可读。原越界ax.text及savefig语句均换行后完整显示，右侧留有页面余量；没有横向截断、行间重叠、缺字或页脚碰撞。

本次视觉范围仅上述六页；没有宣称看过全书其他页或完成全批视觉验收。原数学、教学结论没有由此重新审阅。

| 实际打开图 | SHA256 |
| --- | --- |
| /tmp/recover21_pages/full-872.png | 68409d4f1055ab0ce3a43acb0c8ae8ca0b31d1e4e698b812d19dd0d6a58dbf88 |
| /tmp/recover21_pages/full-873.png | b2714c9cbf9bb5c8cecad13a079fed3d38d8af65d26434e664dbc8f60f0a234a |
| /tmp/recover21_pages/full-874.png | 1eb36a2068cde4fd61fa51b007a8d8d8a26ab377d121e70eb60a2612aae46b1a |
| /tmp/recover21_pages/review-658.png | 311be4e5ddb730bb799dc92b5cad84447d024508cdb2b9344ab09ff9199f4d3e |
| /tmp/recover21_pages/review-659.png | 697362dc736d500a4c0eeaf04686af6ce643a0885310a96b81f33fb9ca619ae2 |
| /tmp/recover21_pages/review-660.png | cd1d622ebab3aa332020b87802d8c52bbc2835d273fca3b5e3a0d3c18a57e949 |

## 完整自动验收实际结果

实际运行 `python tools/validate_learning_batch.py`，退出码0，日志 `/tmp/recover21-qa.log`。正式报告 `data/production/batch_validation.json` 状态为 `automated_checks_passed`，SHA256为 `ace18d636f4812de1f271ffe8b9f8c3855fb33dba3b1138c03dbdb63a90b3af7`。实际覆盖公式、链接、有限计算、插图重生成、构建源/产物绑定与四PDF检查；自动报告仍将总体人工视觉状态保持为 `pending_actual_image_inspection`。本执行者只完成上述六页视觉检查，总体视觉签署留给root。


当前自动验收时间：2026-10-30T01:51:08.575929+00:00。本报告/tmp实际截图副本保存在local-inputs/recovery-2026-10-30/appendix-pages中，原字节及散列不变。
