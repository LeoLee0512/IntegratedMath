# 第23批构建与新增长公式实际页图复核

执行者 recover_build21；日期2026-10-30。

收到root明确READY23后才开始构建。未编辑正式稿、来源、工具、图、审阅或台账；保留e205052及六文件验证快照。下一批B2.27/B2.28不在本批范围，不接受整体人工视觉状态。

## 实际构建与全页边界

`python tools/build_learning_batch.py --incremental` 退出码0，日志/tmp/recover23-build.log。两份新PDF实际重建；旧独立章/目录只在哈希验证后复用。

`python /tmp/recover23_pdf_precheck.py` 退出码0。实际逐页逐词检查四PDF的8pt纸张边界，与正式validator相同：审阅712页、合订926页、旧章31页、目录218页全部零越界。详情及PDF哈希在/tmp/recover23_pdf_precheck.json。

## 实际1.7倍打开的十四页

以PyMuPDF渲染后，分别通过view_image逐张实际打开审阅物理385、386、391、393、394、395、396页及合订物理599、600、605、607、608、609、610页。不是仅生成页图或只查看文字层。以下结论是排版视觉检查，不是替代作者和独立数学审阅者的证明审查。

- 审阅385/合订599：B2.25候选乘积P(A,B)集合定义按三行完整呈现，左花括号、存在量词、正内点条件、q<ab及闭花括号齐全；非负乘法函数域、零积和正性公式完整。上下行无重叠，页末非空说明与页码分离。
- 审阅386/合订600：正外点R/S、两次正因子比较、无最大元的中点分式及乘零集合式完整；分数横线、分母和上下标均清晰。
- 审阅391/合订605：B2.26对象记号中的单行集合定义较长，但左右端完整并有边距；R+、NL1三个条件和有理平移式清晰，未裁切。
- 审阅393/合订607：结合式中点、NL3两侧分配律、负成员q/2+q/2以及正向包含不等式完整。页末引出h,x,y，下一页继续给定义，逻辑衔接可辨。
- 审阅394/合订608：h=(ab+ac-q)/2的分式、精确和三行等式、两组正见证及统一第一因子的不等式完整。下方另一侧分配引语在下一页接三行计算，未发生截字。
- 审阅395/合订609：另一侧分配三行推导、NL4两条双向比较式、差D定义、A⊕D=B展开及P(B,C)=P(A⊕D,C)=P(A,C)⊕P(D,C)长式均完整，没有超出页宽或互相遮挡。
- 审阅396/合订610：不严格反射的跨页比较式完整，随后严格反射、消去、零因子反例与习题区域均可读，未与页脚碰撞。

本报告只覆盖上述十四页；其他页面的整体人工视觉接受由root另行完成。/tmp/recover23_pages还含快速检查自动渲染的末页，未在本报告声称实际打开那些末页。

| 实际打开的页图 | SHA256 |
| --- | --- |
| /tmp/recover23_formula_pages/full-599.png | 6caab781ad3fa275798d75ed1843ca99a4a0d3fe8caf822e64728e18d888a3bc |
| /tmp/recover23_formula_pages/full-600.png | 8ed28e9f77026b27ab21109b2dd4750d40daac0f602a1ef3db0110337a76160a |
| /tmp/recover23_formula_pages/full-605.png | 175531a92cf9279858be938924a4c1dff98e2b52a054713a23e77232d028441d |
| /tmp/recover23_formula_pages/full-607.png | 53ffb996ff868f4314fe47f8bb0c8fb62456da0f2c392314dffc2f10efa0b555 |
| /tmp/recover23_formula_pages/full-608.png | 69a14de6652a3062227f0786ddb4a927762ea2020cea045a8f36ad3297f07052 |
| /tmp/recover23_formula_pages/full-609.png | 6343df274f33a639d03f415b14eba7d5840fc5a2727b19bf16a84da79f9ac2c6 |
| /tmp/recover23_formula_pages/full-610.png | 57daae1e21f58d18cfd12bf9397b13dbc985892fed3ac705cded93097c6d5c89 |
| /tmp/recover23_formula_pages/review-385.png | ce81edd528220e24c38c424e1307869f37e4e04d2784632676151786d27693bc |
| /tmp/recover23_formula_pages/review-386.png | 431d329891a92220f8a8bfbc16c95aff523c553ba02bc4ba0b23547cd3a5600a |
| /tmp/recover23_formula_pages/review-391.png | 4649858021eb39fd06283e2e6d75231378138f64fe189aa58e9b02bfcefb9935 |
| /tmp/recover23_formula_pages/review-393.png | f52c96031250f3ee5f5339628284c42530c752a053abe38df109e3953093850e |
| /tmp/recover23_formula_pages/review-394.png | b32549c3b7629e804e521167a81ddc27f04b8e1440d311dfcbcbb0f305c9eed8 |
| /tmp/recover23_formula_pages/review-395.png | ea9b56bd86acb131423179b76dfe2110d656eeae776bd36ac507e0f78b1c4f0f |
| /tmp/recover23_formula_pages/review-396.png | 9cc4753448cba543c86c94ec2c30992c06acabdb728b50e2d73bfb07ce5e3688 |

## 完整自动验收实际结果

实际运行 `python tools/validate_learning_batch.py`，退出码0，日志 `/tmp/recover23-qa.log`。正式报告 `data/production/batch_validation.json` 状态为 `automated_checks_passed`，SHA256为 `6bd9d4b079ec9f6dd57326a7405a946e69871bae1b32ce9dd3cad556ca0784dd`。正式范围47单元、390对题答、18图；四PDF页数712/926/31/218。公式/链接、既有有限计算、18图重生成、源码及产物绑定、全部PDF边界检查通过，零缺字与TeX越界警告。整体人工视觉仍为 `pending_actual_image_inspection`；本执行者只核上述十四页，不替root签署全批。

## 主编绑定及留存

原报告SHA-256 `ba91ce1b0cfa663cb975b9ee218a040cb4f4a8a14438f84ce5fc59f6d62ccd5b`；当前自动验收时间 2026-10-30T02:28:30.719880+00:00。上述两PDF哈希与报告后记录一致；原14张1.7倍图片另字节原样留存于local-inputs/batch23-formula-pages。
- `dist/综合数学_基础续写审阅版.pdf` SHA-256 `21beb4a4a6f462ced257796159590270f84ad9456bfb4b76e45c8b9c71557504`
- `dist/综合数学.pdf` SHA-256 `263fa832ad3c7cfc1a7a46e0223dce6011ccdd7e0c7bcf6af95c03dc315a960a`
