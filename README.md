# 综合数学

著作人：Leo Lee。全书保留63部分、534章、6006节的 MSC 分类范围与中文标题，按先修依赖安排学习路径，按节的教学目标确定深度。目录列齐不代表教材已写完。

当前第一部分开篇和第1章“绪论：一般与综合专题”草稿：2节直属部分、21节属于第1章，14道题与答案双向链接，4张代码绘制插图。按当前目标分为2节完整教学、13节专题展开、8节导读定位，均待作者审阅；第2章新增第24节“讲座摘要汇编”G级导读草稿，待作者审阅，其余9节未写；全书共24节已有草稿（T 2、S 13、G 9），其余5982节尚未逐项规划。

## 阅读入口

- [第一部分开篇](manuscript/review_ch01/part_opening.md)、[第1章源稿](manuscript/review_ch01/chapter.md)、[答案](manuscript/review_ch01/answers.md)、[附录](manuscript/review_ch01/appendices.md)
- [第2章单节导读草稿](manuscript/review_ch02/chapter.md)：三项先修声明及一次文献定位示范，独立预览，不混入第一章发布包。
- [编辑约定：先修、引用、深度与篇幅](EDITORIAL_POLICY.md)
- [基础干线与深造支线](LEARNING_PATH.md)、[逐节范围和进度](data/editorial_plan.json)
- [GitHub Releases 下载入口](https://github.com/LeoLee0512/IntegratedMath/releases)：本轮完成源文件迁移与发布工具，尚未上传新发布资产；现阶段可阅读源稿或按下述命令本地构建。

PDF、合成Markdown、离线HTML与伴生zip生成在 `dist/`，不再提交 Git。历史版下载仍可从[迁移前快照](https://github.com/LeoLee0512/IntegratedMath/tree/d5a181d81e73c2b7702ad1a49820d840a44a5af5/dist)取得。原始参考DOCX、MSC PDF及全文抽取不分发。

## 构建与检查

安装 `requirements-build.txt` 中的 Python 依赖。系统需有 pandoc、XeLaTeX、poppler-utils，以及 Noto CJK、DejaVu 字体和 fvextra、newunicodechar 等TeX包。

```sh
python -m pip install -r requirements-build.txt
python tools/build_ch01_review.py
python tools/validate_catalog_chinese.py
python tools/validate_ch01_review.py
python -m unittest discover -s tests -v
python tools/build_ch02_preview.py
```

第2章预览命令独立生成 `dist/综合数学_第二章单节导读.{md,pdf,html}` 与伴生zip，附三项先修原文摘录，离线阅读时可直接跳转；检查报告和全部页面截图位于 `build/review_ch02/`。它不进入第一章 Release 上传列表，也不表示整章完成。

干净检出无需预先存在 `dist/`、`build/` 或图片；样式源位于 `tools/style.css`，图片由代码重建。没有原始MSC PDF时，目录生成器使用经完整性校验的 `data/catalog_titles.json`；英文对照、中文标题与归属保存在 `data/catalog_titles_zh.json`。

检查生成PDF的截图，按 [发布流程](RELEASING.md)记录实际视觉检查，再运行 `python tools/package_ch01_review.py`。打包器拒绝未检查、已变更或与构建源稿不对应的产物。自动生成截图不等于人工看过，程序通过也不是全书形式化验证。CI 仅生成待视觉检查的构建产物。

## 版本历史

此前35章历史稿保留在 [history/35-chapter-draft](https://github.com/LeoLee0512/IntegratedMath/tree/history/35-chapter-draft)，对应提交 `818bc3c77023b76dac56fb3b4a3ca3b6eee0ce39`；迁移前的第一章版本保留在 [history/ch01-before-editorial-policy](https://github.com/LeoLee0512/IntegratedMath/tree/history/ch01-before-editorial-policy)。历史稿不混入当前构建。

迁移前当前分支实际有5条提交；本轮新增提交，不压缩、不重写旧历史。解除二进制追踪只阻止后续增长，不会让旧 Git 对象消失。发布标签、历史分支与审校快照的维护规则见 [发布流程](RELEASING.md)。
