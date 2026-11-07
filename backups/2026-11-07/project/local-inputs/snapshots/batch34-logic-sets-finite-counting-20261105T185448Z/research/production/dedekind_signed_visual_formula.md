# 第24批构建与重点公式、标签表实际页图复核

执行者 recover_build21；记录时间UTC：2026-10-30T02:41:58.183430+00:00。本次14页实际放大打开在2026-10-30T02:41:08Z前完成；这是工具返回当前UTC时间，不沿用前批时间。

收到明确READY24后确认ledger进程已结束再构建。未编辑稿件、来源、工具、图、审阅或台账；未提交，未接受整体visual。08f9485及六文件快照保留。

## 实际构建和全页边界

`python tools/build_learning_batch.py --incremental` 实际退出0，日志/tmp/recover24-build.log。随后 `/tmp/recover24_pdf_precheck.py` 实际退出0。按与validator相同的距纸张8pt规则逐页逐词检查四PDF：审阅741页、合订955页、旧章31页、目录218页均零越界。详情见/tmp/recover24_pdf_precheck.json。

## 实际1.7倍打开的十四页

使用PyMuPDF按1.7倍渲染，随后view_image逐张打开：审阅物理398、401、405、406、664、667、668页；合订物理612、615、619、620、878、881、882页。不是仅生成截图或只读文字层。

- 审阅398/合订612：SP1四支乘法定义在同页完整显示；左侧大括号、四个输出和各支两条符号条件完整、对应清晰，无缺行、裁切或重叠。后面的两层有理子集展开及SP2三行公式也完整。
- 审阅401/合订615：正文七列八行二值标签表完整显示在单页，七个表头包括两种括号的末两列均可读；000至111共八行均出现，行列对齐，边框没有穿过文字。上方两种括号公式的下标和嵌套P表达式清晰。
- 审阅664/合订878：题6答案中的七列八行表同样完整、未跨页；末两列和所有八行齐全，列间没有挤压或遮挡。表后第六行示例、标签结合式和幅度结合式均可读。
- 审阅405/合订619：SR异号情形一的D定义、加法移项四行长式完整；情形二的E定义和X⊕N(Y)=N(E)四行计算也完整，页底与页脚分离。
- 审阅406/合订620：异号情形二的P(X,C)⊕N(P(Y,C))嵌套取反长式按多行完整排版；左侧乘积链、交换加项的三行式，以及SR2两侧分配/差式均清晰，最右括号没有裁切。
- 审阅667/合订881：答案题2同加相反数的四行推导、D非负时的乘积链完整；上方同号分配七行推导也可读，未出现行距碰撞。
- 审阅668/合订882：答案题3的X⊕E、X⊕N(Y)、五行嵌套取反推导及最后左侧乘积链均完整。C=0边界说明和页底正文没有与页脚重叠。

这里仅作已列页面的排版视觉检查，不替代独立数学审阅或全书视觉验收。20张候选页图中仅上述14张实际打开；其余候选页、quickbounds自动生成的末页不计入本报告人工覆盖。

## 本次PDF绑定

- 审阅PDF：ac910d846416a7901e20563b7fd9cee75892b36fbb4083e0cc850debfd79a863
- 合订PDF：d9d50ff6bb85636aa7ee7af3cb6feeca7e80349339f68293fc7ed5d4dd03ca23
- 构建manifest：8adb54917850d52b76de0395819b75197579408784d4c886b47cf5c98e40c968

四稿、来源与工具哈希另见/tmp/recover24_hashes.json。

| 实际打开页图 | SHA256 |
| --- | --- |
| /tmp/recover24_formula_pages/review-398.png | 67a215787f075c939a4702d632ba301b027d7562ee0373d17dafadec8619b6e2 |
| /tmp/recover24_formula_pages/review-401.png | 391e1537d3209d6e0ac423396fc5e7e1167859a34a24632d015b9994a1dd6607 |
| /tmp/recover24_formula_pages/review-405.png | 346d5da0779674fffd95d7ca3fd1952473f6d06af182e33710f90fff743e660a |
| /tmp/recover24_formula_pages/review-406.png | 567b069c8fdd6242443236efcd8616a958d8144286a2483647b8d3ecc4f5c771 |
| /tmp/recover24_formula_pages/review-664.png | 184b108c1ce41ea674b7536cc557d7c74c2db9681bb7c35a45a0cd00d666bf0b |
| /tmp/recover24_formula_pages/review-667.png | 0d50adb529f32f9366f677d49c732ec686358e88aa3616ba2141b81b5bf553b1 |
| /tmp/recover24_formula_pages/review-668.png | dc0d62a2f2f0643ca144c07d564f9d44b61385660dfc25bda8b23931061a4440 |
| /tmp/recover24_formula_pages/full-612.png | 416facc129343d0c549b6a2eac38e61179f5ac658675e8ca54bb5af4f25540fc |
| /tmp/recover24_formula_pages/full-615.png | ed0c161e6384c6692f0ddf47f260c9b6039d25a99a92095b40393e66e6f52ab8 |
| /tmp/recover24_formula_pages/full-619.png | 5b7facec13ac60ea787a1ec536d476efea639556ae503ab598f229d0346438fe |
| /tmp/recover24_formula_pages/full-620.png | 3b7aa7f93a2b6d0113fe49d426a6f64f43765a9a0534a5559facd4209ed19af9 |
| /tmp/recover24_formula_pages/full-878.png | e4413e857f537042f44bf58096ae0ad0cff51fd439832055632fdc13c36b009c |
| /tmp/recover24_formula_pages/full-881.png | fe04bdcba8bd5ef1a735766fc265509229bbc8c3367202e5edfd074db064f0ad |
| /tmp/recover24_formula_pages/full-882.png | 79e457569cf66ebdd08f6abdb56080acda945423bebddb9d7b12dd0528220560 |

## 完整自动验收实际结果

在2026-10-30T02:45:24.854149+00:00实际读取完整验收结果。`python tools/validate_learning_batch.py` 退出码0，日志 `/tmp/recover24-qa.log`。正式报告 `data/production/batch_validation.json` 状态为 `automated_checks_passed`，SHA256为 `b3eb3e352968fe7d01569166b28bd4e451268f119f7fceec264cefec4cbc4585`。范围49单元、406对题答、18图；四PDF页数741/955/31/218。全量公式/链接、既有有限计算、18图重生成、源码/产物绑定、四PDF边界检查通过，零缺字及TeX越界警告。整体人工视觉仍为 `pending_actual_image_inspection`，本执行者没有接受aggregate visual。

## 主编绑定及留存

原报告SHA-256 `e7246b4d9e9bf9edc5004992edcd227a3280c41ea5b03b6d340728a672358070`；当前自动验收时间 2026-10-30T02:45:10.461540+00:00。上述两PDF哈希与报告后记录一致；14张实际打开图片及候选图片原样留存于local-inputs/batch24-formula-pages，未打开候选页不计为检查。
- `dist/综合数学_基础续写审阅版.pdf` SHA-256 `ac910d846416a7901e20563b7fd9cee75892b36fbb4083e0cc850debfd79a863`
- `dist/综合数学.pdf` SHA-256 `d9d50ff6bb85636aa7ee7af3cb6feeca7e80349339f68293fc7ed5d4dd03ca23`
