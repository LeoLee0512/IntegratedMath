# 《综合数学》第一部分审阅入口

著作人：Leo Lee。第一部分“数学总论与综合主题”（00-XX）现为复审修订稿：两章、33节、27道原创课后题及独立解答、4张原创图。T2/S13/G18是教学深度计划，不是完成统计。此前完整验收声明已撤回；专题来源仍有缺口，当前完整部分验收为pending，作者审阅也待进行。

正文入口：

- [部分开篇与直属两节](manuscript/review_ch01/part_opening.md)
- [第1章 绪论](manuscript/review_ch01/chapter.md)与[独立答案](manuscript/review_ch01/answers.md)
- [第2章 会议论文集与文章汇编](manuscript/review_ch02/chapter.md)与[独立答案](manuscript/review_ch02/answers.md)
- [范围计划](research/production/part1_scope_plan.json)、[数学审阅](research/production/part1_revision_independent_review.md)、[教学审阅](research/production/part1_revision_pedagogy_review.md)、[生产验收回执](research/production/part1_acceptance.json)

旧提交de08a8a的构建页数和accepted声明仅保留在 `research/production/history/de08a8a/` 供追溯，不作为当前稿验收。新稿的数学、教学、构建、视觉和专题来源分别核对，本轮实际生成审阅版50页、完整目录正文版267页、单独目录218页，共535页；自动检查已通过27题答案往返链接、387个数学节点、4图和分类归属；535页均已实际进行联系表检查，并放大核对关键页，未见阻断排版问题。21项验收工具回归测试通过。最终状态见当前验收回执；没有来源证据时不得恢复完整完成。

## 从源码构建

需已有Python及requirements-build.txt中的相应库、pandoc、XeLaTeX和Noto CJK/DejaVu字体。以下命令不需要上传的MSC原始PDF；目录使用已核分类缓存。

```bash
python tools/build_full_catalog.py
python tools/draw_ch01_figures.py
python tools/build_part1_review.py
python tools/validate_part1_review.py --package
```

输出在dist/part1/：Markdown、PDF、离线HTML及伴生ZIP；实际页面截图在build/part1/。按照既有source-only约定，本次Git推送包含源码和审校记录，不新增这些可再生文件；此前backups目录与历史保持不变。

验收回执记录的是本次本地实际产物及其哈希。干净源码检出没有PDF、ZIP和截图时，验收工具返回pending是正常的；重建后必须重新查看实际页面并记录新产物身份，不能把旧回执直接当作新构建已验收。

来源边界：外部书评、未解问题清单、数学哲学和数学与文学的真实专题来源仍未取得；普通逻辑知识与分类代码不能替代。18个G节中4个有相应专题来源支持，14个仍待补；15个T/S原创内容另行数学和教学审阅。各来源的实际支持范围逐项列在part1_topic_sources.json。第2章A—E仍明确虚构，新增题2-7实际核对公开历史Crossref字段文档，既不虚构论文也不冒充核验数学证明。原始附件与外部教材全文不分发。

恢复边界：919页基础续写版的a9363f6快照已逐文件核验保留。此前第31批数列草稿仍独立保留，939页综合版未因本次第一部分验收而自动升级；本轮仅处理第一部分复审修订，不继续其他部分；未解决的来源缺口按实报告。
