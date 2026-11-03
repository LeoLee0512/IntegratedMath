def rational_gaps_cuts_reference_addition():
    evidence = (ROOT / "research/production/rational_gaps_cuts_sources_2026-10-29.md").read_text()
    for identifier in ["e21ec524ca7d54f800c693b948020c188d21d01f",
                       "7a0bcaf5e279121cb675058d7e323556343087d0", "LowerSet"]:
        if identifier not in evidence:
            raise ValueError("Rational gaps/cuts evidence changed: review curated citations")
    return r"""
## 有理数缺口与戴德金分割次序参考资料 {#rational-gaps-cuts-sources}

本批正文、证明、题答、见证公式与图示独立编写。以下来源用于核查定义版本、定理条件及历史事实，不移植第三方段落、习题、图像或源码。

**[GAP-LEBL]** Jiří Lebl，*Basic Analysis I*，第6.3版。

固定提交：

`e21ec524ca7d54f800c693b948020c188d21d01f`。

[实数章节的界定义与分割练习](https://github.com/jirilebl/ra/blob/e21ec524ca7d54f800c693b948020c188d21d01f/ch-real-nums.tex)及[许可](https://github.com/jirilebl/ra/blob/e21ec524ca7d54f800c693b948020c188d21d01f/LICENSE.md)已核。该项目提供CC BY-SA 4.0与CC BY-NC-SA 4.0双许可；此处不改编其文字或图像。来源已经具备实数与实数上确界，再用实数上确界刻画有理下集。本书不能沿用这一证明起点，而先在有理数内证明稠密、显式自然数界及平方缺口，再独立构造分割的次序。来源中的实数稠密性与阿基米德证明也不充作本书未写的先修。

**[GAP-DEDEKIND]** Richard Dedekind，*Continuity and Irrational Numbers*（1872）；Wooster Woodruff Beman英译，收入 *Essays on the Theory of Numbers*。Project Gutenberg电子书21016于2007年发布，电子版日期与原作历史日期分开记录。

GITenberg固定提交：

`7a0bcaf5e279121cb675058d7e323556343087d0`。

[译本源码](https://github.com/GITenberg/Essays-on-the-Theory-of-Numbers_21016/blob/7a0bcaf5e279121cb675058d7e323556343087d0/21016-t/21016-t.tex)、[元数据](https://github.com/GITenberg/Essays-on-the-Theory-of-Numbers_21016/blob/7a0bcaf5e279121cb675058d7e323556343087d0/metadata.yaml)及[许可](https://github.com/GITenberg/Essays-on-the-Theory-of-Numbers_21016/blob/7a0bcaf5e279121cb675058d7e323556343087d0/LICENSE)已核。元数据声明在美国属公有领域，并有Project Gutenberg许可及所在地法律条件，不能改写成全球无条件公有领域。原著采用两侧分割并讨论有理端点归入哪一侧；本书采用非空、非全体、下闭、无最大元的现代单侧下集约定，不把四条件逐字归作原著定义。原著改进缺口两侧的有理公式与本书公式不同，本书的 $f(q)=(2q+2)/(q+2)$ 由正文独立推导，不冒称历史原式。

**[GAP-MATHLIB]** mathlib项目，v4.24.0，Apache 2.0许可。[有序域中的中点](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Order/Field/Basic.lean)、[阿基米德条件](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Order/Archimedean/Basic.lean)、[下集定义](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Order/UpperLower/Basic.lean)与[下集的并及序结构](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Order/UpperLower/CompleteLattice.lean)用于条件交叉核查。库中的全部 `LowerSet` 包括空集与全体，并形成完整格；本书分割排除这两者，还要求无最大元。因此本书只证明非空、有分割上界的分割族之并仍为分割并给出上确界，不能照搬库的完整格名称或不带条件的任意族结论。库的有理数阿基米德实例所用取整结构也不作为额外先修，本书直接从合法有理记录给出自然数界。

逐条访问时间、固定位置、作者、许可及字节哈希见伴生审计。目录为 `research/production/`。

文件为 `rational_gaps_cuts_sources_2026-10-29.json`。

只读核对源码，未编译Lean或形式化书稿。分割集合的形成公开采用有理数幂集存在的背景；不声称从集合论公理重新证明它。分割算术、有序域结构、实数开方和极限尚未建立。有限见证绘图的完整函数见[附录二十四](#rational-gap-figure-code)。

"""


def rational_gap_figure_source():
    """Publish the exact complete function used by the current figure script."""
    import ast
    source = (ROOT / "tools/draw_foundations_batch.py").read_text()
    functions = [node for node in ast.parse(source).body
                 if isinstance(node, ast.FunctionDef) and node.name == "draw_rational_gap"]
    if len(functions) != 1:
        raise ValueError("Expected exactly one complete rational gap drawing function")
    node = functions[0]
    return "\n".join(source.splitlines()[node.lineno-1:node.end_lineno]) + "\n"


def rational_gap_figure_appendix():
    text = r"""

# 附录二十四 有理缺口的有限见证绘图 {#rational-gap-figure-code}

本附录完整列出绘图脚本 `tools/draw_foundations_batch.py` 中的 `draw_rational_gap(out)`，包括其局部更新函数、精确计算、有限断言与绘图步骤；源码直接从当前脚本提取。它只生成[有理数缺口单元](#qgap-unit)的一张有限见证图，不是任意实数或分割的数值实现，不提供通用求极限、求上确界或分割判等接口。

**计算对象与依据。** 正文QG3先对每个非负有理数证明分母 $q+2>0$，并由有理运算逐项推出

$$
f(q)=\frac{2q+2}{q+2},\qquad f(q)>0.
$$

$$
f(q)-q=\frac{2-q^2}{q+2}.
$$

$$
f(q)^2-2=\frac{2(q^2-2)}{(q+2)^2}.
$$

从一开始只更新两次，得到 $1,4/3,7/5$；从二开始同样只更新两次，得到 $2,3/2,10/7$。六个分数与平方都用 `Fraction` 精确计算。前一行的平方依次为 $1,16/9,49/25$，均小于二，数值严格增加；后一行平方依次为 $4,9/4,100/49$，均大于二，数值严格减少。程序对四次更新检查上述两条恒等式，并核对各行符号和次序。

后一行的每个值是 $S$ 的有理上界，不只是图中前三个样本的上界：正文已证，对任意非负有理 $u$，若 $u^2>2$，任意 $s\in S$ 都满足 $s^2<2<u^2$，由非负平方比较反射得到 $s<u$。有限断言仅核对这六个实例；任意成员、任意上界的结论由正文证明承担。

图中方框、箭头和文字位置是布局坐标，不是数轴间距，不表示全部有理数或极限过程；图没有引入一个未定义的实数平方根。它也不枚举或决定[戴德金分割](#cut-unit)。正文的分割对象和条件上确界证明不依赖绘图。

**依赖与入口。** 完整函数复用绘图脚本头已经导入的 `plt`、`FontProperties`、`Text`：分别来自 `matplotlib.pyplot`、`matplotlib.font_manager`、`matplotlib.text`。该脚本使用Matplotlib的Agg后端，并采用指定的Noto中文字体；数学样本在图形渲染前以精确分数计算，字体与布局仅影响显示。函数内自行导入 `Fraction`，参数 `out` 是已经存在的输出目录路径。构建入口执行绘图脚本的 `main()`，它建立 `dist/figures` 后调用本函数，并生成 `b2_rational_gap.png`。

下面列出完整函数；其中断言是固定样本的诊断，不作为外部输入校验接口或全称证明。

```python
"""
    return (text + rational_gap_figure_source() + "\n```\n\n"
            "在脚本的 `main()` 已建立输出目录 `out` 后，入口调用为：\n\n"
            "```python\ndraw_rational_gap(out)\n```\n")


