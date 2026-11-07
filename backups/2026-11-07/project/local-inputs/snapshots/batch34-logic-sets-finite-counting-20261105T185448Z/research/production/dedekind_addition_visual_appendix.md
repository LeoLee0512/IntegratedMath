# 第22批增量构建与附录二十五实际页图复核

执行者：recover_build21；日期：2026-10-30。

本执行者收到root明确READY22后运行构建。保留aac410d及第21批六文件验证快照，未编辑正式稿、绘图代码、来源、审阅结论或台账；未替root接受整批人工视觉验收。

## 实际构建和快速边界结果

`python tools/build_learning_batch.py --incremental` 退出码0，日志 `/tmp/recover22-build.log`。旧独立章/目录快照通过哈希检查后复用，新的审阅本与合订本实际重建。

实际执行 `/tmp/recover22_pdf_precheck.py`，退出码0。逐页逐词检查四PDF距纸张边界8pt的规则，与完整验收保持一致：审阅687页、合订901页、旧章31页、目录218页全部零越界。页数、SHA256和空越界列表见 `/tmp/recover22_pdf_precheck.json`，主要输入产物哈希见 `/tmp/recover22_hashes.json`。

## 实际打开的放大页图

六页分别按1.7倍渲染，并通过view_image逐张实际打开：审阅物理685、686、687页；合订物理899、900、901页。不是只生成文件或读取文字层。

- 审阅685/合订899：附录二十四绘图源码尾部，原有断言、字体设置、保存图文件和入口调用完整，无裁切或行间遮挡。
- 审阅686/合订900：附录二十五标题、对象范围、六个精确样本、间距式、依赖说明和函数前半部均完整。正文明确指定有理下段不构成任意分割算法；数学分数、下标和不等式可读。代码文档字符串也完整显示。末行for循环在下一页进入循环体，衔接正确。
- 审阅687/合订901：函数余部全部可读，中文成员标签、u/v/b0/M标签、字体配置、tight_layout、savefig与plt.close及入口draw_dedekind_grid(out)均显示完整。没有横向裁切、遮挡、缺字或与页脚碰撞；页尾留白正常。

本次视觉范围仅这六页，不宣称实际检查全书其余页面，不替代正文数学审阅或整批视觉签署。

| 实际打开图 | SHA256 |
| --- | --- |
| /tmp/recover22_pages/full-899.png | 82bfe91e3bee046e415cfcb7d59ba2375fed209171570cdcd14893119f8c456f |
| /tmp/recover22_pages/full-900.png | 1e7a77693aec837b3d80dd100bf159218dae8e2345e97c2e8242986f10362ece |
| /tmp/recover22_pages/full-901.png | 5e858fb4edc892aff98b0e76f041448d52573e40957fa9f786e59217a6752d3e |
| /tmp/recover22_pages/review-685.png | f6c9ec403015ee0a9d2b8d2bb4c997bf2637886d19163172c89b886fc694b48a |
| /tmp/recover22_pages/review-686.png | c86a6896546accd8f1b85ada4e40a1d8183cc31bd9285f22d1506cc90e503ff2 |
| /tmp/recover22_pages/review-687.png | 4636360a2602affe6a64f32d1eeb15aca5239f80c1138f1fb3e708cc0ab8c601 |

## 完整自动验收实际结果

实际运行 `python tools/validate_learning_batch.py`，退出码0，日志 `/tmp/recover22-qa.log`。正式报告 `data/production/batch_validation.json` 状态为 `automated_checks_passed`，SHA256为 `b84ad0893d860d45deec39baf7f6394e39bbb1e7f3c62b630e375d626f253db5`。全部已注册文档/公式/链接、有限计算、插图重生成、源码/产物绑定和四PDF检查通过，实际页数687/901/31/218。整体视觉状态仍为 `pending_actual_image_inspection`；此报告只覆盖上列六页，不替root接受整批视觉。

主编整合绑定：当前自动验收时间 2026-10-30T02:12:54.672078+00:00；整合前自动报告SHA与上文一致。六张原始页图已另保存在local-inputs/batch22-appendix-pages，逐文件哈希与原报告一致。
