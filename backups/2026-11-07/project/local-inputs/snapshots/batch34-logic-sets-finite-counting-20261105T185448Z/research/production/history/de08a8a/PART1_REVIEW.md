# 《综合数学》第一部分审阅入口

著作人：Leo Lee。第一部分“数学总论与综合主题”（00-XX）现已按声明深度完成生产验收：两章、33节、20道原创课后题及独立解答、4张原创图。深度为T2（完整教学）、S13（专题）、G18（导读）；不表示穷尽对应领域。作者审阅尚待进行。全书其余部分仍在编写。

正文入口：

- [部分开篇与直属两节](manuscript/review_ch01/part_opening.md)
- [第1章 绪论](manuscript/review_ch01/chapter.md)与[独立答案](manuscript/review_ch01/answers.md)
- [第2章 会议论文集与文章汇编](manuscript/review_ch02/chapter.md)与[独立答案](manuscript/review_ch02/answers.md)
- [范围计划](research/production/part1_scope_plan.json)、[数学审阅](research/production/part1_math_review.md)、[教学审阅](research/production/part1_pedagogy_review.md)、[生产验收回执](research/production/part1_acceptance.json)

本地实际构建：第一部分审阅PDF40页；含全书中文分类目录的PDF257页；独立目录PDF218页。全部515页实际按联系表查看，并对公式、图表、代码及长目录条目放大复核。20题题答链接、229个数学节点、4图、33节归属和离线HTML检查通过。少量正常跨页文字/答案链接不影响定位；不声称逐字校对每张放大页或形式化证明认证。

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

来源边界：仅使用已说明的公开资料和原创示例；部分拓展网站受当前网络策略限制，未冒充已访问。第2章A—E资料明确虚构用于训练，不是伪造的真实学术引用。原始附件与外部教材全文不分发。

恢复边界：919页基础续写版的a9363f6快照已逐文件核验保留。此前第31批数列草稿仍独立保留，939页综合版未因本次第一部分验收而自动升级；本轮停止点为第一部分完成，不继续新增其他部分正文。
