# 综合数学

著作人：Leo Lee。当前工作方式为按 MSC 目录逐章编写、逐章由作者审阅。

当前稿仅包含第一部分开篇与第1章“绪论：一般与综合专题”（00Axx）。直属部分的第1、2节保留原归属；第1章展开第3—23节。全书范围仍为63部分、534章、6006节，各级目录标题已译为中文；目录列齐不代表正文已经全部写成。

## 阅读

- [第一章审阅版 PDF](dist/综合数学_第一章审阅版.pdf)
- [第一章审阅版 Markdown](dist/综合数学_第一章审阅版.md)
- [含完整目录的当前全稿 PDF](dist/综合数学.pdf)
- [完整目录 PDF](dist/综合数学_完整数学目录.pdf)
- [当前伴生文件包](dist/综合数学_第一章_伴生文件.zip)

题目与答案分开，例题保留示范推导。正文有四张代码绘制插图，图源说明集中于附录。沿用用户示例中的“操作说明、公式、方括号依据”写法；原始参考DOCX不公开分发。第二章尚未开始。

## 构建与检查

安装 requirements-build.txt 中的Python依赖。系统需有 pandoc、XeLaTeX、poppler-utils，以及 Noto CJK、DejaVu 字体和 fvextra、newunicodechar 等TeX包。

```sh
python tools/build_ch01_review.py
python tools/validate_catalog_chinese.py
python tools/validate_ch01_review.py
python tools/package_ch01_review.py
```

先检查生成的PDF截图，再在 data/ch01_validation.json 记录实际视觉检查。自动生成截图不等于已看过截图。打包前须完成此项。

没有上传的原始MSC PDF时，目录生成器使用 data/catalog_titles.json 中带完整性校验的标题缓存。缓存仅含分类名及定位信息，不包含原始PDF或全文。中文标题使用 data/catalog_titles_zh.json，其中保留逐项英文对照、代码与归属。实际数学证明仍以正文条件、推导及独立审校为依据；程序检查不是全书形式化验证。

## 版本记录

此前35章历史主线工作稿保留于 Git 提交 `818bc3c77023b76dac56fb3b4a3ca3b6eee0ce39`，不混入当前逐章审阅正文。旧版 tools/build_book.sh 与旧稿数据不是本版构建入口。来源许可、独立审校与写法分析位于当前伴生包的 research 目录。
