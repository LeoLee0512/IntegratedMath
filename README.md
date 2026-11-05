# 综合数学

著作人：Leo Lee。全书保留63部分、534章、6006节的 MSC 分类范围与中文标题，按先修依赖安排学习路径，按节的教学目标确定深度。目录列齐不代表教材已写完。

当前第一部分正文已有两章、33节和27道课后题及独立答案，保留4张原创图；深度计划为T2/S13/G18。复审已撤回此前完整验收声明：外部书评、未解问题清单、数学哲学、数学与文学等专题来源仍需补核。正文写成、数学/教学检查、来源和构建状态分别记录，不能把某一项通过当成全部分完成。

## 阅读入口

- [第一部分开篇](manuscript/review_ch01/part_opening.md)、[第1章源稿](manuscript/review_ch01/chapter.md)、[答案](manuscript/review_ch01/answers.md)、[附录](manuscript/review_ch01/appendices.md)
- [第2章源稿](manuscript/review_ch02/chapter.md)、[第2章独立答案](manuscript/review_ch02/answers.md)
- [编辑约定：先修、引用、深度与篇幅](EDITORIAL_POLICY.md)
- [基础干线与深造支线](LEARNING_PATH.md)、[逐节范围和进度](data/editorial_plan.json)
- [GitHub Releases 下载入口](https://github.com/LeoLee0512/IntegratedMath/releases)：本轮完成源文件迁移与发布工具，尚未上传新发布资产；现阶段可阅读源稿或按下述命令本地构建。

PDF、合成Markdown、离线HTML与伴生zip生成在 `dist/`，不再提交 Git。历史版下载仍可从[迁移前快照](https://github.com/LeoLee0512/IntegratedMath/tree/d5a181d81e73c2b7702ad1a49820d840a44a5af5/dist)取得。原始参考DOCX、MSC PDF及全文抽取不分发。

## 构建与检查

安装 `requirements-build.txt` 中的 Python 依赖。系统需有 pandoc、XeLaTeX、poppler-utils，以及 Noto CJK、DejaVu 字体和 fvextra、newunicodechar 等TeX包。

```sh
python -m pip install -r requirements-build.txt
python tools/build_full_catalog.py
python tools/draw_ch01_figures.py
python tools/build_part1_review.py
python tools/validate_part1_review.py --package
```

干净检出无需预先存在 `dist/`、`build/` 或图片；样式源位于 `tools/style.css`，图片由代码重建。没有原始MSC PDF时，目录生成器使用经完整性校验的 `data/catalog_titles.json`；英文对照、中文标题与归属保存在 `data/catalog_titles_zh.json`。

第一部分输出在 `dist/part1/`，全页截图在 `build/part1/`。打包成功只代表自动检查；还须实际查看页面并按新的来源门槛复核 `tools/validate_part1_acceptance.py`。缺来源时完整部分状态应为pending，不能为使程序变绿而跳过门槛。CI仅生成待视觉和来源复核的构建产物，不执行Release发布。

## 版本历史

此前35章历史稿保留在 [history/35-chapter-draft](https://github.com/LeoLee0512/IntegratedMath/tree/history/35-chapter-draft)，对应提交 `818bc3c77023b76dac56fb3b4a3ca3b6eee0ce39`；迁移前的第一章版本保留在 [history/ch01-before-editorial-policy](https://github.com/LeoLee0512/IntegratedMath/tree/history/ch01-before-editorial-policy)。历史稿不混入当前构建。

迁移前当前分支实际有5条提交；本轮新增提交，不压缩、不重写旧历史。解除二进制追踪只阻止后续增长，不会让旧 Git 对象消失。发布标签、历史分支与审校快照的维护规则见 [发布流程](RELEASING.md)。


## 第一部分新审阅入口

[第一部分正文、独立答案与本地构建说明](PART1_REVIEW.md)。第一部分为已补强正文的修订审阅稿，完整验收因专题来源缺口保持pending；作者审阅仍待进行。全书其余部分未完成，旧备份保持不变。
