#!/usr/bin/env python3
"""Build the local learning batch; never publish or change authored chapter sources.

The legacy chapter build and validator run BEFORE replacing the combined book.
Use --reuse-legacy-validation only immediately after a separately verified legacy
build: its complete input/output hash gate must still pass.
Use --incremental to reuse unchanged independent chapter/catalogue artifacts only
after checking a prior build manifest, legacy validation snapshot and their hashes.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import sys

from build_ch01_review import compact_catalog
from review_artifacts import artifact_hashes as legacy_artifact_hashes
from review_artifacts import check_build_inputs, source_hashes as legacy_source_hashes

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist"
BUILD = ROOT / "build/learning_batch"
CHAPTER = ROOT / "manuscript/review_ch01"
FOUNDATIONS = ROOT / "manuscript/foundations"
REVIEW_STEM = "综合数学_基础续写审阅版"
NEW_STEMS = [REVIEW_STEM, "综合数学"]
PDF_STEMS = NEW_STEMS + ["综合数学_第一章审阅版", "综合数学_完整数学目录"]
FIGURES = ["ch01_disjoint.png", "ch01_overlap.png", "ch01_rhythm.png",
           "ch01_square.png", "b1_place_value.png", "b1_rational_distance.png", "b1_ratio_allocation.png",
           "b2_function_mapping.png", "b2_inverse_mapping.png", "b2_elimination_steps.png",
           "b2_absolute_bounds.png", "b2_affine_coordinates.png", "b2_finite_sum.png", "b2_polynomial_records.png", "b2_polynomial_product.png", "b2_quadratic_bound.png", "b2_rational_gap.png"]
UNITS = [
    ("natural_numbers", "b1-natural-numbers", "b1", "natural_number"),
    ("place_value", "b1-place-value", "b1-pv", "place_value"),
    ("natural_order", "ord-natural-order", "ord", "natural_order"),
    ("division_remainder", "div-unit", "div", "division_remainder"),
    ("positional_representation", "pos-unit", "pos", "positional_representation"),
    ("natural_subtraction", "sub-unit", "sub", "natural_subtraction"),
    ("integers_addition_order", "int-unit", "int", "integers_addition_order"),
    ("integers_multiplication", "imul-unit", "imul", "integers_multiplication"),
    ("integer_division", "idiv-unit", "idiv", "integer_division"),
    ("divisibility", "dvs-unit", "dvs", "divisibility"),
    ("gcd_euclidean", "gcd-unit", "gcd", "gcd_euclidean"),
    ("bezout", "bez-unit", "bez", "bezout"),
    ("coprimality", "cop-unit", "cop", "coprimality"),
    ("rationals_construction", "rat-unit", "rat", "rationals_construction"),
    ("rationals_addition", "radd-unit", "radd", "rationals_addition"),
    ("rationals_multiplication", "rmul-unit", "rmul", "rationals_multiplication"),
    ("rationals_division", "rdiv-unit", "rdiv", "rationals_division"),
    ("rationals_order", "rord-unit", "rord", "rationals_order"),
    ("rationals_absolute", "rabs-unit", "rabs", "rationals_absolute"),
    ("ratios_proportions", "ratio-unit", "ratio", "ratios_proportions"),
    ("quantities_units", "qty-unit", "qty", "quantities_units"),
    ("functions_definition", "fun-unit", "fun", "functions_definition"),
    ("functions_composition", "funcomp-unit", "funcomp", "functions_composition"),
    ("functions_bijections", "bij-unit", "bij", "functions_bijections"),
    ("functions_inverse", "inv-unit", "inv", "functions_inverse"),
    ("linear_equations", "lin-unit", "lin", "linear_equations"),
    ("linear_systems", "sys-unit", "sys", "linear_systems"),
    ("linear_inequalities", "ineq-unit", "ineq", "linear_inequalities"),
    ("absolute_inequalities", "absineq-unit", "absineq", "absolute_inequalities"),
    ("rational_coordinates", "coord-unit", "coord", "rational_coordinates"),
    ("affine_graphs", "affgraph-unit", "affgraph", "affine_graphs"),
    ("rational_powers", "pow-unit", "pow", "rational_powers"),
    ("finite_sums", "sum-unit", "sum", "finite_sums"),
    ("polynomial_records", "polyrec-unit", "polyrec", "polynomial_records"),
    ("polynomial_linear_operations", "polyops-unit", "polyops", "polynomial_linear_operations"),
    ("polynomial_multiplication", "polymul-unit", "polymul", "polynomial_multiplication"),
    ("polynomial_product_structure", "polyprod-unit", "polyprod", "polynomial_product_structure"),
    ("polynomial_linear_division", "polydiv-unit", "polydiv", "polynomial_linear_division"),
    ("polynomial_roots_identity", "polyroot-unit", "polyroot", "polynomial_roots_identity"),
    ("rational_square_equations", "sqrat-unit", "sqrat", "rational_square_equations"),
    ("rational_quadratic_equations", "quad-unit", "quad", "rational_quadratic_equations"),
    ("rational_gaps_bounds", "qgap-unit", "qgap", "rational_gaps_bounds"),
    ("dedekind_cuts_order", "cut-unit", "cut", "dedekind_cuts_order"),
]
EDUCATION_UNITS = {
    "ratio-unit": {"chapter": 526, "code": "97Fxx", "section": "97F80"},
    "qty-unit": {"chapter": 526, "code": "97Fxx", "section": "97F70"},
    "fun-unit": {"chapter": 529, "code": "97Ixx", "section": "97I20"},
    "funcomp-unit": {"chapter": 529, "code": "97Ixx", "section": "97I20"},
    "bij-unit": {"chapter": 529, "code": "97Ixx", "section": "97I20"},
    "inv-unit": {"chapter": 529, "code": "97Ixx", "section": "97I20"},
    "lin-unit": {"chapter": 528, "code": "97Hxx", "section": "97H30"},
    "sys-unit": {"chapter": 528, "code": "97Hxx", "section": "97H30"},
    "ineq-unit": {"chapter": 528, "code": "97Hxx", "section": "97H30"},
    "absineq-unit": {"chapter": 528, "code": "97Hxx", "section": "97H30"},
    "coord-unit": {"chapter": 529, "code": "97Ixx", "section": "97I20"},
    "affgraph-unit": {"chapter": 529, "code": "97Ixx", "section": "97I20"},
    "pow-unit": {"chapter": 528, "code": "97Hxx", "section": "97H20"},
    "sum-unit": {"chapter": 528, "code": "97Hxx", "section": "97H20"},
    "polyrec-unit": {"chapter": 528, "code": "97Hxx", "section": "97H20"},
    "polyops-unit": {"chapter": 528, "code": "97Hxx", "section": "97H20"},
    "polymul-unit": {"chapter": 528, "code": "97Hxx", "section": "97H20"},
    "polyprod-unit": {"chapter": 528, "code": "97Hxx", "section": "97H20"},
    "polydiv-unit": {"chapter": 528, "code": "97Hxx", "section": "97H20"},
    "polyroot-unit": {"chapter": 528, "code": "97Hxx", "section": "97H20"},
    "sqrat-unit": {"chapter": 528, "code": "97Hxx", "section": "97H30"},
    "quad-unit": {"chapter": 528, "code": "97Hxx", "section": "97H30"},
    "qgap-unit": {"chapter": 526, "code": "97Fxx", "section": "97F50"},
    "cut-unit": {"chapter": 526, "code": "97Fxx", "section": "97F50"},
}
WRITTEN_REPORT = ROOT / "research/production/written_arithmetic_validation.json"
INTEGER_REPORT = ROOT / "research/production/integer_pairs_validation.json"
EUCLIDEAN_REPORT = ROOT / "research/production/integer_euclidean_validation.json"
EXTENDED_REPORT = ROOT / "research/production/extended_euclidean_validation.json"
RATIONAL_REPORT = ROOT / "research/production/rational_addition_validation.json"
RATIONAL_MULTIPLICATION_REPORT = ROOT / "research/production/rational_multiplication_validation.json"
RATIONAL_ORDER_REPORT = ROOT / "research/production/rational_order_validation.json"
RATIOS_UNITS_REPORT = ROOT / "research/production/ratios_units_validation.json"
FINITE_FUNCTIONS_REPORT = ROOT / "research/production/finite_functions_validation.json"
FINITE_FUNCTION_INVERSES_REPORT = ROOT / "research/production/finite_function_inverses_validation.json"
LINEAR_EQUATION_SOLVERS_REPORT = ROOT / "research/production/linear_equation_solvers_validation.json"
RATIONAL_INEQUALITIES_REPORT = ROOT / "research/production/rational_inequalities_validation.json"
RATIONAL_AFFINE_REPORT = ROOT / "research/production/rational_affine_validation.json"
RATIONAL_POWERS_SUMS_REPORT = ROOT / "research/production/rational_powers_sums_validation.json"
RATIONAL_POLYNOMIAL_BASIC_REPORT = ROOT / "research/production/rational_polynomial_basic_validation.json"
RATIONAL_POLYNOMIAL_PRODUCT_REPORT = ROOT / "research/production/rational_polynomial_product_validation.json"
RATIONAL_POLYNOMIAL_LINEAR_DIVISION_REPORT = ROOT / "research/production/rational_polynomial_linear_division_validation.json"

RATIONAL_QUADRATICS_REPORT = ROOT / "research/production/rational_quadratics_validation.json"


def hashes(paths):
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(set(paths))}


def source_hashes():
    paths = [ROOT / name for name in legacy_source_hashes()]
    paths += [FOUNDATIONS / (stem + suffix + ".md")
              for stem, *_ in UNITS for suffix in ["", "_answers"]]
    paths += [ROOT / "tools/build_learning_batch.py",
              ROOT / "tools/validate_learning_batch.py",
              ROOT / "tools/package_learning_batch.py",
              ROOT / "tools/draw_foundations_batch.py",
              ROOT / "tools/natural_algorithms.py",
              ROOT / "tools/written_arithmetic.py",
              ROOT / "tools/validate_written_arithmetic.py",
              ROOT / "tools/integer_pairs.py",
              ROOT / "tools/validate_integer_pairs.py",
              ROOT / "tools/integer_euclidean.py",
              ROOT / "tools/validate_integer_euclidean.py",
              ROOT / "tools/extended_euclidean.py",
              ROOT / "tools/validate_extended_euclidean.py",
              ROOT / "tools/rational_addition.py",
              ROOT / "tools/validate_rational_addition.py",
              ROOT / "tools/rational_multiplication.py",
              ROOT / "tools/validate_rational_multiplication.py",
              ROOT / "tools/rational_order.py",
              ROOT / "tools/validate_rational_order.py",
              ROOT / "tools/ratios_units.py",
              ROOT / "tools/validate_ratios_units.py",
              ROOT / "tools/finite_functions.py",
              ROOT / "tools/validate_finite_functions.py",
              ROOT / "tools/finite_function_inverses.py",
              ROOT / "tools/validate_finite_function_inverses.py",
              ROOT / "tools/linear_equation_solvers.py",
              ROOT / "tools/validate_linear_equation_solvers.py",
              ROOT / "tools/rational_inequalities.py",
              ROOT / "tools/validate_rational_inequalities.py",
              ROOT / "tools/rational_affine.py",
              ROOT / "tools/validate_rational_affine.py",
              ROOT / "tools/rational_powers_sums.py",
              ROOT / "tools/validate_rational_powers_sums.py",
              ROOT / "tools/rational_polynomial_basic.py",
              ROOT / "tools/validate_rational_polynomial_basic.py",
              ROOT / "tools/rational_polynomial_product.py",
              ROOT / "tools/validate_rational_polynomial_product.py",
              ROOT / "tools/rational_quadratics.py",
              ROOT / "tools/validate_rational_quadratics.py",
              ROOT / "research/production/rational_quadratics_algorithm_notes.md",
              ROOT / "tools/rational_polynomial_linear_division.py",
              ROOT / "tools/validate_rational_polynomial_linear_division.py",
              ROOT / "tools/validate_ch01_review.py",
              ROOT / "tools/validate_catalog_chinese.py",
              ROOT / "tools/review_artifacts.py",
              ROOT / "research/production/foundations_sources_2026-10-27.md",
              ROOT / "research/production/foundations_sources_2026-10-27.json",
              ROOT / "research/production/integers_sources_2026-10-27.md",
              ROOT / "research/production/integers_sources_2026-10-27.json",
              ROOT / "research/production/divisibility_sources_2026-10-27.md",
              ROOT / "research/production/divisibility_sources_2026-10-27.json",
              ROOT / "research/production/bezout_sources_2026-10-27.md",
              ROOT / "research/production/bezout_sources_2026-10-27.json",
              ROOT / "research/production/rationals_sources_2026-10-27.md",
              ROOT / "research/production/rationals_sources_2026-10-27.json",
              ROOT / "research/production/rationals_multiplication_sources_2026-10-27.md",
              ROOT / "research/production/rationals_multiplication_sources_2026-10-27.json",
              ROOT / "research/production/rationals_order_sources_2026-10-27.md",
              ROOT / "research/production/rationals_order_sources_2026-10-27.json",
              ROOT / "research/production/ratios_units_sources_2026-10-27.md",
              ROOT / "research/production/ratios_units_sources_2026-10-27.json",
              ROOT / "research/production/functions_sources_2026-10-29.md",
              ROOT / "research/production/functions_sources_2026-10-29.json",
              ROOT / "research/production/inverse_functions_sources_2026-10-29.md",
              ROOT / "research/production/inverse_functions_sources_2026-10-29.json",
              ROOT / "research/production/linear_equations_sources_2026-10-29.md",
              ROOT / "research/production/linear_equations_sources_2026-10-29.json",
              ROOT / "research/production/linear_inequalities_sources_2026-10-29.md",
              ROOT / "research/production/linear_inequalities_sources_2026-10-29.json",
              ROOT / "research/production/coordinates_affine_sources_2026-10-29.md",
              ROOT / "research/production/coordinates_affine_sources_2026-10-29.json",
              ROOT / "research/production/powers_sums_sources_2026-10-29.md",
              ROOT / "research/production/powers_sums_sources_2026-10-29.json",
              ROOT / "research/production/polynomial_basic_sources_2026-10-29.md",
              ROOT / "research/production/polynomial_basic_sources_2026-10-29.json",
              ROOT / "research/production/polynomial_product_sources_2026-10-29.md",
              ROOT / "research/production/polynomial_product_sources_2026-10-29.json",
              ROOT / "research/production/polynomial_linear_division_sources_2026-10-29.md",
              ROOT / "research/production/polynomial_linear_division_sources_2026-10-29.json",
              ROOT / "research/production/rational_quadratic_sources_2026-10-29.md",
              ROOT / "research/production/rational_quadratic_sources_2026-10-29.json",
              ROOT / "research/production/rational_gaps_cuts_sources_2026-10-29.md",
              ROOT / "research/production/rational_gaps_cuts_sources_2026-10-29.json"]
    return hashes(paths)


def artifact_hashes():
    paths = [OUT / (stem + ext) for stem in PDF_STEMS for ext in [".md", ".pdf"]]
    paths += [OUT / (stem + ".html") for stem in NEW_STEMS + ["综合数学_第一章审阅版"]]
    paths += [OUT / "figures" / name for name in FIGURES]
    paths += [OUT / "style.css"]
    paths += [WRITTEN_REPORT, INTEGER_REPORT, EUCLIDEAN_REPORT, EXTENDED_REPORT,
              RATIONAL_REPORT, RATIONAL_MULTIPLICATION_REPORT, RATIONAL_ORDER_REPORT, RATIOS_UNITS_REPORT,
              FINITE_FUNCTIONS_REPORT, FINITE_FUNCTION_INVERSES_REPORT, LINEAR_EQUATION_SOLVERS_REPORT,
              RATIONAL_INEQUALITIES_REPORT, RATIONAL_AFFINE_REPORT, RATIONAL_POWERS_SUMS_REPORT,
              RATIONAL_POLYNOMIAL_BASIC_REPORT, RATIONAL_POLYNOMIAL_PRODUCT_REPORT,
              RATIONAL_POLYNOMIAL_LINEAR_DIVISION_REPORT, RATIONAL_QUADRATICS_REPORT]
    return hashes(paths)


def run(args, log=None):
    if log:
        with log.open("w") as stream:
            subprocess.run(args, cwd=ROOT, check=True, stdout=stream, stderr=stream)
    else:
        subprocess.run(args, cwd=ROOT, check=True)


def localize_book_links(text):
    """Only normalize known manuscript links in the generated book, not sources."""
    unit_names = "|".join(re.escape(stem + suffix) for stem, *_ in UNITS
                          for suffix in ["", "_answers"])
    allowed = (r"(?:\.\./review_ch01/)?(?:chapter|part_opening|answers)\.md|"
               r"(?:" + unit_names + r")\.md")
    text = re.sub(r"\]\((?:" + allowed + r")#([^\s)]+)\)", r"](#\1)", text)
    text = text.replace(
        "](../../research/production/foundations_sources_2026-10-27.md)",
        "](#foundation-sources)")
    text = text.replace(
        "](../../research/production/integers_sources_2026-10-27.md)",
        "](#integer-sources)")
    text = text.replace(
        "](../../research/production/divisibility_sources_2026-10-27.md)",
        "](#divisibility-sources)")
    text = text.replace(
        "](../../research/production/bezout_sources_2026-10-27.md)",
        "](#bezout-sources)")
    text = text.replace(
        "](../../research/production/rationals_sources_2026-10-27.md)",
        "](#rationals-sources)")
    text = text.replace(
        "](../../research/production/rationals_multiplication_sources_2026-10-27.md)",
        "](#rationals-multiplication-sources)")
    text = text.replace(
        "](../../research/production/rationals_order_sources_2026-10-27.md)",
        "](#rationals-order-sources)")
    text = text.replace(
        "](../../research/production/ratios_units_sources_2026-10-27.md)",
        "](#ratios-units-sources)")
    text = text.replace(
        "](../../research/production/functions_sources_2026-10-29.md)",
        "](#functions-sources)")
    text = text.replace(
        "](../../research/production/inverse_functions_sources_2026-10-29.md)",
        "](#inverse-functions-sources)")
    text = text.replace(
        "](../../research/production/linear_equations_sources_2026-10-29.md)",
        "](#linear-equations-sources)")
    text = text.replace(
        "](../../research/production/linear_inequalities_sources_2026-10-29.md)",
        "](#linear-inequalities-sources)")
    text = text.replace(
        "](../../research/production/coordinates_affine_sources_2026-10-29.md)",
        "](#coordinates-affine-sources)")
    text = text.replace(
        "](../../research/production/powers_sums_sources_2026-10-29.md)",
        "](#powers-sums-sources)")
    text = text.replace(
        "](../../research/production/polynomial_basic_sources_2026-10-29.md)",
        "](#poly-basic-sources)")
    text = text.replace(
        "](../../research/production/polynomial_product_sources_2026-10-29.md)",
        "](#poly-product-sources)")
    text = text.replace(
        "](../../research/production/polynomial_linear_division_sources_2026-10-29.md)",
        "](#poly-linear-division-sources)")
    text = text.replace(
        "](../../research/production/rational_quadratic_sources_2026-10-29.md)",
        "](#rational-quadratic-sources)")
    text = text.replace(
        "](../../research/production/rational_gaps_cuts_sources_2026-10-29.md)",
        "](#rational-gaps-cuts-sources)")
    # A bare attribute after bold paragraph text is NOT a Pandoc identifier.
    # Make question labels real headings in the assembled document only.
    return re.sub(r"^\*\*(题[^*\n]+)\*\* (\{#[^}]+\})$", r"#### \1 \2", text, flags=re.M)


def catalog_with_unique_ids(text):
    compact = compact_catalog(text)
    def explicit(match):
        hashes_, number, kind, title = match.groups()
        noun = "part" if kind == "部分" else "chapter"
        return f"{hashes_} 第{number}{kind} {title} {{#catalog-{noun}-{number}}}"
    return re.sub(r"^(#{2,3}) 第(\d+)(部分|章) (.+)$", explicit, compact, flags=re.M)


def reference_addition():
    # Curated citations, deliberately not the HTTP-request/review audit transcript.
    evidence = (ROOT / "research/production/foundations_sources_2026-10-27.md").read_text()
    for identifier in ["FND-OPENSTAX", "FND-LEVIN", "FND-LEAN"]:
        if identifier not in evidence:
            raise ValueError("Source evidence changed: review the curated citations")
    return """
## 本批基础单元参考资料 {#foundation-sources}

本批自然数、归纳、递归和位值的文字、论证、例题与练习独立撰写。以下资料用于交叉核对，不复制其题干、答案、图片或连续正文。核验日期为2026年10月27日；公开访问不等于可以无条件转载。

**[F1]** Lynn Marecek、MaryAnne Anthony-Smith、Andrea Honeycutt Mathis，OpenStax，*Prealgebra 2e*。[自然数与位值模块](https://github.com/openstax/osbooks-prealgebra-bundle/blob/main/modules/m81243/index.cnxml)。核对十进位值与占位零；所核验版本为CC BY-NC-SA 4.0。本书明示自然数包含零；参考教材的命名约定不同，不混同两者。

**[F2]** Oscar Levin，*Discrete Mathematics: An Open Introduction*，第四版。[归纳证明](https://github.com/oscarlevin/discrete-book/blob/master/source/sec_seq-induction.ptx)、[递归数列](https://github.com/oscarlevin/discrete-book/blob/master/source/sec_seq-basics.ptx)。核对归纳的基例与归纳步、递推关系与初始条件。所核验第四版为CC BY-NC-SA 4.0。参考资料仅用于核对条件与方法；本批商余存在唯一性由B1.4正文独立证明，递归原则仍明示采用，未从集合论重建。

**[F3]** Lean 4 项目，Leonardo de Moura、Mario Carneiro等，[核心自然数源码](https://github.com/leanprover/lean4/blob/master/src/Init/Prelude.lean)。以零、后继及沿第二变量的加乘递归规则作另一视角核对。所核验文件采用Apache 2.0。本书没有据此宣称自身论证已经过证明助手形式验证。

版本、许可依据、访问记录、文件哈希与适用限制另存于伴生文件 `research/production/foundations_sources_2026-10-27.json`。有限计算交叉检查由 `tools/validate_learning_batch.py` 执行；它检查零至十二的加乘法实例、27加15与38加24的位值展开，以及零至一百二十的商余和位值算法实例。程序检查不替代对任意自然数的证明；算法完整源码见[附录五](#natural-algorithms)。

"""


def integer_reference_addition():
    evidence = (ROOT / "research/production/integers_sources_2026-10-27.md").read_text()
    for identifier in ["INT-JUDSON", "INT-LEAN", "INT-MATHLIB"]:
        if identifier not in evidence:
            raise ValueError("Integer source evidence changed: review curated citations")
    return """
## 整数单元参考资料 {#integer-sources}

本批整数单元独立撰写定义、证明、例题和习题。以下公开资料用于核对标准定义及条件；不复制其题目、答案、插图或连续正文。核验日期为2026年10月27日。

**[INT-JUDSON]** Thomas W. Judson，*Abstract Algebra: Theory and Applications*，2026年版。[等价关系与等价类](https://github.com/twjudson/aata/blob/3069910e3ded72ff5e18837a97a0e810c92790e2/src/sets.xml)，定位 `sets-subsection-equivalence-relations`。用于核对等价关系与划分的定义，未据此认定已核验本书自然数对整数构造的全部内容。固定提交的根许可文件写GNU自由文档许可证1.3或以后版本，前言写1.2或以后版本；共同范围为1.3或以后版本，均无不变章节与封面文字。

**[INT-LEAN]** Jeremy Avigad、Leonardo de Moura等，Lean 4核心整数源码，[v4.24.0版本](https://github.com/leanprover/lean4/tree/v4.24.0/src/Init/Data/Int)，Apache 2.0许可。`Lemmas.lean` 的 `Int.neg_mul_neg` 等用于核对符号恒等式；`Order.lean` 中正、负、非负、非正因子的乘法比较定理用于核对严格与非严格条件。该版本采用自然数与负后继两类整数构造，不是自然数对商集的直接实现。

**[INT-MATHLIB]** Amelia Livingston、Alex J. Best、Yaël Dillies，mathlib的[幺半群局部化与群完备化](https://github.com/leanprover-community/mathlib4/tree/master/Mathlib/GroupTheory/MonoidLocalization)，Apache 2.0许可。以 `Basic.lean` 的 `liftOn`及其双输入版本 及消去条件下的代表元等价判据，核对定义与代表元无关的证明义务；以 `GrothendieckGroup.lean` 的 `of_injective` 核对嵌入所需的消去条件。它提供一般框架，本书整数乘法与序仍在正文独立证明。读取的是当日活动分支快照，精确内容由伴生记录的逐文件哈希标识，不声称核验了整个一致构建。

以上源码只作人工数学条件核对；本项目未运行相应Lean或mathlib形式证明，不宣称书稿经过形式化验证。完整定位、许可证据和内容哈希见伴生文件 `research/production/integers_sources_2026-10-27.json`；检索流水不收入教学正文。

"""


def divisibility_reference_addition():
    evidence = (ROOT / "research/production/divisibility_sources_2026-10-27.md").read_text()
    for identifier in ["DIV-JUDSON", "DIV-LEAN"]:
        if identifier not in evidence:
            raise ValueError("Divisibility source evidence changed: review curated citations")
    return """
## 带余除法、整除与最大公因数参考资料 {#divisibility-sources}

本批定义、证明、例题与习题独立撰写；以下公开资料用于核对条件和约定，不收入外部原题、答案、插图或连续段落。核验日期为2026年10月27日。

**[DIV-JUDSON]** Thomas W. Judson，*Abstract Algebra: Theory and Applications*，2026年版，[整数章](https://github.com/twjudson/aata/blob/3069910e3ded72ff5e18837a97a0e810c92790e2/src/integers.xml)。定位 `integers-theorem-division_algorithm`、`integers-theorem-gcd` 与 `integers-subsection-euclidean-algorithm`。前者直接陈述正除数的带余除法；整除定义允许零与负整数；所读最大公因数线性组合定理要求两个输入均非零，最大公因数定义采用正值。本书负除数及双零边界由正文另证，不能扩写成来源原陈述。根许可为GNU自由文档许可证1.3或以后版本，前言为1.2或以后版本；共同授权范围为1.3或以后版本，均无不变章节和封面文字要求。

**[DIV-LEAN]** Jeremy Avigad、Mario Carneiro、Kim Morrison、Markus Himmel、Leonardo de Moura等，Lean 4 [v4.24.0基础数据源码](https://github.com/leanprover/lean4/tree/v4.24.0/src/Init/Data)，Apache 2.0许可。`Int/DivMod` 中的非负余数约定与正、负除数唯一性分别核对余数范围和符号；`Bootstrap.lean` 的 `dvd_def`、`zero_dvd` 核对整除见证及零边界；`Int/Gcd.lean` 的 `gcd_eq_zero_iff`、`gcd_eq_iff` 核对非负最大公因数及双零情形；`Nat/Gcd.lean` 核对余数递降的终止论证。库为程序全函数另外规定零除数行为；本书带余除法仍排除零除数，余数判别整除也须保留这一前提。库的递归参数顺序与本书迭代状态不同，不能直接照抄索引。

本次仅核对公开源码的条件、约定与证明结构，未运行Lean编译或本书形式化证明，也不据库的实现宣称本书程序高效。完整定位、作者分工、许可证据与文件哈希见伴生文件 `research/production/divisibility_sources_2026-10-27.json`。

"""


def bezout_reference_addition():
    evidence = (ROOT / "research/production/bezout_sources_2026-10-27.md").read_text()
    for identifier in ["BEZ-JUDSON", "BEZ-LEAN", "BEZ-MATHLIB"]:
        if identifier not in evidence:
            raise ValueError("Bezout source evidence changed: review curated citations")
    return """
## 贝祖恒等式、扩展算法与互素参考资料 {#bezout-sources}

本批论证与题目独立撰写。以下仅核对公开资料的数学条件和证明结构，不收入外部题干、解答、图片或连续正文。核验日期为2026年10月27日。

**[BEZ-JUDSON]** Thomas W. Judson，*Abstract Algebra: Theory and Applications*，2026年版，[固定提交的整数章](https://github.com/twjudson/aata/blob/3069910e3ded72ff5e18837a97a0e810c92790e2/src/integers.xml)。`integers-theorem-gcd` 直接要求两输入均非零；`integers-corollary-coprime` 与欧几里得算法小节用于核对线性组合与回代思想。本书单零、双零与系数状态仍独立证明。根GNU自由文档许可证声明1.3或以后版本，前言声明1.2或以后版本；共同范围为1.3或以后版本，均无不变章节和封面文字要求。

**[BEZ-LEAN]** Mario Carneiro、Markus Himmel，Lean [v4.24.0整数最大公因数源码](https://github.com/leanprover/lean4/blob/v4.24.0/src/Init/Data/Int/Gcd.lean)，Apache 2.0许可。核对非负最大公因数、零输入和除去公因数后互素的条件；约去最大公因数必须要求它严格为正，不能用于双零输入。

**[BEZ-MATHLIB]** Sangwoo Jo、Guy Leroy、Johannes Hölzl、Mario Carneiro，mathlib [v4.24.0整数最大公因数源码](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Data/Int/GCD.lean)，Apache 2.0许可。`Nat.xgcdAux_P` 核对系数不变量，`Int.gcd_eq_gcd_ab` 核对全体整数的贝祖恒等式；互素消去定理提供不依赖素数分解的参照。库选取的贝祖系数可以与本书不同，不能据系数不同判错；`Int.gcd_dvd_iff` 的目标类型为自然数，本书任意整数目标须另证。正第二分量的互素整数对唯一性由正文独立推导，不冒称是本次读取的外部同名定理。

Judson教材与Lean/mathlib提供两个来源系列；后两者相互关联，不算三个完全独立来源。本次未运行Lean或mathlib编译、扩展算法或本书形式化证明。完整条件、定位、许可证据与逐文件哈希见 `research/production/bezout_sources_2026-10-27.json`。

"""


def rational_reference_addition():
    evidence = (ROOT / "research/production/rationals_sources_2026-10-27.md").read_text()
    for identifier in ["RAT-JUDSON", "RAT-LEAN", "RAT-MATHLIB"]:
        if identifier not in evidence:
            raise ValueError("Rational source evidence changed: review curated citations")
    return """
## 有理数构造与加法参考资料 {#rationals-sources}

本批定义、论证、例题和习题独立撰写。以下公开资料只用于核对条件及证明结构，不收入外部原题、解答、图像或连续正文。核验日期为2026年10月27日。

**[RAT-JUDSON]** Thomas W. Judson，*Abstract Algebra: Theory and Applications*，2026年版，[整域章的分式构造](https://github.com/twjudson/aata/blob/3069910e3ded72ff5e18837a97a0e810c92790e2/src/domains.xml)，定位 `domains-section-field-of-fractions`。核对交叉乘积等价关系、加法良定义、零元与整数嵌入。来源讨论一般整域及任意非零分母，本书独立特化为整数与正分母；来源未逐步展开的加法律仍由正文证明。根GNU自由文档许可证声明1.3或以后版本，前言为1.2或以后版本；共同范围为1.3或以后版本，均无不变章节和封面文字要求。

**[RAT-LEAN]** Mario Carneiro、Johannes Hölzl、Robin Arnez，Lean [v4.24.0有理数核心源码](https://github.com/leanprover/lean4/tree/v4.24.0/src/Init/Data/Rat)，Apache 2.0许可。`Rat` 存储互素正分母规范结构，并非直接存储等价类集合；`normalize_eq_iff` 与 `add_def` 核对规范表示、交叉乘积及加法公式的联系，`add_assoc` 等核对加法律。库有先约去分母公因子的实现，本书程序直接交叉相加后规范化，不宣称中间量相同。`mkRat` 对零分母的程序回退不能作为本书允许零分母的依据。

**[RAT-MATHLIB]** Johannes Hölzl、Mario Carneiro，mathlib [v4.24.0有理数定义源码](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Data/Rat/Defs.lean)，Apache 2.0许可。`intCast_injective`、`eq_iff_mul_eq_mul` 及零与相反数的规范分量用于核对嵌入和表示；类型中已有的非零分母证据不能代替本书原始关系的条件检查。

Judson与Lean/mathlib提供两个来源系列；Lean与mathlib相互依赖，不计为三个完全独立来源。本项目未运行相应源码编译或本书形式化证明。完整条件、定位、许可证据与哈希见 `research/production/rationals_sources_2026-10-27.json`。

"""


def rational_multiplication_reference_addition():
    evidence = (ROOT / "research/production/rationals_multiplication_sources_2026-10-27.md").read_text()
    for identifier in ["RMUL-JUDSON", "RMUL-LEAN"]:
        if identifier not in evidence:
            raise ValueError("Rational multiplication source evidence changed: review curated citations")
    return """
## 有理数乘法、倒数与除法参考资料 {#rationals-multiplication-sources}

本批定义、证明、例题和习题独立撰写。以下两个公开来源系列仅用于核对事实、条件与证明结构，不收入外部题干、答案、插图或连续段落。核验日期为2026年10月27日。

**[RMUL-JUDSON]** Thomas W. Judson，*Abstract Algebra: Theory and Applications*，2026年版，[固定提交的整域章](https://github.com/twjudson/aata/blob/3069910e3ded72ff5e18837a97a0e810c92790e2/src/domains.xml)，定位 `domains-section-field-of-fractions` 与 `domains-lemma-field-of-fractions`。核对乘法代表公式、单位、分配和非零分子的倒数。来源允许任意非零分母，本书固定正分母，负分子倒数需调整符号。来源把乘法良定义及交换、结合的详细核查留作练习，本书须独立展开。根GNU自由文档许可证为1.3或以后版本，前言为1.2或以后版本；共同授权范围为1.3或以后版本，均无不变章节和封面文字要求。

**[RMUL-LEAN]** Mario Carneiro、Johannes Hölzl、Robin Arnez，Lean [v4.24.0有理数核心源码](https://github.com/leanprover/lean4/tree/v4.24.0/src/Init/Data/Rat)，Apache 2.0许可。`mul_def`、`mul_assoc`、`add_mul` 与 `mul_add` 核对规范乘法及运算律；`mul_inv_cancel`、`inv_mul_cancel` 和 `div_mul_cancel` 核对非零条件下的逆元与除法。本书直接乘后规范化，库先做交叉约分；不宣称内部计算或复杂度相同。

**定义域与证明顺序。** Lean为程序总函数规定零的倒数为零，并据此规定零除数下的程序输出；本书不定义零的倒数或任何零除法，配套程序明确拒绝。所读 `mul_eq_zero` 证明先使用倒数，本书B1.16在倒数之前，独立从代表分子乘积及整数零积推出结论，不能倒置先修顺序。此处只核对公开源码，没有运行Lean编译或本书形式化证明。完整定位、条件、许可证据与内容哈希见 `research/production/rationals_multiplication_sources_2026-10-27.json`。

"""


def rational_order_reference_addition():
    evidence = (ROOT / "research/production/rationals_order_sources_2026-10-27.md").read_text()
    for identifier in ["RORD-LEBL", "RORD-LEAN"]:
        if identifier not in evidence:
            raise ValueError("Rational order source evidence changed: review curated citations")
    return """
## 有理数序、绝对值与距离参考资料 {#rationals-order-sources}

本批文字、论证、例题和图独立创作。以下两个公开来源系列用于核对条件及证明结构，不转载正文、题目或图像。核验日期为2026年10月27日。

**[RORD-LEBL]** Jiří Lebl，*Basic Analysis: Introduction to Real Analysis*，第一卷，第6.3版，[固定提交的实数章](https://github.com/jirilebl/ra/blob/e21ec524ca7d54f800c693b948020c188d21d01f/ch-real-nums.tex)与[度量章](https://github.com/jirilebl/ra/blob/e21ec524ca7d54f800c693b948020c188d21d01f/ch-metric.tex)。采用CC BY-NC-SA 4.0与CC BY-SA 4.0双重许可，公开授权不等于公有领域。核对有序域符号条件、绝对值的夹界证明、三角与反三角推导。来源的绝对值命题在实数上陈述，标准距离例也是实数值；本书在有理数内独立重证，距离值域取非负有理数，不偷用尚未构造的实数嵌入或完备性。来源将有理数有序域细节及部分负因子证明留给读者，不视为已展开的书稿证明。

**[RORD-LEAN]** Mario Carneiro、Johannes Hölzl、Robin Arnez，Lean [v4.24.0有理数源码](https://github.com/leanprover/lean4/tree/v4.24.0/src/Init/Data/Rat)，Apache 2.0许可。`lt_iff` 与 `le_iff` 核对正分母交叉比较，序与加法定理核对同加保序；正、非负乘数的比较定理核对零因子边界。严格乘积不等式本身可以排除零因子，不能误读为零因子保持严格序。所读除法比较为正除数版本，本书负除数情形独立证明；库的零倒数总函数约定不扩展本书的除法定义域。

Lean的规范结构不能替代本书换代表元的良定义证明；本次也未读取其有理数三角、反三角专门定理，相关推理以Lebl和本书独立有理数证明核对。本项目未运行Lean编译或本书形式化证明。完整条件、定位、许可证据和哈希见 `research/production/rationals_order_sources_2026-10-27.json`。

"""


def ratios_units_reference_addition():
    evidence = (ROOT / "research/production/ratios_units_sources_2026-10-27.md").read_text()
    for identifier in ["RU-PREALGEBRA", "RU-PHYSICS"]:
        if identifier not in evidence:
            raise ValueError("Ratios and units source evidence changed: review curated citations")
    return """
## 比例、量与单位参考资料 {#ratios-units-sources}

本批数学文字、例题、练习及插图独立创作；以下资料仅用于核对条件和精确换算约定，不搬入教材原文、表格、题目或图像。核验日期为2026年10月27日。两套教材作者与课程不同，但同属OpenStax出版体系，不能称为两个完全独立出版机构。

**[RU-PREALGEBRA]** Lynn Marecek、MaryAnne Anthony-Smith、Andrea Honeycutt Mathis，*Prealgebra 2e*，固定提交 `ad40c7e3c9a909cde81a24c526f52fe26a51fb14`。[比与率](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81303/index.cnxml)、[比例](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81311/index.cnxml)核对同单位比较、不同量类别的率及比例两个后项非零的条件；[测量单位](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81330/index.cnxml)核对米、厘米、千米与秒、分、时的精确关系。未把近似英美制数值或概括一年天数的说法作为精确常数。

**[RU-PHYSICS]** Samuel J. Ling、Jeff Sanny、William Moebs，*University Physics Volume 1*，固定提交 `2300d5b8ca2571dacc6ec25ebef56ba8d49000a2`。[单位与前缀](https://github.com/openstax/osbooks-university-physics-bundle/blob/2300d5b8ca2571dacc6ec25ebef56ba8d49000a2/modules/m58270/index.cnxml)、[换算方向](https://github.com/openstax/osbooks-university-physics-bundle/blob/2300d5b8ca2571dacc6ec25ebef56ba8d49000a2/modules/m58271/index.cnxml)核对长度、时间、率与乘性换算；[量纲](https://github.com/openstax/osbooks-university-physics-bundle/blob/2300d5b8ca2571dacc6ec25ebef56ba8d49000a2/modules/m58272/index.cnxml)用于检查物理一致性的必要条件。相同量纲不能保证相同量类别，也不能保证物理模型正确。

两套所核版本均采用CC BY-NC-SA 4.0，含非商业与相同方式共享限制，不是公有领域或无限制转载许可。本书的有理数模型、代数证明与教学表达独立完成。本次没有直接核验BIPM或NIST官方全文、最新国际单位制修订；辅助检索中的转码草案不作为本书规范依据。完整定位、许可证据、范围限制和文件哈希见 `research/production/ratios_units_sources_2026-10-27.json`。

"""


def functions_reference_addition():
    evidence = (ROOT / "research/production/functions_sources_2026-10-29.md").read_text()
    for identifier in ["FUN-JUDSON", "FUN-LEAN-MATHLIB"]:
        if identifier not in evidence:
            raise ValueError("Function source evidence changed: review curated citations")
    return """
## 函数定义、限制与复合参考资料 {#functions-sources}

本批定义说明、论证、例题和图独立创作；以下公开资料只用于核对条件及证明结构，不收入外部题目、解答、图片或连续正文。核验日期为2026年10月29日。

**[FUN-JUDSON]** Thomas W. Judson，*Abstract Algebra: Theory and Applications*，2026年版，[固定提交的集合章](https://github.com/twjudson/aata/blob/3069910e3ded72ff5e18837a97a0e810c92790e2/src/sets.xml)。定位 `sets-subsection-cartesian-products` 及其函数、复合与结合律段落。核对笛卡尔积、每输入唯一输出、像包含于目标集合，以及中间集合匹配的正式复合定义。来源把函数表述为特殊关系，没有直接采用本书的三数据对象；本书须自行明确域、目标和图共同决定函数。前导散文对像与目标的模糊用语不作为定义依据，空函数的分类也由本书证明。根GNU自由文档许可证为1.3或以后版本，前言为1.2或以后版本；共同范围为1.3或以后版本，均无不变章节和封面文本要求。

**[FUN-LEAN-MATHLIB]** Leonardo de Moura、Mario Carneiro、Jeremy Avigad、Johannes Hölzl等，Lean与mathlib的v4.24.0固定版本，Apache 2.0许可。[Lean函数基础](https://github.com/leanprover/lean4/blob/v4.24.0/src/Init/Prelude.lean)的恒等与复合、[函数定义](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Logic/Function/Defs.lean)、[限制](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Data/Set/Restrict.lean)及[像](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Data/Set/Image.lean)用于核对中间类型、目标不变、嵌套限制与复合像的条件。限制恒等得到子集的包含映射，不可忽略目标集合后直接视为子集恒等。类型化函数与本书集合三元组编码不同，相关源码不是本书集合构造的直接替代。

Lean与mathlib合为一个相关来源系列，与Judson教材形成两个来源系列。本项目未运行其编译或本书机器证明，也不据此宣称朴素集合背景、有序对的集合论构造已形式化完成。完整文件作者、定位、许可依据和内容哈希见 `research/production/functions_sources_2026-10-29.json`。

"""


def inverse_functions_reference_addition():
    evidence = (ROOT / "research/production/inverse_functions_sources_2026-10-29.md").read_text()
    for identifier in ["INV-JUDSON", "INV-LEAN-MATHLIB"]:
        if identifier not in evidence:
            raise ValueError("Inverse function source evidence changed: review curated citations")
    return """
## 单射、满射、双射与逆函数参考资料 {#inverse-functions-sources}

本批定义说明、证明、例题、练习及图独立编写。以下公开资料用于核对条件和证明结构，不收入外部题干、答案、图片或连续正文。核验日期为2026年10月29日。

**[INV-JUDSON]** Thomas W. Judson，*Abstract Algebra: Theory and Applications*，2026年版，[固定提交的集合章](https://github.com/twjudson/aata/blob/3069910e3ded72ff5e18837a97a0e810c92790e2/src/sets.xml)。单射、满射、双射定义，复合保性及可逆当且仅当双射的段落用于交叉核对；其中单射复合的证明留作练习，本书另给出完整推导。来源以特殊关系表述函数，本书仍须保留定义域、目标集合和图三个数据，并自行核查空集边界。根许可文件采用GNU自由文档许可证1.3或以后版本，前言写1.2或以后版本；共同范围为1.3或以后版本，均无不变章节及封面文本要求。

**[INV-LEAN-MATHLIB]** Lean与mathlib项目，v4.24.0固定版本，Apache 2.0许可。[函数基础](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Logic/Function/Basic.lean)核对双侧逆唯一性及可逆判据，[等价定义](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Logic/Equiv/Defs.lean)核对逆复合的反序，[集合像与原像](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Data/Set/Image.lean)核对原像的复合性质。来源使用类型化函数，与本书集合三数据约定不同。`surjInv` 使用 `Classical.choose`；本书只从双射的唯一原像构造逆函数，不把任意满射有右逆当作无需选择原则的已证结论。

Lean与mathlib属于同一个相关来源系列，与Judson形成两个来源系列；本项目未运行Lean编译，也未形式化本书的一般证明。精确定位、作者信息、许可依据、逐文件哈希及适用边界见伴生审计 `research/production/inverse_functions_sources_2026-10-29.json`。有限实现与验证见[附录十五](#finite-function-inverses-code)，有限测试不能替代正文证明。

"""


def linear_equations_reference_addition():
    evidence = (ROOT / "research/production/linear_equations_sources_2026-10-29.md").read_text()
    for identifier in ["LIN-OPENSTAX", "LIN-BEEZER"]:
        if identifier not in evidence:
            raise ValueError("Linear equation source evidence changed: review curated citations")
    return """
## 一次方程与方程组参考资料 {#linear-equations-sources}

本批文字、推导、题答及操作示意图独立编写。以下公开资料用于交叉核对定义、条件及证明结构，不收入第三方例题、题干、解答、插图或连续原文。核验日期为2026年10月29日。

**[LIN-OPENSTAX]** Lynn Marecek、MaryAnne Anthony-Smith、Andrea Honeycutt Mathis，*Elementary Algebra 2e*，固定提交 `ad40c7e3c9a909cde81a24c526f52fe26a51fb14`。[解与等式加减](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m82463/index.cnxml)、[乘除等式](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m82464/index.cnxml)、[恒等与矛盾](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m82467/index.cnxml)、[分母禁值](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m82538/index.cnxml)及[消元](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m82495/index.cnxml)用于核查原定义域、非零除数与特殊分支。来源乘法性质只保证正向保持，不能由此把乘零当作等价变形。本书自行证明同一允许范围内的双向解集包含。所核版本为CC BY-NC-SA 4.0，含非商业和相同方式共享条件，不是无限制转载许可。

**[LIN-BEEZER]** Robert A. Beezer，*A First Course in Linear Algebra*，3.50版，固定提交 `347f27fe909b54b26970bcc0fcbf69c7e853c766`。[方程组、等价系统与初等操作](https://github.com/rbeezer/fcla/blob/347f27fe909b54b26970bcc0fcbf69c7e853c766/src/section-SSLE.xml)中的SLE、ESYS、EO及EOPSS，给出交换、非零倍乘、保留另一式的倍加操作的双向证明。倍加的倍数可为零；它与整式倍乘必须非零的条件不同。所核版本采用GNU自由文档许可证1.2或以后版本，无不变章节与封面文本要求。

OpenStax的实数和图像叙述、Beezer的复数域及一般行最简形理论，不是本书当前已建立的先修。本批限于有理数上一元与二元两式系统，自行证明零系数、矛盾、唯一解和参数解的全部分支，不借来源省略这些证明。原式分母禁值仍须保留；有限求解代码不自动解析它们。完整定位、版权依据、适用边界及逐文件哈希见 `research/production/linear_equations_sources_2026-10-29.json`；代码与验证责任见[附录十六](#linear-equation-solvers-code)。

"""


def linear_inequalities_reference_addition():
    evidence = (ROOT / "research/production/linear_inequalities_sources_2026-10-29.md").read_text()
    for identifier in ["INEQ-OPENSTAX", "INEQ-MATHLIB"]:
        if identifier not in evidence:
            raise ValueError("Linear inequality source evidence changed: review curated citations")
    return """
## 一次不等式、区间与绝对值条件参考资料 {#linear-inequalities-sources}

本批文字、证明、题答及示意图独立编写。以下两个来源系列用于核对条件和边界，不复制来源的例题、题干、解答、表格、图或连续原文。来源实际访问时间、响应哈希及精确定位保留在2026年10月29日的伴生审计中。

**[INEQ-OPENSTAX]** Lynn Marecek、MaryAnne Anthony-Smith、Andrea Honeycutt Mathis，*Elementary Algebra 2e*；Lynn Marecek、Andrea Honeycutt Mathis，*Intermediate Algebra 2e*。固定提交 `ad40c7e3c9a909cde81a24c526f52fe26a51fb14` 的[解与端点](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m82470/index.cnxml)、[正负乘除条件](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81366/index.cnxml)、[且与或](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81367/index.cnxml)及[绝对值条件](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81426/index.cnxml)供交叉核对。当前版本为CC BY-NC-SA 4.0，含非商业和相同方式共享条件。绝对值资料局部写“总为正”，与其自身非负定义不一致；本书采用已证明的非负性，并单列零半径。来源实数数轴和只对正半径写出的公式，不能省去本书有理数上的独立证明与零、负半径分支。

**[INEQ-MATHLIB]** mathlib项目，v4.24.0，Apache 2.0许可。[正除数条件](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Order/GroupWithZero/Unbundled/Basic.lean)、[负除数条件](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Order/Field/Basic.lean)、[绝对值条件](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Order/Group/Unbundled/Abs.lean)与[泛型区间定义](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Order/Interval/Set/Defs.lean)用于核对比较方向、内侧的且、外侧的或及端点归属。库中零逆为零的约定不同于本书禁止除零的约定，只对照明确正、负除数的结论。部分绝对值声明由乘法版本转换生成；本项目未运行Lean，也未形式化本书证明。

本批区间均是有理数中的集合，正负无穷只作无界记号，不调用实数完备性或连续线段。正文以成员条件证明交并及解集等价；若允许范围另限为D，结果仍须限制在D中。完整作者、许可、条件差异和精确行号见 `research/production/linear_inequalities_sources_2026-10-29.json`；程序接口及验证责任见[附录十七](#rational-inequalities-code)。有限计算不能替代一般证明。

"""


def coordinates_affine_reference_addition():
    evidence = (ROOT / "research/production/coordinates_affine_sources_2026-10-29.md").read_text()
    for identifier in ["COORD-OPENSTAX", "COORD-MATHLIB"]:
        if identifier not in evidence:
            raise ValueError("Coordinate source evidence changed: review curated citations")
    return """
## 有理坐标与仿射函数参考资料 {#coordinates-affine-sources}

本批文字、证明、题答及图独立编写。两个公开来源系列用于核对定义、条件及教学边界，不复制题干、解答、连续原文、表格或图。来源的实际访问时间与响应哈希保留在2026年10月29日伴生审计中，正式化时间不冒充重新抓取时间。

**[COORD-OPENSTAX]** Lynn Marecek、Andrea Honeycutt Mathis，*Intermediate Algebra 2e*，固定提交 `ad40c7e3c9a909cde81a24c526f52fe26a51fb14`。[有序对、坐标轴与截点](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81369/index.cnxml)、[斜率与斜截式](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81370/index.cnxml)、[关系与函数](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81373/index.cnxml)及[图像与函数性](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81374/index.cnxml)用于对照。当前版本为CC BY-NC-SA 4.0，含非商业和相同方式共享条件；来源图片有例外说明，本批不使用它们。来源的通常实平面与连点作图步骤不直接作为本书有理坐标集合的证明。两点斜率须先排除横坐标相同；同斜率还须区分截距相同的重合与截距不同的不交，不能一概称为平行。

**[COORD-MATHLIB]** mathlib项目，v4.24.0，Apache 2.0许可。[集合积与函数图](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Data/Set/Prod.lean)、[图的逆向存在](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Data/Set/Function.lean)及[正因子严格保序](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Order/GroupWithZero/Unbundled/Basic.lean)用于核查成员条件、空域、投影与正斜率条件。库中逆向存在证明有非空类型前提并用选择作全域延拓；本书直接按声明域和目标集合验证存在唯一，不借用任意延拓。正倍乘源码不能代替本书负斜率及零斜率分支证明。本项目未运行Lean，也未形式化本书。

本批以有理数对为点，图为满足公式的全部有理数对；有限点样本不决定无限定义域上的函数。目标集合仍是函数数据的一部分，竖线至多交一点不保证每个声明输入都有输出。精确行号、逐文件作者、许可与适用边界见 `research/production/coordinates_affine_sources_2026-10-29.json`；有限实现与验证责任见[附录十八](#rational-affine-code)。

"""


def powers_sums_reference_addition():
    evidence = (ROOT / "research/production/powers_sums_sources_2026-10-29.md").read_text()
    for identifier in ["POWSUM-OPENSTAX", "POWSUM-MATHLIB"]:
        if identifier not in evidence:
            raise ValueError("Powers and sums source evidence changed: review curated citations")
    return """
## 非负整数幂与有限和参考资料 {#powers-sums-sources}

本批文字、归纳证明、题答及有限记录图独立编写。以下两个来源系列用于交叉核对条件，不复制第三方题目、解答、表格、图、连续原文或程序实现。实际访问时间、响应哈希及许可依据保留在2026年10月29日的伴生审计中。

**[POWSUM-OPENSTAX]** Lynn Marecek、Andrea Honeycutt Mathis，*Intermediate Algebra 2e*，固定提交 `ad40c7e3c9a909cde81a24c526f52fe26a51fb14`。[指数记号与运算性质](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81384/index.cnxml)核对重复乘法、同底乘积、幂的幂与乘积幂。当前版本为CC BY-NC-SA 4.0，含非商业和相同方式共享条件；本批不使用来源图片。来源零指数条款只限非零底数，不能据此推出本书的零底数零次幂。本书从离散递归统一定义所有有理底数的零次值为一，明确含零底数；此约定不允许除零，也不是极限规则。来源更广的整数指数语境不纳入本批。

**[POWSUM-MATHLIB]** mathlib项目，v4.24.0，Apache 2.0许可。[自然数幂定义与归纳性质](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Group/Defs.lean)、[可交换乘法中的乘积幂](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Group/Basic.lean)、[有限运算与空范围](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/BigOperators/Group/Finset/Defs.lean)、[前缀后继与拼接](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/BigOperators/Group/Finset/Basic.lean)和[常数乘有限和](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/BigOperators/Ring/Finset.lean)用于核查前提。自然数幂零次值不要求底数非零；乘积幂须有乘法交换性。库中有限集合求和预设可交换加法，本书先定义有序前缀和并独立归纳证明所用性质。部分空和与拼接声明从乘法版本生成；本项目只读源码，未运行Lean编译，未形式化书稿。

本批指数仅为非负整数；前n项和只含索引零至n−1，空和为零。有限表的前缀一致性、拼接及零尾稳定性不授权无限求和或任意多重重排。完整作者、精确行号与条件差异见 `research/production/powers_sums_sources_2026-10-29.json`；有限实现与验证责任见[附录十九](#rational-powers-sums-code)。审计保留的后续多项式预读记录不表示本批已有相应正文或证明。

"""


def polynomial_basic_reference_addition():
    evidence = (ROOT / "research/production/polynomial_basic_sources_2026-10-29.md").read_text()
    for identifier in ["POLY-OPENSTAX", "POLY-MATHLIB"]:
        if identifier not in evidence:
            raise ValueError("Polynomial source evidence changed: review curated citations")
    return """
## 多项式系数记录与线性运算参考资料 {#poly-basic-sources}

本批正文、题答、证明与记录图独立编写。以下来源用于核对术语和条件，不复制第三方题目、解答、图像或程序实现。

**[POLY-OPENSTAX]** Lynn Marecek、Andrea Honeycutt Mathis，*Intermediate Algebra 2e*，固定提交 `ad40c7e3c9a909cde81a24c526f52fe26a51fb14`。[多项式、次数及加减](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81383/index.cnxml)、[分配律中的常数倍](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81385/index.cnxml)用于核对同指标系数运算。当前版本为CC BY-NC-SA 4.0，含非商业和相同方式共享条件。来源笼统的常数次数措辞不覆盖本书零对象：本书只定义非零多项式次数。求值中的零次幂沿用B2.11的离散约定，包含零底数，不能由来源仅限非零底数的零指数条款扩大推出。

**[POLY-MATHLIB]** mathlib项目，v4.24.0，Apache 2.0许可。[形式多项式及系数相等判据](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Basic.lean)、[逐系数加法与数乘](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Coeff.lean)、[次数约定](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Degree/Definitions.lean)及[求值](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Eval/Defs.lean)用于交叉核查。库用有限支持结构，本书采用非空有限系数记录的唯一规范代表；未把库的半环、模或多项式乘法作为已写先修。库中零对象的degree为底元素、natDegree为零，本书则不定义零次数，三者不可混用。只读源码核对，未运行Lean或形式化本书。

B2.13先证明系数相等推出所有有理输入处求值相等，当时未使用反向识别；后续[因式定理与恒等识别](#polyroot-unit)才证明标准有理求值函数相等可识别形式系数，并给出带共同系数上界的有限点判等条件。没有共同系数上界的任意有限采样仍不能代替一般系数判据。表示无关、规范唯一与求值兼容由正文独立证明，B2.13—B2.14没有多项式乘法或根数定理；乘法接在后续B2.15—B2.16建立。逐请求原访问时间、哈希、作者及条件差异保留于伴生来源审计：目录 `research/production/`，文件 `polynomial_basic_sources_2026-10-29.json`。精确程序见[附录二十](#rational-polynomial-basic-code)。

"""


def rational_polynomial_basic_appendix():
    text = r"""

# 附录二十 多项式系数记录与线性运算的精确计算 {#rational-polynomial-basic-code}

本附录对应[多项式记录](#polyrec-unit)与[加法和数乘](#polyops-unit)，完整列出 `tools/rational_polynomial_basic.py`。数值采用Python标准库 `fractions.Fraction`；输入检查复用[附录十六](#linear-equation-solvers-code)的 `rational`，索引检查、自然数幂与有限和复用[附录十九](#rational-powers-sums-code)的 `natural_index`、`power` 与 `finite_sum`，这些依赖的完整源码已列在对应附录。

**记录与规范化。** `record(values)` 只接受非空列表或元组，逐项检查精确整数或 `Fraction`，拒绝布尔值、浮点数及其他非数值项。长度为 $n\ge1$ 的输入 $A=(a_0,\ldots,a_{n-1})$ 对应补零系数

$$
c_A(i)=\begin{cases}a_i,&i<n,\\0,&i\ge n.\end{cases}
$$

`coefficient(values,index)` 返回 $c_A(i)$，索引必须为非负精确整数；即使值为整数的 `Fraction` 也不充当索引。`normalize(values)` 将全零记录化为 $(0)$；否则只删最后非零项之后的尾零，保留开头和中间的零。它返回非空的精确有理数元组，不把空记录当作零。`same_polynomial(left,right)` 返回布尔值，判断两记录规范化后是否相同；正文证明这恰等价于全部补零系数相同。

**次数与求值。** `degree(values)` 对非零记录返回最后非零指标，非零常数次数为零；零记录抛出 `ValueError`，不把零次数记成零或其他数。`evaluate(values,at)` 对有理输入 $t$ 计算

$$
E_A(t)=\sum_{i=0}^{n-1}a_i t^i.
$$

每个幂均为已定义的自然数幂，特别是 $0^0=1$，故零输入正确读取常数项。返回值为精确有理数；输入点也拒绝浮点数和布尔值。尾零不改变求值，但删中间零可能改变求值。多项式对象与它产生的求值函数仍须区分；有限取值判等须满足B2.18所证的共同系数上界和足够多个互异输入条件，不能任取少量样本即判等。

**加法、缩放与差。** `add(left,right)` 将两条非空记录补到共同正长度，逐系数相加后规范化；`scale(scalar,values)` 逐项乘有理标量后规范化；`subtract(left,right)` 加上右记录的负一倍。设 $P,Q$ 分别为输入记录规范化所得的多项式；返回记录分别表示 $P+Q$、$\lambda P$ 与 $P-Q$，对每个自然数指标 $i$ 都有

$$
c_{P+Q}(i)=c_P(i)+c_Q(i),\qquad
c_{\lambda P}(i)=\lambda c_P(i),\qquad
c_{P-Q}(i)=c_P(i)-c_Q(i).
$$

零标量或全抵消返回 $(0)$，不求它的次数。最高项抵消后可以降次，也可以得到零，必须分开判断。非零标量与非零记录的次数保持，依赖有理数非零乘积仍非零的事实。输入的所有项先检查，即使缩放标量为零，也不忽略非法系数；各接口不修改输入列表。本模块没有多项式乘法、负指数、无限记录或从函数采样反推系数的接口。

独立检查程序为 `tools/validate_rational_polynomial_basic.py`。

报告目录为 `research/production/`。

报告文件名为 `rational_polynomial_basic_validation.json`。

报告绑定本模块、检查程序、幂与有限和模块及方程输入检查模块四份源码。外部检查采用SymPy有理系数多项式；主验收另以稀疏非零系数字典和Horner代入重算规范化、系数、求值及线性运算，核对零次数拒绝、尾零边界、非法输入和具体例子。Horner只用于独立程序核查，不增加正文先修或替代一般证明。以下完整源码使用已有幂与有限和接口实现求值；所有这些有限检查都不是任意长度或全部有理输入上的形式证明。

```python
"""
    return text + (ROOT / "tools/rational_polynomial_basic.py").read_text() + "\n```\n"


def polynomial_product_reference_addition():
    evidence = (ROOT / "research/production/polynomial_product_sources_2026-10-29.md").read_text()
    for identifier in ["coeff_mul", "eval_mul", "degree_mul", "ad40c7e3c9a909cde81a24c526f52fe26a51fb14"]:
        if identifier not in evidence:
            raise ValueError("Polynomial product source evidence changed: review curated citations")
    return """
## 多项式乘法、求值与次数参考资料 {#poly-product-sources}

本批正文、题答、证明、计算模块和系数贡献图独立编写。以下来源只用于核对术语和适用条件，不复制外部题目、解答、图像或实现。

**[POLY-PRODUCT-OPENSTAX]** Lynn Marecek、Andrea Honeycutt Mathis，*Intermediate Algebra 2e*，固定提交 `ad40c7e3c9a909cde81a24c526f52fe26a51fb14`。[多项式乘法](https://github.com/openstax/osbooks-prealgebra-bundle/blob/ad40c7e3c9a909cde81a24c526f52fe26a51fb14/modules/m81385/index.cnxml)用于核对分配、同类项及二项式方法的适用范围。当前版本为CC BY-NC-SA 4.0，含非商业与相同方式共享条件。来源从表达式运算入手，本书则须先定义规范系数对象上的乘法，并证明表示无关；二项式的FOIL口诀不能当作任意长度记录的通法。

**[POLY-PRODUCT-MATHLIB]** mathlib项目，v4.24.0，Apache 2.0许可。[多项式结构与乘法](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Basic.lean)、[乘积系数](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Coeff.lean)、[求值保乘](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Eval/Defs.lean)及[乘积次数](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Degree/Operations.lean)用于交叉核查。库已具备半环和有限支持代数，不能把这些结构或任意有限换序当作本书的已证先修。本书按常数项与移位分解证明结合及求值保乘。求值目标为有理数，包含零输入，其零次幂沿用离散约定；B2.15—B2.16的乘法证明不从求值相同反推系数相等。次数相加只在两个因子非零并已证明积非零后使用；库的底元素次数及零的natDegree约定不能直接替代本书零次数未定义的约定。

逐条源码定位、署名、原访问记录与哈希保留于伴生审计：目录 `research/production/`，文件 `polynomial_product_sources_2026-10-29.json`。只读源码核对，未编译Lean或形式化书稿；有限计算不替代全指标证明。B2.15—B2.16自身不涉及多项式除法、根数上界、因式定理或插值；后续B2.17—B2.18再建立一次除式商余、因式定理与不同有理根数界，一般多项式长除法和插值仍未建立。完整精确程序见[附录二十一](#rational-polynomial-product-code)。

"""


def rational_polynomial_product_appendix():
    text = r"""

# 附录二十一 多项式乘法的精确计算 {#rational-polynomial-product-code}

本附录对应[移位与乘法](#polymul-unit)及[结合、求值与次数](#polyprod-unit)，完整列出 `tools/rational_polynomial_product.py`。本模块只有 `shift(values)` 和 `multiply(left,right)` 两个新接口；输入检查与规范化复用[附录二十](#rational-polynomial-basic-code)的 `record` 和 `normalize`，其余传递依赖的完整源码见附录十六、十九。

**输入与输出。** 每个系数记录必须是非空列表或元组，系数必须为精确整数或 `Fraction`；拒绝布尔值、浮点数、空记录及其他不合法类型。即使另一个因子是零，也先检查两份完整输入，不跳过非法系数。两接口均返回由精确有理数组成的非空规范元组，不修改输入列表；只删尾零，不删开头或中间的零。

**单步移位。** `shift` 在原记录最前面接一个零，再规范化。若原记录有 $n\ge1$ 项，候选有 $n+1$ 项，故仍非空。对全部自然指标 $j$，

$$
c_{S(P)}(0)=0,\qquad c_{S(P)}(j+1)=c_P(j).
$$

全零记录的移位仍规范为 $(0)$。本模块不新增任意多步移位或多项式幂接口。

**乘法候选与规范化。** 两份输入分别有 $n,m\ge1$ 项。`multiply` 明确建立长度 $n+m\ge2$ 的全零候选表，然后将每个输入对的乘积 $a_i b_j$ 加入指标 $i+j$。这里 $i<n$ 且 $j<m$，因此 $i+j<n+m$，所有写入均在候选表内。故意保留一个最终零位置，不要求先以 $n+m-1$ 定义候选长度；最后交由 `normalize` 得到唯一规范代表。正文证明其全部补零系数满足

$$
c_{P\star Q}(k)=\sum_{i=0}^{k}c_P(i)c_Q(k-i).
$$

求和中 $i\le k$，自然差 $k-i$ 有定义。界外的系数由补零规则解释，不读取原记录之外的项；不同尾零表示形成同一个规范结果。模块以逐对累加实现有限卷积，正文的表示无关与运算规律仍须由全指标论证建立，不能用几个求值样本替代。

求值和次数继续调用附录二十的接口，本模块没有另定义零次数。正文先分零因子，再在两个因子非零时证明积非零，才使用

$$
\deg(P\star Q)=\deg P+\deg Q.
$$

输入有零因子时返回 $(0)$，不得对其调用已规定拒绝零输入的 `degree`。有理输入处求值满足 $E_{P\star Q}(t)=E_P(t)E_Q(t)$，包括 $t=0$；这是正文已证性质及有限程序检查的对象，不是从函数反向定义形式乘积。

独立检查程序为 `tools/validate_rational_polynomial_product.py`。

报告目录为 `research/production/`。

报告文件名为 `rational_polynomial_product_validation.json`。

报告绑定乘法模块、检查程序、基本多项式模块、幂与有限和模块、方程输入检查模块五份源码。外部检查使用SymPy有理系数多项式；主验收另用常数项加移位的递归算法重算乘积，并用Horner代入独立核对求值，核对尾零、零因子、次数条件、非法输入及具体例子。该递归核查不复制下面的双循环卷积，也不借用SymPy结果。所有枚举都只有有限范围，不是任意长度和全部有理系数的形式证明。

```python
"""
    return text + (ROOT / "tools/rational_polynomial_product.py").read_text() + "\n```\n"


def polynomial_linear_division_reference_addition():
    evidence = (ROOT / "research/production/polynomial_linear_division_sources_2026-10-29.md").read_text()
    for identifier in ["463991614337632b0e02cbb6c76223cbb0d423d3", "div_modByMonic_unique", "eq_of_infinite_eval_eq"]:
        if identifier not in evidence:
            raise ValueError("Linear polynomial division source evidence changed: review curated citations")
    return """
## 一次除式、不同有理根与恒等识别参考资料 {#poly-linear-division-sources}

本批正文、例题、题答、证明与计算模块独立编写。以下来源核对术语、算法范围及定理条件，不复制第三方段落、题目、图像或程序实现。

**[POLY-DIV-OPENSTAX]** Jay Abramson等，*College Algebra 2e*。

固定提交：

`463991614337632b0e02cbb6c76223cbb0d423d3`。

[多项式除法与综合除法](https://github.com/openstax/osbooks-college-algebra-bundle/blob/463991614337632b0e02cbb6c76223cbb0d423d3/modules/m51277/index.cnxml)、[余式与因式定理](https://github.com/openstax/osbooks-college-algebra-bundle/blob/463991614337632b0e02cbb6c76223cbb0d423d3/modules/m51278/index.cnxml)用于教学对照。当前版本为CC BY-NC-SA 4.0，含非商业和相同方式共享条件。本书只构造有理参数对应的一次首一除式商余，独立覆盖零及常量被除式；未借来源扩展为一般多项式长除法。来源相邻的复数根和重数陈述不能移作“每个有理系数多项式都有足够的不同有理根”。

**[POLY-DIV-MATHLIB]** mathlib项目，v4.24.0，Apache 2.0许可。[首一除法、线性余式及唯一性](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Div.lean)、[根与求值识别](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Roots.lean)及[零次数约定](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/Polynomial/Degree/Definitions.lean)用于条件交叉核查。库已具备一般环、首一除法、根多重集及有限集合基数工具；本书以正长度记录归纳构造商余，再用互异有理列表证明根数界，不将库结构当作未写先修。库的零多项式根多重集设为空，不表示零多项式在有理输入处没有根；本书零多项式处处取零且次数不定义。根数界只用于非零对象，有限点判等需要共同系数上界及足够多个互异输入；标准函数识别明确在有理数域上，不外推到有限系数域。

原访问记录、固定源码位置、作者、许可及哈希见伴生审计：目录 `research/production/`，文件 `polynomial_linear_division_sources_2026-10-29.json`。只读源码核对，未运行Lean或形式化书稿。一般长除法、根重数、插值、任意多项式分解和其他数系的根存在性均不在本批范围；有限程序实例不证明一般根数定理。一次除式精确程序见[附录二十二](#rational-polynomial-linear-division-code)。

"""


def rational_polynomial_linear_division_appendix():
    text = r"""

# 附录二十二 一次除式商余的精确计算 {#rational-polynomial-linear-division-code}

本附录完整列出 `tools/rational_polynomial_linear_division.py`，对应[一次除式商余](#polydiv-unit)的构造与算法。[因式定理与恒等识别](#polyroot-unit)在正文另给一般证明；本模块不提供根枚举或有限样本判等接口。输入检查复用[附录十六](#linear-equation-solvers-code)的 `rational`，记录和加法复用[附录二十](#rational-polynomial-basic-code)的 `record`、`add`，移位复用[附录二十一](#rational-polynomial-product-code)的 `shift`；其余传递依赖的完整源码亦已列出。

**接口与范围。** `divide_linear(values,at)` 接受非空的升序系数列表或元组，以及有理参数 $a$。系数和参数仅接受精确整数或 `Fraction`，拒绝布尔值、浮点数、空记录、迭代器及其他非法类型。除式固定为

$$
D_a=X-C(a)=(-a,1).
$$

因其一次系数为一，所有有理 $a$ 都给非零一次除式，特别允许 $a=0$。这里没有除以数值 $a$ 的步骤，也不接受任意除数多项式作为第二参数。

返回值是二元组 `(quotient,remainder)`：第一项为非空的精确有理数规范系数元组 $Q$，第二项为精确有理数 $r$。余数是数值，恒等式中的余项则是常量多项式 $C(r)$，二者分清：

$$
P=D_a\star Q+C(r),\qquad r=E_P(a).
$$

**有限状态更新。** 输入写成 $(p_0,\ldots,p_d)$，其中 $d$ 仅指原记录最后指标，不能未经规范化就称为次数。沿用正文的步骤指标，程序初始 $Q_0=(0)$、$r_0=p_d$。当 $j<d$ 时，有 $j+1\le d$，下一读取指标 $d-(j+1)$ 合法；先用旧余数更新商，再更新余数：

$$
Q_{j+1}=S(Q_j)+C(r_j).
$$

$$
r_{j+1}=p_{d-(j+1)}+a r_j.
$$

对每个 $0\le j\le d$，已处理后缀满足正文所证不变式

$$
N(p_{d-j},\ldots,p_d)=D_a\star Q_j+C(r_j).
$$

最后输出 $(Q_d,r_d)$。

循环恰处理原记录除末项外的有限项；$d=0$ 时不进入循环，返回零商和该常量值。首部与中间零照常处理，尾零表示也可直接输入；输入记录不被修改，输出商经已有移位和加法接口保持规范。全零记录得到 $(Q,r)=((0),0)$。若 $P$ 非零且 $\deg P=e\ge1$，正文先证明商非零，再得到 $\deg Q=e-1$；常量及零输入不使用零商的未定义次数。

独立检查程序目录为 `tools/`，文件名为 `validate_rational_polynomial_linear_division.py`。

报告目录为 `research/production/`。

报告文件名为 `rational_polynomial_linear_division_validation.json`。

报告绑定本模块、检查程序、乘法模块、基本多项式模块、幂与有限和模块、方程输入检查模块六份源码。外部检查用SymPy在有理系数域除以一次多项式；主验收另按原系数的显式幂加权有限和重算每个商系数和余数，并逐系数核对乘回结果，检查所有所列非空后缀、尾零表示、非法输入与例子。该独立诊断不复刻下面的倒序状态循环，也不从测试推断任意输入上的唯一性、终止性或根数定理。

```python
"""
    return text + (ROOT / "tools/rational_polynomial_linear_division.py").read_text() + "\n```\n"


def rational_quadratic_reference_addition():
    evidence = (ROOT / "research/production/rational_quadratic_sources_2026-10-29.md").read_text()
    for identifier in ["463991614337632b0e02cbb6c76223cbb0d423d3", "Rat.isSquare_iff", "quadratic_eq_zero_iff"]:
        if identifier not in evidence:
            raise ValueError("Rational quadratic source evidence changed: review curated citations")
    return r"""
## 有理平方、配方与二次方程参考资料 {#rational-quadratic-sources}

本批正文、题答、证明、图示与计算模块独立编写。以下来源只核对术语、条件和范围，不复制第三方题目、段落、图像或程序实现。

**[QUAD-OPENSTAX]** Jay Abramson等，*College Algebra 2e*。

固定提交：

`463991614337632b0e02cbb6c76223cbb0d423d3`。

[二次方程、配方及判别式](https://github.com/openstax/osbooks-college-algebra-bundle/blob/463991614337632b0e02cbb6c76223cbb0d423d3/modules/m51256/index.cnxml)用于教学对照。当前版本采用CC BY-NC-SA 4.0，含非商业和相同方式共享条件。来源使用实数及已具备的复数背景，其判别式表的有理性分类还需要补明有理系数条件。本书始终限定参数与未知量为有理数：正判别式只有在它是有理数的平方时才给两个有理解，正而非有理平方时仍无有理解；不借用表格断言其他数系的根存在。零二次系数先按一次、常量或恒零方程处理。

**[QUAD-MATHLIB]** mathlib项目，v4.24.0，Apache 2.0许可。[有理规范分子分母与平方判据](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Data/Rat/Lemmas.lean)、[有理平方根计算约定](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Data/Rat/Sqrt.lean)、[判别式与同域平方条件](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/Mathlib/Algebra/QuadraticDiscriminant.lean)用于条件交叉核对。平方判据必须用于正分母、互素的规范记录；本书直接使用已证互素乘积与规范代表唯一性，不新增素因子分解先修。库的 `Rat.sqrt` 是全域计算函数，是否为真平方根还要检查平方等于原数；本书 $\operatorname{sqrt}_{\mathbb Q}$ 只在确有非负有理平方根的集合上定义，不能把两种接口混同。二次公式要求非零二次系数、二非零及同一域内的平方见证；有理定义域上的二次式界直接由配方和平方非负推出，不引用极限或完备性。

原始访问记录、固定源码位置、作者、许可及哈希见伴生审计。目录为 `research/production/`。

文件为 `rational_quadratic_sources_2026-10-29.json`。

只读核对源码，未编译Lean或形式化书稿。完整精确程序与平方界证明见[附录二十三](#rational-quadratics-code)；有限实例不替代一般证明。

"""


def rational_quadratics_appendix():
    text = r"""

# 附录二十三 有理平方与二次方程的精确计算 {#rational-quadratics-code}

本附录完整列出目录 `tools/` 中的 `rational_quadratics.py`。输入检查复用[附录十六](#linear-equation-solvers-code)的 `rational`。正文[SQ1—SQ4](#sqrat-unit)和[配方与解集分类](#quad-unit)先给一般证明；下述平方界算法补足实现的终止性与正确性。

**接口。** `integer_sqrt` 仅接受非负的精确整数，拒绝布尔值及其他类型；返回精确整数平方界。`rational_square_root` 与 `solve_quadratic` 的每个输入仅接受整数或 `Fraction`，拒绝布尔值、浮点数及其他类型。前者返回非负的精确有理平方根，合法输入没有有理平方根时返回 `None`；非法类型抛出异常。后者返回字典：`kind` 为 `all` 表示全体有理数，为 `none` 表示空集，为 `finite` 时还含 `roots`，它是按有理次序递增、去重的非空精确有理元组。

**整数平方界的存在与唯一性。** 给定整数 $n\ge0$，目标为非负整数 $s$ 满足

$$
s^2\le n<(s+1)^2.
$$

初始下端 $\ell=0$、上端 $h=n+1$。因为 $h\ge1$，有 $h^2\ge h>n$，故不变式为

$$
0\le\ell<h,\qquad \ell^2\le n<h^2.
$$

只在 $h-\ell>1$ 时更新。令 $m$ 为 $\ell+h$ 除以正整数二的商；带余除法给出

$$
\ell+h=2m+r,\qquad r\in\{0,1\}.
$$

这时 $h\ge\ell+2$。若 $m\le\ell$，则 $\ell+h\le2\ell+1$，与 $\ell+h\ge2\ell+2$ 矛盾；若 $m\ge h$，则 $\ell+h\ge2h$，与 $\ell<h$ 矛盾。因此 $\ell<m<h$，新端点严格在两端之间。

当 $m^2\le n$ 时，把下端改为 $m$，保留上端；否则由整数全序有 $n<m^2$，把上端改为 $m$，保留下端。两个分支都保持不变式。新差分别为 $h-m$ 或 $m-\ell$，仍是正整数且严格小于旧差 $h-\ell$，因而至多为旧差减一。

初始差为 $n+1$。若执行了 $j$ 次更新，归纳可得当前差至多为 $n+1-j$；这里仅在 $j\le n+1$ 时书写该自然差。若能执行 $n+1$ 次，正差便至多为零，矛盾。因此至多执行 $n$ 次即停止；$n=0$ 时初始差一，不更新。这给出有限的显式终止上界。

停止时正差不大于一，故 $h=\ell+1$；不变式给出所需平方界，返回 $s=\ell$。若另一非负整数 $u$ 也满足同样界，且 $u>s$，则离散次序给出 $u\ge s+1$。由非负整数乘法保序，$u^2\ge(s+1)^2>n$，与 $u^2\le n$ 矛盾；$u<s$ 时交换两者同样矛盾。因此输出唯一。这里平方保序来自已建立的乘法次序，也可用正文的平方差法。

**从整数界到有理平方。** 类型检查后，输入由 `Fraction` 规范化。负输入不是有理平方；非负输入写为互素规范记录 $p/q$，其中 $p\ge0$、$q\ge1$。分别计算平方界 $m,v$：

$$
m^2\le p<(m+1)^2,\qquad v^2\le q<(v+1)^2.
$$

由 $q\ge1$ 可知 $v\ne0$，否则后一严格不等式给出 $q<1$。当 $m^2=p$ 且 $v^2=q$，非负有理数 $m/v$ 的平方恰为输入。若任一等式不成立，相应整数不存在非负整数平方根：任何这样的根也满足平方界，唯一性迫使它等于 $m$ 或 $v$，与等式不成立矛盾。因此由正文SQ4排除有理平方根，返回 `None`。零输入的规范记录为 $(0,1)$，返回精确有理数零。

**全参数解集。** 程序先验证全部 $a,b,c$ 为精确有理数。若 $a=0$，仅按一次方程分支：$b\ne0$ 时唯一根为 $-c/b$；$b=c=0$ 时为全体有理数；$b=0,c\ne0$ 时为空集。这个分支不形成除以 $2a$ 的表达式。

若 $a\ne0$，计算 $\Delta=b^2-4ac$。正文配方给出

$$
ax^2+bx+c=0\quad\Longleftrightarrow\quad(2ax+b)^2=\Delta.
$$

若 $\Delta$ 没有非负有理平方根，正文平方存在判据及QC2、QC3给出空的有理解集。若存在 $s\ge0$ 且 $s^2=\Delta$，因 $2a\ne0$，全部有理解恰为

$$
\left\{\frac{-b-s}{2a},\frac{-b+s}{2a}\right\}.
$$

$s=0$ 时集合去重为一项；$s>0$ 时两项之差为 $s/a\ne0$，所以有两项。排序只改变表示顺序，不预设 $a$ 的正负。所有结论和返回值都在有理数域，不将“没有有理解”改称其他数系中的存在结论。

独立检查程序位于目录 `tools/`，文件为 `validate_rational_quadratics.py`；报告位于目录 `research/production/`，文件为 `rational_quadratics_validation.json`。报告绑定本模块、检查程序及输入检查模块三份源码。有限检查以Python整数平方界和SymPy有理根为外部参照；主验收另执行整数平方界、规范分子分母检查、全部所列系数三元组的有理根核对、非法输入及八个例子。上述全称证明不依赖有限测试。

```python
"""
    return text + (ROOT / "tools/rational_quadratics.py").read_text() + "\n```\n"


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

**依赖与入口。** 完整函数复用绘图脚本头已经导入的 `plt`、`FontProperties`、`Text`：分别来自 `matplotlib.pyplot`、`matplotlib.font_manager`、`matplotlib.text`。该脚本使用Matplotlib的Agg后端，并采用指定的Noto中文字体；数学样本在图形渲染前以精确分数计算，字体与布局仅影响显示。脚本头还用 `from fractions import Fraction as F` 导入精确分数类型；参数 `out` 是已经存在的输出目录路径。构建入口执行绘图脚本的 `main()`，它建立 `dist/figures` 后调用本函数，并生成 `b2_rational_gap.png`。

下面列出完整函数；其中断言是固定样本的诊断，不作为外部输入校验接口或全称证明。

```python
"""
    return (text + "from fractions import Fraction as F\n\n" + rational_gap_figure_source() + "\n```\n\n"
            "在脚本的 `main()` 已建立输出目录 `out` 后，入口调用为：\n\n"
            "```python\ndraw_rational_gap(out)\n```\n")


def compose_body():
    opening = (CHAPTER / "part_opening.md").read_text()
    notice = ("**本批范围。** 本稿包含第一部分开篇、第1章补强稿，以及四十三个基础桥接单元。"
              "B1.1—B1.19归入第7部分第26章；B1.20—B1.21归入第63部分第526章的数学教育主题。"
              "B2.1—B2.4归入同部分第529章的函数教学桥接。"
              "B2.5—B2.8归入同部分第528章的方程与不等式教学桥接。"
              "B2.9—B2.10在这些先修之后续写第529章的有理坐标与仿射函数图像教学。"
              "B2.11—B2.20随后续写第528章的有理数幂、有限和、多项式系数记录、运算、一次除式商余、有理根与恒等识别、有理平方及二次方程。"
              "B2.21—B2.22再续写第526章97F50的有理数缺口、戴德金分割次序及非空有上界分割族的上确界。"
              "第26章仅有部分单元，第526章、第529章和第528章也只有部分教学桥接，不等于相应整章或分类条目完成；本次没有第2章教学正文。"
              "本稿教学正文按先修关系接续，不能把这一学习顺序说成MSC分类顺序。"
              "全目录仍为63部分、534章、6006节。自然数单元明确采用佩亚诺规则、归纳与递归原则，"
              "尚未进行集合论中的自然数形式构造，也未形式证明递归原则。所有课后题答案统一置于全部教学正文之后；例题解答随文保留。\n\n")
    heading, rest = opening.split("\n", 1)
    teaching = heading + "\n\n" + notice + rest
    teaching += "\n\n" + (CHAPTER / "chapter.md").read_text()
    teaching += """

# 第7部分 数论（MSC 11-XX） {#part-11}

本部分目前仅开始第26章的自然数基础桥接。原分类目录与先修学习顺序是两个层次：本批从最基础的对象与运算开始，不声称已展开其余数论章节。

# 第26章 初等数论（11Axx） {#chapter-26}

本章当前收入B1.1“自然数、后继与加法”、B1.2“乘法与十进制位值”，以及接续的B1.3自然数序、B1.4带余除法、B1.5任意底数的位值表示与算法、B1.6自然数减法与逐位加减、B1.7整数的构造、加法与序、B1.8整数乘法、B1.9整数带余除法、B1.10整除、B1.11最大公因数与欧几里得算法、B1.12贝祖恒等式、B1.13互素、B1.14有理数构造、B1.15有理数加法、B1.16有理数乘法、B1.17有理数倒数与除法、B1.18有理数序、B1.19有理数绝对值。它们不另占MSC章号或节号，也不表示11A05、11A63或整章已经完成。后续单元明确区分一般证明、算法终止论证与有限计算检查。

"""
    for index, (stem, *_rest) in enumerate(UNITS):
        if index == 2:
            teaching += ("\n\n**后续单元衔接。** B1.2中的“下一批”与“当前仍待写”保留其首次成稿时的范围说明；"
                         "本批以下B1.3—B1.5接续这些内容，分别建立序、商余分解和位值表示。"
                         "应把新单元的证明与先前单元的边界说明连起来阅读。\n\n")
        if stem == "ratios_proportions":
            teaching += """

# 第63部分 数学教育（MSC 97-XX） {#part-97}

以下单元把已建立的有理数运算用于比例、量与函数的教学桥接。它们接续当前学习路径，不表示已展开数学教育研究的全部主题，也不改变前文完整分类目录的编号。

# 第526章 算术与数论教育（97Fxx） {#chapter-526}

B1.20对应97F80“比、比例与百分数（教育方面）”，B1.21对应97F70“量与单位（教育方面）”。此处只收入部分基础教学内容，尚未覆盖相应分类的全部教育研究或课程主题；第526章未完成。它们沿用B1单元编号以标明先修联系，不归作第26章的两个新数论条目。

"""
        if stem == "functions_definition":
            teaching += """

# 第529章 分析学教育（97Ixx） {#chapter-529}

B2.1函数的定义、B2.2函数的复合、B2.3单射满射与双射、B2.4逆函数均对应97I20函数教学主题，接续前述学习路径。这里只建立部分基础概念与论证，不覆盖全部函数教学或分析学教育研究；第529章未完成。B2是教学单元编号，不是第2章正文，也不新增MSC分类编号。

"""
        if stem == "linear_equations":
            teaching += """

# 第528章 代数教育（97Hxx） {#chapter-528}

B2.5一元一次方程、B2.6二元一次方程组、B2.7一次不等式与有理区间、B2.8绝对值不等式对应97H30“方程与不等式（教育方面）”。它们接续[有理数除法](#rdiv-unit)及[逆函数](#inv-unit)的教学路径，先说明有理数范围内解集与可逆变形，再建立消元步骤，并依据[有理数序](#rord-unit)与[绝对值](#rabs-unit)处理不等式的正负零分支、区间端点和内外条件；不提前使用未建立的坐标直线、实数连续线段或交点结论。第528章未完成，97H30也只有部分内容。

此处的第526章、第529章、第528章按本稿先修学习路径排列，章号保留原分类目录编号。编号不递增不表示分类次序改变，也不表示这些教育主题的历史先后；阅读顺序与分类顺序分别记录。

"""
        if stem == "rational_coordinates":
            teaching += """

# 第529章 分析学教育（97Ixx，续） {#chapter-529-continuation}

以下B2.9有理坐标与B2.10仿射函数图像接续[第529章前段](#chapter-529)的函数定义，复用刚建立的[方程组](#sys-unit)、[一次不等式](#ineq-unit)和[绝对值条件](#absineq-unit)。它们仍归入同一分类章的97I20函数教学主题；这是第529章续写，不新增分类章或节，也不表示第529章完成。先修学习路径回到该章，不改变完整分类目录的排列或编号。

本批仅在有理数对中定义坐标点和图像的成员条件，先作代数推导，再使用有限绘图说明。图示不把有理数对等同于全体实平面，也不以连线、倾斜程度或目测交点代替证明。

"""
        if stem == "rational_powers":
            teaching += """

# 第528章 代数教育（97Hxx，续） {#chapter-528-continuation}

以下B2.11有理数幂、B2.12有限和、B2.13多项式系数记录、B2.14多项式加法和数乘、B2.15多项式乘法、B2.16乘法的结合、求值和次数、B2.17一次除式商余与B2.18因式定理及恒等识别接续当前学习路径，归入97H20初等代数教学主题；随后B2.19有理平方与平方方程、B2.20配方与有理二次方程主属97H30，交叉关联97H20，始终以有理数为定义域。这是[第528章前段](#chapter-528)之后的同一分类章续写，不新增分类章或节，第528章仍未完成。这里复用已建立的有理数运算和自然数递归、归纳规则，依次说明重复乘法、有限项相加、规范系数记录、线性运算、有限卷积乘法、一次除式商余及不同有理根数界；不提前引入分数指数、无限求和、收敛理论、一般多项式长除法或插值。

章号继续保留完整分类目录编号，先修学习顺序在第529章续写之后回到第528章，不表示分类次序或历史先后发生改变。

"""
        if stem == "rational_gaps_bounds":
            teaching += """

# 第526章 算术与数论教育（97Fxx，续） {#chapter-526-continuation}

以下B2.21有理数的稠密、界与平方缺口，B2.22戴德金分割、次序与上确界，接在第528章续写的有理平方与二次方程之后。两单元主属97F50“实数、复数（教育方面）”，交叉关联06A05与03E20；本次只处理有理数缺口和实数构造的集合、次序部分，不涉及复数。这是[第526章前段](#chapter-526)之后的第526章续写，不新增分类章或节。第526章未完成；教学先修次序不改变完整分类目录的63部分、534章、6006节。

先在有理数内证明中点、显式自然数界及一个非空有界集合没有有理上确界，再公开采用有理数幂集存在的集合背景，构造非空、非全体、下闭且无最大元的有理下段。只在这些分割组成的集合上证明包含全序、有理数保序嵌入以及非空有上界分割族的并集上确界。分割加法、乘法、有序域结构、实数平方根及收敛结论均须另行建立，不能由有限见证图或名称自动获得。

"""
        teaching += "\n\n" + (FOUNDATIONS / (stem + ".md")).read_text()
    teaching += ("\n\n**多项式单元范围衔接。** B2.13—B2.16保留各单元初建时的范围说明；"
                 "本批后续B2.17—B2.18已接着建立一次除式商余、因式定理、不同有理根数界与标准求值函数的恒等识别。"
                 "有限点判等须带共同系数上界及互异输入数量条件，仍不能把任意有限采样当一般判据。\n")
    answers = (CHAPTER / "answers.md").read_text()
    first, remainder = answers.split("\n", 1)
    if not first.startswith("# 附录一 "):
        raise ValueError("Unexpected chapter-answer structure")
    remainder = re.sub(r"^(#{2,5}) ", r"#\1 ", remainder, flags=re.M)
    answers = ("# 附录一 全部课后题参考答案 {#answers}\n\n"
               "## 第1章参考答案 {#ch01-answers}\n" + remainder)
    answers += "\n\n" + "\n\n".join((FOUNDATIONS / (stem + "_answers.md")).read_text()
                                      for stem, *_ in UNITS)
    appendices = (CHAPTER / "appendices.md").read_text()
    appendices = appendices.replace("本审阅稿所用四张插图", "本批审阅稿所用十七张插图")
    appendices = appendices.replace("生成代码为 `tools/draw_ch01_figures.py`；",
                                    "前四张生成代码为 `tools/draw_ch01_figures.py`，后十三张为 `tools/draw_foundations_batch.py`；")
    figure_row = "| ch01_square.png | 第17节 | 四个单位格组成的正方形 |"
    if figure_row not in appendices:
        raise ValueError("Original figure appendix changed; inspect before assembly")
    appendices = appendices.replace(figure_row, figure_row +
        "\n| b1_place_value.png | 基础单元B1.2 | 203的百位、十位与个位 |"
        "\n| b1_rational_distance.png | 基础单元B1.19 | 有理刻度的距离与三角等号实例；不表示实数完备直线的构造 |"
        "\n| b1_ratio_allocation.png | 基础单元B1.20 | 总量10按2比3分配为4与6；五个等份各表示2 |"
        "\n| b2_function_mapping.png | 基础单元B2.1 | 有限集合之间的函数对应示意；一般定义和证明以正文为准 |"
        "\n| b2_inverse_mapping.png | 基础单元B2.4 | 有限双射及其逆函数的反向对应；不表示有理数或实数连续函数图像 |"
        "\n| b2_elimination_steps.png | 基础单元B2.6 | 方程组的可逆消元与代回步骤；只表示代数操作，不引用坐标几何结论 |"
        "\n| b2_absolute_bounds.png | 基础单元B2.8 | 有理数绝对值的内外条件与端点示意；不表示实数连续线段，结论依据正文成员等价证明 |"
        "\n| b2_affine_coordinates.png | 基础单元B2.10 | 有理坐标中的仿射函数有限点示意；图像由成员条件定义，不以连线代替证明 |"
        "\n| b2_finite_sum.png | 基础单元B2.12 | 有限记录的项数与拼接示意；只表示有限项，不表示无限级数或收敛 |"
        "\n| b2_polynomial_records.png | 基础单元B2.13 | 尾零规范化与中间零位置示意；不以有限取值判定一般多项式相等 |"
        "\n| b2_polynomial_product.png | 基础单元B2.15 | 同一目标指标的系数贡献示意；只作有限实例，不替代全指标卷积及表示无关证明 |"
        "\n| b2_quadratic_bound.png | 基础单元B2.20 | 有理二次式的有限采样与界；不画实数连续曲线，不以样本替代一般配方证明 |"
        "\n| b2_rational_gap.png | 基础单元B2.21 | 六个有理见证和四次显式更新；不表示极限、全部有理数或任意分割的数值实现 |"
        "\n\n图 `b2_rational_gap.png` 的分数、平方和比较先以精确有理数计算；框和箭头仅安排六个有限样本，完整函数见附录二十四。"
        "\n\n图 `b2_quadratic_bound.png` 的采样值先用精确有理数计算；浮点转换只用于绘图位置，不参与数学判断。"
        "\n\n新图 `b2_affine_coordinates.png` 的样本值先用 `Fraction` 精确计算，再转换为Matplotlib绘图所需的浮点坐标。转换只用于渲染位置，不用于数学判断；计算模块的精确有理数输入与结果，不意味着绘图软件也全程使用有理数。"
        "图 `b2_finite_sum.png` 的项值、前缀和及两段和也先用 `Fraction` 精确计算，再以分数文本显示；框、箭头与文字位置使用绘图坐标，只安排版面，不参与求和或数学判断。"
        "图 `b2_polynomial_records.png` 的系数与示例求值先按精确有理数计算；框和文字位置只用于渲染，不作为对象相等或次数的数学判据。"
        "图 `b2_polynomial_product.png` 的系数乘积与同指标合计先用精确有理数计算；格子和文字只显示有限例子，图形位置不参与数学判断。\n")
    appendix_four = "# 附录四 第21节模拟代码 {#simulation-code}"
    if appendix_four not in appendices:
        raise ValueError("Original simulation appendix changed; inspect before assembly")
    appendices = appendices.replace(appendix_four, reference_addition() + integer_reference_addition()
                                    + divisibility_reference_addition() + bezout_reference_addition()
                                    + rational_reference_addition() + rational_multiplication_reference_addition()
                                    + rational_order_reference_addition() + ratios_units_reference_addition()
                                    + functions_reference_addition() + inverse_functions_reference_addition()
                                    + linear_equations_reference_addition() + linear_inequalities_reference_addition()
                                    + coordinates_affine_reference_addition() + powers_sums_reference_addition()
                                    + polynomial_basic_reference_addition() + polynomial_product_reference_addition()
                                    + polynomial_linear_division_reference_addition()
                                    + rational_quadratic_reference_addition()
                                    + rational_gaps_cuts_reference_addition() + appendix_four)
    appendices += "\n\n```python\n" + (ROOT / "tools/ch01_simulation.py").read_text() + "```\n"
    appendices += algorithm_appendix()
    appendices += written_arithmetic_appendix()
    appendices += integer_pairs_appendix()
    appendices += integer_euclidean_appendix()
    appendices += extended_euclidean_appendix()
    appendices += rational_addition_appendix()
    appendices += rational_multiplication_appendix()
    appendices += rational_order_appendix()
    appendices += ratios_units_appendix()
    appendices += finite_functions_appendix()
    appendices += finite_function_inverses_appendix()
    appendices += linear_equation_solvers_appendix()
    appendices += rational_inequalities_appendix()
    appendices += rational_affine_appendix()
    appendices += rational_powers_sums_appendix()
    appendices += rational_polynomial_basic_appendix()
    appendices += rational_polynomial_product_appendix()
    appendices += rational_polynomial_linear_division_appendix()
    appendices += rational_quadratics_appendix()
    appendices += rational_gap_figure_appendix()
    return localize_book_links(teaching + "\n\n" + answers + "\n\n" + appendices)


def algorithm_appendix():
    text = r"""

# 附录五 自然数商余与位值算法 {#natural-algorithms}

本附录把[带余除法单元](#div-unit)与[位值表示单元](#pos-unit)中的数学规则写成精确整数程序。它不模拟经验数据，不用浮点近似，也不把程序返回结果当作一般证明。自然数、归纳与递归仍采用正文明确列出的基础规则，未另行形式构造自然数。

**商余程序的状态。** 输入为自然数 $n$ 与正自然数 $b$。从 $q_0=0$、$r_0=0$ 开始，依次处理 $k=0,\ldots,n-1$，执行

$$
(q_{k+1},r_{k+1})=
\begin{cases}
(q_k,r_k+1),&r_k+1<b,\\
(q_k+1,0),&r_k+1=b.
\end{cases}
$$

这里 $k$ 是已经处理的数量，$q_k,r_k$ 是当前状态。相应不变量是 $k=bq_k+r_k$ 与 $0\le r_k<b$；正除数保证后继余量只需检查上述两种情况。程序完成恰好 $n$ 次处理后返回商余；一般的存在性、唯一性与次序依据见上述正文单元。

**逐次取余与数字方向。** 对底数 $b\ge2$，从 $m_0=n$ 开始，在 $m_i>0$ 时写出 $m_i=bm_{i+1}+r_i$、$0\le r_i<b$。每步记录的 $r_i$ 从最低位开始；返回前把它们倒序，因此 `digits_nat` 返回的列表最高位在前。零单独返回 `[0]`。[商严格下降](#pos-quotient-descent)和[取位算法的终止](#pos-extraction-algorithm)在正文证明，不能仅据有限运行成功推断。

**数字串的求值。** 若输入列表按最高位在前排列为 $[d_0,\ldots,d_{s-1}]$，其中 $s\ge1$、$0\le d_i<b$，定义 $v_0=0$，逐步计算 $v_{i+1}=bv_i+d_i$，最后返回 $v_s$。此处 $d_0$ 表示最左边的数字，与[正文位值定义](#pos-base-digits)中从个位起标号的公式须按位置对应；不是把最高位误作最低位。求值函数允许前导零，而[规范表示的唯一性](#pos-uniqueness)要求排除非零数的前导零。

**超标系数的进位。** 与求值函数不同，`normalize_coefficients` 允许输入非空的非负系数串，其中某个系数可以不小于底数。若从最低位起编号的系数 $c_j=bq+r$，其中 $q\ge1$、$0\le r<b$，一次进位把 $c_j$ 换成 $r$，把左邻系数 $c_{j+1}$ 换成 $c_{j+1}+q$；原来没有左邻时，先把该处的系数视为零。这一局部替换保持位值的总值。设进位前后所有系数的和分别为 $C_{\mathrm{old}}$、$C_{\mathrm{new}}$，设 $p$ 是底数的前驱，即 $S(p)=b$，则

$$
C_{\mathrm{old}}=C_{\mathrm{new}}+pq>C_{\mathrm{new}}.
$$

因为 $b\ge2$，其前驱 $p$ 为正；非规范位置使 $q\ge1$。系数和严格下降所给出的[任意合法进位过程终止证明](#pos-carry-termination)，与反复取商算法的终止证明是两条独立论证。代码选择优先处理最低的超标系数，仅指定一种执行顺序，并没有把这一选择作为一般终止结论的前提。

接口拒绝布尔值、负值及非整数；除法要求 $b\ge1$，位值转换要求 $b\ge2$，求值还拒绝空串和越界数字。下面完整列出配套文件 `tools/natural_algorithms.py`。实际有限交叉检查另由校验工具对 $0\le n\le120$、除数 $1\le b\le16$ 与底数 $2\le b\le16$ 执行，并在伴生报告中保存结果；这些检查不是证明。

```python
"""
    return text + (ROOT / "tools/natural_algorithms.py").read_text() + "\n```\n"


def written_arithmetic_appendix():
    text = r"""

# 附录六 逐位加减的精确实现 {#written-arithmetic-code}

本附录对应[B1.6自然数减法与逐位加减](#sub-unit)。两个输入都是按最高位在前排列的非空数字表，使用同一底数 $b\ge2$，每个数字均为自然数且严格小于 $b$；允许前导零，输出采用规范写法。减法另外要求被减数的值不小于减数的值，依据[自然数差的存在唯一性](#sub-definition)定义结果；范围外输入被拒绝，不把负结果截成零。

**加法的本位关系。** 从最低位起编号，把不足的位置补零，记两输入的本位数字为 $x_i,y_i$，输入进位为 $e_i$，输出数字为 $z_i$。程序使用正除数的商余分解，使

$$
x_i+y_i+e_i=z_i+b e_{i+1},\qquad 0\le z_i<b,\qquad e_0=0.
$$

进位只取零或一、固定轮数后如何处理最高进位，以及结果与原和相等的理由，见[逐位加法证明](#sub-addition-algorithm)。程序没有以有限算例替代这些一般结论。

**减法的本位关系。** 仍从最低位起编号，令 $e_i$ 是本位输入借位，$e_0=0$，并记 $u_i=y_i+e_i$。当 $u_i\le x_i$ 时，取 $z_i=x_i-u_i$、$e_{i+1}=0$；当 $x_i<u_i$ 时，取 $z_i=(x_i+b)-u_i$、$e_{i+1}=1$。相应等式为

$$
x_i+b e_{i+1}=y_i+e_i+z_i.
$$

各分支中的差都是非负差，且输出数字仍在允许范围内；这些条件以及最终借位为零的依据见[逐位减法证明](#sub-borrow-algorithm)。实现用Python精确整数执行这些已经保证非负的差，不作浮点近似，也不把程序返回值当作自然数减法的定义或证明。外层循环只遍历补齐后的有限数位，输入表不被修改。

下面完整列出 `tools/written_arithmetic.py`。它复用[附录五](#natural-algorithms)中已列出的数字求值与商余程序。独立有限检查入口是 `python tools/validate_written_arithmetic.py`；检查使用Python整数运算与独立的数字转换交叉核对，结果和源码哈希保存于伴生报告 `research/production/written_arithmetic_validation.json`。这些有限检查不证明对任意长度、任意底数的结论。

```python
"""
    return text + (ROOT / "tools/written_arithmetic.py").read_text() + "\n```\n"


def integer_pairs_appendix():
    text = r"""

# 附录七 整数数对的精确实现 {#integer-pairs-code}

本附录对应[整数构造、加法与序](#int-unit)和[整数乘法](#imul-unit)。输入数对的两个分量都是自然数。数对 $(a,b)$ 与 $(c,d)$ 表示同一个整数，当且仅当 $a+d=c+b$。加法、相反数、乘法和序分别按照以下自然数公式计算或比较：

$$
[(a,b)]+[(c,d)]=[(a+c,b+d)].
$$

$$
-[(a,b)]=[(b,a)].
$$

$$
[(a,b)]\cdot[(c,d)]=[(ac+bd,ad+bc)].
$$

$$
[(a,b)]\le[(c,d)]\iff a+d\le c+b.
$$

方括号表示数对所属的等价类；左边的整数运算通过右边的代表元公式定义。换代表元不改变结果、运算律与序的性质分别在上述正文单元论证。程序操作的是有限的自然数数对，并不枚举一个等价类的全部元素，也不以输出实例替代良定义性证明。实际接口、合法输入检查与返回值约定见下列完整源码；使用Python精确整数，不进行浮点近似。

`checked_pair` 只接受长度为二的列表或元组，各分量必须是非负整数；布尔值、负数及非整数均被拒绝。`equivalent` 使用上面的交叉相加条件判断两个代表元是否等价，不能用Python的元组相等代替它。`embed(n)` 返回 $(n,0)$，`add`、`negate`、`multiply` 和 `leq` 分别实现上述四条规则。

整数减法 `subtract` 通过加上相反数定义：对代表元 $(a,b)$ 与 $(c,d)$，返回代表元 $(a+d,b+c)$；它不要求左边的整数较大。`canonical` 把一个代表元改写成规范代表元：当 $b\le a$ 时返回 $(a-b,0)$，否则返回 $(0,b-a)$。其中使用的自然数差均在非负范围内；两种分支分别表示非负整数与负整数，零返回 $(0,0)$。原始加法和乘法接口只返回一个合法代表元，未承诺直接返回规范代表元；需要规范形式时再调用 `canonical`。

独立有限检查由 `tools/validate_integer_pairs.py` 执行，结果及所测源码哈希保存在伴生文件 `research/production/integer_pairs_validation.json`。它与整数表示的独立计算交叉核对，但不证明对所有自然数数对成立的数学结论。

```python
"""
    return text + (ROOT / "tools/integer_pairs.py").read_text() + "\n```\n"


def integer_euclidean_appendix():
    text = r"""

# 附录八 整数带余除法与欧几里得算法 {#integer-euclidean-code}

本附录对应[整数带余除法](#idiv-unit)、[整除](#dvs-unit)与[最大公因数及欧几里得算法](#gcd-unit)。程序使用Python精确整数，并复用[附录五的自然数除法](#natural-algorithms)；不进行浮点近似，不以运行结果替代正文证明，也不承诺适合大整数的计算效率。所有整数输入都拒绝布尔值及非整数。

**有符号带余除法。** `divide_integer(a,b)` 要求 $b\ne0$，返回整数商 $q$ 与自然数余数 $r$，使

$$
a=bq+r,\qquad 0\le r<|b|.
$$

令 $m=|b|$，先用自然数程序计算 $|a|=mu+v$，其中 $0\le v<m$。把除数暂取为正数 $m$，商余 $(t,r)$ 按下列规则转换：

$$
(t,r)=\begin{cases}
(u,v),&a\ge0,\\
(-u,0),&a<0\text{ 且 }v=0,\\
(-(u+1),m-v),&a<0\text{ 且 }v>0.
\end{cases}
$$

若原除数 $b>0$，取 $q=t$；若 $b<0$，取 $q=-t$，余数保持不变。最后一分支的自然数差合法，因为 $0<v<m$。负除数也采用非负余数，不能不加转换地用某种语言的默认负除数取余约定替换本接口。

**整除判别。** `divides(d,n)` 实现存在整数 $k$ 使 $n=dk$ 的定义。$d=0$ 时单独判断 $n=0$；$d\ne0$ 时才调用带余除法，以余数是否为零判断整除。允许 $0\mid0$ 与允许零作带余除法的除数是两回事。

**欧几里得状态。** `gcd_trace(a,b)` 先置 $(u_0,v_0)=(|a|,|b|)$。只要 $v_i\ne0$，用自然数除法取得

$$
u_i=v_iq_i+r_i,\qquad 0\le r_i<v_i,
$$

并更新 $(u_{i+1},v_{i+1})=(v_i,r_i)$。每行记录更新前的 $u_i,v_i,q_i,r_i$。两状态的整数公因数完全相同：对任意整数 $d$，

$$
(d\mid u_i\ \text{且}\ d\mid v_i)
\iff(d\mid v_i\ \text{且}\ d\mid r_i).
$$

第二分量在继续迭代时严格下降，因此终止；每次调用的自然数除法本身也有限完成。到达 $v_i=0$ 时返回非负值 $u_i$ 与轨迹；`gcd_integer` 只返回该值。单零输入得到另一个输入的绝对值，双零输入立即返回零和空轨迹。双零处的最大公因数按正文的整除刻画定义，不是从正公因数中选数值最大的一个。代码没有输出贝祖系数，不能把此程序描述成扩展欧几里得算法。

独立有限检查入口为 `tools/validate_integer_euclidean.py`，结果及本程序、检验程序、自然数算法的源码哈希存于 `research/production/integer_euclidean_validation.json`。检验比较商余重构、余数范围、公因数刻画与每一步轨迹；这些有限实例不是对所有整数的证明。下面列出完整源码。

```python
"""
    return text + (ROOT / "tools/integer_euclidean.py").read_text() + "\n```\n"


def extended_euclidean_appendix():
    text = r"""

# 附录九 扩展欧几里得与整数线性组合 {#extended-euclidean-code}

本附录对应[贝祖恒等式](#bez-unit)与[互素](#cop-unit)。程序使用Python精确整数，复用[附录八的整数检查及带余除法](#integer-euclidean-code)和[附录五的自然数除法](#natural-algorithms)。它不作浮点近似，也不以有限运行替代正文的存在性、终止与唯一性论证；当前自然数除法实现仅供解释，不宣称大整数计算高效。

**两个余数的系数必须同时保存。** 原输入整数 $a,b$ 在整个算法中固定。定义符号因子 $\varepsilon(z)$：$z\ge0$ 时取 $1$，$z<0$ 时取 $-1$，因此本程序明确取 $\varepsilon(0)=1$。`extended_gcd(a,b)` 从以下状态开始：

$$
(u_0,v_0)=(|a|,|b|),
$$

$$
(x_0,y_0)=(\varepsilon(a),0),\qquad
(X_0,Y_0)=(0,\varepsilon(b)).
$$

每轮同时维持两条等式；大小写表示不同的系数，不是更换原输入：

$$
u_i=ax_i+by_i,\qquad v_i=aX_i+bY_i.
$$

若 $v_i\ne0$，用自然数除法得到 $u_i=v_iq_i+r_i$、$0\le r_i<v_i$。更新为

$$
(u_{i+1},v_{i+1})=(v_i,r_i),
$$

$$
(x_{i+1},y_{i+1})=(X_i,Y_i),
$$

$$
(X_{i+1},Y_{i+1})=(x_i-q_iX_i,\ y_i-q_iY_i).
$$

系数可以为负数，余数仍为自然数。保存的每行轨迹包含更新前两组系数、商余及新余数的系数。第二余数严格下降所给出的终止论证见正文；到达 $v_i=0$ 时返回 $g=u_i$、$x=x_i$、$y=y_i$ 和轨迹，使 $ax+by=g=\gcd(a,b)$。双零输入立即返回 $(g,x,y)=(0,1,0)$；这是一个合法见证，不是系数唯一的声明。

**一个线性方程解。** `linear_solution(a,b,c)` 求整数方程 $ax+by=c$ 的一组解，或返回 `None` 表示无解。若 $g>0$，先检查 $g\mid c$；精确整数商为 $k$ 时，将上述贝祖系数同时乘 $k$，得到一组解。若 $g=0$，则两输入均为零：$c=0$ 时返回 $(0,0)$，$c\ne0$ 时无解。接口不返回全体解，也不声明返回的解唯一。

**互素整数对。** `reduced_record(a,b)` 要求 $a$ 为整数、$b$ 为正整数，取 $g=\gcd(a,b)>0$，返回精确商构成的整数对 $(p,q)$，满足

$$
a=gp,\qquad b=gq,\qquad q>0,\qquad \gcd(p,q)=1.
$$

它只返回整数对；此处尚未借程序定义有理数类型或有理数除法。零第一分量返回 $(0,1)$。全部接口拒绝布尔值及非整数，整数对接口另拒绝非正第二分量。符号、双零和互素约去的数学依据在正文展开。

独立有限检验入口为 `tools/validate_extended_euclidean.py`。结果及本体、检验程序、整数带余除法和自然数算法四份源码哈希见 `research/production/extended_euclidean_validation.json`。有限网格与具体算例检查不构成对所有整数的证明，也不保证贝祖系数与其他实现逐项相同。以下完整列出源码。

```python
"""
    return text + (ROOT / "tools/extended_euclidean.py").read_text() + "\n```\n"


def rational_addition_appendix():
    text = r"""

# 附录十 有理数规范记录与加法 {#rational-addition-code}

本附录对应[有理数构造](#rat-unit)与[有理数加法](#radd-unit)。输入记录为两个整数构成的列表或元组 $(a,b)$，要求 $b>0$；布尔值、浮点数、非整数及非正分母均被拒绝。程序元组只是一个代表元，不是由全部等价代表元组成的集合；正文在构造等价类之后，证明它与唯一规范记录的对应。

**等价关系与规范化。** 对合法记录 $(a,b)$、$(c,d)$，`equivalent` 检查整数等式 $ad=bc$；不能用原始元组的逐项相等代替它。`normalize` 令 $g=\gcd(a,b)$，由 $b>0$ 得 $g>0$，返回精确整数商组成的 $(p,q)$，满足

$$
a=gp,\qquad b=gq,\qquad q>0,\qquad \gcd(p,q)=1.
$$

精确商由已建立的整数算法得到；这里没有调用有理数除法。原记录与规范记录的交叉乘积相等。规范记录的存在唯一性见正文，零的规范记录为 $(0,1)$。`embed(n)` 返回 $(n,1)$。

**类上的加法与相反数。** 方括号表示等价类，以下式子中的分量乘法均为整数乘法：

$$
[(a,b)]+[(c,d)]=[(ad+bc,bd)].
$$

$$
-[(a,b)]=[(-a,b)].
$$

因为 $b,d>0$，乘积分母 $bd$ 仍为正。`add` 先计算代表元 $(ad+bc,bd)$，再返回其规范记录；`negate` 对 $(-a,b)$ 规范化。更换代表元不影响和或相反数的类，这项良定义性由正文证明，程序的有限检验不能替代它。

**减法。** 对两个已构造的有理数 $\alpha,\beta$，定义 $\alpha-\beta=\alpha+(-\beta)$。`subtract` 按该规则组合 `negate` 与 `add`；两个输入仍必须具有正分母，输出为规范记录。此接口只处理加法结构，没有实现有理数乘法、倒数、除法或次序。

源码复用[附录九的整数对约分](#extended-euclidean-code)与[附录八的整数输入检查](#integer-euclidean-code)，只执行精确整数运算。独立有限检验由 `tools/validate_rational_addition.py` 执行，以Python标准库 `Fraction` 和交叉乘积为外部核对工具；该库不是本书定义或程序实现的前置依据。结果及本体、检验程序、扩展算法、整数算法、自然数算法五份源码哈希保存于 `research/production/rational_addition_validation.json`。检验不能构成无限等价类构造或一般定理的证明，也不声明当前算法高效。以下完整列出源码。

```python
"""
    return text + (ROOT / "tools/rational_addition.py").read_text() + "\n```\n"


def rational_multiplication_appendix():
    text = r"""

# 附录十一 有理数乘法、倒数与除法 {#rational-multiplication-code}

本附录对应[有理数乘法](#rmul-unit)与[有理数倒数及除法](#rdiv-unit)。输入是整数列表或元组 $(a,b)$，分母须满足 $b>0$；布尔值、非整数及非正分母被拒绝。程序存储代表元，输出唯一的互素正分母规范记录；它不枚举整个等价类。输入检查和规范化复用[附录十](#rational-addition-code)。

公开资料的条件核对见[本批参考资料](#rationals-multiplication-sources)。其中Lean的零倒数、零除数总函数约定不纳入本书定义；其先用倒数的零积证明链也不作为本书乘法单元的先修。本书先由整数零积建立有理数零积，再处理倒数与除法。

**乘法。** 对合法代表元 $(a,b)$、$(c,d)$，类上的定义是

$$
[(a,b)]\cdot[(c,d)]=[(ac,bd)].
$$

右边的 $ac$ 与 $bd$ 都是整数乘积，且 $bd>0$。`multiply` 先计算代表元 $(ac,bd)$，再规范化。代表元无关、乘法律与分配律由正文证明；本程序不以有限算例替代这些证明。

**非零才有倒数。** 输入类非零当且仅当 $a\ne0$。为维持正分母，倒数定义按整数分子符号分支：

$$
[(a,b)]^{-1}=\begin{cases}
[(b,a)],&a>0,\\
[(-b,-a)],&a<0.
\end{cases}
$$

`reciprocal` 对相应代表元规范化；$a=0$ 时抛出 `ValueError`，不返回零或其他约定值。这里比较的是整数分子的符号，不需要预先定义有理数的次序。倒数存在唯一性的数学论证见正文。

**除法的定义域。** 对有理数 $\alpha,\beta$，仅在 $\beta\ne0$ 时定义

$$
\alpha\div\beta=\alpha\cdot\beta^{-1}.
$$

`divide(left,right)` 先确认左输入合法，再通过右输入的倒数与乘法计算。右输入的分子为零时拒绝运算；左输入可以为零，只要右输入非零。交换输入次序会改变定义域，因此不能把“零作被除数”与“零作除数”混为一谈。

全部计算只用精确整数及已建立的规范化算法，没有浮点近似，也不宣称当前教学实现高效。独立有限检验入口是 `tools/validate_rational_multiplication.py`，使用Python标准库 `Fraction` 与整数交叉乘积作外部核对；它们不是正文证明的前提。检验范围、零输入拒绝及具体算例记录在 `research/production/rational_multiplication_validation.json`，并绑定本体、检验程序、有理数加法、扩展欧几里得、整数算法、自然数算法六份源码哈希。有限检查不构成一般数学证明或形式化验证。下面完整列出源码。

```python
"""
    return text + (ROOT / "tools/rational_multiplication.py").read_text() + "\n```\n"


def rational_order_appendix():
    text = r"""

# 附录十二 有理数比较、绝对值与距离 {#rational-order-code}

本附录对应[有理数序](#rord-unit)与[绝对值和距离](#rabs-unit)。输入均为整数列表或元组 $(a,b)$，且 $b>0$；仍采用[附录十](#rational-addition-code)的检查与规范化，拒绝布尔值、非整数和非正分母。记录表示一个有理数的代表元，输出记录为互素正分母规范形式，不是把等价类的所有元素保存下来。

公开资料及其适用范围见[本批参考资料](#rationals-order-sources)。本书此处的距离取非负有理数值；来源中的实数值度量只作证明方法参照，不预设有理数已经嵌入构造完成的实数体系。

**比较只需整数交叉乘积。** 对 $b,d>0$，正式的类上定义为

$$
[(a,b)]\le[(c,d)]\iff ad\le bc,
$$

$$
[(a,b)]<[(c,d)]\iff ad<bc.
$$

`compare` 计算整数 $\Delta=ad-bc$，在其为负、零、正时分别返回整数标记 $-1,0,1$。标记表示比较结果，不是两个有理数之差的值。`leq` 判断该标记不大于零，`lt` 判断它小于零。由于两分母均正，交叉比较无需另行反转不等号；这一条件和代表元无关性在正文证明。

**绝对值与距离。** `absolute` 对分子取整数绝对值，再规范化记录 $(|a|,b)$；这里 $|a|$ 是已定义的整数绝对值。其对应的有理数定义为

$$
|\alpha|=\begin{cases}
\alpha,&0\le\alpha,\\
-\alpha,&\alpha<0.
\end{cases}
$$

`distance(left,right)` 先作已定义的有理数减法，再取绝对值，返回规范记录，对应

$$
d(\alpha,\beta)=|\alpha-\beta|.
$$

例如有理刻度 $r=-3/2$、$s=-1/2$、$t=3/2$ 给出距离 $1,2,3$，只核对这个实例的三角等号；一般非负性、对称性与三角不等式由正文证明。图形是有限刻度示意，不构成实数完备性或连续统的构造。

全部程序只用精确整数运算。检验入口 `tools/validate_rational_order.py` 以Python标准库 `Fraction` 作外部有限比较，另检查代表元变换、零与正负乘除条件以及绝对值不等式实例；不把检验当作一般证明。结果存于 `research/production/rational_order_validation.json`，绑定本体、检验程序、有理数乘法、加法、扩展欧几里得、整数算法、自然数算法七份源码哈希。当前教学实现不宣称适合大整数的高效计算。以下完整列出源码。

```python
"""
    return text + (ROOT / "tools/rational_order.py").read_text() + "\n```\n"


def ratios_units_appendix():
    text = r"""

# 附录十三 比、比例与单位数值换算 {#ratios-units-code}

本附录对应[比与比例](#ratio-unit)及[量与单位](#qty-unit)。接口接收有理数的整数代表元 $(a,b)$，其中 $b>0$；复用[附录十的合法性检查](#rational-addition-code)与[附录十一的有理数乘除](#rational-multiplication-code)，返回互素正分母规范记录或逻辑判断，不使用浮点数。布尔值、非整数或非正记录分母均被拒绝。

精确换算约定的公开教材核对与许可边界见[本批参考资料](#ratios-units-sources)。教材提供条件参照，模型与证明仍在正文建立；没有把辅助转码草案当作已核验的官方规范。

**有理数的比和比例。** 对有理数 $a,b$，`ratio(a,b)` 计算 $a:b=a\div b$，前提为 $b\ne0$；后项可正可负。对有理数 $a,b,c,d$，`proportion(a,b,c,d)` 先检查 $b\ne0$ 且 $d\ne0$，再使用已经证明的等价关系

$$
a:b=c:d\iff ad=bc.
$$

这里输入 $a,b,c,d$ 是四个有理数，不是某一原始代表元的四个分量。交叉等式不取消两个后项非零的条件；代码不会接受零后项后仅靠交叉乘积判真。

**换单位时的数值。** 调用者须先确定同一种量的两个单位 $u,v$ 以及正确的单位关系 $v=ku$，其中 $k$ 是正有理数。若同一量写成 $Q=xu=yv$，由这套乘性计量模型得

$$
y=x\div k,\qquad k>0.
$$

`convert_value(x,k)` 实现这条数值规则；`positive_scale` 检查尺度严格为正。尺度方向是“新单位等于旧单位的 $k$ 倍”，不是“新数值等于旧数值的 $k$ 倍”。例如在已知一米等于一百厘米的单位关系下，375厘米改用米表示，$k=100$，数值为 $375\div100=15/4$。

**两个单位都改变的率。** 设旧分子单位为 $u$、旧分母单位为 $w$，新单位满足 $v=ku$、$z=\ell w$，其中 $k,\ell>0$。在率的乘性单位模型中，同一率分别写成 $x(u/w)$ 与 $y(v/z)$，相应数值为

$$
y=x\ell\div k.
$$

`convert_rate(x,k,l)` 分别检查两个尺度为正，按此式计算。例如从千米每小时改为米每秒，新分子单位的尺度为 $1/1000$，新分母单位的尺度为 $1/3600$；数值5变成 $5(1/3600)\div(1/1000)=25/18$。

**接口的责任边界。** 模块只收到数值记录，不存储单位名称或量的种类。调用者负责确认量可比较、单位关系适用、尺度方向正确；程序不会自动识别量纲，也不校验物理测量精度。负数值是否适用于某一种量须由所选模型决定；程序接受有理数输入不等于所有实物量都允许负值。这里只实现乘性尺度换算，不实现带平移常数的仿射标度变换。数学模型和适用条件在正文说明，实际测量的不确定性不能由精确有理数计算消除。

独立有限核对入口是 `tools/validate_ratios_units.py`，以Python标准库 `Fraction` 为外部核对工具，检查比、比例、代表元变换、往返与组合换算、零后项和非正尺度拒绝。结果见 `research/production/ratios_units_validation.json`，绑定本体、检验程序、有理数乘法、加法、扩展欧几里得、整数及自然数算法七份源码哈希。有限核对不是一般证明、量纲检查或真实测量认证。以下完整列出源码。

```python
"""
    return text + (ROOT / "tools/ratios_units.py").read_text() + "\n```\n"


def finite_functions_appendix():
    text = r"""

# 附录十四 有限函数表、限制与复合 {#finite-functions-code}

本附录对应[函数定义](#fun-unit)与[函数限制及复合](#funcomp-unit)，公开条件核对见[本批参考资料](#functions-sources)。本程序只接收有限、显式列出的整数标签集合；不表示定义在全体有理数上的一般函数，不构造实数连续函数，也不以有限穷举替代正文的一般证明。

**三个数据均须保存。** `FiniteFunction(A,B,G)` 保存定义域 $A$、目标集合 $B$ 与图 $G$，要求

$$
G\subseteq A\times B,\qquad
\text{对每个 }x\in A\text{，恰有一个 }y\in B\text{ 使 }(x,y)\in G.
$$

输入集合可用列表、元组、集合或不可变集合表达；标签必须是整数，布尔值与非整数被拒绝。图须是显式的二坐标列表或元组组成的有限集合记录。重复写同一对只表示同一个集合元素，不构成多个输出；同一输入配不同输出、缺少某个域元素的输出或坐标越界均被拒绝。对象内部改存不可变集合，不随原输入列表之后的修改而改变。程序相等比较域、目标和图三个数据；只看图相同不足以断定函数相等。

**求值与像。** 调用 `f(x)` 前检查整数标签 $x\in A$，再从图中找唯一的输出；域外输入被拒绝。`image()` 返回

$$
f(A)=\{y\in B:\text{存在 }x\in A\text{ 使 }(x,y)\in G\}.
$$

它未必等于 $B$。空定义域的图必须为空；同一空图配不同目标，得到的是不同的三数据函数。若定义域非空而目标为空，不存在通过检查的图。

**限制保持目标。** `restrict(f,S)` 要求 $S\subseteq A$，返回

$$
f|_S=(S,B,G|_S),\qquad
G|_S=\{(x,y)\in G:x\in S\}.
$$

目标仍是 $B$。例如将 $A$ 上的恒等函数限制到真子集 $S$，目标仍为 $A$，不能忽略目标把它直接等同于 $S$ 上的恒等函数。

**中间集合须完全匹配的复合接口。** 给定 $f:A\to B$ 与 $g:B\to C$，`compose(g,f)` 返回从 $A$ 到 $C$ 的函数，图为

$$
G_{g\circ f}=\{(x,g(f(x))):x\in A\}.
$$

程序检查 `f.codomain == g.domain`，而不只是检查实际像包含在后函数定义域中；中间集合不相等时，即使逐点求值看似可行，本接口仍拒绝。这里只实现正文当前选定的复合约定，不宣称其他像相容的复合约定不可能。`identity(A)` 返回 $(A,A,\{(x,x):x\in A\})$。限制与复合逐一遍历有限输入集合，求值只扫描有限图，因此所有这些过程有限完成；一般函数的恒等、结合及限制相容性由正文论证。

独立有限检查入口为 `tools/validate_finite_functions.py`，在声明的三个小集合之间枚举全部函数表，以独立字典与明确的域、目标比较作核对。结果保存在 `research/production/finite_functions_validation.json`，绑定本体和检验程序两份源码哈希。主构建校验另直接检查有限函数表和具体案例，仍不能把有限成功推广为一般定理。以下完整列出源码。

```python
"""
    return text + (ROOT / "tools/finite_functions.py").read_text() + "\n```\n"


def finite_function_inverses_appendix():
    text = r"""

# 附录十五 有限双射、逆函数与原像 {#finite-function-inverses-code}

本附录对应[单射、满射与双射](#bij-unit)和[逆函数](#inv-unit)。它复用[附录十四](#finite-functions-code)的 `FiniteFunction`、集合标签检查与函数检查；该附录已完整列出域、目标、图的存储与验证代码。这里只处理显式有限整数标签，不表示全体有理数或实数上的函数，不把有限检查当作一般证明。

**三个性质。** 对已验证的 $f:A\to B$，程序按以下定义返回逻辑值：

$$
\begin{aligned}
\text{单射：}&\quad \forall x_1,x_2\in A,\quad
 f(x_1)=f(x_2)\Longrightarrow x_1=x_2;\\
\text{满射：}&\quad \forall y\in B,\quad
 \exists x\in A,\ f(x)=y;\\
\text{双射：}&\quad f\text{ 同时是单射和满射。}
\end{aligned}
$$

`injective(f)` 检查不同图对是否重复使用输出；合法图已保证一个输入只有一个输出，因此这等价于上述单射判据。`surjective(f)` 比较像与声明的目标集合是否相等，`bijective(f)` 合取这两个判断。目标是数据的一部分：同一图扩大目标后可能不再满射。空域到空目标的函数是双射；空域到非空目标的函数是单射但不是满射。

**逆函数只接收双射。** `inverse(f)` 先核查双射，再返回

$$
f^{-1}=(B,A,G^{-1}),\qquad
G^{-1}=\{(y,x):(x,y)\in G\}.
$$

存在性由满射给出，唯一性由单射给出；该一般论证在正文完成，程序仅把有限表的箭头反转并复用函数构造器检查。非双射输入直接拒绝，不任意选取一个原像，也不把函数逆写成输出值的倒数。原函数输出零不妨碍双射的逆函数存在。

**集合原像不要求可逆。** `preimage(f,T)` 要求 $T\subseteq B$，返回有限集合

$$
f^{-1}[T]=\{x\in A:f(x)\in T\}.
$$

这个接口不返回函数。即使 $f$ 非单射或非满射，原像仍有定义；$T$ 为空时原像为空，$T=B$ 时原像为 $A$。接口拒绝目标以外元素、布尔值、非整数标签及非显式集合容器；所有函数接口拒绝未验证的函数对象。有限遍历终止不依赖选择公理，也不证明无限集合上任意满射存在右逆。

独立有限检查入口为 `tools/validate_finite_function_inverses.py`，枚举 $\{0,1\}$ 的全部子集之间的全部函数，以量词定义及独立字典核查三种性质、逆图、双侧恒等、复合逆的反序、单侧逆的必要条件及全部目标子集的原像。报告 `research/production/finite_function_inverses_validation.json` 绑定本模块、检查程序与所依赖的 `finite_functions.py` 三份源码哈希。主构建验收还直接重算这些有限模型并核查非法输入；有限结果不替代正文的一般证明。以下完整列出新增模块源码。

```python
"""
    return text + (ROOT / "tools/finite_function_inverses.py").read_text() + "\n```\n"


def linear_equation_solvers_appendix():
    text = r"""

# 附录十六 有理数一次方程与方程组求解 {#linear-equation-solvers-code}

本附录对应[一元一次方程](#lin-unit)与[二元一次方程组](#sys-unit)。下面完整列出 `tools/linear_equation_solvers.py`。程序依赖Python标准库 `fractions.Fraction` 进行精确有理数运算，不使用浮点近似；它不是本书已构造的有理数商集本身，也不替代正文关于解集与等价变形的一般证明。此前附录的整数、有理数及函数模块保持原样，本模块没有调用它们。

**输入范围与责任。** 每个系数只接收Python精确整数或 `Fraction` 值，布尔值、浮点数、字符串及整数对记录均拒绝。未知数遍历全体 $\mathbb Q$；模块不解析任意代数式，不自动清除含未知数的分母，也不自动记录或筛选用户另给的定义域限制。若原问题排除了某些值，调用者仍须对照原问题筛选并代回。

**一元全部分支。** `solve_linear(a,b,c)` 求解 $ax+b=c$，先把输入转换成精确有理数。若 $a\ne0$，唯一解为

$$
x=\frac{c-b}{a}.
$$

若 $a=0$ 且 $b=c$，返回全体有理数；若 $a=0$ 且 $b\ne c$，返回空解集。返回字典的 `kind` 分别为 `unique`、`all`、`none`；唯一解由 `value` 保存。程序不会把零系数分支当作可以除以零的普通公式。

**二元消元。** `solve_system(a,b,c,d,e,f)` 求解

$$
\begin{cases}
ax+by=c,\\
dx+ey=f.
\end{cases}
$$

若第一式的两个未知数系数均为零，先判断常数是否矛盾；恒等时再看第二式是否也为恒等或矛盾，必要时交换两式。第一式非零后，若 $a\ne0$，保留第一式，以第二式减去第一式的 $d/a$ 倍，得到

$$
\left(e-\frac{db}{a}\right)y=f-\frac{dc}{a}.
$$

该变形能由加回同一倍数恢复。左端系数非零时先求 $y$ 再代回求 $x$；系数为零但右端非零时无解；两者均零时以 $y=t$ 为自由参数，得到全部解

$$
(x,y)=\left(\frac ca-\frac ba t,t\right),\qquad t\in\mathbb Q.
$$

若 $a=0$，此时已经知道 $b\ne0$，故先得 $y=c/b$，再判断第二式的 $x$ 系数 $d$。$d\ne0$ 时有唯一 $x$；$d=0$ 时按 $f-ey$ 是否为零，区分无解与 $x$ 自由。每一次除法之前均核对分母非零。

**解集的返回记录。** `kind` 为 `unique` 时，`point` 是唯一有理数对；`none` 表示空集；`all` 表示全体 $\mathbb Q^2$。`line` 是程序标签，`base` 与非零 `direction` 表示

$$
\{(p_1+t u_1,p_2+t u_2):t\in\mathbb Q\}.
$$

这里只定义一个有理数对的参数集合，不借标签宣称已建立坐标直线或交点理论。参数化包含所有满足两原式的有理数对，双向说明由正文的可逆消元给出；抽查若干参数只能核对程序实例。

独立入口 `tools/validate_linear_equation_solvers.py` 使用外部SymPy 1.14.0的精确解集、矩阵秩及逆矩阵作有限oracle，并以 `Fraction` 代回原式。SymPy仅是检查工具，不是正文的先修证明依据；版本固定在 `requirements-build.txt`。报告 `research/production/linear_equation_solvers_validation.json` 绑定本模块及独立检查程序两份源码。主构建验收另直接用精确增广行化简核对各返回分支、参数集合、交换两式和非法输入；有限检查不能证明对任意有理数系数的一般命题。

```python
"""
    return text + (ROOT / "tools/linear_equation_solvers.py").read_text() + "\n```\n"


def rational_inequalities_appendix():
    text = r"""

# 附录十七 有理数不等式的精确区间求解 {#rational-inequalities-code}

本附录对应[一次不等式](#ineq-unit)与[绝对值不等式](#absineq-unit)，完整列出 `tools/rational_inequalities.py`。它复用[附录十六](#linear-equation-solvers-code)已完整列出的 `linear_equation_solvers.rational`，借Python标准库 `fractions.Fraction` 做精确有理数运算。两个求解器的系数输入及 `contains` 的待检验值仅接收精确整数或 `Fraction`，拒绝布尔值、浮点数、字符串及整数对记录；不使用浮点近似。内部辅助函数 `compare` 只核验比较符号，数值类型由调用它的求解器预先检查。

**定义域与返回记录。** 未知数遍历全体 $\mathbb Q$。`solve_linear(a,b,c,relation)` 求 $ax+b$ 与 $c$ 的比较；`solve_absolute(a,b,radius,relation)` 求 $|ax+b|$ 与比较值 $r$ 的比较，参数名 `radius` 也允许负值。`relation` 仅接收 `<`、`<=`、`>`、`>=` 四个字符串，不接收等号。程序不解析任意代数式、不自动排除原分母禁值，也不筛选另给的允许范围 $D$；此时调用者须把所得集合与 $D$ 取交。

返回值是若干区间记录组成的元组，表示这些有理区间的并；空元组表示空集。每条记录为 `(lower, upper, left_closed, right_closed)`，有限端点必须是精确有理数，两个逻辑值标记是否包含对应端点。`None` 只标记该侧无界，不是可参与运算的数；无界侧的闭端标记为假。双侧无界记录表示全体有理数；两端相等且都闭合的记录表示单点集。`contains(solution,value)` 以这些成员条件判断有理数是否属于解集，仅用于两个求解器产生的记录，不是任意外来记录的解析器或合法性校验器。

**一次不等式。** 若 $a=0$，直接比较 $b$ 与 $c$，返回全体有理数或空集；非严格和严格比较分别判断，不能混同。当 $a\ne0$ 时置

$$
t=\frac{c-b}{a}.
$$

$a>0$ 时保留比较方向，$a<0$ 时反向；严格比较排除端点，非严格比较包含端点。例如 $ax+b<c$ 在 $a>0$ 时返回 $(-\infty,t)_{\mathbb Q}$，在 $a<0$ 时返回 $(t,+\infty)_{\mathbb Q}$。另外三种比较按相同符号规则与各自端点条件处理。任何除法只出现在已核实 $a\ne0$ 的分支。

**绝对值条件。** 首先处理 $a=0$，按 $|b|$ 与 $r$ 的比较返回全体或空集。其余分支中 $a\ne0$，令 $h=-b/a$。若 $r<0$，小于和不大于的解集为空，大于和不小于的解集为全体有理数。若 $r=0$，四种比较分别为

$$
\begin{array}{c|c|c|c|c}
\text{比较}&< &\le &> &\ge\\\hline
\text{解集}&\varnothing&\{h\}&\{x\in\mathbb Q:x\ne h\}&\mathbb Q
\end{array}
$$

若 $r>0$，由 $|ax+b|=|a|\,|x-h|$，置 $w=r/|a|>0$、$l=h-w$、$u=h+w$。内侧两种解集为 $(l,u)_{\mathbb Q}$ 和 $[l,u]_{\mathbb Q}$；外侧两种解集为

$$
\begin{aligned}
|ax+b|>r&:\quad(-\infty,l)_{\mathbb Q}\cup(u,+\infty)_{\mathbb Q},\\
|ax+b|\ge r&:\quad(-\infty,l]_{\mathbb Q}\cup[u,+\infty)_{\mathbb Q}.
\end{aligned}
$$

负系数不产生负半径：程序除以 $|a|$，而非直接以 $a$ 作半宽。内侧的两个条件须同时成立，外侧是至少一个成立。这里全是有理数成员条件，不借助实数连续线段或尚未建立的几何理论。

独立检查入口 `tools/validate_rational_inequalities.py` 采用已固定的SymPy 1.14.0精确实区间并集作有限外部oracle。全部有限端点是有理数；实区间并集相等蕴含其限制到有理数后相等，不表示本书已构造实数。报告 `research/production/rational_inequalities_validation.json` 绑定本模块、检查程序及所依赖的旧方程模块三份源码。主构建验收另按原条件的全部断点及返回端点划分有理数域，直接检查端点和每段成员条件，并复核非法输入与另给允许范围的显式筛选。两种检查均只覆盖有限系数实例，不能替代正文的一般证明；本项目未运行Lean。

```python
"""
    return text + (ROOT / "tools/rational_inequalities.py").read_text() + "\n```\n"


def rational_affine_appendix():
    text = r"""

# 附录十八 有理坐标与仿射函数的精确计算 {#rational-affine-code}

本附录对应[有理坐标](#coord-unit)与[仿射函数图像](#affgraph-unit)，完整列出 `tools/rational_affine.py`。数值计算依赖Python标准库 `fractions.Fraction`，输入转换复用[附录十六](#linear-equation-solvers-code)完整列出的 `linear_equation_solvers.rational`。以下六个接口的数值参数只接受精确整数或 `Fraction`，拒绝布尔值、浮点数、字符串及非数值记录。有限点集容器另按下述规则检查。程序不构造实平面，不使用浮点近似，不把有限画点当作全部有理图像的证明。

**求值与两点确定。** `affine_value(a,b,x)` 返回精确有理数 $ax+b$，函数的定义域及目标集合均为 $\mathbb Q$。`slope_through(x1,y1,x2,y2)` 只在 $x_1\ne x_2$ 时返回系数对

$$
a=\frac{y_2-y_1}{x_2-x_1},\qquad b=y_1-ax_1.
$$

返回的是 $(a,b)$，不是给定点的坐标。代回两点核对存在，相减并消去非零横坐标差核对唯一，证明见正文。$x_1=x_2$ 时接口一律拒绝：纵坐标相同只给一个点，不能确定唯一系数；纵坐标不同则没有函数图同时经过这两点。程序不为这两种情况擅自选择系数，也不把竖直斜率记为无穷大。

**两轴交集。** `intercepts(a,b)` 返回 `vertical` 为 $(0,b)$。`horizontal_kind` 在 $a\ne0$ 时为 `unique`，并以 `horizontal` 保存 $(-b/a,0)$；$a=0,b\ne0$ 时为 `none`；$a=b=0$ 时为 `all`。后两种情况下 `horizontal` 均为 `None`，区别由标签给出。此处 `all` 只表示整条有理横轴 $\{(x,0):x\in\mathbb Q\}$，不表示全部有理数对；截点是有序对，不能与单个截距数混同。

**两图交集。** `intersect_affine(a,b,c,d)` 比较图 $y=ax+b$ 与 $y=cx+d$。若 $a\ne c$，返回 `kind='unique'`，`point` 为

$$
\left(\frac{d-b}{a-c},\ a\frac{d-b}{a-c}+b\right).
$$

若 $a=c,b=d$，返回 `coincident`；若 $a=c,b\ne d$，返回 `none`。后两种记录的 `point` 都为 `None`。重合表示两图的全部成员相同，不表示只有一个交点。接口求的是全有理定义域上的交集；两图另有限制域时，调用者须再核查共同输入是否属于两个允许范围。

**一次关系分类。** `classify_linear_relation(p,q,r)` 研究所有满足 $px+qy=r$ 的有理数对。$q\ne0$ 时返回 `affine` 与 $a=-p/q,b=r/q$；$q=0,p\ne0$ 时返回 `vertical` 与固定第一坐标 $x=r/p$，第二坐标可为任意有理数；$p=q=0$ 时根据 $r=0$ 或 $r\ne0$ 分别返回 `all` 或 `none`。这里的 `all` 才表示全部 $\mathbb Q^2$。各返回记录只保存本类需要的字段，不把竖直集合当成横坐标输入的函数图。

**有限函数图判别。** `finite_graph_test(domain,codomain,points)` 的三个容器须为列表、元组、集合或不可变集合；每个点须为长度二的列表或元组，坐标按精确有理数要求检查。重复域元素、目标元素和点记录按集合合并；所有输入先验证，非法形状或数值引发 `ValueError`。对于合法有限数据，令声明域为 $D$、目标为 $B$、点集为 $G$，返回真当且仅当

$$
G\subseteq D\times B\quad\text{且}\quad
\forall x\in D,\ \text{恰有一个 }y\in B\text{ 使 }(x,y)\in G.
$$

合法但位于声明域或目标以外的点使结果为假；某个声明输入没有输出也为假，不能只检验至多一个输出。空域与空图相容，空域却有点不相容。这个接口只判断全部给定的有限集合数据，不把无限函数的若干采样点误作完整函数图，也不从图擅自恢复唯一目标集合。

独立检查入口为 `tools/validate_rational_affine.py`，以已固定的SymPy 1.14.0精确求解原方程，并枚举给定小集合间的全部有限函数图。报告 `research/production/rational_affine_validation.json` 绑定本模块、检查程序与旧方程模块三份源码。主构建验收另用精确增广行化简核对完整有限实例的点或参数集合，以每个输入对应的输出个数核对有限函数图，并检查非法输入。SymPy与行化简是实现检查工具，不作为本书已教过的先修理论；有限核算只提供实现证据，不替代正文关于任意有理参数的证明。

```python
"""
    return text + (ROOT / "tools/rational_affine.py").read_text() + "\n```\n"


def rational_powers_sums_appendix():
    text = r"""

# 附录十九 非负整数幂与有限和的精确计算 {#rational-powers-sums-code}

本附录对应[有理数幂](#pow-unit)与[有限和](#sum-unit)，完整列出 `tools/rational_powers_sums.py`。数值运算使用Python标准库 `fractions.Fraction`，有理数输入检查复用[附录十六](#linear-equation-solvers-code)完整列出的 `linear_equation_solvers.rational`。底数与有限记录中的项只接受精确整数或 `Fraction`，拒绝布尔值、浮点数、字符串及非数值记录。指数和索引只接受非负的精确整数，布尔值及值恰好为整数的 `Fraction` 也不能作为索引。计算不使用浮点近似。

**幂的接口。** `power(base,exponent)` 对 $a\in\mathbb Q$、$n\in\mathbb N$ 从一开始，执行恰好 $n$ 次乘以固定底数 $a$，返回精确有理数。其规则为

$$
a^0=1,\qquad a^{n+1}=a^n a.
$$

空次迭代返回一，故包括 $0^0=1$；这是本书离散自然数幂的明确约定。零的正次幂为零，不能把这条正次结论套到零次。接口不接受负指数、分数指数或实指数，不作除零或极限推断。正文用已采用的递归原则给出定义，再用归纳证明指数律；有限循环只实现这些规则。

**完整前缀记录。** `partial_sums(values)` 只接受长度有限的列表或元组，先验证每一项，再返回元组 $(S_0,\ldots,S_n)$。若输入长度为 $n$，输出长度是 $n+1$，每项均为精确有理数，满足

$$
S_0=0,\qquad S_{i+1}=S_i+u_i\quad(0\le i<n).
$$

$S_i$ 是前 $i$ 项的和，不包含索引 $i$ 的项；空输入返回只含零的元组。`finite_sum(values)` 返回最后一个前缀值 $S_n$，空和为零。重复项分别占记录的位置并各加一次，不按集合去重。

**连续片段。** `segment_sum(values,start,count)` 中起始索引 $s$ 和项数 $k$ 必须满足

$$
0\le s\le n,\qquad k\ge0,\qquad s+k\le n.
$$

当 $k=0$ 时不取任何项，返回零，包括 $s=n,k=0$ 的末尾空段。当 $k>0$ 时，才列出所取索引 $s,s+1,\ldots,s+k-1$，返回这恰好 $k$ 项的和。非法越界直接拒绝，不由Python切片自动缩短。全部输入项在取段之前验证，因此即使非法项位于所选片段之外，也不会被忽略。由正文的拼接性质，返回值还等于 $S_{s+k}-S_s$；这给出独立核对接口结果的方法。

**有限范围。** `natural_index` 检查指数或索引，`finite_record` 检查并转换全部有限项，二者完整源码也列在下面。模块不接受无限序列、任意回调、迭代生成器、集合或字典作为有限记录；不会把若干项的和称为无限级数的和。正文一般前缀和的固定状态递归及表外延拓独立性仍须由正文证明，不能由列表计算替代。

独立检查入口为 `tools/validate_rational_powers_sums.py`。

报告位于 `research/production/` 目录，文件名为 `rational_powers_sums_validation.json`，绑定本模块、检查程序及旧方程模块三份源码。主构建验收实际重算精确幂、前缀和与片段和，并核查零次、空和、索引边界及非法输入。指数律、求和律的有限实例仅是实现证据，不替代任意有理底数、任意有限长度上的一般归纳证明。

```python
"""
    return text + (ROOT / "tools/rational_powers_sums.py").read_text() + "\n```\n"


def reuse_legacy_snapshot():
    """Verify unchanged dependencies and independent artifacts, not the newer full book."""
    manifest_path = BUILD / "build_inputs.json"
    snapshot_path = BUILD / "legacy_validation_snapshot.json"
    previous = json.loads(manifest_path.read_text())
    snapshot_digest = hashlib.sha256(snapshot_path.read_bytes()).hexdigest()
    if previous.get("legacy_snapshot_sha256") != snapshot_digest:
        raise ValueError("Legacy snapshot differs from prior manifest; cannot reuse")
    previous_sources = previous["source_sha256"]
    dependencies = legacy_source_hashes()
    dependencies.update(hashes([ROOT / "tools/validate_ch01_review.py",
                               ROOT / "tools/validate_catalog_chinese.py",
                               ROOT / "tools/review_artifacts.py"]))
    changed = [path for path, digest in dependencies.items()
               if previous_sources.get(path) != digest]
    if changed:
        raise ValueError("Legacy inputs changed; run a full build: " + ", ".join(changed))
    legacy = json.loads(snapshot_path.read_text())
    if legacy.get("status") != "automated_checks_passed":
        raise ValueError("The preserved legacy snapshot did not pass validation")
    independent = {path: digest for path, digest in legacy["artifact_sha256"].items()
                   if path not in {"dist/综合数学" + ext for ext in [".md", ".pdf", ".html"]}}
    if not independent:
        raise ValueError("Legacy snapshot has no independent artifacts")
    actual = hashes([ROOT / path for path in independent])
    if actual != independent:
        raise ValueError("Independent legacy artifacts changed; run a full build")
    return legacy, {"mode": "validated_snapshot_reuse", "legacy_source_sha256": dependencies,
                    "independent_artifact_sha256": actual,
                    "prior_manifest_sha256": hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
                    "snapshot_sha256": snapshot_digest}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    reuse = parser.add_mutually_exclusive_group()
    reuse.add_argument("--reuse-legacy-validation", action="store_true")
    reuse.add_argument("--incremental", action="store_true",
                       help="Reuse only hash-verified legacy chapter and catalogue artifacts")
    args = parser.parse_args()
    BUILD.mkdir(parents=True, exist_ok=True)
    (OUT / "figures").mkdir(parents=True, exist_ok=True)
    inputs = source_hashes()  # Fail before a costly build if any needed source is absent.
    os.environ["XDG_CACHE_HOME"] = str(BUILD / "fontcache")
    (BUILD / "fontcache").mkdir(exist_ok=True)
    legacy_reuse = {"mode": "fresh_legacy_validation"}
    if args.incremental:
        legacy, legacy_reuse = reuse_legacy_snapshot()
        cached_manifest = BUILD / "legacy_reuse_inputs.json"
        shutil.copy2(BUILD / "build_inputs.json", cached_manifest)
        legacy_reuse["prior_manifest_path"] = str(cached_manifest.relative_to(ROOT))
    elif not args.reuse_legacy_validation:
        run([sys.executable, "tools/build_ch01_review.py"], BUILD / "legacy-build.log")
        run([sys.executable, "tools/validate_catalog_chinese.py"], BUILD / "legacy-catalog-validation.log")
        run([sys.executable, "tools/validate_ch01_review.py"], BUILD / "legacy-validation.log")
    if not args.incremental:
        check_build_inputs()
        legacy = json.loads((ROOT / "data/ch01_validation.json").read_text())
        if (legacy.get("status") != "automated_checks_passed"
                or legacy.get("artifact_sha256") != legacy_artifact_hashes()):
            raise ValueError("Legacy artifacts are not freshly validated; run without --reuse-legacy-validation")
        (BUILD / "legacy_validation_snapshot.json").write_text(json.dumps(legacy, ensure_ascii=False, indent=2) + "\n")
    run([sys.executable, "tools/draw_foundations_batch.py"], BUILD / "figures.log")
    # Preserve an independently reviewed result when every tested dependency is
    # unchanged; a timestamp-only rerun would invalidate that review's report hash.
    written_dependencies = hashes([ROOT / "tools" / name for name in
        ["written_arithmetic.py", "natural_algorithms.py", "validate_written_arithmetic.py"]])
    written_result = json.loads(WRITTEN_REPORT.read_text()) if WRITTEN_REPORT.exists() else {}
    written_reused = (written_result.get("result") == "pass"
                      and written_result.get("source_sha256") == written_dependencies)
    if not written_reused:
        run([sys.executable, "tools/validate_written_arithmetic.py"], BUILD / "written-arithmetic-validation.log")
        written_result = json.loads(WRITTEN_REPORT.read_text())
    if (written_result.get("result") != "pass"
            or written_result.get("source_sha256") != written_dependencies):
        raise ValueError("Written-arithmetic report does not match the tested sources")
    integer_dependencies = hashes([ROOT / "tools" / name for name in
        ["integer_pairs.py", "validate_integer_pairs.py"]])
    integer_result = json.loads(INTEGER_REPORT.read_text()) if INTEGER_REPORT.exists() else {}
    integer_reused = (integer_result.get("result") == "pass"
                      and integer_result.get("source_sha256") == integer_dependencies)
    if not integer_reused:
        run([sys.executable, "tools/validate_integer_pairs.py"], BUILD / "integer-pairs-validation.log")
        integer_result = json.loads(INTEGER_REPORT.read_text())
    if (integer_result.get("result") != "pass"
            or integer_result.get("source_sha256") != integer_dependencies):
        raise ValueError("Integer-pair report does not match the tested sources")
    euclidean_dependencies = hashes([ROOT / "tools" / name for name in
        ["integer_euclidean.py", "validate_integer_euclidean.py", "natural_algorithms.py"]])
    euclidean_result = json.loads(EUCLIDEAN_REPORT.read_text()) if EUCLIDEAN_REPORT.exists() else {}
    euclidean_reused = (euclidean_result.get("status") == "passed"
                        and euclidean_result.get("source_sha256") == euclidean_dependencies)
    if not euclidean_reused:
        run([sys.executable, "tools/validate_integer_euclidean.py"], BUILD / "integer-euclidean-validation.log")
        euclidean_result = json.loads(EUCLIDEAN_REPORT.read_text())
    if (euclidean_result.get("status") != "passed"
            or euclidean_result.get("source_sha256") != euclidean_dependencies):
        raise ValueError("Integer Euclidean report does not match the tested sources")
    extended_dependencies = hashes([ROOT / "tools" / name for name in
        ["extended_euclidean.py", "validate_extended_euclidean.py", "integer_euclidean.py", "natural_algorithms.py"]])
    extended_result = json.loads(EXTENDED_REPORT.read_text()) if EXTENDED_REPORT.exists() else {}
    extended_reused = (extended_result.get("status") == "passed"
                       and extended_result.get("source_sha256") == extended_dependencies)
    if not extended_reused:
        run([sys.executable, "tools/validate_extended_euclidean.py"], BUILD / "extended-euclidean-validation.log")
        extended_result = json.loads(EXTENDED_REPORT.read_text())
    if (extended_result.get("status") != "passed"
            or extended_result.get("source_sha256") != extended_dependencies):
        raise ValueError("Extended Euclidean report does not match the tested sources")
    rational_dependencies = hashes([ROOT / "tools" / name for name in
        ["rational_addition.py", "validate_rational_addition.py", "extended_euclidean.py",
         "integer_euclidean.py", "natural_algorithms.py"]])
    rational_result = json.loads(RATIONAL_REPORT.read_text()) if RATIONAL_REPORT.exists() else {}
    rational_reused = (rational_result.get("status") == "passed"
                       and rational_result.get("source_sha256") == rational_dependencies)
    if not rational_reused:
        run([sys.executable, "tools/validate_rational_addition.py"], BUILD / "rational-addition-validation.log")
        rational_result = json.loads(RATIONAL_REPORT.read_text())
    if (rational_result.get("status") != "passed"
            or rational_result.get("source_sha256") != rational_dependencies):
        raise ValueError("Rational addition report does not match the tested sources")
    multiplication_dependencies = hashes([ROOT / "tools" / name for name in
        ["rational_multiplication.py", "validate_rational_multiplication.py", "rational_addition.py",
         "extended_euclidean.py", "integer_euclidean.py", "natural_algorithms.py"]])
    multiplication_result = (json.loads(RATIONAL_MULTIPLICATION_REPORT.read_text())
                             if RATIONAL_MULTIPLICATION_REPORT.exists() else {})
    multiplication_reused = (multiplication_result.get("status") == "passed"
                             and multiplication_result.get("source_sha256") == multiplication_dependencies)
    if not multiplication_reused:
        run([sys.executable, "tools/validate_rational_multiplication.py"], BUILD / "rational-multiplication-validation.log")
        multiplication_result = json.loads(RATIONAL_MULTIPLICATION_REPORT.read_text())
    if (multiplication_result.get("status") != "passed"
            or multiplication_result.get("source_sha256") != multiplication_dependencies):
        raise ValueError("Rational multiplication report does not match the tested sources")
    order_dependencies = hashes([ROOT / "tools" / name for name in
        ["rational_order.py", "validate_rational_order.py", "rational_multiplication.py",
         "rational_addition.py", "extended_euclidean.py", "integer_euclidean.py", "natural_algorithms.py"]])
    order_result = json.loads(RATIONAL_ORDER_REPORT.read_text()) if RATIONAL_ORDER_REPORT.exists() else {}
    order_reused = (order_result.get("status") == "passed"
                   and order_result.get("source_sha256") == order_dependencies)
    if not order_reused:
        run([sys.executable, "tools/validate_rational_order.py"], BUILD / "rational-order-validation.log")
        order_result = json.loads(RATIONAL_ORDER_REPORT.read_text())
    if (order_result.get("status") != "passed" or order_result.get("source_sha256") != order_dependencies):
        raise ValueError("Rational order report does not match the tested sources")
    ratios_dependencies = hashes([ROOT / "tools" / name for name in
        ["ratios_units.py", "validate_ratios_units.py", "rational_multiplication.py",
         "rational_addition.py", "extended_euclidean.py", "integer_euclidean.py", "natural_algorithms.py"]])
    ratios_result = json.loads(RATIOS_UNITS_REPORT.read_text()) if RATIOS_UNITS_REPORT.exists() else {}
    ratios_reused = (ratios_result.get("status") == "passed"
                    and ratios_result.get("source_sha256") == ratios_dependencies)
    if not ratios_reused:
        run([sys.executable, "tools/validate_ratios_units.py"], BUILD / "ratios-units-validation.log")
        ratios_result = json.loads(RATIOS_UNITS_REPORT.read_text())
    if (ratios_result.get("status") != "passed" or ratios_result.get("source_sha256") != ratios_dependencies):
        raise ValueError("Ratios and units report does not match the tested sources")
    functions_dependencies = hashes([ROOT / "tools" / name for name in
        ["finite_functions.py", "validate_finite_functions.py"]])
    functions_result = json.loads(FINITE_FUNCTIONS_REPORT.read_text()) if FINITE_FUNCTIONS_REPORT.exists() else {}
    functions_reused = (functions_result.get("status") == "passed"
                        and functions_result.get("source_sha256") == functions_dependencies)
    if not functions_reused:
        run([sys.executable, "tools/validate_finite_functions.py"], BUILD / "finite-functions-validation.log")
        functions_result = json.loads(FINITE_FUNCTIONS_REPORT.read_text())
    if (functions_result.get("status") != "passed"
            or functions_result.get("source_sha256") != functions_dependencies):
        raise ValueError("Finite functions report does not match the tested sources")
    inverse_dependencies = hashes([ROOT / "tools" / name for name in
        ["finite_functions.py", "finite_function_inverses.py", "validate_finite_function_inverses.py"]])
    inverse_result = (json.loads(FINITE_FUNCTION_INVERSES_REPORT.read_text())
                      if FINITE_FUNCTION_INVERSES_REPORT.exists() else {})
    inverse_reused = (inverse_result.get("status") == "passed"
                      and inverse_result.get("source_sha256") == inverse_dependencies)
    if not inverse_reused:
        run([sys.executable, "tools/validate_finite_function_inverses.py"],
            BUILD / "finite-function-inverses-validation.log")
        inverse_result = json.loads(FINITE_FUNCTION_INVERSES_REPORT.read_text())
    if (inverse_result.get("status") != "passed"
            or inverse_result.get("source_sha256") != inverse_dependencies):
        raise ValueError("Finite function inverses report does not match the tested sources")
    linear_dependencies = hashes([ROOT / "tools" / name for name in
        ["linear_equation_solvers.py", "validate_linear_equation_solvers.py"]])
    linear_result = (json.loads(LINEAR_EQUATION_SOLVERS_REPORT.read_text())
                     if LINEAR_EQUATION_SOLVERS_REPORT.exists() else {})
    linear_reused = (linear_result.get("status") == "passed"
                     and linear_result.get("source_sha256") == linear_dependencies)
    if not linear_reused:
        run([sys.executable, "tools/validate_linear_equation_solvers.py"],
            BUILD / "linear-equation-solvers-validation.log")
        linear_result = json.loads(LINEAR_EQUATION_SOLVERS_REPORT.read_text())
    if (linear_result.get("status") != "passed"
            or linear_result.get("source_sha256") != linear_dependencies):
        raise ValueError("Linear equation solver report does not match the tested sources")
    inequalities_dependencies = hashes([ROOT / "tools" / name for name in
        ["linear_equation_solvers.py", "rational_inequalities.py", "validate_rational_inequalities.py"]])
    inequalities_result = (json.loads(RATIONAL_INEQUALITIES_REPORT.read_text())
                           if RATIONAL_INEQUALITIES_REPORT.exists() else {})
    inequalities_reused = (inequalities_result.get("status") == "passed"
                           and inequalities_result.get("source_sha256") == inequalities_dependencies)
    if not inequalities_reused:
        run([sys.executable, "tools/validate_rational_inequalities.py"],
            BUILD / "rational-inequalities-validation.log")
        inequalities_result = json.loads(RATIONAL_INEQUALITIES_REPORT.read_text())
    if (inequalities_result.get("status") != "passed"
            or inequalities_result.get("source_sha256") != inequalities_dependencies):
        raise ValueError("Rational inequalities report does not match the tested sources")
    affine_dependencies = hashes([ROOT / "tools" / name for name in
        ["linear_equation_solvers.py", "rational_affine.py", "validate_rational_affine.py"]])
    affine_result = (json.loads(RATIONAL_AFFINE_REPORT.read_text())
                     if RATIONAL_AFFINE_REPORT.exists() else {})
    affine_reused = (affine_result.get("status") == "passed"
                     and affine_result.get("source_sha256") == affine_dependencies)
    if not affine_reused:
        run([sys.executable, "tools/validate_rational_affine.py"],
            BUILD / "rational-affine-validation.log")
        affine_result = json.loads(RATIONAL_AFFINE_REPORT.read_text())
    if (affine_result.get("status") != "passed"
            or affine_result.get("source_sha256") != affine_dependencies):
        raise ValueError("Rational affine report does not match the tested sources")
    powers_sums_dependencies = hashes([ROOT / "tools" / name for name in
        ["linear_equation_solvers.py", "rational_powers_sums.py", "validate_rational_powers_sums.py"]])
    powers_sums_result = (json.loads(RATIONAL_POWERS_SUMS_REPORT.read_text())
                          if RATIONAL_POWERS_SUMS_REPORT.exists() else {})
    powers_sums_reused = (powers_sums_result.get("status") == "passed"
                          and powers_sums_result.get("source_sha256") == powers_sums_dependencies)
    if not powers_sums_reused:
        run([sys.executable, "tools/validate_rational_powers_sums.py"],
            BUILD / "rational-powers-sums-validation.log")
        powers_sums_result = json.loads(RATIONAL_POWERS_SUMS_REPORT.read_text())
    if (powers_sums_result.get("status") != "passed"
            or powers_sums_result.get("source_sha256") != powers_sums_dependencies):
        raise ValueError("Rational powers and sums report does not match the tested sources")
    polynomial_dependencies = hashes([ROOT / "tools" / name for name in
        ["linear_equation_solvers.py", "rational_powers_sums.py", "rational_polynomial_basic.py",
         "validate_rational_polynomial_basic.py"]])
    polynomial_result = (json.loads(RATIONAL_POLYNOMIAL_BASIC_REPORT.read_text())
                         if RATIONAL_POLYNOMIAL_BASIC_REPORT.exists() else {})
    polynomial_reused = (polynomial_result.get("status") == "passed"
                         and polynomial_result.get("source_sha256") == polynomial_dependencies)
    if not polynomial_reused:
        run([sys.executable, "tools/validate_rational_polynomial_basic.py"],
            BUILD / "rational-polynomial-basic-validation.log")
        polynomial_result = json.loads(RATIONAL_POLYNOMIAL_BASIC_REPORT.read_text())
    if (polynomial_result.get("status") != "passed"
            or polynomial_result.get("source_sha256") != polynomial_dependencies):
        raise ValueError("Rational polynomial report does not match the tested sources")
    product_dependencies = hashes([ROOT / "tools" / name for name in
        ["linear_equation_solvers.py", "rational_powers_sums.py", "rational_polynomial_basic.py",
         "rational_polynomial_product.py", "validate_rational_polynomial_product.py"]])
    product_result = (json.loads(RATIONAL_POLYNOMIAL_PRODUCT_REPORT.read_text())
                      if RATIONAL_POLYNOMIAL_PRODUCT_REPORT.exists() else {})
    product_reused = (product_result.get("status") == "passed"
                      and product_result.get("source_sha256") == product_dependencies)
    if not product_reused:
        run([sys.executable, "tools/validate_rational_polynomial_product.py"],
            BUILD / "rational-polynomial-product-validation.log")
        product_result = json.loads(RATIONAL_POLYNOMIAL_PRODUCT_REPORT.read_text())
    if (product_result.get("status") != "passed"
            or product_result.get("source_sha256") != product_dependencies):
        raise ValueError("Rational polynomial product report does not match the tested sources")
    division_dependencies = hashes([ROOT / "tools" / name for name in
        ["linear_equation_solvers.py", "rational_powers_sums.py", "rational_polynomial_basic.py",
         "rational_polynomial_product.py", "rational_polynomial_linear_division.py",
         "validate_rational_polynomial_linear_division.py"]])
    division_result = (json.loads(RATIONAL_POLYNOMIAL_LINEAR_DIVISION_REPORT.read_text())
                       if RATIONAL_POLYNOMIAL_LINEAR_DIVISION_REPORT.exists() else {})
    division_reused = (division_result.get("status") == "passed"
                       and division_result.get("source_sha256") == division_dependencies)
    if not division_reused:
        run([sys.executable, "tools/validate_rational_polynomial_linear_division.py"],
            BUILD / "rational-polynomial-linear-division-validation.log")
        division_result = json.loads(RATIONAL_POLYNOMIAL_LINEAR_DIVISION_REPORT.read_text())
    if (division_result.get("status") != "passed"
            or division_result.get("source_sha256") != division_dependencies):
        raise ValueError("Rational linear polynomial division report does not match the tested sources")
    quadratic_dependencies = hashes([ROOT / "tools" / name for name in
        ["linear_equation_solvers.py", "rational_quadratics.py", "validate_rational_quadratics.py"]])
    quadratic_result = (json.loads(RATIONAL_QUADRATICS_REPORT.read_text())
                        if RATIONAL_QUADRATICS_REPORT.exists() else {})
    quadratic_reused = (quadratic_result.get("status") == "passed"
                        and quadratic_result.get("source_sha256") == quadratic_dependencies)
    if not quadratic_reused:
        run([sys.executable, "tools/validate_rational_quadratics.py"],
            BUILD / "rational-quadratics-validation.log")
        quadratic_result = json.loads(RATIONAL_QUADRATICS_REPORT.read_text())
    if (quadratic_result.get("status") != "passed"
            or quadratic_result.get("source_sha256") != quadratic_dependencies):
        raise ValueError("Rational quadratics report does not match the tested sources")
    for name in FIGURES:
        if not (OUT / "figures" / name).is_file():
            raise FileNotFoundError("Missing generated figure: " + name)
    shutil.copy2(ROOT / "tools/style.css", OUT / "style.css")
    metadata = "---\ntitle: 综合数学\nauthor: Leo Lee\nlang: zh-CN\n---\n\n"
    body = compose_body()
    catalog = catalog_with_unique_ids((OUT / "综合数学_完整数学目录.md").read_text())
    for stem, text in [(REVIEW_STEM, metadata + body), ("综合数学", metadata + catalog + body)]:
        (OUT / (stem + ".md")).write_text(text)
    header = (ROOT / "tools/pdf_header.tex").read_text().replace("第一批工作稿", "基础续写审阅稿")
    # Keep the cited author's Czech spelling with the existing Latin fallback.
    header += '\n\\newunicodechar{ř}{{\\cataloglatinfont\\char"0159}}\n'
    header += "\n\\usepackage{float}\n\\floatplacement{figure}{H}\n\\postdisplaypenalty=10000\n"
    # Restrict modest TOC compaction to this generated batch, leaving legacy
    # artifacts and teaching-body typography untouched. Inspect the final pages.
    header += r"""
\usepackage[titles]{tocloft}
\let\batchtableofcontents\tableofcontents
\renewcommand{\tableofcontents}{%
  \begingroup
  \fontsize{10.5}{12.5}\selectfont
  \setlength{\parskip}{0pt}
  \setlength{\cftbeforesecskip}{5pt}
  \widowpenalty=10000\clubpenalty=10000
  \batchtableofcontents
  \endgroup}
"""
    (BUILD / "header.tex").write_text(header)
    common = ["pandoc", "--standalone", "--resource-path=.:dist", "--pdf-engine=xelatex",
              "-V", "mainfont=Noto Serif CJK SC", "-V", "sansfont=Noto Sans CJK SC",
              "-V", "monofont=Noto Sans Mono CJK SC", "-V", "monofontoptions=AutoFakeSlant=0.15",
              "-V", "geometry:margin=22mm", "-V", "fontsize=11pt", "-V", "colorlinks=true",
              "-V", "linkcolor=blue", "-H", str(BUILD / "header.tex")]
    for stem in NEW_STEMS:
        path = OUT / (stem + ".md")
        depth = "2" if stem == REVIEW_STEM else "1"
        run(common + [str(path), "--toc", "--toc-depth=" + depth, "-o", str(OUT / (stem + ".pdf"))],
            BUILD / (stem + ".log"))
        run(["pandoc", str(path), "--standalone", "--toc", "--toc-depth=" + depth,
             "--resource-path=.:dist", "--mathml", "--embed-resources", "--css=dist/style.css",
             "-o", str(OUT / (stem + ".html"))], BUILD / (stem + "-html.log"))
    if source_hashes() != inputs:
        raise RuntimeError("Source files changed during the build; rebuild once editing is complete")
    manifest = {"schema_version": 1, "built_at": datetime.now(timezone.utc).isoformat(),
                "build_command": shlex.join([sys.executable, "tools/build_learning_batch.py"] + sys.argv[1:]),
                "source_sha256": inputs, "artifact_sha256": artifact_hashes(),
                "legacy_validation_order": "verified_before_combined_book_assembly",
                "legacy_reuse": legacy_reuse,
                "written_arithmetic_validation": {"mode": "matching_source_report_reuse" if written_reused else "executed",
                    "report_sha256": hashes([WRITTEN_REPORT]), "source_sha256": written_dependencies},
                "integer_pairs_validation": {"mode": "matching_source_report_reuse" if integer_reused else "executed",
                    "report_sha256": hashes([INTEGER_REPORT]), "source_sha256": integer_dependencies},
                "integer_euclidean_validation": {"mode": "matching_source_report_reuse" if euclidean_reused else "executed",
                    "report_sha256": hashes([EUCLIDEAN_REPORT]), "source_sha256": euclidean_dependencies},
                "extended_euclidean_validation": {"mode": "matching_source_report_reuse" if extended_reused else "executed",
                    "report_sha256": hashes([EXTENDED_REPORT]), "source_sha256": extended_dependencies},
                "rational_addition_validation": {"mode": "matching_source_report_reuse" if rational_reused else "executed",
                    "report_sha256": hashes([RATIONAL_REPORT]), "source_sha256": rational_dependencies},
                "rational_multiplication_validation": {"mode": "matching_source_report_reuse" if multiplication_reused else "executed",
                    "report_sha256": hashes([RATIONAL_MULTIPLICATION_REPORT]), "source_sha256": multiplication_dependencies},
                "rational_order_validation": {"mode": "matching_source_report_reuse" if order_reused else "executed",
                    "report_sha256": hashes([RATIONAL_ORDER_REPORT]), "source_sha256": order_dependencies},
                "ratios_units_validation": {"mode": "matching_source_report_reuse" if ratios_reused else "executed",
                    "report_sha256": hashes([RATIOS_UNITS_REPORT]), "source_sha256": ratios_dependencies},
                "finite_functions_validation": {"mode": "matching_source_report_reuse" if functions_reused else "executed",
                    "report_sha256": hashes([FINITE_FUNCTIONS_REPORT]), "source_sha256": functions_dependencies},
                "finite_function_inverses_validation": {"mode": "matching_source_report_reuse" if inverse_reused else "executed",
                    "report_sha256": hashes([FINITE_FUNCTION_INVERSES_REPORT]), "source_sha256": inverse_dependencies},
                "linear_equation_solvers_validation": {"mode": "matching_source_report_reuse" if linear_reused else "executed",
                    "report_sha256": hashes([LINEAR_EQUATION_SOLVERS_REPORT]), "source_sha256": linear_dependencies},
                "rational_inequalities_validation": {"mode": "matching_source_report_reuse" if inequalities_reused else "executed",
                    "report_sha256": hashes([RATIONAL_INEQUALITIES_REPORT]), "source_sha256": inequalities_dependencies},
                "rational_affine_validation": {"mode": "matching_source_report_reuse" if affine_reused else "executed",
                    "report_sha256": hashes([RATIONAL_AFFINE_REPORT]), "source_sha256": affine_dependencies},
                "rational_powers_sums_validation": {"mode": "matching_source_report_reuse" if powers_sums_reused else "executed",
                    "report_sha256": hashes([RATIONAL_POWERS_SUMS_REPORT]), "source_sha256": powers_sums_dependencies},
                "rational_polynomial_basic_validation": {"mode": "matching_source_report_reuse" if polynomial_reused else "executed",
                    "report_sha256": hashes([RATIONAL_POLYNOMIAL_BASIC_REPORT]), "source_sha256": polynomial_dependencies},
                "rational_polynomial_product_validation": {"mode": "matching_source_report_reuse" if product_reused else "executed",
                    "report_sha256": hashes([RATIONAL_POLYNOMIAL_PRODUCT_REPORT]), "source_sha256": product_dependencies},
                "rational_polynomial_linear_division_validation": {"mode": "matching_source_report_reuse" if division_reused else "executed",
                    "report_sha256": hashes([RATIONAL_POLYNOMIAL_LINEAR_DIVISION_REPORT]), "source_sha256": division_dependencies},
                "legacy_snapshot_sha256": hashlib.sha256((BUILD / "legacy_validation_snapshot.json").read_bytes()).hexdigest(),
                "rational_quadratics_validation": {"mode": "matching_source_report_reuse" if quadratic_reused else "executed",
                    "report_sha256": hashes([RATIONAL_QUADRATICS_REPORT]), "source_sha256": quadratic_dependencies},
                "scope": "chapter 1; B1.1 through B1.19 in partial chapter 26; B1.20 and B1.21 in partial chapter 526 (97Fxx); B2.1 through B2.4 in partial chapter 529 (97Ixx); B2.5 through B2.8 in partial chapter 528 (97Hxx); B2.9 and B2.10 continue partial chapter 529 after those prerequisites; B2.11 through B2.18 continue partial chapter 528 (97H20); B2.19 and B2.20 continue that chapter (main 97H30, cross 97H20), over Q; B2.21 and B2.22 continue partial chapter 526 (97F50) with rational gaps and cut order, not cut arithmetic; teaching prerequisite order is not MSC or historical order"}
    (BUILD / "build_inputs.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": "built", "artifacts": NEW_STEMS,
                      "next": "python tools/validate_learning_batch.py"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
