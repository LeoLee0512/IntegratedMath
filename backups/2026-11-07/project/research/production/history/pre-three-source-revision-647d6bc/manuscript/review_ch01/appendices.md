# 附录二 插图说明与来源 {#figures}

本审阅稿所用四张插图均由本书配套代码原创绘制，未采用外部教材或论文的插图。生成代码为 `tools/draw_ch01_figures.py`；图片只作概念说明，不替代正文中的论证。

| 文件 | 所在节 | 所说明的对象 |
|---|---|---|
| ch01_disjoint.png | 第3节 | 没有共同成员的两组圆片 |
| ch01_overlap.png | 第7节 | 两组共享一个成员 |
| ch01_rhythm.png | 第16节 | 同一单位时间的二等分与四等分 |
| ch01_square.png | 第17节 | 四个单位格组成的正方形 |

# 附录三 本章参考资料 {#sources}

**复审状态。** 原完整部分验收声明已撤回。00A17、00A27、00A30、00A64仍缺本专题的已核验参考入口；S2的逻辑知识和S3的分类代码不能替代这些入口。本轮具体访问和内容核验见`research/production/part1_revision_sources.json`及同名说明，当前来源门槛另记，不因数学例子正确而自动通过。

本章数学说明、例题、练习和答案独立撰写。下列资料用于核对基础规则与证明方法；没有复制或翻译其中的题干、解答、插图或连续正文。公开访问不等于无条件再分发，所列许可是所核验版本的许可。

**[S1]** OpenStax, Rice University，*Elementary Algebra 2e*。核对模块 m82463（等式同加同减）和 m82464（等式乘除及非零限制）。[官方教材项目](https://github.com/openstax/osbooks-prealgebra-bundle)，[同加同减章节](https://github.com/openstax/osbooks-prealgebra-bundle/blob/main/modules/m82463/index.cnxml)，[乘除章节](https://github.com/openstax/osbooks-prealgebra-bundle/blob/main/modules/m82464/index.cnxml)。本次访问的仓库许可及该书元数据为 CC BY-NC-SA 4.0，不能据此声称允许无条件商业转载。

**[S2]** Oscar Levin，*Discrete Mathematics: An Open Introduction*，所核验第四版材料。核对 *Rules of Logic* 中的量词、反例与真值表完整枚举，以及 *Proofs* 中的穷尽情况论证。[项目入口](https://github.com/oscarlevin/discrete-book)，[逻辑章节](https://github.com/oscarlevin/discrete-book/blob/master/source/sec_logic-rules.ptx)。所核验第四版材料声明 CC BY-NC-SA 4.0；不能把第三版的不同许可套到第四版上。

**[S3]** Mathematical Reviews 与 zbMATH，*Mathematics Subject Classification 2020*，用户提供的224页附件。用于核对分类代码与归属，原始PDF不随本书公开分发。

来源访问时间、状态、哈希和许可依据见伴生文件 `research/ch01_source_checks.json`。目录各级标题已译为中文，保留原MSC代码、归属和数学记号；英文原名与中文译名对照保存在伴生文件 `data/catalog_titles_zh.json` 中。

**本轮核验边界。** 来源访问记录补充见 `research/production/part1_sources_2026-11-05.json`。本轮重新取得[S1]、[S2]的项目、版本和许可材料；上述具体数学模块的内容核对仍引用原2026年10月21日记录，不把元数据复核说成再次审读整本教材。外部书评、开放问题、数学哲学和数学文学的若干拓展网站在本次环境中未能访问；不据此判断网站不存在，也不把这些候选入口列成已读参考文献。本章采用的量词和反例示范只由[S2]支持，分类定位只由[S3]支持，不能扩张为哲学史、文学研究或最新开放问题状态已经核验。

**[S4]** Stacks Project维护者，*The Stacks Project*，[维护者仓库的项目说明](https://github.com/stacks/stacks-project/blob/master/README)。本轮只读取项目说明，核对它讨论代数叠及相关代数几何这一研究层次定位；未审阅其定理、证明或独立许可文件，不复制教材正文。它在本部分仅作为“先辨认研究对象，再查所需背景”的阅读入口示例，不把其专门学科改归数学总论。

# 附录四 第21节模拟代码 {#simulation-code}

对应模型为 $V_0=5$、$V_{n+1}=V_n+2$，$n$ 是非负整数，下标为经过的整分钟数，水量单位为升。代码精确执行这一离散规则，不作浮点近似，不证明模型适用于真实容器。运行 `python tools/ch01_simulation.py` 输出从零到三分钟的四条状态，水量依次为五、七、九、十一。

Python 整数用于精确表示这里的整数状态。循环开始前保存初始值，每次循环只推进一分钟。参数要求非负整数，零步只返回初始状态。完整实现如下。
