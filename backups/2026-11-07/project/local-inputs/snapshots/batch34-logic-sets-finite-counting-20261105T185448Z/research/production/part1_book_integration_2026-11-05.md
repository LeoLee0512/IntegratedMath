# 第一部分修订回接全书：清单、边界与检查

本次由 `/root/part1_audit` 执行。来源提交 `ee27ceae26d810d3b37cf2c2db4079bab83ee569`，全书起点 `0056e85176168e912af14d778fb81681974a283a`。没有 merge、rebase、push，也没有删除历史文件。

## 同步结果

- 已核实 `local-inputs/resume-0056e85-before-integration/manifest.json` 全部六项备份哈希，且 0056e85 Git 对象可读。
- 精确同步第一部分六份变更稿：`review_ch01/{part_opening,chapter,answers,appendices}.md` 与 `review_ch02/{chapter,answers}.md`；复制 `data/editorial_plan.json`、`PART1_REVIEW.md`、已跟踪的第一部分专属范围/数学/教学/来源/构建/视觉报告、验收器及21项测试、de08a8a历史记录。
- 字节复制 `dist/part1/` 与 `build/part1/` 的独立第一部分产物和图像证据；不借全书PDF替换这些签署产物。文件允许列表共685项，189项发生字节变更或新建；全部源与目标SHA-256见同名整合manifest。未删目标旧文件。
- 覆盖前不同的旧文件126项保存历史：源稿和报告在 `research/production/history/0056e85-preintegration/`，本地旧第一部分产物在 `local-inputs/resume-0056e85-before-integration/part1-prior-artifacts/`。原备份manifest未改。旧accepted声明保留为历史、当前撤回，不改旧签署。
- 全书 `EDITORIAL_POLICY.md` 与 `LEARNING_PATH.md` 保留原内容，仅附加本轮整合记录；不能整文件复制publish裁剪版，否则会丢失全书生产授权和63个桥接单元路线。
- `tools/part1_ledger.py` 显式接入来源审阅；保存来源、构建、视觉独立门槛及逐节来源状态，数学/教学/构建的真实通过与完整范围完成分开。来源不足时2章33节coverage均false、第一部分partial_draft/完整验收pending，作者审阅pending；其他部分不改。

## 验证

21项验收器测试全部通过。另以内存副本调用真实 `refresh_part1`、`finish_part1_record`：35个第一部分记录完成注册，数学、教学、构建、视觉均true，唯一失败门槛是14个G专题来源；其他532章、5973节和62部分逐字序列化比较不变。未写生产台账或验收收据。

来源待核验节：00-02、00A17、00A27、00A30、00A64、00B05、00B15、00B20、00B25、00B30、00B50、00B55、00B60、00B99。原创T/S独立审读不冒充外部来源verified；G仍要求topic_specific入口。

`accepted_reviews.json` 126条（63单元各数学/教学两条）及对应源稿、证据散列在同步前核验全部有效，本代理未改该文件。B4.3、B4.4四份正文/答案也保持0056e85字节，每单元8题与8解；旧台账数学/教学passed，构建pending、coverage false。其SHA-256另列manifest。

## 全书构建由主代理处理

`tools/build_learning_batch.py`、`tools/validate_learning_batch.py` 不由本代理修改。全书若收入当前完整第一部分，应组装第2章正文与7题答案、纳入源文件哈希及链接转换，更新章序/33节检查与题答计数：504基础题+20绪论题+7第二章题=531。仅替换第一章则为524题，仍是没有第二章的局部学习版，不能声称已纳入完整第一部分。

旧 `dist/综合数学_基础续写审阅版.pdf` 为939页，SHA-256 `5632e674850480b83bee6cb984b161859382148441782be6cdce7aca78330779`；旧主PDF为1153页，SHA-256 `1db9e6aafdff60581290397051a4a0bd68fd4e408c16dd04e22de876cbc6d810`。它们与2026-10-30既有构建manifest的产物哈希一致；但同步前当前book已有4个第一章源文件不匹配该manifest，不能代表当前输入。旧批次视觉状态为pending_actual_image_inspection；B4.3—B4.4仍待新产物核验。

旧 `--incremental` 路线会因第一章输入改变而拒绝复用，不能改旧快照哈希强行通过。应保留原legacy snapshot，再对变更后输入完整构建并实际查看新页。新的全书构建不会自动升第一部分来源门槛，也不会自动把单元审读提升为整章或整部分完成。
