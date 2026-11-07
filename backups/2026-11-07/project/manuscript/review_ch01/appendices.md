# 附录二 插图说明与来源 {#figures}

本审阅稿所用四张插图均由本书配套代码原创绘制，未采用外部教材或论文的插图。生成代码为 `tools/draw_ch01_figures.py`；图片只作概念说明，不替代正文中的论证。

| 文件 | 所在节 | 所说明的对象 |
|---|---|---|
| ch01_disjoint.png | 第3节 | 没有共同成员的两组圆片 |
| ch01_overlap.png | 第7节 | 两组共享一个成员 |
| ch01_rhythm.png | 第16节 | 同一单位时间的二等分与四等分 |
| ch01_square.png | 第17节 | 四个单位格组成的正方形 |

# 附录三 本章参考资料 {#sources}

**复审状态。** 原完整部分验收声明仍撤回。00A17、00A27及第二章等条目的专题来源仍有缺口；此前已为00-02、00A30、00A64补入限定的实际阅读入口；本次再为第二章00B05补入真实讲座摘要入口，见第二章来源说明[C2-S3]。其对应全文与证明尚未取得或核验，不把S2的逻辑知识和S3的分类代码扩张为专题研究。来源状态与数学、教学、构建分别核验；整个部分是否完成仍以当前逐项目台账为准。旧访问记录保留，三项先前核读见下列S4—S6，本次摘要核读见C2-S3及对应研究记录。

本章数学说明、例题、练习和答案独立撰写。下列资料用于核对基础规则与证明方法；没有复制或翻译其中的题干、解答、插图或连续正文。公开访问不等于无条件再分发，所列许可是所核验版本的许可。

**[S1]** OpenStax, Rice University，*Elementary Algebra 2e*。核对模块 m82463（等式同加同减）和 m82464（等式乘除及非零限制）。[官方教材项目](https://github.com/openstax/osbooks-prealgebra-bundle)，[同加同减章节](https://github.com/openstax/osbooks-prealgebra-bundle/blob/main/modules/m82463/index.cnxml)，[乘除章节](https://github.com/openstax/osbooks-prealgebra-bundle/blob/main/modules/m82464/index.cnxml)。本次访问的仓库许可及该书元数据为 CC BY-NC-SA 4.0，不能据此声称允许无条件商业转载。

**[S2]** Oscar Levin，*Discrete Mathematics: An Open Introduction*，所核验第四版材料。核对 *Rules of Logic* 中的量词、反例与真值表完整枚举，以及 *Proofs* 中的穷尽情况论证。[项目入口](https://github.com/oscarlevin/discrete-book)，[逻辑章节](https://github.com/oscarlevin/discrete-book/blob/master/source/sec_logic-rules.ptx)。所核验第四版材料声明 CC BY-NC-SA 4.0；不能把第三版的不同许可套到第四版上。

**[S3]** Mathematical Reviews 与 zbMATH，*Mathematics Subject Classification 2020*，用户提供的224页附件。用于核对分类代码与归属，原始PDF不随本书公开分发。

来源访问时间、状态、哈希和许可依据见伴生文件 `research/ch01_source_checks.json`。目录各级标题已译为中文，保留原MSC代码、归属和数学记号；英文原名与中文译名对照保存在伴生文件 `data/catalog_titles_zh.json` 中。

**本轮核验边界。** 早期访问记录见`research/production/part1_sources_2026-11-05.json`；其中若干拓展网站未能访问的事实不改写。此后分别取得下列S4—S6的独立公开档案并实际核读所列片段。没有把这些访问当作受阻网站的核验，也没有把取得全文等同于审读全文。量词示范仍由[S2]核对，分类定位由[S3]核对；历史思想与文学原作各按其限定用途引用。

**[S4]** The Stacks Project contributors，*The Stacks Project*，本次固定档案的[“概形”章](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/schemes.tex#L503-L590)、[全局约定](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/conventions.tex#L47-L54)、[项目介绍与许可通知](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/introduction.tex#L16-L44)、[许可全文](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/COPYING)。早期只读项目说明；2026年11月5日新增核读标准开集引理的陈述、证明位置及相关约定，未逐一审读其所引代数、层论或EGA结果。文档许可通知为GNU FDL 1.2或后续版本，无固定章节及封面、封底固定文字。本书仅给链接和原创阅读说明，不分发源书。精确版本、哈希与阅读范围见`research/production/part1_research_exposition_followup.json`及同名说明。

**[S5]** Bertrand Russell（伯特兰·罗素），*Introduction to Mathematical Philosophy*（《数学哲学导论》），所读电子档案载第二版，1920年；[第一章固定文本](https://github.com/GITenberg/Introduction-to-Mathematical-Philosophy_41654/blob/7f4e90716794406bb99e227bedc1c6c465bc53b2/41654-t/41654-t.tex#L769-L1159)，GITenberg／Project Gutenberg 41654。本次只核读采用起点与分析起点、暂未定义的项及不同解释的相关段落，不作为现代数学哲学全景或本书数学定理的依据。档案元数据声明美国公有领域，未核美国以外的再分发权利；不转载原文或中文译文。版本差异、许可限制及精确阅读范围见`research/production/part1_math_philosophy_followup.json`及同名说明。

**[S6]** Edwin A. Abbott（埃德温·阿博特），*Flatland: A Romance of Many Dimensions*（《平面国》），1884年，所读档案载第二次修订版序；GITenberg／Project Gutenberg 97。[第21—22节相关片段](https://github.com/GITenberg/Flatland--a-romance-of-many-dimensions_97/blob/5ed685b7d3d8484f94ea5f1a061b7ef6fb93d2c8/97.txt#L3173-L3290)、[第19节类比对话](https://github.com/GITenberg/Flatland--a-romance-of-many-dimensions_97/blob/5ed685b7d3d8484f94ea5f1a061b7ef6fb93d2c8/97.txt#L2862-L3045)、[修订版序的范围提示](https://github.com/GITenberg/Flatland--a-romance-of-many-dimensions_97/blob/5ed685b7d3d8484f94ea5f1a061b7ef6fb93d2c8/97.txt#L3538-L3546)。它是数学概念参与叙事的文学原作；人物话语不是本书的几何证明，也不是本节量词交换例子的出处。档案声明美国公有领域，未核美国以外再分发权利；本书不转载原文、插图或译文。具体核读及许可边界见`research/production/part1_math_literature_followup.json`及同名说明。

# 附录四 第21节模拟代码 {#simulation-code}

对应模型为 $V_0=5$、$V_{n+1}=V_n+2$，$n$ 是非负整数，下标为经过的整分钟数，水量单位为升。代码精确执行这一离散规则，不作浮点近似，不证明模型适用于真实容器。运行 `python tools/ch01_simulation.py` 输出从零到三分钟的四条状态，水量依次为五、七、九、十一。

Python 整数用于精确表示这里的整数状态。循环开始前保存初始值，每次循环只推进一分钟。参数要求非负整数，零步只返回初始状态。完整实现如下。
