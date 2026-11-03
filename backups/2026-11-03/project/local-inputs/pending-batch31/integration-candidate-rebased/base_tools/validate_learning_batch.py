#!/usr/bin/env python3
"""Validate the assembled learning batch; actual visual acceptance remains manual.

Do not invoke validate_ch01_review here: its main-book one-chapter assumptions
apply only before build_learning_batch replaces the combined book.
"""
from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
from functools import lru_cache
from html.parser import HTMLParser
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

import fitz
from PIL import Image, ImageDraw

from build_learning_batch import (ROOT, OUT, BUILD, REVIEW_STEM, NEW_STEMS,
                                 PDF_STEMS, FIGURES, UNITS, WRITTEN_REPORT, INTEGER_REPORT, EUCLIDEAN_REPORT,
                                 EXTENDED_REPORT, RATIONAL_REPORT, RATIONAL_MULTIPLICATION_REPORT,
                                 RATIONAL_ORDER_REPORT, RATIOS_UNITS_REPORT, FINITE_FUNCTIONS_REPORT,
                                 FINITE_FUNCTION_INVERSES_REPORT, LINEAR_EQUATION_SOLVERS_REPORT, EDUCATION_UNITS, ANALYSIS_UNITS, CLASSIFIED_UNITS,
                                 RATIONAL_INEQUALITIES_REPORT, RATIONAL_AFFINE_REPORT, RATIONAL_POWERS_SUMS_REPORT,
                                 RATIONAL_POLYNOMIAL_BASIC_REPORT, RATIONAL_POLYNOMIAL_PRODUCT_REPORT,
                                 RATIONAL_POLYNOMIAL_LINEAR_DIVISION_REPORT, RATIONAL_QUADRATICS_REPORT, source_hashes, artifact_hashes,
                                 hashes, rational_gap_figure_source, dedekind_grid_figure_source, real_plane_figure_source, real_projection_figure_source, real_sequence_epsilon_figure_source)

REPORT = ROOT / "data/production/batch_validation.json"
SCREEN = BUILD / "screenshots"
PAIRS = ([(f"question-{i:02}", f"answer-{i:02}") for i in range(1, 15)]
         + [(f"{prefix}-q{i:02}", f"{prefix}-a{i:02}")
            for _stem, _anchor, prefix, _name in UNITS for i in range(1, 9)])


def require(condition, message):
    if not condition:
        raise ValueError(message)


class HTMLAudit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.images = []
        self.math = 0
        self.scripts = 0
        self.suppressed = 0
        self.prose = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "a":
            self.links.append(attrs.get("href", ""))
        if tag == "img":
            self.images.append(attrs.get("src", ""))
        if tag == "math":
            self.math += 1
        if tag == "script":
            self.scripts += 1
        if tag in {"math", "code", "pre", "style", "script"}:
            self.suppressed += 1

    def handle_endtag(self, tag):
        if tag in {"math", "code", "pre", "style", "script"}:
            self.suppressed -= 1

    def handle_data(self, data):
        if not self.suppressed:
            self.prose.append(data)


def nodes(tree):
    if isinstance(tree, dict):
        if "t" in tree:
            yield tree
        for value in tree.values():
            yield from nodes(value)
    elif isinstance(tree, list):
        for value in tree:
            yield from nodes(value)


def inline_text(inlines):
    text = []
    for node in nodes(inlines):
        if node["t"] == "Str":
            text.append(node["c"])
        elif node["t"] == "Space":
            text.append(" ")
    return "".join(text)


def ast_of(path):
    return json.loads(subprocess.check_output(["pandoc", str(path), "-t", "json"], cwd=ROOT))


def audit_book(stem, expected_images, pairs):
    path = OUT / (stem + ".md")
    text = path.read_text()
    ast = ast_of(path)
    all_nodes = list(nodes(ast))
    counts = Counter(node["t"] for node in all_nodes)
    source_math_nodes = [node for node in all_nodes if node["t"] == "Math"]
    image_nodes = [node for node in all_nodes if node["t"] == "Image"]
    # Pandoc Figure stores the visible caption and image alternative text
    # separately. Math inside alt text becomes a plain HTML attribute, whereas
    # caption math is rendered once as MathML. Do not count the alt duplicate
    # as a second visible formula; continue checking every actual caption node.
    alt_math_ids = {id(node) for image in image_nodes
                    for node in nodes(image["c"][1]) if node["t"] == "Math"}
    math_nodes = [node for node in source_math_nodes if id(node) not in alt_math_ids]
    links = [node for node in all_nodes if node["t"] == "Link"]
    require(len(image_nodes) == expected_images, f"{stem}: wrong image count")
    require(len(math_nodes) > 100, f"{stem}: unexpectedly few parsed formulae")
    for node in image_nodes:
        name = node["c"][2][0]
        image_path = OUT / name
        require(image_path.is_file(), f"{stem}: missing image {name}")
        with Image.open(image_path) as image:
            image.verify()
    # A literal dollar or TeX delimiter in a prose string signals failed math parsing.
    unparsed = [node["c"] for node in all_nodes if node["t"] == "Str"
                and ("$" in node["c"] or "\\(" in node["c"] or "\\[" in node["c"])]
    require(not unparsed, f"{stem}: unparsed mathematics {unparsed[:8]}")
    html = HTMLAudit()
    html.feed((OUT / (stem + ".html")).read_text())
    duplicates = [key for key, count in Counter(html.ids).items() if count > 1]
    require(not duplicates, f"{stem}: duplicate HTML anchors {duplicates}")
    prefixes = "|".join(re.escape(prefix) for _stem, _anchor, prefix, _name in UNITS)
    question_ids = {key for key in html.ids
                    if re.fullmatch(r"question-\d+|(?:" + prefixes + r")-q\d+", key)}
    answer_ids = {key for key in html.ids
                  if re.fullmatch(r"answer-\d+|(?:" + prefixes + r")-a\d+", key)}
    require(question_ids == {question for question, _answer in pairs}
            and answer_ids == {answer for _question, answer in pairs},
            f"{stem}: unexpected exercise/answer count or IDs")
    require(html.scripts == 0, f"{stem}: offline HTML unexpectedly needs scripts")
    require(html.math == len(math_nodes), f"{stem}: MathML count differs from source AST")
    require(len(html.images) == expected_images and
            all(src.startswith("data:image/png;base64,") for src in html.images),
            f"{stem}: HTML images are not all embedded PNGs")
    for href in html.links:
        if href.startswith("#"):
            require(unquote(href[1:]) in html.ids, f"{stem}: unresolved HTML link {href}")
        require(not re.search(r"\.md#", href), f"{stem}: leaked manuscript-file link {href}")
        require(href.startswith(("#", "https://", "http://", "mailto:")),
                f"{stem}: nonportable relative link in standalone book {href}")
    prose = "".join(html.prose)
    require(not re.search(r"\$\$|\\(?:frac|mathbb|cdot|begin)\b", prose),
            f"{stem}: visible raw mathematical code in HTML")
    targets = [node["c"][2][0] for node in links]
    for question, answer in pairs:
        require(question in html.ids and answer in html.ids,
                f"{stem}: missing exercise anchor {question}/{answer}")
        qmark, amark = "{#" + question + "}", "{#" + answer + "}"
        require(text.count(qmark) == text.count(amark) == 1,
                f"{stem}: duplicate/missing explicit exercise anchors")
        qpos, apos = text.index(qmark), text.index(amark)
        require(qpos < apos, f"{stem}: answer precedes question")
        next_q = min([text.index("{#" + q + "}") for q, _ in pairs
                      if text.index("{#" + q + "}") > qpos] + [text.index("# 附录一 ")])
        next_a = min([text.index("{#" + a + "}") for _, a in pairs
                      if text.index("{#" + a + "}") > apos] + [len(text)])
        require("](#" + answer + ")" in text[qpos:next_q],
                f"{stem}: wrong/missing answer link in {question}")
        require("](#" + question + ")" in text[apos:next_a],
                f"{stem}: wrong/missing question backlink in {answer}")
        require("#" + answer in targets and "#" + question in targets,
                f"{stem}: exercise links not parsed")
    headers = [node for node in all_nodes if node["t"] == "Header"]
    return {"math_nodes": len(math_nodes), "source_math_nodes": len(source_math_nodes),
            "image_alt_math_nodes": len(alt_math_ids), "images": len(image_nodes),
            "exercise_pairs": len(pairs), "html_ids": len(html.ids),
            "html_internal_links": sum(href.startswith("#") for href in html.links),
            "headers": [(h["c"][0], h["c"][1][0], inline_text(h["c"][2])) for h in headers]}


@lru_cache(maxsize=None, typed=True)
def recursive_add(a, b):
    """a+0=a; a+S(b)=S(a+b); host integers encode the finite instances."""
    if type(a) is not int or type(b) is not int or a < 0 or b < 0:
        raise ValueError("Only nonnegative Python integers represent these test inputs")
    return a if b == 0 else recursive_add(a, b - 1) + 1


@lru_cache(maxsize=None, typed=True)
def recursive_multiply(a, b):
    """a*0=0; a*S(b)=(a*b)+a, using independently recursive addition."""
    if type(a) is not int or type(b) is not int or a < 0 or b < 0:
        raise ValueError("Only nonnegative Python integers represent these test inputs")
    return 0 if b == 0 else recursive_add(recursive_multiply(a, b - 1), a)


def finite_arithmetic_checks():
    for a in range(13):
        for b in range(13):
            require(recursive_add(a, b) == a + b, "Recursive addition mismatch")
            require(recursive_multiply(a, b) == a * b, "Recursive multiplication mismatch")
            require(recursive_add(a, b) == recursive_add(b, a), "Finite addition symmetry mismatch")
            require(recursive_multiply(a, b) == recursive_multiply(b, a), "Finite multiplication symmetry mismatch")
    for invalid in [-1, True, 1.5, "1"]:
        for function in [recursive_add, recursive_multiply]:
            try:
                function(0, invalid)
            except ValueError:
                pass
            else:
                raise ValueError("Arithmetic checker accepted an invalid input")
    examples = []
    for left, right, expected in [(27, 15, 42), (38, 24, 62)]:
        lt, lu = divmod(left, 10)
        rt, ru = divmod(right, 10)
        left_expanded = recursive_add(recursive_multiply(lt, 10), lu)
        right_expanded = recursive_add(recursive_multiply(rt, 10), ru)
        units = recursive_add(lu, ru)
        require(units == 12, "Unexpected units sum")
        tens = recursive_add(recursive_add(lt, rt), 1)
        regrouped = recursive_add(recursive_multiply(tens, 10), 2)
        direct = recursive_add(left_expanded, right_expanded)
        require(left_expanded == left and right_expanded == right and
                regrouped == direct == expected, "Place-value expansion mismatch")
        examples.append({"left": left, "right": right, "expanded_result": direct,
                         "regrouped_result": regrouped, "expected": expected,
                         "units_before_carry": units, "carry_tens": 1})
    return {"domain": "0..12 inclusive", "addition_pairs": 169,
            "multiplication_pairs": 169, "examples": examples,
            "status": "passed", "limits": "Finite cross-checks, not proofs or a construction of natural numbers."}


def finite_natural_algorithm_checks():
    """Compare authored algorithms with separate built-in arithmetic on finite inputs."""
    from natural_algorithms import divide_nat, digits_nat, value_digits, normalize_coefficients
    division_count = representation_count = normalization_count = rejected_count = 0
    alphabet = "0123456789abcdef"

    def independent_digits(value, base):
        if value == 0:
            return [0]
        result = []
        while value:
            value, digit = divmod(value, base)
            result.append(digit)
        return result[::-1]

    def independent_value(digits, base):
        return sum(digit * base ** (len(digits) - position - 1)
                   for position, digit in enumerate(digits))

    def check_canonical(digits, n, base):
        require(isinstance(digits, list) and len(digits) >= 1,
                "Digit output must be a nonempty list")
        require(all(type(d) is int and 0 <= d < base for d in digits),
                "Output digit outside its base")
        require((digits == [0]) if n == 0 else digits[0] != 0, "Noncanonical leading zero")
        require(digits == independent_digits(n, base), "Independent digit expansion differs")
        require(independent_value(digits, base) == n, "Independent positional value differs")
        require(int("".join(alphabet[d] for d in digits), base) == n,
                "Built-in base parsing differs")

    for n in range(121):
        for divisor in range(1, 17):
            result = divide_nat(n, divisor)
            require(isinstance(result, tuple) and len(result) == 2,
                    "Division output must be a quotient/remainder tuple")
            q, r = result
            require(type(q) is int and type(r) is int and q >= 0 and 0 <= r < divisor,
                    "Invalid quotient/remainder types or range")
            require(result == divmod(n, divisor) and n == divisor * q + r,
                    "Independent division cross-check differs")
            division_count += 1
        for base in range(2, 17):
            digits = digits_nat(n, base)
            check_canonical(digits, n, base)
            require(value_digits(digits, base) == n, "Round-trip value differs")
            require(value_digits([0, 0] + digits, base) == n, "Allowed leading zeros changed value")
            representation_count += 1
    for base in range(2, 17):
        for left in range(4 * base + 1):
            for right in range(4 * base + 1):
                coefficients = [left, right]
                expected_value = independent_value(coefficients, base)
                normalized = normalize_coefficients(coefficients, base)
                check_canonical(normalized, expected_value, base)
                require(value_digits(normalized, base) == expected_value,
                        "Normalized digit value differs")
                normalization_count += 1
    special = []
    for coefficients, base, expected in [([2, 15], 10, [3, 5]), ([1, 25, 100], 10, [4, 5, 0]),
                                         ([0], 2, [0]), ([0, 0, 0], 16, [0])]:
        result = normalize_coefficients(coefficients, base)
        require(result == expected, "Carry example differs")
        special.append({"coefficients": coefficients, "base": base, "digits": result,
                        "independent_value": independent_value(coefficients, base)})

    def must_reject(function, *arguments):
        nonlocal rejected_count
        try:
            function(*arguments)
        except (ValueError, TypeError):
            rejected_count += 1
        else:
            raise ValueError(f"{function.__name__} accepted invalid input {arguments!r}")

    for bad in [True, False, -1, 1.5, "2", None]:
        must_reject(divide_nat, bad, 2)
        must_reject(divide_nat, 3, bad)
        must_reject(digits_nat, bad, 2)
        must_reject(digits_nat, 3, bad)
        must_reject(value_digits, [1], bad)
        must_reject(normalize_coefficients, [1], bad)
        must_reject(value_digits, [bad], 10)
        must_reject(normalize_coefficients, [bad], 10)
    must_reject(divide_nat, 1, 0)
    for base in [0, 1]:
        must_reject(digits_nat, 1, base)
        must_reject(value_digits, [1], base)
        must_reject(normalize_coefficients, [1], base)
    for empty_or_invalid in [[], None, 2, "12"]:
        must_reject(value_digits, empty_or_invalid, 10)
        must_reject(normalize_coefficients, empty_or_invalid, 10)
    for base in range(2, 17):
        must_reject(value_digits, [base], base)
        must_reject(value_digits, [0, base], base)
    return {"status": "passed", "division_domain": "0<=n<=120, 1<=divisor<=16",
            "division_pairs": division_count, "digit_domain": "0<=n<=120, 2<=base<=16",
            "digit_pairs": representation_count,
            "normalization_domain": "2<=base<=16; both coefficients range from 0 through 4*base",
            "normalization_pairs": normalization_count, "special_carry_examples": special,
            "invalid_inputs_rejected": rejected_count,
            "limits": "Finite exact-integer checks using independent divmod, powers, sums and int parsing; not a proof of universal correctness or termination."}


def render_contacts(pdf, stem, every_page):
    slug = {REVIEW_STEM: "batch", "综合数学": "full", "综合数学_第一章审阅版": "ch01",
            "综合数学_完整数学目录": "catalog"}[stem]
    selected = set(range(len(pdf))) if every_page else {0, 1, len(pdf) // 2, len(pdf) - 1}
    if stem == "综合数学":
        for index, page in enumerate(pdf):
            text = "".join(page.get_text().split())
            if ("第26章初等数论" in text or "第526章算术与数论教育" in text or "第529章分析学教育" in text
                    or "第528章代数教育" in text
                    or "基础单元B1.20" in text or "基础单元B1.21" in text
                    or "基础单元B2.1" in text or "基础单元B2.2" in text
                    or "基础单元B2.3" in text or "基础单元B2.4" in text
                    or "基础单元B2.5" in text or "基础单元B2.6" in text
                    or "基础单元B2.7" in text or "基础单元B2.8" in text
                    or "基础单元B2.9" in text or "基础单元B2.10" in text
                    or "基础单元B2.11" in text or "基础单元B2.12" in text
                    or "基础单元B2.13" in text or "基础单元B2.14" in text
                    or "基础单元B2.15" in text or "基础单元B2.16" in text
                    or "基础单元B2.17" in text or "基础单元B2.18" in text
                    or "基础单元B2.19" in text or "基础单元B2.20" in text
                    or "基础单元B2.21" in text or "基础单元B2.22" in text
                    or "基础单元B2.23" in text or "基础单元B2.24" in text
                    or "基础单元B2.25" in text or "基础单元B2.26" in text
                    or "基础单元B2.27" in text or "基础单元B2.28" in text
                    or "基础单元B2.29" in text or "基础单元B2.30" in text
                    or "基础单元B2.31" in text or "基础单元B2.32" in text
                    or "基础单元B2.33" in text or "基础单元B2.34" in text
                    or "基础单元B2.35" in text or "基础单元B2.36" in text
                    or "基础单元B2.37" in text or "基础单元B2.38" in text
                    or "基础单元B4.1" in text or "基础单元B4.2" in text
                    or "附录十五有限双射" in text
                    or "附录十六有理数一次方程" in text
                    or "附录十七有理数不等式" in text
                    or "附录十八有理坐标" in text
                    or "附录十九非负整数幂" in text
                    or "附录二十多项式系数记录" in text
                    or "附录二十一多项式乘法" in text
                    or "附录二十二一次除式" in text
                    or "附录二十三有理平方" in text
                    or "附录二十四有理缺口" in text
                    or "附录二十五分割网格" in text
                    or "附录二十六实数坐标" in text
                    or "附录二十七正交投影" in text
                    or "附录二十八数列严格" in text
                    or "附录一全部课后题参考答案" in text
                    or "基础单元B1.1自然数" in text or "基础单元B1.2乘法" in text):
                selected.add(index)
    selected = sorted(index for index in selected if 0 <= index < len(pdf))
    for index in selected:
        pdf[index].get_pixmap(matrix=fitz.Matrix(1.25, 1.25)).save(SCREEN / f"{slug}-page-{index+1:03}.png")
    contacts = []
    for offset in range(0, len(selected), 12):
        group = selected[offset:offset + 12]
        sheet = Image.new("RGB", (1200, 440 * ((len(group) + 2) // 3)), "#dfe6ec")
        for position, index in enumerate(group):
            with Image.open(SCREEN / f"{slug}-page-{index+1:03}.png") as original:
                im = original.convert("RGB")
            im.thumbnail((380, 405))
            x, y = (position % 3) * 400, (position // 3) * 440
            sheet.paste(im, (x + (400 - im.width) // 2, y + 5))
            ImageDraw.Draw(sheet).text((x + 12, y + 419), f"{slug}: PDF page {index+1}", fill="black")
        contact = SCREEN / f"{slug}-contact-{offset+1:03}.png"
        sheet.save(contact)
        contacts.append(str(contact.relative_to(ROOT)))
    return {"rendered_pages": [n + 1 for n in selected], "contact_sheets": contacts,
            "all_pages_rendered": every_page}


def audit_pdf(stem):
    path = OUT / (stem + ".pdf")
    with fitz.open(path) as pdf:
        texts = [page.get_text() for page in pdf]
        require("Leo Lee" in "\n".join(texts), f"{stem}: author absent")
        require(not any("$$" in text or "\ufffd" in text for text in texts),
                f"{stem}: raw math delimiter or replacement glyph in PDF")
        overflow = []
        forward, backward = [], []
        for index, page in enumerate(pdf):
            # get_textbox also picks up neighbouring punctuation/line descenders.
            # Character centres identify the actual text covered by the link.
            raw = page.get_text("rawdict")
            characters = [char for block in raw["blocks"] for line in block.get("lines", [])
                          for span in line["spans"] for char in span["chars"]]
            for word in page.get_text("words"):
                if word[0] < 8 or word[2] > page.rect.width - 8 or word[1] < 8 or word[3] > page.rect.height - 8:
                    overflow.append({"page": index + 1, "text": word[4]})
            labelled_links = []
            for link in page.get_links():
                label = "".join(char["c"] for char in characters
                                if link["from"].contains(fitz.Point(
                                    (char["bbox"][0] + char["bbox"][2]) / 2,
                                    (char["bbox"][1] + char["bbox"][3]) / 2)))
                label = "".join(label.split())
                labelled_links.append((label, link))
            position = 0
            while position < len(labelled_links):
                label, link = labelled_links[position]
                position += 1
                # A line-wrapped link can produce two adjacent PDF annotations.
                if position < len(labelled_links):
                    following, next_link = labelled_links[position]
                    joined = label + following
                    if (link.get("page") == next_link.get("page") and
                            (joined in {"参考答案", "查看完整解答", "完整解答", "返回题目"} or
                             re.fullmatch(r"查看题\d+答案|返回题\d+", joined))):
                        label = joined
                        position += 1
                is_forward = label in {"参考答案", "查看完整解答", "完整解答"} or re.fullmatch(r"查看题\d+答案", label)
                is_back = label == "返回题目" or re.fullmatch(r"返回题\d+", label)
                if not (is_forward or is_back):
                    continue
                dest = link.get("page", -1)
                require(0 <= dest < len(pdf), f"{stem}: invalid PDF exercise destination")
                if is_forward:
                    require("返回题" in texts[dest], f"{stem}: answer link does not land on answers")
                    forward.append([index + 1, dest + 1])
                else:
                    require("参考答案" in texts[dest] or "查看完整解答" in "".join(texts[dest].split()) or "完整解答" in "".join(texts[dest].split()) or re.search(r"查看题\d+答案", "".join(texts[dest].split())),
                            f"{stem}: backlink does not land on questions")
                    backward.append([index + 1, dest + 1])
        require(not overflow, f"{stem}: page-boundary overflow {overflow[:8]}")
        expected = len(PAIRS) if stem in NEW_STEMS else 14 if stem == "综合数学_第一章审阅版" else 0
        require(len(forward) == len(backward) == expected,
                f"{stem}: PDF exercise links {len(forward)}/{len(backward)}, expected {expected}")
        rendering = render_contacts(pdf, stem, stem == REVIEW_STEM)
        return {"pages": len(pdf), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                "page_boundary_overflow": overflow, "question_answer_links": len(forward),
                "answer_question_links": len(backward), "forward_destinations": forward,
                "backward_destinations": backward, **rendering}


def written_arithmetic_report_check(manifest):
    """Verify the independently executed tester result without rewriting evidence."""
    report = json.loads(WRITTEN_REPORT.read_text())
    expected_sources = hashes([ROOT / "tools" / name for name in
        ["written_arithmetic.py", "natural_algorithms.py", "validate_written_arithmetic.py"]])
    require(report.get("result") == "pass" and report.get("source_sha256") == expected_sources,
            "Written-arithmetic test result is stale or failed")
    provenance = manifest["written_arithmetic_validation"]
    require(provenance["report_sha256"] == hashes([WRITTEN_REPORT])
            and provenance["source_sha256"] == expected_sources, "Written-arithmetic evidence differs from build")
    scope = report["scope"]
    require(scope["bases"] == [2, 3, 10, 16]
            and scope["left_value_inclusive_range"] == scope["right_value_inclusive_range"] == [0, 60]
            and scope["checks_input_immutability"] and scope["checks_canonical_output"],
            "Written-arithmetic finite scope changed")
    require(report["counts"] == {"addition": 14884, "nonnegative_subtraction": 7564,
            "negative_subtraction_rejected": 7320, "invalid_input_rejected": 16,
            "input_immutability": 29773, "manuscript_examples": 5}
            and report["arithmetic_and_negative_rejection_checks"] == 29768,
            "Written-arithmetic check counts changed")
    require(set(scope["invalid_case_labels"]) == {"empty_left", "empty_right", "boolean_digit",
            "negative_digit", "digit_equal_to_base", "base_one", "boolean_base", "floating_digit"},
            "Written-arithmetic invalid input coverage changed")
    examples = {"1002 - 587": (10, 1002, 587, 415), "1000 - 46": (10, 1000, 46, 954),
                "758 + 486": (10, 758, 486, 1244), "999 + 1": (10, 999, 1, 1000),
                "11010 - 01011 in base 2": (2, 26, 11, 15)}
    require(len(report["manuscript_examples"]) == len(examples)
            and {e["case"] for e in report["manuscript_examples"]} == set(examples),
            "Written-arithmetic manuscript examples missing")
    for example in report["manuscript_examples"]:
        base, left, right, result = examples[example["case"]]
        value = lambda digits: sum(d * base ** i for i, d in enumerate(reversed(digits)))
        require(example["result"] == "pass" and example["base"] == base
                and value(example["left"]) == left and value(example["right"]) == right
                and example["actual"] == example["expected_canonical_result"]
                and value(example["actual"]) == result
                and all(type(d) is int and 0 <= d < base for d in example["actual"])
                and example["actual"][0] != 0, "Written-arithmetic example mismatch")
    return {"status": "passed", "evidence_mode": provenance["mode"],
            "report_sha256": hashes([WRITTEN_REPORT]), "source_sha256": expected_sources,
            "scope": scope, "counts": report["counts"], "manuscript_examples": report["manuscript_examples"],
            "limits": "Source-bound independent finite checks; not a general mathematical proof."}


def integer_pairs_report_check(manifest):
    """Check the source-bound independent integer tester evidence, without rerunning it."""
    report = json.loads(INTEGER_REPORT.read_text())
    expected_sources = hashes([ROOT / "tools" / name for name in
        ["integer_pairs.py", "validate_integer_pairs.py"]])
    require(report.get("result") == "pass" and report.get("source_sha256") == expected_sources,
            "Integer-pair test result is stale or failed")
    provenance = manifest["integer_pairs_validation"]
    require(provenance["report_sha256"] == hashes([INTEGER_REPORT])
            and provenance["source_sha256"] == expected_sources, "Integer-pair evidence differs from build")
    scope = report["scope"]
    require(scope["pair_entry_inclusive_range"] == [0, 6]
            and scope["triple_pair_entry_inclusive_range"] == [0, 3]
            and scope["comparison_model"] == "Independent Python signed integer arithmetic"
            and scope["representative_checks"] == "All same-value pair replacements within the stated finite domain",
            "Integer-pair finite scope changed")
    require(report["counts"] == {"unary_records": 49, "binary_pairs": 2401,
            "law_triples": 4096, "replacement_checks": 11319, "invalid_input_rejected": 101,
            "input_immutability": 7203, "examples": 14}, "Integer-pair check counts changed")
    expected = [
        ("add", [0, 3], [5, 0], [2, 0]),
        ("subtract", [3, 0], [5, 0], [0, 2]),
        ("multiply", [0, 3], [0, 4], [12, 0]),
        ("multiply", [0, 3], [4, 0], [0, 12]),
        ("multiply", [5, 5], [0, 4], [0, 0]),
        ("multiply", [3, 1], [1, 4], [0, 6]),
        ("multiply", [5, 3], [1, 4], [0, 6]),
        ("multiply", [0, 2], [0, 3], [6, 0]),
        ("multiply", [3, 5], [2, 7], [10, 0]),
        ("add", [2, 5], [7, 1], [3, 0]),
        ("add", [0, 3], [6, 0], [3, 0]),
        ("subtract", [3, 0], [8, 0], [0, 5]),
        ("subtract", [3, 0], [0, 8], [11, 0]),
        ("subtract", [0, 3], [0, 8], [5, 0]),
    ]
    require(len(report["manuscript_examples"]) == len(expected), "Integer-pair examples missing")
    for item, (operation, left, right, answer) in zip(report["manuscript_examples"], expected):
        require(item["operation"] == operation and item["left"] == left and item["right"] == right
                and item["expected"] == item["actual"] == answer and item["result"] == "pass",
                "Integer-pair example mismatch")
        a, b = left[0] - left[1], right[0] - right[1]
        wanted = a + b if operation == "add" else a - b if operation == "subtract" else a * b
        require(answer[0] - answer[1] == wanted, "Independent integer example check failed")
        x, y = left
        u, v = right
        raw = ([x + u, y + v] if operation == "add" else
               [x + v, y + u] if operation == "subtract" else [x * u + y * v, x * v + y * u])
        require(item["raw_result"] == raw and raw[0] - raw[1] == wanted,
                "Integer-pair raw representative mismatch")
    return {"status": "passed", "evidence_mode": provenance["mode"],
            "report_sha256": hashes([INTEGER_REPORT]), "source_sha256": expected_sources,
            "scope": scope, "counts": report["counts"], "manuscript_examples": report["manuscript_examples"],
            "limits": "Source-bound independent finite checks; not a proof for all representatives or integer classes."}


def integer_euclidean_report_check(manifest):
    """Bind all three tested dependencies and independently verify recorded examples."""
    from math import gcd
    report = json.loads(EUCLIDEAN_REPORT.read_text())
    sources = hashes([ROOT / "tools" / name for name in
        ["integer_euclidean.py", "validate_integer_euclidean.py", "natural_algorithms.py"]])
    require(report.get("status") == "passed" and report.get("source_sha256") == sources,
            "Integer Euclidean report is stale or failed")
    provenance = manifest["integer_euclidean_validation"]
    require(provenance["report_sha256"] == hashes([EUCLIDEAN_REPORT])
            and provenance["source_sha256"] == sources, "Integer Euclidean evidence differs from build")
    require(report["scope"] == {"integer_inputs": [-36, 36], "division_divisors": [-12, 12],
            "division_excludes_zero": True, "common_divisor_probes": [-36, 36],
            "gcd_double_zero": 0, "remainder_convention": "0 <= r < abs(b)"},
            "Integer Euclidean finite scope changed")
    require(report["counts"] == {"division_pairs": 1752, "divisibility_pairs": 5329,
            "gcd_pairs": 5329, "trace_rows": 16464, "common_divisor_checks": 1590889,
            "invalid_rejections": 67}, "Integer Euclidean finite counts changed")
    expected = {
        "division": [(-23, 5), (-23, -5), (-20, 5), (0, -7)],
        "divides": [(0, 0), (0, 7), (-3, 6), (4, 6)],
        "gcd": [(48, 18), (-48, 18), (0, -7), (-7, 0), (0, 0),
                (84, 30), (-84, -30), (14, 25), (18, 30)],
    }
    required = {(operation, a, b) for operation, inputs in expected.items() for a, b in inputs}
    examples = report["examples"]
    require(len(examples) == len(required)
            and {(e["operation"], *e["inputs"]) for e in examples} == required,
            "Integer Euclidean manuscript examples changed")
    for example in examples:
        a, b = example["inputs"]
        result = example["result"]
        if example["operation"] == "division":
            q, r = result
            require(type(q) is int and type(r) is int and b != 0
                    and a == b * q + r and 0 <= r < abs(b), "Recorded division example is invalid")
        elif example["operation"] == "divides":
            wanted = (a == 0 and b == 0) or (a != 0 and b % a == 0)
            require(type(result) is bool and result == wanted, "Recorded divisibility example is invalid")
        else:
            require(type(result) is int and result == gcd(a, b), "Recorded gcd example is invalid")
            u, v = abs(a), abs(b)
            for row in example["trace"]:
                require(v != 0 and row["u"] == u and row["v"] == v
                        and (row["q"], row["r"]) == divmod(u, v), "Recorded gcd trace is invalid")
                u, v = v, row["r"]
            require(v == 0 and u == result, "Recorded gcd trace does not terminate at the result")
    return {"status": "passed", "evidence_mode": provenance["mode"],
            "report_sha256": hashes([EUCLIDEAN_REPORT]), "source_sha256": sources,
            "scope": report["scope"], "counts": report["counts"], "examples": examples,
            "limits": "Source-bound independent finite checks and recorded trace verification; not a general proof."}


def extended_euclidean_report_check(manifest):
    """Verify four dependency hashes and both coefficient invariants in each example."""
    from math import gcd
    report = json.loads(EXTENDED_REPORT.read_text())
    sources = hashes([ROOT / "tools" / name for name in
        ["extended_euclidean.py", "validate_extended_euclidean.py", "integer_euclidean.py", "natural_algorithms.py"]])
    require(report.get("status") == "passed" and report.get("source_sha256") == sources,
            "Extended Euclidean report is stale or failed")
    provenance = manifest["extended_euclidean_validation"]
    require(provenance["report_sha256"] == hashes([EXTENDED_REPORT])
            and provenance["source_sha256"] == sources, "Extended Euclidean evidence differs from build")
    require(report["scope"] == {"gcd_inputs": [-30, 30], "equation_ab": [-8, 8],
            "equation_c": [-12, 12], "equation_witness_box": [-12, 12], "record_a": [-12, 12],
            "record_b": [1, 12], "coprime_abc": [-8, 8], "sign_of_zero": 1},
            "Extended Euclidean finite scope changed")
    require(report["counts"] == {"gcd_pairs": 3721, "invariant_rows": 10968,
            "coefficient_shift_checks": 18605, "linear_equations": 7225, "reduced_records": 300,
            "equivalent_record_pairs": 1008, "coprime_cancellation_cases": 1176,
            "coprime_product_cases": 4913, "invalid_rejections": 58},
            "Extended Euclidean finite counts changed")
    expected = {
        "extended_gcd": [(48, 18), (-48, 18), (0, -7), (-7, 0), (0, 0), (6, 10),
                         (84, 30), (-84, 30), (30, 18)],
        "linear_solution": [(6, 10, 14), (6, 10, 7), (0, 0, 0), (0, 0, 1),
                            (48, 18, 30), (48, 18, 31), (30, 18, 42), (30, 18, 41)],
        "reduced_record": [(-12, 18), (0, 9), (14, 21), (-42, 30), (-14, 10), (12, 18), (0, 7)],
    }
    required = {(operation, *inputs) for operation, cases in expected.items() for inputs in cases}
    examples = report["examples"]
    require(len(examples) == len(required)
            and {(e["operation"], *e["inputs"]) for e in examples} == required,
            "Extended Euclidean manuscript examples changed")
    for example in examples:
        a, b = example["inputs"][:2]
        result = example["result"]
        if example["operation"] == "extended_gcd":
            u, v, x, y, X, Y = abs(a), abs(b), 1 if a >= 0 else -1, 0, 0, 1 if b >= 0 else -1
            for row in result["trace"]:
                require(v != 0 and (row["u"], row["v"], row["x"], row["y"], row["X"], row["Y"])
                        == (u, v, x, y, X, Y) and u == a*x + b*y and v == a*X + b*Y,
                        "Extended Euclidean fixed-input coefficient invariant failed")
                q, r = divmod(u, v)
                nx, ny = x-q*X, y-q*Y
                require((row["q"], row["r"], row["next_x"], row["next_y"]) == (q, r, nx, ny)
                        and r == a*nx + b*ny, "Extended Euclidean row transition failed")
                u, v, x, y, X, Y = v, r, X, Y, nx, ny
            require(v == 0 and (result["g"], result["x"], result["y"]) == (u, x, y)
                    and u == gcd(a, b) == a*x + b*y, "Extended Euclidean terminal witness failed")
        elif example["operation"] == "linear_solution":
            c = example["inputs"][2]
            g = gcd(a, b)
            exists = (c == 0) if g == 0 else c % g == 0
            require((result is not None) == exists, "Linear equation solvability example failed")
            if result is not None:
                require(len(result) == 2 and all(type(t) is int for t in result)
                        and a*result[0] + b*result[1] == c, "Linear equation witness failed")
                if g == 0:
                    require(result == [0, 0], "Double-zero solution interface changed")
        else:
            p, q = result
            g = gcd(a, b)
            require(b > 0 and q > 0 and gcd(p, q) == 1 and a == g*p and b == g*q,
                    "Reduced integer record example failed")
    return {"status": "passed", "evidence_mode": provenance["mode"],
            "report_sha256": hashes([EXTENDED_REPORT]), "source_sha256": sources,
            "scope": report["scope"], "counts": report["counts"], "examples": examples,
            "limits": "Source-bound finite checks; no general proof, unique-coefficient claim or rational-type construction."}


def rational_addition_report_check(manifest):
    """Verify five dependencies and canonical rational records against an independent oracle."""
    from fractions import Fraction
    from math import gcd
    report = json.loads(RATIONAL_REPORT.read_text())
    sources = hashes([ROOT / "tools" / name for name in
        ["rational_addition.py", "validate_rational_addition.py", "extended_euclidean.py",
         "integer_euclidean.py", "natural_algorithms.py"]])
    require(report.get("status") == "passed" and report.get("source_sha256") == sources,
            "Rational addition report is stale or failed")
    provenance = manifest["rational_addition_validation"]
    require(provenance["report_sha256"] == hashes([RATIONAL_REPORT])
            and provenance["source_sha256"] == sources, "Rational addition evidence differs from build")
    require(report["scope"] == {"record_a": [-6, 6], "record_b": [1, 5],
            "triple_a": [-2, 2], "triple_b": [1, 3], "embedding": [-8, 8],
            "scaling_pairs": [[2, 3], [3, 2]]}, "Rational addition finite scope changed")
    require(report["counts"] == {"records": 65, "record_pairs": 4225, "representative_changes": 8450,
            "association_triples": 3375, "equivalence_transitivity_triples": 51,
            "embedding_pairs": 289, "invalid_rejections": 113}, "Rational addition finite counts changed")
    expected = [
        ("normalize", [[-42, 30]]), ("normalize", [[0, 9]]),
        ("equivalent", [[1, 2], [2, 4]]), ("equivalent", [[1, 2], [1, 3]]),
        ("embed", [-3]), ("add", [[1, 2], [1, 3]]), ("add", [[-2, 3], [1, 6]]),
        ("add", [[2, 4], [2, 6]]), ("add", [[-2, 3], [4, 6]]),
        ("negate", [[-2, 6]]), ("subtract", [[1, 3], [5, 6]]),
        ("normalize", [[-18, 30]]), ("normalize", [[8, 12]]), ("normalize", [[14, 21]]),
        ("normalize", [[0, 11]]), ("normalize", [[-6, 15]]), ("normalize", [[6, 15]]),
        ("normalize", [[0, 15]]), ("equivalent", [[8, 12], [14, 21]]),
        ("add", [[-5, 8], [3, 8]]), ("add", [[1, 2], [-1, 3]]), ("add", [[1, 6], [1, 6]]),
        ("add", [[-1, 3], [1, 6]]), ("add", [[1, 2], [-3, 18]]), ("negate", [[-3, 7]]),
        ("add", [[-3, 7], [3, 7]]), ("add", [[-2, 1], [1, 3]]),
        ("subtract", [[1, 3], [-2, 5]]), ("add", [[11, 15], [-2, 5]]),
        ("add", [[3, 6], [-4, 6]]),
    ]
    examples = report["examples"]
    require([(e["operation"], e["inputs"]) for e in examples] == expected,
            "Rational addition manuscript examples changed")
    for example in examples:
        operation, inputs, result = example["operation"], example["inputs"], example["result"]
        if operation == "embed":
            wanted = Fraction(inputs[0], 1)
        else:
            values = [Fraction(*record) for record in inputs]
            if operation == "equivalent":
                a, b = inputs[0]
                c, d = inputs[1]
                require(type(result) is bool and result == (values[0] == values[1]) == (a*d == b*c),
                        "Rational equivalence example failed")
                continue
            if operation == "normalize":
                wanted = values[0]
            elif operation == "negate":
                wanted = -values[0]
            elif operation == "add":
                wanted = values[0] + values[1]
            else:
                wanted = values[0] - values[1]
        require(len(result) == 2 and all(type(n) is int for n in result)
                and result[1] > 0 and gcd(*result) == 1
                and result == [wanted.numerator, wanted.denominator],
                "Rational canonical result example failed")
    return {"status": "passed", "evidence_mode": provenance["mode"],
            "report_sha256": hashes([RATIONAL_REPORT]), "source_sha256": sources,
            "scope": report["scope"], "counts": report["counts"], "examples": examples,
            "limits": "Source-bound finite checks using an independent oracle; not an infinite quotient construction or general proof."}


def rational_multiplication_report_check(manifest):
    """Verify all six dependencies and the partial-division example domain."""
    from fractions import Fraction
    from math import gcd
    report = json.loads(RATIONAL_MULTIPLICATION_REPORT.read_text())
    sources = hashes([ROOT / "tools" / name for name in
        ["rational_multiplication.py", "validate_rational_multiplication.py", "rational_addition.py",
         "extended_euclidean.py", "integer_euclidean.py", "natural_algorithms.py"]])
    require(report.get("status") == "passed" and report.get("source_sha256") == sources,
            "Rational multiplication report is stale or failed")
    provenance = manifest["rational_multiplication_validation"]
    require(provenance["report_sha256"] == hashes([RATIONAL_MULTIPLICATION_REPORT])
            and provenance["source_sha256"] == sources, "Rational multiplication evidence differs from build")
    require(report["scope"] == {"record_a": [-6, 6], "record_b": [1, 5],
            "triple_a": [-2, 2], "triple_b": [1, 3], "embedding": [-8, 8],
            "scaling_pairs": [[2, 3], [3, 2]]}, "Rational multiplication finite scope changed")
    require(report["counts"] == {"records": 65, "reciprocals": 60, "zero_reciprocal_rejections": 5,
            "product_pairs": 4225, "division_pairs": 3900, "zero_division_rejections": 325,
            "representative_changes": 8450, "association_triples": 3375, "distributivity_triples": 3375,
            "cancellation_triples": 2700, "integer_embedding_pairs": 289, "invalid_input_rejections": 60},
            "Rational multiplication finite counts changed")
    expected = [
        ("multiply", [[-2, 3], [9, 4]]), ("multiply", [[-2, 3], [-9, 4]]),
        ("multiply", [[0, 7], [3, 5]]), ("reciprocal", [[-6, 8]]),
        ("reciprocal", [[6, 8]]), ("divide", [[2, 3], [-4, 5]]),
        ("divide", [[0, 7], [3, 5]]), ("divide", [[-3, 1], [-6, 1]]),
        ("multiply", [[-2, 3], [3, 5]]), ("multiply", [[0, 7], [-3, 2]]),
        ("multiply", [[2, 4], [-6, 10]]), ("multiply", [[-6, 15], [5, 7]]),
        ("multiply", [[2, 3], [-15, 35]]), ("multiply", [[-2, 3], [10, 8]]),
        ("multiply", [[-3, 1], [2, 5]]), ("multiply", [[1, 2], [9, 18]]),
        ("reciprocal", [[-4, 6]]), ("reciprocal", [[-6, 15]]),
        ("divide", [[-5, 6], [-2, 9]]), ("multiply", [[-2, 9], [15, 4]]),
        ("divide", [[6, 5], [-3, 7]]), ("multiply", [[-3, 7], [-14, 5]]),
        ("divide", [[3, 5], [-4, 7]]), ("divide", [[-6, 15], [8, 21]]),
        ("divide", [[-6, 1], [-15, 1]]), ("divide", [[6, 1], [-15, 1]]),
        ("divide", [[1, 2], [5, 6]]), ("divide", [[1, 3], [5, 6]]),
        ("divide", [[5, 6], [5, 6]]), ("divide", [[1, 2], [3, 1]]),
        ("divide", [[1, 1], [2, 3]]),
    ]
    examples = report["examples"]
    require([(e["operation"], e["inputs"]) for e in examples] == expected,
            "Rational multiplication manuscript examples changed")
    for example in examples:
        operation, inputs, result = example["operation"], example["inputs"], example["result"]
        require(all(len(record) == 2 and all(type(n) is int for n in record) and record[1] > 0
                    for record in inputs), "Illegal rational example input")
        values = [Fraction(*record) for record in inputs]
        if operation == "multiply":
            wanted = values[0] * values[1]
        elif operation == "reciprocal":
            require(inputs[0][0] != 0, "Zero reciprocal recorded as a valid example")
            wanted = 1 / values[0]
        else:
            require(inputs[1][0] != 0, "Zero division recorded as a valid example")
            wanted = values[0] / values[1]
        require(len(result) == 2 and all(type(n) is int for n in result)
                and result[1] > 0 and gcd(*result) == 1
                and result == [wanted.numerator, wanted.denominator],
                "Rational multiplication canonical result example failed")
    return {"status": "passed", "evidence_mode": provenance["mode"],
            "report_sha256": hashes([RATIONAL_MULTIPLICATION_REPORT]), "source_sha256": sources,
            "scope": report["scope"], "counts": report["counts"], "examples": examples,
            "limits": "Source-bound finite checks with nonzero inverse/divisor conditions; not a general proof."}


def rational_order_report_check(manifest):
    """Verify seven source dependencies and exact comparison/absolute/distance examples."""
    from fractions import Fraction
    from math import gcd
    report = json.loads(RATIONAL_ORDER_REPORT.read_text())
    sources = hashes([ROOT / "tools" / name for name in
        ["rational_order.py", "validate_rational_order.py", "rational_multiplication.py",
         "rational_addition.py", "extended_euclidean.py", "integer_euclidean.py", "natural_algorithms.py"]])
    require(report.get("status") == "passed" and report.get("source_sha256") == sources,
            "Rational order report is stale or failed")
    provenance = manifest["rational_order_validation"]
    require(provenance["report_sha256"] == hashes([RATIONAL_ORDER_REPORT])
            and provenance["source_sha256"] == sources, "Rational order evidence differs from build")
    require(report["scope"] == {"record_a": [-6, 6], "record_b": [1, 5],
            "triple_a": [-2, 2], "triple_b": [1, 3], "embedding": [-8, 8],
            "scaling_pairs": [[2, 3], [3, 2]]}, "Rational order finite scope changed")
    require(report["counts"] == {"records": 65, "order_pairs": 4225, "representative_changes": 8450,
            "absolute_product_pairs": 4225, "absolute_quotient_pairs": 3900, "triangle_pairs": 4225,
            "reverse_triangle_pairs": 4225, "order_triples": 3375, "translation_triples": 3375,
            "multiplication_triples": 3375, "division_triples": 2700, "distance_triples": 3375,
            "distance_translation_triples": 3375, "distance_scaling_triples": 3375,
            "integer_embedding_pairs": 289, "invalid_input_rejections": 108},
            "Rational order finite counts changed")
    expected = [
        ("compare", [[-2, 3], [-3, 4]]), ("compare", [[1, 2], [2, 4]]),
        ("absolute", [[-6, 8]]), ("absolute", [[0, 7]]),
        ("distance", [[-3, 2], [-1, 2]]), ("distance", [[-1, 2], [3, 2]]),
        ("distance", [[-3, 2], [3, 2]]),
        ("absolute", [[7, 3]]), ("absolute", [[8, 27]]), ("absolute", [[5, 12]]),
        ("absolute", [[-11, 12]]), ("compare", [[1, 6], [5, 6]]),
        ("compare", [[5, 12], [11, 12]]), ("compare", [[7, 3], [0, 1]]),
        ("compare", [[-9, 4], [0, 1]]), ("compare", [[-5, 6], [5, 4]]),
        ("compare", [[2, 4], [6, 10]]), ("compare", [[-1, 3], [1, 2]]),
        ("compare", [[4, 5], [3, 2]]), ("compare", [[-5, 4], [5, 6]]),
        ("absolute", [[3, 2]]), ("distance", [[-2, 3], [1, 4]]),
        ("distance", [[1, 3], [2, 3]]),
    ]
    examples = report["examples"]
    require([(e["operation"], e["inputs"]) for e in examples] == expected,
            "Rational order manuscript examples changed")
    for example in examples:
        operation, inputs, result = example["operation"], example["inputs"], example["result"]
        require(all(len(record) == 2 and all(type(n) is int for n in record) and record[1] > 0
                    for record in inputs), "Illegal rational order example input")
        values = [Fraction(*record) for record in inputs]
        if operation == "compare":
            wanted = (values[0] > values[1]) - (values[0] < values[1])
            a, b = inputs[0]
            c, d = inputs[1]
            delta = a*d - b*c
            require(type(result) is int and result == wanted == (delta > 0) - (delta < 0),
                    "Rational comparison example failed")
            continue
        wanted = abs(values[0]) if operation == "absolute" else abs(values[0] - values[1])
        require(len(result) == 2 and all(type(n) is int for n in result)
                and result[1] > 0 and gcd(*result) == 1 and result[0] >= 0
                and result == [wanted.numerator, wanted.denominator],
                "Rational absolute/distance canonical result failed")
    return {"status": "passed", "evidence_mode": provenance["mode"],
            "report_sha256": hashes([RATIONAL_ORDER_REPORT]), "source_sha256": sources,
            "scope": report["scope"], "counts": report["counts"], "examples": examples,
            "limits": "Source-bound finite exact checks; not a general proof or construction of a complete real line."}


def ratios_units_report_check(manifest):
    """Verify numerical kernels without claiming to check quantity kinds or measurements."""
    from fractions import Fraction
    from math import gcd
    report = json.loads(RATIOS_UNITS_REPORT.read_text())
    sources = hashes([ROOT / "tools" / name for name in
        ["ratios_units.py", "validate_ratios_units.py", "rational_multiplication.py",
         "rational_addition.py", "extended_euclidean.py", "integer_euclidean.py", "natural_algorithms.py"]])
    require(report.get("status") == "passed" and report.get("source_sha256") == sources,
            "Ratios and units report is stale or failed")
    provenance = manifest["ratios_units_validation"]
    require(provenance["report_sha256"] == hashes([RATIOS_UNITS_REPORT])
            and provenance["source_sha256"] == sources, "Ratios and units evidence differs from build")
    require(report["scope"] == {"records_a": [-3, 3], "records_b": [1, 3],
            "quadruple_a": [-1, 1], "quadruple_b": [1, 2],
            "positive_scales_a": [1, 3], "positive_scales_b": [1, 2]},
            "Ratios and units finite scope changed")
    require(report["counts"] == {"ratio_pairs": 378, "ratio_zero_rejections": 63,
            "proportion_quadruples": 576, "proportion_zero_rejections": 720,
            "representative_changes": 504, "conversion_round_trips": 126,
            "conversion_compositions": 756, "rate_conversions": 756,
            "invalid_input_rejections": 132, "nonpositive_scale_rejections": 9},
            "Ratios and units finite counts changed")
    expected = [
        ("ratio", [[2, 3], [4, 5]]), ("ratio", [[0, 1], [-2, 1]]), ("ratio", [[-3, 1], [2, 1]]),
        ("proportion", [[2, 1], [3, 1], [4, 1], [6, 1]]),
        ("proportion", [[0, 1], [2, 1], [0, 1], [-3, 1]]),
        ("proportion", [[2, 1], [3, 1], [3, 1], [4, 1]]),
        ("convert_value", [[375, 1], [100, 1]]), ("convert_value", [[3, 4], [1, 100]]),
        ("convert_value", [[0, 1], [1000, 1]]), ("convert_value", [[-3, 2], [1, 100]]),
        ("ratio", [[15, 2], [3, 2]]), ("convert_rate", [[5, 1], [1, 1000], [1, 3600]]),
        ("convert_rate", [[25, 18], [1000, 1], [3600, 1]]),
        ("convert_value", [[7, 4], [1, 100]]), ("convert_value", [[7, 4], [1000, 1]]),
        ("convert_value", [[6, 1], [3, 2]]), ("convert_value", [[7, 1], [2, 3]]),
        ("convert_value", [[21, 2], [5, 2]]), ("convert_value", [[7, 1], [5, 3]]),
        ("convert_value", [[21, 5], [3, 5]]), ("ratio", [[3, 2], [3, 4]]),
        ("ratio", [[9, 2], [3, 4]]), ("convert_rate", [[6, 1], [1, 1000], [1, 3600]]),
        ("ratio", [[10, 1], [4, 1]]), ("convert_rate", [[5, 2], [2, 1], [3, 1]]),
        ("proportion", [[4, 1], [6, 1], [2, 1], [3, 1]]),
        ("ratio", [[3, 4], [5, 6]]), ("proportion", [[2, 1], [3, 1], [8, 1], [12, 1]]),
        ("ratio", [[18, 1], [24, 1]]),
    ]
    examples = report["examples"]
    require([(e["operation"], e["inputs"]) for e in examples] == expected,
            "Ratios and units manuscript examples changed")
    for example in examples:
        operation, inputs, result = example["operation"], example["inputs"], example["result"]
        require(all(len(record) == 2 and all(type(n) is int for n in record) and record[1] > 0
                    for record in inputs), "Illegal ratio/unit example input")
        values = [Fraction(*record) for record in inputs]
        if operation == "proportion":
            a, b, c, d = values
            require(b != 0 and d != 0 and type(result) is bool
                    and result == (a/b == c/d) == (a*d == b*c), "Proportion example failed")
            continue
        if operation == "ratio":
            require(values[1] != 0, "Ratio example has zero second term")
            wanted = values[0] / values[1]
        elif operation == "convert_value":
            require(values[1] > 0, "Conversion example has nonpositive scale")
            wanted = values[0] / values[1]
        else:
            require(values[1] > 0 and values[2] > 0, "Rate example has nonpositive scale")
            wanted = values[0] * values[2] / values[1]
        require(len(result) == 2 and all(type(n) is int for n in result)
                and result[1] > 0 and gcd(*result) == 1
                and result == [wanted.numerator, wanted.denominator],
                "Ratio/unit canonical example result failed")
    return {"status": "passed", "evidence_mode": provenance["mode"],
            "report_sha256": hashes([RATIOS_UNITS_REPORT]), "source_sha256": sources,
            "scope": report["scope"], "counts": report["counts"], "examples": examples,
            "limits": "Finite numerical checks only; not general proof, quantity-kind validation, measurement certification or affine conversion."}


def finite_functions_report_check(manifest):
    """Bind the independent report and recheck implementations against explicit finite models."""
    from itertools import product
    from finite_functions import FiniteFunction, identity, restrict, compose
    report = json.loads(FINITE_FUNCTIONS_REPORT.read_text())
    sources = hashes([ROOT / "tools" / name for name in ["finite_functions.py", "validate_finite_functions.py"]])
    require(report.get("status") == "passed" and report.get("source_sha256") == sources,
            "Finite functions report is stale or failed")
    provenance = manifest["finite_functions_validation"]
    require(provenance["report_sha256"] == hashes([FINITE_FUNCTIONS_REPORT])
            and provenance["source_sha256"] == sources, "Finite functions evidence differs from build")
    require(report["scope"] == {"set_family": [[], [0], [0, 1]],
            "labels": "exact Python integers; bool rejected",
            "enumeration": "all maps between each ordered pair of declared sets"},
            "Finite functions scope changed")
    require(report["counts"] == {"functions": 11, "evaluations": 13, "equality_pairs": 121,
            "restrictions": 29, "nested_restrictions": 57, "identity_laws": 22,
            "compositions": 47, "mismatched_compositions": 74, "associative_triples": 211,
            "composition_restrictions": 129, "invalid_rejections": 25},
            "Finite functions check counts changed")

    def check(actual, a, b, values):
        # The expected dictionary is generated independently, never from actual.graph.
        require(actual.domain == frozenset(a) and actual.codomain == frozenset(b)
                and actual.graph == frozenset(values.items()), "Finite function data differ from oracle")
        require(actual.image() == frozenset(values.values()), "Finite function image differs from oracle")
        require(all(type(actual(x)) is int and actual(x) == values[x] for x in a),
                "Finite function evaluation differs from oracle")

    def rejected(fn, *args):
        try:
            fn(*args)
        except ValueError:
            return
        raise ValueError("Finite function accepted an invalid domain/interface input")

    def subsets(a):
        return [tuple(x for i, x in enumerate(a) if mask & (1 << i)) for mask in range(1 << len(a))]

    family = [(), (0,), (0, 1)]
    models = []
    for a, b in product(family, repeat=2):
        for outputs in product(b, repeat=len(a)):
            oracle = dict(zip(a, outputs))
            actual = FiniteFunction(list(a), list(b), list(oracle.items()))
            check(actual, a, b, oracle)
            check(FiniteFunction(a, b, list(oracle.items()) * 2), a, b, oracle)
            models.append((a, b, oracle, actual))
    checks = {"functions": len(models), "equality_pairs": 0, "restrictions": 0,
              "compositions": 0, "mismatched_compositions": 0, "associative_triples": 0}
    for a, b, fo, f in models:
        check(compose(identity(b), f), a, b, fo)
        check(compose(f, identity(a)), a, b, fo)
        for subset in subsets(a):
            check(restrict(f, subset), subset, b, {x: fo[x] for x in subset})
            checks["restrictions"] += 1
        for c, d, go, g in models:
            require((f == g) == (a == c and b == d and fo == go),
                    "Finite function equality ignored declared sets")
            checks["equality_pairs"] += 1
            if b != c:
                rejected(compose, g, f)
                checks["mismatched_compositions"] += 1
                continue
            composite = compose(g, f)
            oracle = {x: go[fo[x]] for x in a}
            check(composite, a, d, oracle)
            checks["compositions"] += 1
            for e, target, ho, h in models:
                if d == e:
                    three = {x: ho[go[fo[x]]] for x in a}
                    check(compose(h, composite), a, target, three)
                    check(compose(compose(h, g), f), a, target, three)
                    checks["associative_triples"] += 1
    require(all(report["counts"][key] == value for key, value in checks.items()),
            "Direct finite-model enumeration disagrees with recorded scope")

    # Check rejection and immutable storage directly, rather than trusting report labels.
    for args in [([0], [0], []), ([0], [0], [(1, 0)]), ([0], [0], [(0, 1)]),
                 ([0], [0, 1], [(0, 0), (0, 1)]), ([True], [0], [(True, 0)])]:
        rejected(FiniteFunction, *args)
    rejected(restrict, identity([0]), [1])
    rejected(identity([0]), True)
    a, b, graph = [0, 1], [0, 1], [[0, 0], [1, 1]]
    stored = FiniteFunction(a, b, graph)
    a.append(2); b.append(2); graph[0][1] = 1
    check(stored, (0, 1), (0, 1), {0: 0, 1: 1})

    def encoded(a, b, values):
        return {"domain": list(a), "codomain": list(b), "graph": [list(pair) for pair in sorted(values.items())]}
    square = encoded((0, 1, 2), (0, 1, 4, 9), {0: 0, 1: 1, 2: 4})
    wide = encoded((0,), (0, 1), {0: 0})
    narrow = encoded((0,), (0,), {0: 0})
    expected = [
        {"label": "finite square diagram", "function": square, "image": [0, 1, 4]},
        {"label": "empty domain, distinct codomains", "left": encoded((), (), {}),
         "right": encoded((), (0,), {}), "equal": False},
        {"label": "restricted identity retains old codomain", "left": wide, "right": narrow, "equal": False},
        {"label": "image fits but strict middle sets differ", "first": wide, "second": narrow,
         "composition": "rejected by this declared interface"},
        {"label": "input mutation does not change stored function",
         "function": encoded((0, 1), (0, 1), {0: 0, 1: 1})},
        {"label": "exercise finite composition",
         "first": encoded((0, 1), (2, 3, 4), {0: 2, 1: 3}),
         "second": encoded((2, 3, 4), (5, 6), {2: 5, 3: 5, 4: 6}),
         "result": encoded((0, 1), (5, 6), {0: 5, 1: 5}),
         "image": [5], "reverse": "rejected"},
    ]
    require(report["examples"] == expected, "Finite function concrete examples changed")
    check(FiniteFunction(square["domain"], square["codomain"], square["graph"]),
          (0, 1, 2), (0, 1, 4, 9), {0: 0, 1: 1, 2: 4})
    exercise_f = FiniteFunction([0, 1], [2, 3, 4], [(0, 2), (1, 3)])
    exercise_g = FiniteFunction([2, 3, 4], [5, 6], [(2, 5), (3, 5), (4, 6)])
    check(exercise_f, (0, 1), (2, 3, 4), {0: 2, 1: 3})
    check(exercise_g, (2, 3, 4), (5, 6), {2: 5, 3: 5, 4: 6})
    check(compose(exercise_g, exercise_f), (0, 1), (5, 6), {0: 5, 1: 5})
    rejected(compose, exercise_f, exercise_g)
    return {"status": "passed", "evidence_mode": provenance["mode"],
            "report_sha256": hashes([FINITE_FUNCTIONS_REPORT]), "source_sha256": sources,
            "scope": report["scope"], "counts": report["counts"], "examples": report["examples"],
            "direct_dictionary_oracle_checks": checks,
            "limits": "Finite integer-label checks only; not a proof about arbitrary sets or infinite function domains."}


def finite_function_inverses_report_check(manifest):
    """Replay bounded fiber and dictionary oracles; report counts alone are insufficient."""
    from itertools import product
    from finite_functions import FiniteFunction, identity, compose
    from finite_function_inverses import injective, surjective, bijective, inverse, preimage

    report = json.loads(FINITE_FUNCTION_INVERSES_REPORT.read_text())
    sources = hashes([ROOT / "tools" / name for name in
                      ["finite_functions.py", "finite_function_inverses.py", "validate_finite_function_inverses.py"]])
    require(report.get("status") == "passed" and report.get("source_sha256") == sources,
            "Finite inverse function report is stale or failed")
    provenance = manifest["finite_function_inverses_validation"]
    require(provenance["report_sha256"] == hashes([FINITE_FUNCTION_INVERSES_REPORT])
            and provenance["source_sha256"] == sources, "Finite inverse evidence differs from build")
    require(report["domain"] == "All total functions between all subsets of {0,1}; finite integer labels only",
            "Finite inverse enumeration scope changed")

    def rejected(fn, *args):
        try:
            fn(*args)
        except ValueError:
            return
        raise ValueError("Finite inverse API accepted an invalid input")

    def check_function(actual, a, b, table):
        require(type(actual) is FiniteFunction
                and actual.domain == frozenset(a) and actual.codomain == frozenset(b)
                and actual.graph == frozenset(table.items()), "Finite inverse function differs from independent table")
        require(all(type(actual(x)) is int and actual(x) == y for x, y in table.items()),
                "Finite inverse evaluation differs from independent table")

    def properties(table, target):
        # Fiber sizes are computed from independently enumerated tables, never API output.
        sizes = [sum(value == y for value in table.values()) for y in target]
        return all(size <= 1 for size in sizes), all(size >= 1 for size in sizes)

    def check_properties(f, table, target):
        inj, sur = properties(table, target)
        actual = (injective(f), surjective(f), bijective(f))
        require(all(type(value) is bool for value in actual)
                and actual == (inj, sur, inj and sur), "Finite function property differs from fiber oracle")
        return inj, sur

    def subsets(values):
        values = sorted(values)
        return [frozenset(x for i, x in enumerate(values) if mask & (1 << i))
                for mask in range(1 << len(values))]

    family = [(), (0,), (1,), (0, 1)]
    models = []
    checks = dict(functions=0, property_checks=0, inverse_functions=0,
                  inverse_rejections=0, preimages=0, compositions=0,
                  inverse_compositions=0, opposite_type_pairs=0,
                  two_sided_inverses=0, one_sided_implications=0, invalid_rejections=0)
    for a, b in product(family, repeat=2):
        for outputs in product(b, repeat=len(a)):
            table = dict(zip(a, outputs))
            f = FiniteFunction(a, b, list(table.items()))
            inj, sur = check_properties(f, table, b)
            models.append((a, b, table, f, inj, sur))
            checks["functions"] += 1
            checks["property_checks"] += 3
            if inj and sur:
                expected = {y: x for x, y in table.items()}
                inv = inverse(f)
                check_function(inv, b, a, expected)
                check_function(inverse(inv), a, b, table)
                check_function(compose(inv, f), a, a, {x: x for x in a})
                check_function(compose(f, inv), b, b, {y: y for y in b})
                checks["inverse_functions"] += 1
            else:
                rejected(inverse, f)
                checks["inverse_rejections"] += 1
            for target in subsets(b):
                expected = frozenset(x for x, y in table.items() if y in target)
                actual = preimage(f, target)
                require(type(actual) is frozenset and actual == expected,
                        "Finite preimage differs from membership oracle")
                checks["preimages"] += 1
    for a, b, ft, f, fi, fs in models:
        for c, d, gt, g, gi, gs in models:
            if b == c:
                table = {x: gt[ft[x]] for x in a}
                composite = compose(g, f)
                check_function(composite, a, d, table)
                ci, cs = check_properties(composite, table, d)
                require((not (fi and gi) or ci) and (not (fs and gs) or cs)
                        and (not ci or fi) and (not cs or gs), "Finite composite property implication failed")
                checks["compositions"] += 1
                if fi and fs and gi and gs:
                    expected = {y: x for x, y in table.items()}
                    check_function(inverse(composite), d, a, expected)
                    check_function(compose(inverse(f), inverse(g)), d, a, expected)
                    checks["inverse_compositions"] += 1
            if a == d and b == c:
                left = all(gt[ft[x]] == x for x in a)
                right = all(ft[gt[y]] == y for y in b)
                require((compose(g, f) == identity(a)) == left
                        and (compose(f, g) == identity(b)) == right,
                        "Finite one-sided inverse identity differs from pointwise oracle")
                require((not left or fi) and (not right or fs), "Finite one-sided inverse implication failed")
                checks["opposite_type_pairs"] += 1
                checks["one_sided_implications"] += 2
                if left and right:
                    require(fi and fs and inverse(f) == g, "Finite two-sided inverse uniqueness failed")
                    checks["two_sided_inverses"] += 1
    for api in [injective, surjective, bijective, inverse]:
        for bad in [None, {}, 1, True]:
            rejected(api, bad)
            checks["invalid_rejections"] += 1
    singleton = FiniteFunction([0], [0], [(0, 0)])
    for bad in [None, {True}, {0.0}, {1}, "0"]:
        rejected(preimage, singleton, bad)
        checks["invalid_rejections"] += 1
    rejected(preimage, None, set())
    checks["invalid_rejections"] += 1
    require(report["counts"] == checks, "Finite inverse report counts disagree with direct API oracle replay")

    # Replay every named concrete boundary, including a table outside the tiny family.
    empty = FiniteFunction([], [], [])
    check_properties(empty, {}, ())
    check_function(inverse(empty), (), (), {})
    empty_wide = FiniteFunction([], [0], [])
    require(check_properties(empty_wide, {}, (0,)) == (True, False), "Empty-domain boundary changed")
    rejected(inverse, empty_wide)
    wide = FiniteFunction([0], [0, 1], [(0, 0)])
    require(check_properties(wide, {0: 0}, (0, 1)) == (True, False)
            and bijective(singleton), "Declared codomain did not affect surjectivity")
    rejected(inverse, wide)
    constant = FiniteFunction([-1, 1], [1], [(-1, 1), (1, 1)])
    require(check_properties(constant, {-1: 1, 1: 1}, (1,)) == (False, True)
            and preimage(constant, [1]) == frozenset([-1, 1]), "Noninvertible preimage boundary changed")
    rejected(inverse, constant)
    affine = FiniteFunction([0, 1, 2], [1, 3, 5], [(0, 1), (1, 3), (2, 5)])
    check_function(inverse(affine), (1, 3, 5), (0, 1, 2), {1: 0, 3: 1, 5: 2})
    zero_output = FiniteFunction([1], [0], [(1, 0)])
    check_function(inverse(zero_output), (0,), (1,), {0: 1})
    examples = ["empty-to-empty bijection is its own inverse",
                "empty domain with nonempty codomain is not surjective",
                "same graph and different codomain change surjectivity",
                "preimage exists for a noninvertible constant function",
                "finite affine table inverse reverses all three arrows",
                "zero output does not prevent a function inverse; reciprocal differs"]
    require(report["explicit_examples"] == examples, "Finite inverse example inventory changed")
    return {"status": "passed", "evidence_mode": provenance["mode"],
            "report_sha256": hashes([FINITE_FUNCTION_INVERSES_REPORT]), "source_sha256": sources,
            "domain": report["domain"], "counts": report["counts"],
            "direct_fiber_and_dictionary_oracle_checks": checks, "explicit_examples": examples,
            "limits": "Finite implementation checks only; no general proof or choice principle is inferred."}


def linear_equation_solvers_report_check(manifest):
    """Check actual solver records against a separate general augmented-row oracle."""
    from fractions import Fraction
    from itertools import product
    from importlib.metadata import version
    from linear_equation_solvers import solve_linear, solve_system

    report = json.loads(LINEAR_EQUATION_SOLVERS_REPORT.read_text())
    sources = hashes([ROOT / "tools" / name for name in
                      ["linear_equation_solvers.py", "validate_linear_equation_solvers.py"]])
    require(report.get("status") == "passed" and report.get("source_sha256") == sources,
            "Linear equation solver report is stale or failed")
    provenance = manifest["linear_equation_solvers_validation"]
    require(provenance["report_sha256"] == hashes([LINEAR_EQUATION_SOLVERS_REPORT])
            and provenance["source_sha256"] == sources, "Linear solver evidence differs from build")
    require(report["domain"] == "125 one-variable equations on {-2,-1,0,1,2}; 729 two-row systems on {-1,0,1} plus 3 rational cases; 25 candidate pairs per system",
            "Linear solver test domain changed")
    require(version("sympy") == "1.14.0"
            and report["oracle"] == "SymPy 1.14.0 exact solveset/rank/inverse, direct Fraction substitution",
            "Linear solver external oracle version differs from recorded evidence")

    def row_oracle(rows, variables):
        # Generic Gauss-Jordan elimination, separate from the production case tree.
        rows = [[Fraction(value) for value in row] for row in rows]
        pivots = []
        next_row = 0
        for column in range(variables):
            pivot = next((i for i in range(next_row, len(rows)) if rows[i][column]), None)
            if pivot is None:
                continue
            rows[next_row], rows[pivot] = rows[pivot], rows[next_row]
            divisor = rows[next_row][column]
            rows[next_row] = [value / divisor for value in rows[next_row]]
            for i in range(len(rows)):
                if i != next_row:
                    factor = rows[i][column]
                    rows[i] = [value - factor * pivot_value
                               for value, pivot_value in zip(rows[i], rows[next_row])]
            pivots.append(column)
            next_row += 1
        inconsistent = any(not any(row[:variables]) and row[-1] for row in rows)
        kind = "none" if inconsistent else "unique" if len(pivots) == variables else "all" if not pivots else "line"
        return kind, rows, pivots

    def check_record(actual, oracle, variables):
        kind, rows, pivots = oracle
        require(type(actual) is dict and actual.get("kind") == kind,
                "Linear solver classification differs from augmented-row oracle")
        if kind in ("none", "all"):
            require(actual == {"kind": kind}, "Unexpected empty/universal solution record")
            return
        if kind == "unique":
            point = actual.get("point") if variables == 2 else (actual.get("value"),)
            expected_keys = {"kind", "point" if variables == 2 else "value"}
            expected = [Fraction(0)] * variables
            for row, pivot in zip(rows, pivots):
                expected[pivot] = row[-1]
            require(set(actual) == expected_keys and type(point) is tuple and len(point) == variables
                    and all(type(value) is Fraction for value in point) and point == tuple(expected),
                    "Linear solver unique solution differs from exact row oracle")
            return
        require(variables == 2 and set(actual) == {"kind", "base", "direction"},
                "Unexpected parameter-family solution record")
        base, direction = actual["base"], actual["direction"]
        require(type(base) is tuple and type(direction) is tuple and len(base) == len(direction) == 2
                and all(type(value) is Fraction for value in base + direction),
                "Parameter family does not use exact Fraction pairs")
        free = next(i for i in range(variables) if i not in pivots)
        # In a rank-one system, nonzero free coordinate covers every possible free
        # variable. Checking base and direction proves equality of the finite record
        # with the oracle's affine family, beyond merely sampling parameter points.
        require(direction[free] != 0
                and all(sum(row[i] * base[i] for i in range(variables)) == row[-1] for row in rows)
                and all(sum(row[i] * direction[i] for i in range(variables)) == 0 for row in rows),
                "Parameter family differs from the complete exact row-oracle solution set")

    def member(result, point):
        if result["kind"] == "none":
            return False
        if result["kind"] == "all":
            return True
        if result["kind"] == "unique":
            return point == result["point"]
        base, direction = result["base"], result["direction"]
        index = next(i for i in range(2) if direction[i])
        parameter = (point[index] - base[index]) / direction[index]
        return point == tuple(base[i] + parameter * direction[i] for i in range(2))

    def rejected(fn, args):
        try:
            fn(*args)
        except ValueError:
            return
        raise ValueError("Linear solver accepted an invalid coefficient")

    checks = dict(linear_equations=0, linear_candidate_checks=0,
                  systems=0, unique=0, none=0, line=0, all=0,
                  candidate_pairs=0, parameter_points=0, row_swap_checks=0, invalid_rejections=0)
    small = [Fraction(n) for n in range(-2, 3)]
    for a, b, c in product(small, repeat=3):
        result = solve_linear(a, b, c)
        check_record(result, row_oracle([[a, c-b]], 1), 1)
        for value in small:
            included = result["kind"] == "all" or (result["kind"] == "unique" and value == result["value"])
            require(included == (a * value + b == c), "Linear solution membership disagrees with original equation")
            checks["linear_candidate_checks"] += 1
        checks["linear_equations"] += 1
    systems = list(product([Fraction(-1), Fraction(0), Fraction(1)], repeat=6))
    systems += [(Fraction(1, 2), Fraction(-2, 3), Fraction(5, 7), Fraction(-3, 4), Fraction(2, 5), Fraction(0)),
                (Fraction(0), Fraction(0), Fraction(0), Fraction(2, 3), Fraction(4, 3), Fraction(-1, 2)),
                (Fraction(1, 2), Fraction(1, 3), Fraction(1, 4), Fraction(1), Fraction(2, 3), Fraction(1, 2))]
    transforms = {"nonzero_row_scalings": 0, "retained_row_replacements": 0}
    for values in systems:
        a, b, c, d, e, f = values
        oracle = row_oracle([[a, b, c], [d, e, f]], 2)
        result = solve_system(*values)
        check_record(result, oracle, 2)
        swapped = solve_system(d, e, f, a, b, c)
        check_record(swapped, oracle, 2)
        checks["row_swap_checks"] += 1
        if result["kind"] == "line":
            for parameter in small:
                x, y = (result["base"][i] + parameter * result["direction"][i] for i in range(2))
                require(a*x+b*y == c and d*x+e*y == f, "Parameter point fails an original equation")
                checks["parameter_points"] += 1
        for point in product(small, repeat=2):
            x, y = point
            expected = a*x+b*y == c and d*x+e*y == f
            require(member(result, point) == expected and member(swapped, point) == expected,
                    "System solution membership disagrees with original equations")
            checks["candidate_pairs"] += 1
        check_record(solve_system(-2*a, -2*b, -2*c, d, e, f), oracle, 2)
        transforms["nonzero_row_scalings"] += 1
        check_record(solve_system(a, b, c, d+3*a, e+3*b, f+3*c), oracle, 2)
        transforms["retained_row_replacements"] += 1
        checks["systems"] += 1
        checks[result["kind"]] += 1
    for fn, arity in [(solve_linear, 3), (solve_system, 6)]:
        for position in range(arity):
            for bad in [None, True, False, 0.5, "1/2", (1, 2)]:
                args = [0] * arity
                args[position] = bad
                rejected(fn, args)
                checks["invalid_rejections"] += 1
    require(report["counts"] == checks, "Linear solver report counts disagree with direct oracle replay")

    for values in [(0, 2, 2), (0, 2, 3)]:
        a, b, c = values
        check_record(solve_linear(*values), row_oracle([[a, c-b]], 1), 1)
    for values in [(0, 0, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0),
                   (1, 2, 3, 2, 4, 7), (1, 2, 3, 2, 4, 6),
                   (0, 2, 4, 3, 1, 5), (0, 0, 0, 2, 4, 6), (2, 3, 7, 4, -1, 7)]:
        a, b, c, d, e, f = values
        check_record(solve_system(*values), row_oracle([[a, b, c], [d, e, f]], 2), 2)
    examples = ["zero one-variable coefficient: identity and contradiction distinguished",
                "both zero rows: all pairs or contradiction",
                "zero scalar combination: inconsistent and dependent consistent distinguished",
                "zero first coefficient uses a nonzero second-coordinate pivot",
                "first zero row is swapped with the nonzero row",
                "unique pair checked in both original equations"]
    require(report["explicit_examples"] == examples, "Linear solver concrete example inventory changed")
    return {"status": "passed", "evidence_mode": provenance["mode"],
            "report_sha256": hashes([LINEAR_EQUATION_SOLVERS_REPORT]), "source_sha256": sources,
            "domain": report["domain"], "external_oracle": report["oracle"], "counts": report["counts"],
            "direct_augmented_row_oracle_checks": checks, "additional_row_transformations": transforms,
            "explicit_examples": examples,
            "limits": "Finite exact implementation checks, not general proofs; extra user-domain exclusions are not imposed."}


def rational_inequalities_report_check(manifest):
    """Compare whole finite-case sets using exact sign-invariant rational cells."""
    from fractions import Fraction as F
    from itertools import product
    from importlib.metadata import version
    import operator
    from rational_inequalities import solve_linear, solve_absolute, contains

    report = json.loads(RATIONAL_INEQUALITIES_REPORT.read_text())
    sources = hashes([ROOT / "tools" / name for name in
                      ["linear_equation_solvers.py", "rational_inequalities.py",
                       "validate_rational_inequalities.py"]])
    require(report.get("status") == "passed" and report.get("source_sha256") == sources,
            "Rational inequality report is stale or failed")
    provenance = manifest["rational_inequalities_validation"]
    require(provenance["report_sha256"] == hashes([RATIONAL_INEQUALITIES_REPORT])
            and provenance["source_sha256"] == sources, "Inequality evidence differs from build")
    require(report["domain"] == "Five coefficients {-1,-1/2,0,1/2,1}, three slots, four comparisons, each of two solver families",
            "Rational inequality test domain changed")
    require(version("sympy") == "1.14.0"
            and report["oracle"] == "SymPy 1.14.0 exact full real interval unions, then rational membership checks",
            "Inequality external oracle version differs from recorded evidence")
    ops = {'<': operator.lt, '<=': operator.le, '>': operator.gt, '>=': operator.ge}
    checks = dict(linear=0, absolute=0, full_set_oracle=0,
                  rational_membership=0, finite_endpoint_checks=0,
                  invalid_coefficients=0, invalid_relations=0,
                  invalid_membership_values=0, extra_domain_checks=0)
    cells = dict(solution_sets=0, boundary_points=0, open_cells=0)

    def record_member(result, value):
        # Independent interval interpretation; do not call production contains.
        return any((low is None or (low <= value if lc else low < value))
                   and (high is None or (value <= high if rc else value < high))
                   for low, high, lc, rc in result)

    def inspect_case(absolute, a, b, c, relation):
        result = (solve_absolute if absolute else solve_linear)(a, b, c, relation)
        require(type(result) is tuple, "Inequality solution must be a tuple of intervals")
        for interval in result:
            require(type(interval) is tuple and len(interval) == 4, "Invalid interval record")
            low, high, lc, rc = interval
            require(type(lc) is bool and type(rc) is bool
                    and (low is None or type(low) is F) and (high is None or type(high) is F),
                    "Inequality endpoints must be exact Fractions and flags must be booleans")
            require((low is not None or not lc) and (high is not None or not rc),
                    "An unbounded side cannot be a closed endpoint")
            require(low is None or high is None or low < high or (low == high and lc and rc),
                    "Empty or reversed interval record")
        endpoints = {q for interval in result for q in interval[:2] if q is not None}
        cuts = set(endpoints)
        if a:
            # The affine condition changes truth only at its threshold. Absolute
            # value additionally splits at its cusp and both signed thresholds.
            cuts.add((c-b)/a)
            if absolute:
                cuts.update([-b/a, (-c-b)/a])
        ordered = sorted(cuts)
        representatives = ([ordered[0]-1]
                           + [(left+right)/2 for left, right in zip(ordered, ordered[1:])]
                           + [ordered[-1]+1]) if ordered else [F(0)]
        # On every open cell both the original condition and record membership
        # are constant; include all returned cuts to expose extraneous intervals.
        for q in ordered + representatives:
            original = abs(a*q+b) if absolute else a*q+b
            expected = ops[relation](original, c)
            require(record_member(result, q) == expected and contains(result, q) == expected,
                    "Inequality solution differs on an exact boundary or sign-invariant cell")
        cells['solution_sets'] += 1
        cells['boundary_points'] += len(ordered)
        cells['open_cells'] += len(representatives)
        return result, endpoints

    values = [F(-1), F(-1, 2), F(0), F(1, 2), F(1)]
    for absolute in [False, True]:
        for a, b, c in product(values, repeat=3):
            for relation, op in ops.items():
                result, endpoints = inspect_case(absolute, a, b, c, relation)
                checks['absolute' if absolute else 'linear'] += 1
                checks['full_set_oracle'] += 1
                candidates = {F(n, 2) for n in range(-4, 5)} | endpoints
                for endpoint in endpoints:
                    candidates.update([endpoint-F(1, 3), endpoint+F(1, 3)])
                for q in candidates:
                    original = abs(a*q+b) if absolute else a*q+b
                    require(contains(result, q) == record_member(result, q) == op(original, c),
                            "Inequality rational membership or endpoint check failed")
                    checks['rational_membership'] += 1
                    if q in endpoints:
                        checks['finite_endpoint_checks'] += 1

    def rejected(fn, args):
        try:
            fn(*args)
        except ValueError:
            return
        raise ValueError("Inequality API accepted an invalid value")

    bad = [None, True, False, 0.5, '1/2', (1, 2)]
    for fn in [solve_linear, solve_absolute]:
        for position in range(3):
            for value in bad:
                args = [1, 0, 1, '<=']
                args[position] = value
                rejected(fn, args)
                checks['invalid_coefficients'] += 1
        for relation in ['=', '!=', 'le', None, True, 1]:
            rejected(fn, [1, 0, 1, relation])
            checks['invalid_relations'] += 1
    for value in bad:
        rejected(contains, [(), value])
        checks['invalid_membership_values'] += 1
    domain = [F(-1), F(0), F(1), F(2)]
    result = solve_linear(-2, 1, 0, '<')
    require(tuple(q for q in domain if contains(result, q)) == tuple(q for q in domain if -2*q+1 < 0),
            "Caller-supplied finite domain filtering failed")
    checks['extra_domain_checks'] += 1
    require(tuple(q for q in [] if contains(solve_absolute(1, 0, 1, '<'), q)) == (),
            "Empty caller-supplied domain must stay empty")
    checks['extra_domain_checks'] += 1
    require(report['counts'] == checks, "Inequality report counts disagree with actual oracle replay")

    # Recheck every named example through the independent cell oracle; compare
    # names only after the corresponding calls have actually been inspected.
    example_cases = [
        [(False, -2, 1, 0, '<')],
        [(False, 0, 1, 1, '<'), (False, 0, 1, 1, '<=')],
        [(True, 1, 0, -1, '<='), (True, 1, 0, -1, '>')],
        [(True, 2, -1, 0, relation) for relation in ops],
        [(True, 0, -2, 1, '<='), (True, 0, -2, 1, '>')],
        [(True, -2, 1, 3, '<=')],
    ]
    for cases in example_cases:
        for absolute, a, b, c, relation in cases:
            inspect_case(absolute, F(a), F(b), F(c), relation)
    examples = ["negative coefficient reverses strict direction",
                "zero coefficient equal threshold: strict false, weak true",
                "negative absolute threshold: upper empty and lower all",
                "zero threshold distinguishes singleton, empty, all, punctured set",
                "constant absolute value checked before dividing by a",
                "negative affine slope has a positive half width"]
    require(report['explicit_examples'] == examples, "Inequality concrete example inventory changed")
    return {"status": "passed", "evidence_mode": provenance['mode'],
            "report_sha256": hashes([RATIONAL_INEQUALITIES_REPORT]), "source_sha256": sources,
            "domain": report['domain'], "external_oracle": report['oracle'], "counts": checks,
            "direct_sign_invariant_cell_oracle": cells, "explicit_examples": examples,
            "limits": "Finite coefficient implementation checks over Q only; no general proof, expression parser or automatic extra-domain filtering."}


def rational_affine_report_check(manifest):
    """Replay exact APIs against generic row reduction and finite fiber counts."""
    from fractions import Fraction as F
    from itertools import product, combinations
    from importlib.metadata import version
    from rational_affine import (affine_value, slope_through, intercepts,
                                 intersect_affine, classify_linear_relation, finite_graph_test)

    report = json.loads(RATIONAL_AFFINE_REPORT.read_text())
    sources = hashes([ROOT / "tools" / name for name in
                      ["linear_equation_solvers.py", "rational_affine.py", "validate_rational_affine.py"]])
    require(report.get("schema_version") == 1 and report.get("status") == "passed"
            and report.get("source_sha256") == sources, "Rational affine report is stale or failed")
    provenance = manifest["rational_affine_validation"]
    require(provenance["report_sha256"] == hashes([RATIONAL_AFFINE_REPORT])
            and provenance["source_sha256"] == sources, "Affine evidence differs from build")
    require(version("sympy") == "1.14.0"
            and report['oracle'] == "SymPy 1.14.0 exact linsolve; original-equation membership; all finite maps",
            "Affine external oracle version differs from recorded evidence")

    def rows_oracle(rows):
        # RREF for two unknowns, without using production parameter branches.
        rows = [[F(v) for v in row] for row in rows]
        pivots = []
        for column in range(2):
            k = len(pivots)
            found = next((i for i in range(k, len(rows)) if rows[i][column]), None)
            if found is None:
                continue
            rows[k], rows[found] = rows[found], rows[k]
            scale = rows[k][column]
            rows[k] = [v / scale for v in rows[k]]
            for i in range(len(rows)):
                if i != k:
                    scale = rows[i][column]
                    rows[i] = [v-scale*w for v, w in zip(rows[i], rows[k])]
            pivots.append(column)
        if any(not any(row[:2]) and row[-1] for row in rows):
            return 'none', None, None
        base = [F(0), F(0)]
        for row, pivot in zip(rows, pivots):
            base[pivot] = row[-1]
        if len(pivots) == 2:
            return 'unique', tuple(base), None
        if not pivots:
            return 'all', None, None
        free = next(i for i in range(2) if i not in pivots)
        direction = [F(0), F(0)]
        direction[free] = F(1)
        for row, pivot in zip(rows, pivots):
            direction[pivot] = -row[free]
        return 'family', tuple(base), tuple(direction)

    def exact_pair(value):
        return type(value) is tuple and len(value) == 2 and all(type(q) is F for q in value)

    def check_intersection(a, b, c, d):
        result = intersect_affine(a, b, c, d)
        kind, base, direction = rows_oracle([[-a, 1, b], [-c, 1, d]])
        expected = 'coincident' if kind == 'family' else kind
        require(type(result) is dict and set(result) == {'kind', 'point'} and result['kind'] == expected,
                "Affine intersection classification differs from row oracle")
        if kind == 'unique':
            require(exact_pair(result['point']) and result['point'] == base,
                    "Affine intersection point differs from row oracle")
        else:
            require(result['point'] is None, "Nonunique intersection must not supply a point")
        if kind == 'family':
            require(direction[0] != 0 and base[1] == a*base[0]+b == c*base[0]+d
                    and direction[1] == a*direction[0] == c*direction[0],
                    "Coincident record does not cover the full affine graph")
        return result

    def check_intercepts(a, b):
        result = intercepts(a, b)
        kind, base, _ = rows_oracle([[-a, 1, b], [0, 1, 0]])
        expected = 'all' if kind == 'family' else kind
        require(type(result) is dict and set(result) == {'vertical', 'horizontal', 'horizontal_kind'}
                and exact_pair(result['vertical']) and result['vertical'] == (F(0), b)
                and result['horizontal_kind'] == expected, "Axis intercept classification differs from row oracle")
        require((exact_pair(result['horizontal']) and result['horizontal'] == base) if kind == 'unique'
                else result['horizontal'] is None, "Horizontal intercept record differs from row oracle")
        return result

    def check_relation(p, q, r):
        result = classify_linear_relation(p, q, r)
        kind, base, direction = rows_oracle([[p, q, r]])
        expected = ('affine' if direction[0] else 'vertical') if kind == 'family' else kind
        require(type(result) is dict and result.get('kind') == expected,
                "Linear relation classification differs from row-oracle family")
        if expected == 'affine':
            require(set(result) == {'kind', 'a', 'b'}
                    and type(result['a']) is F and type(result['b']) is F
                    and base[1] == result['a']*base[0]+result['b']
                    and direction[1] == result['a']*direction[0],
                    "Affine record does not equal the full row-oracle family")
        elif expected == 'vertical':
            require(set(result) == {'kind', 'x'} and type(result['x']) is F and result['x'] == base[0],
                    "Vertical relation has an incorrect fixed coordinate")
        else:
            require(result == {'kind': expected}, "Unexpected universal/empty relation fields")
        return result

    def reject(fn, *args):
        try:
            fn(*args)
        except ValueError:
            return
        raise ValueError("Affine API accepted an invalid or nonunique input")

    counts = dict(values=0, two_points=0, equal_x_rejected=0,
                  intersections=0, intersection_membership=0,
                  intercepts=0, linear_relations=0, relation_membership=0,
                  finite_graphs=0, input_rejections=0, duplicate_graphs=0)
    values = [F(-1), F(-1, 2), F(0), F(1, 2), F(1)]
    for a, b, t in product(values, repeat=3):
        result = affine_value(a, b, t)
        require(type(result) is F and result-b == a*t, "Affine evaluation fails exact substitution")
        counts['values'] += 1
    for x1, y1, x2, y2 in product(values, repeat=4):
        kind, base, _ = rows_oracle([[x1, 1, y1], [x2, 1, y2]])
        if kind != 'unique':
            reject(slope_through, x1, y1, x2, y2)
            counts['equal_x_rejected'] += 1
        else:
            result = slope_through(x1, y1, x2, y2)
            require(exact_pair(result) and result == base, "Two-point coefficients differ from row oracle")
            counts['two_points'] += 1
    for a, b, c, d in product(values, repeat=4):
        result = check_intersection(a, b, c, d)
        for u, v in product(values, repeat=2):
            included = (result['point'] == (u, v) if result['kind'] == 'unique'
                        else v == a*u+b if result['kind'] == 'coincident' else False)
            require(included == (v == a*u+b and v == c*u+d), "Intersection membership fails original equations")
            counts['intersection_membership'] += 1
        counts['intersections'] += 1
    for a, b in product(values, repeat=2):
        check_intercepts(a, b)
        counts['intercepts'] += 1
    for p, q, r in product(values, repeat=3):
        result = check_relation(p, q, r)
        for u, v in product(values, repeat=2):
            kind = result['kind']
            included = (True if kind == 'all' else False if kind == 'none'
                        else u == result['x'] if kind == 'vertical' else v == result['a']*u+result['b'])
            require(included == (p*u+q*v == r), "Relation membership fails original equation")
            counts['relation_membership'] += 1
        counts['linear_relations'] += 1

    def subsets(items):
        return [tuple(c) for n in range(len(items)+1) for c in combinations(items, n)]

    universe = [F(-1), F(0), F(1)]
    graphs = subsets(list(product(universe, repeat=2)))
    for domain in subsets(universe):
        for codomain in subsets(universe):
            rectangle = set(product(domain, codomain))
            for graph in graphs:
                expected = set(graph) <= rectangle and all(sum(u == x for u, _ in graph) == 1 for x in domain)
                result = finite_graph_test(domain, codomain, graph)
                require(type(result) is bool and result == expected,
                        "Finite graph disagrees with rectangle containment and exact fiber cardinalities")
                counts['finite_graphs'] += 1
    for args in [([0, 0], [1, 1], [(0, 1), (0, 1)]), ([], [], []), ([], [0], [])]:
        require(finite_graph_test(*args) is True, "Duplicate/empty graph set semantics failed")
        counts['duplicate_graphs'] += 1
    bad = [None, True, False, 0.5, '1/2', (1, 2)]
    specs = [(affine_value, [1, 0, 1]), (slope_through, [0, 1, 1, 2]),
             (intercepts, [1, 0]), (intersect_affine, [1, 0, -1, 0]),
             (classify_linear_relation, [1, 1, 1])]
    for fn, template in specs:
        for position in range(len(template)):
            for value in bad:
                args = list(template)
                args[position] = value
                reject(fn, *args)
                counts['input_rejections'] += 1
    for args in [([True], [0], []), ([0], [0.5], []),
                 ([0], [0], [(0, False)]), ([0], [0], [(0,)]),
                 ([0], [0], [(0, 0, 0)]), ([0], [0], [0]),
                 ('0', [0], []), ([0], None, []), ([0], [0], None),
                 ([0], [0], [(1, 0), (0, True)])]:
        reject(finite_graph_test, *args)
        counts['input_rejections'] += 1
    require(report['counts'] == counts, "Affine report counts disagree with actual API replay")
    examples = [
        {'case': '2x-1 and -x+2', 'result': check_intersection(F(2), F(-1), F(-1), F(2))},
        {'case': 'zero graph intercepts', 'result': check_intercepts(F(0), F(0))},
        {'case': 'constant nonzero intercepts', 'result': check_intercepts(F(0), F(3))},
        {'case': 'vertical relation 2x=1', 'result': check_relation(F(2), F(0), F(1))},
        {'case': 'two points (0,-1),(1,1)', 'result': slope_through(0, -1, 1, 1)},
        {'case': 'missing input', 'result': finite_graph_test([0, 1], [0], [(0, 0)])},
    ]
    require(examples[4]['result'] == rows_oracle([[0, 1, -1], [1, 1, 1]])[1]
            and examples[5]['result'] is False, "Affine explicit two-point/missing-input example failed")
    require(report['examples'] == json.loads(json.dumps(examples, default=str)),
            "Affine explicit example results differ from independently checked API results")
    return {"status": "passed", "evidence_mode": provenance['mode'],
            "report_sha256": hashes([RATIONAL_AFFINE_REPORT]), "source_sha256": sources,
            "external_oracle": report['oracle'], "counts": counts,
            "direct_oracle": "Exact two-variable RREF; complete family identities; finite fiber cardinalities",
            "examples": report['examples'],
            "limits": "Finite rational implementation checks only; no proof of all parameters or inference from sampled points to an infinite graph."}


def rational_powers_sums_report_check(manifest):
    """Replay APIs using integer powers and common-denominator integer sums."""
    from fractions import Fraction as F
    from itertools import product
    from math import prod
    from rational_powers_sums import power, partial_sums, finite_sum, segment_sum

    report = json.loads(RATIONAL_POWERS_SUMS_REPORT.read_text())
    sources = hashes([ROOT / 'tools' / name for name in
                      ['linear_equation_solvers.py', 'rational_powers_sums.py',
                       'validate_rational_powers_sums.py']])
    require(report.get('schema_version') == 1 and report.get('status') == 'passed'
            and report.get('source_sha256') == sources, 'Powers/sums report is stale or failed')
    provenance = manifest['rational_powers_sums_validation']
    require(provenance['report_sha256'] == hashes([RATIONAL_POWERS_SUMS_REPORT])
            and provenance['source_sha256'] == sources, 'Powers/sums evidence differs from build')
    require(report['oracle'] == 'Python Fraction integer powers and standard exact sum of independently sliced records',
            'Powers/sums external oracle description changed')
    expected_scope = {'rational_values': ['-2', '-1/2', '0', '1/3', '2'],
                      'power_exponents': [0, 9], 'law_exponents': [0, 6],
                      'record_lengths': [0, 4], 'pointwise_pair_lengths': [0, 3],
                      'padding_lengths': [0, 3]}
    require(report['scope'] == expected_scope, 'Powers/sums finite test scope changed')

    def power_oracle(base, exponent):
        base = F(base)
        return F(pow(base.numerator, exponent), pow(base.denominator, exponent))

    def sum_oracle(items):
        # Aggregate integer numerators over one common denominator, rather than
        # following production's recursive Fraction prefix accumulation.
        items = tuple(F(q) for q in items)
        denominator = prod(q.denominator for q in items)
        numerator = sum(q.numerator*(denominator//q.denominator) for q in items)
        return F(numerator, denominator)

    def exact(actual, expected):
        require(type(actual) is F and actual == expected,
                'Powers/sums result differs from independent exact integer oracle')

    def reject(fn, *args):
        try:
            fn(*args)
        except ValueError:
            return
        raise ValueError('Powers/sums API accepted an invalid input')

    values = [F(-2), F(-1, 2), F(0), F(1, 3), F(2)]
    counts = dict(powers=0, exponent_addition=0, power_iteration=0,
                  product_power=0, records=0, prefix_values=0, segments=0,
                  splits=0, padded_records=0, scaled_records=0,
                  pointwise_sums=0, rejected_inputs=0, input_immutability=0)
    for a, n in product(values, range(10)):
        exact(power(a, n), power_oracle(a, n))
        counts['powers'] += 1
    for a, m, n in product(values, range(7), range(7)):
        combined, left, right = power(a, m+n), power(a, m), power(a, n)
        exact(combined, power_oracle(a, m+n))
        exact(left, power_oracle(a, m))
        exact(right, power_oracle(a, n))
        require(combined == left*right, 'Exponent addition finite identity failed')
        counts['exponent_addition'] += 1
        exact(power(left, n), power_oracle(a, m*n))
        counts['power_iteration'] += 1
    for a, b, n in product(values, values, range(7)):
        exact(power(a*b, n), power_oracle(a, n)*power_oracle(b, n))
        counts['product_power'] += 1
    for length in range(5):
        for items in product(values, repeat=length):
            mutable = list(items)
            prefixes = partial_sums(mutable)
            require(type(prefixes) is tuple and len(prefixes) == length+1,
                    'Prefix record must contain n+1 values, including the empty prefix')
            for n, actual in enumerate(prefixes):
                exact(actual, sum_oracle(items[:n]))
                counts['prefix_values'] += 1
            total = sum_oracle(items)
            exact(finite_sum(mutable), total)
            counts['records'] += 1
            for start in range(length+1):
                for count in range(length-start+1):
                    actual = segment_sum(mutable, start, count)
                    exact(actual, sum_oracle(items[start:start+count]))
                    require(actual == prefixes[start+count]-prefixes[start],
                            'Segment result disagrees with independently checked prefix difference')
                    counts['segments'] += 1
            for k in range(length+1):
                left, right = segment_sum(items, 0, k), segment_sum(items, k, length-k)
                exact(left, sum_oracle(items[:k]))
                exact(right, sum_oracle(items[k:]))
                require(left+right == total, 'Finite split identity failed')
                counts['splits'] += 1
            for count in range(4):
                exact(finite_sum(items+(F(0),)*count), total)
                counts['padded_records'] += 1
            for c in values:
                exact(finite_sum(tuple(c*t for t in items)), c*total)
                counts['scaled_records'] += 1
            require(mutable == list(items), 'A sum API mutated its input record')
            counts['input_immutability'] += 1
    for length in range(4):
        for flat in product(values, repeat=2*length):
            left, right = flat[:length], flat[length:]
            exact(finite_sum(tuple(a+b for a, b in zip(left, right))), sum_oracle(left)+sum_oracle(right))
            counts['pointwise_sums'] += 1
    for base in [None, True, False, 0.5, '2', (1, 2)]:
        reject(power, base, 0)
        counts['rejected_inputs'] += 1
    for exponent in [-1, True, False, F(1), 1.0, '1', None]:
        reject(power, 0, exponent)
        counts['rejected_inputs'] += 1
    for bad in [None, True, False, 0.5, '1', (1, 2)]:
        for fn in [partial_sums, finite_sum]:
            reject(fn, [0, bad])
            counts['rejected_inputs'] += 1
        reject(segment_sum, [0, bad], 0, 0)
        counts['rejected_inputs'] += 1
    for container in [None, {1, 2}, frozenset(), '12', 1, True]:
        for fn in [partial_sums, finite_sum]:
            reject(fn, container)
            counts['rejected_inputs'] += 1
        reject(segment_sum, container, 0, 0)
        counts['rejected_inputs'] += 1
    for index in [-1, True, False, F(0), 0.0, '0', None]:
        reject(segment_sum, [1], index, 0)
        reject(segment_sum, [1], 0, index)
        counts['rejected_inputs'] += 2
    for items, start, count in [([], 1, 0), ([], 0, 1), ([1], 2, 0), ([1], 1, 1), ([1, 2], 0, 3)]:
        reject(segment_sum, items, start, count)
        counts['rejected_inputs'] += 1
    require(report['counts'] == counts, 'Powers/sums report counts disagree with actual API replay')
    four_terms = [F(1, 2), F(-1), F(3, 2), F(2)]
    examples = [
        {'case': 'zero base zero exponent', 'result': power(0, 0)},
        {'case': 'negative fractional cube', 'result': power(F(-2, 3), 3)},
        {'case': 'empty record prefixes', 'result': partial_sums([])},
        {'case': 'four terms', 'result': partial_sums(four_terms)},
        {'case': 'shifted last three terms', 'result': segment_sum([1, -2, 3, -4, 5], 2, 3)},
        {'case': 'empty segment at end', 'result': segment_sum([1, -1], 2, 0)},
    ]
    expected = [power_oracle(0, 0), power_oracle(F(-2, 3), 3), (sum_oracle([]),),
                tuple(sum_oracle(four_terms[:n]) for n in range(5)), sum_oracle([3, -4, 5]), sum_oracle([])]
    for record, result in zip(examples, expected):
        actual = record['result']
        if type(result) is tuple:
            require(type(actual) is tuple and len(actual) == len(result), 'Explicit prefix example shape changed')
            for a, b in zip(actual, result):
                exact(a, b)
        else:
            exact(actual, result)
    require(report['examples'] == json.loads(json.dumps(examples, default=str)),
            'Powers/sums explicit example results differ from independently checked APIs')
    return {'status': 'passed', 'evidence_mode': provenance['mode'],
            'report_sha256': hashes([RATIONAL_POWERS_SUMS_REPORT]), 'source_sha256': sources,
            'scope': expected_scope, 'external_oracle': report['oracle'], 'counts': counts,
            'direct_oracle': 'Integer numerator/denominator powers and integer sums over a common denominator',
            'examples': report['examples'],
            'limits': 'Finite exact implementation checks only; no negative exponent, infinite sum, callback or universal proof.'}


def rational_polynomial_basic_report_check(manifest):
    """Independent sparse-coefficient oracle and Horner evaluation; finite scope."""
    from fractions import Fraction as F
    from itertools import product
    import rational_polynomial_basic as api

    report = json.loads(RATIONAL_POLYNOMIAL_BASIC_REPORT.read_text())
    sources = hashes([ROOT / 'tools' / name for name in
                      ['linear_equation_solvers.py', 'rational_powers_sums.py',
                       'rational_polynomial_basic.py', 'validate_rational_polynomial_basic.py']])
    require(report.get('status') == 'passed' and report.get('source_sha256') == sources,
            'Polynomial report is stale or failed')
    provenance = manifest['rational_polynomial_basic_validation']
    require(provenance['report_sha256'] == hashes([RATIONAL_POLYNOMIAL_BASIC_REPORT])
            and provenance['source_sha256'] == sources, 'Polynomial evidence differs from build')
    require(report['oracle'] == 'SymPy 1.14.0 Poly over QQ from independent coefficient dictionary',
            'Polynomial external oracle changed')
    scope = {'coefficient_values': ['-1', '0', '1/2'], 'record_lengths': [1, 4],
             'pair_lengths': [1, 3], 'triple_lengths': [1, 2],
             'points': ['-2', '-1/2', '0', '1', '2']}
    require(report['scope'] == scope, 'Polynomial finite test scope changed')
    values = (F(-1), F(0), F(1, 2))
    points = (F(-2), F(-1, 2), F(0), F(1), F(2))

    def records(maximum):
        return [a for n in range(1, maximum+1) for a in product(values, repeat=n)]

    def sparse(a):
        return {i: F(q) for i, q in enumerate(a) if q != 0}

    def canonical(d):
        support = {i: q for i, q in d.items() if q != 0}
        return tuple(support.get(i, F(0)) for i in range(max(support, default=0)+1))

    def combine(*terms):
        # Work on support dictionaries, not production's dense aligned loops.
        keys = set().union(*(d for scalar, d in terms))
        return canonical({i: sum((scalar*d.get(i, F(0)) for scalar, d in terms), F(0))
                          for i in keys})

    def horner(a, t):
        result = F(0)
        for coefficient in reversed(a):
            result = result*t+coefficient
        return result

    def exact(actual, expected):
        require(type(actual) is F and actual == expected,
                'Polynomial exact value differs from independent oracle')

    def exact_record(actual, expected):
        require(type(actual) is tuple and len(actual) == len(expected),
                'Polynomial canonical record shape differs')
        for a, b in zip(actual, expected):
            exact(a, b)

    def reject(fn, *args):
        try:
            fn(*args)
        except (TypeError, ValueError):
            return
        raise ValueError('Polynomial API accepted invalid input: '+fn.__name__)

    counts = dict.fromkeys(['records', 'coefficients', 'evaluations', 'padding', 'scalings',
                            'pairs', 'evaluation_linearity', 'triples', 'rejected_inputs',
                            'input_immutability'], 0)
    for a in records(4):
        d = sparse(a)
        expected = canonical(d)
        actual = api.normalize(a)
        exact_record(actual, expected)
        exact_record(api.normalize(actual), expected)
        if d:
            degree = api.degree(a)
            require(type(degree) is int and degree == max(d), 'Polynomial degree differs')
        else:
            reject(api.degree, a)
        counts['records'] += 1
        for i in range(len(a)+3):
            exact(api.coefficient(a, i), d.get(i, F(0)))
            counts['coefficients'] += 1
        for t in points:
            exact(api.evaluate(a, t), horner(a, t))
            counts['evaluations'] += 1
        for extra in range(4):
            padded = a+(F(0),)*extra
            exact_record(api.normalize(padded), expected)
            require(api.same_polynomial(a, padded) is True, 'Tail-zero equality failed')
            for t in points:
                exact(api.evaluate(padded, t), horner(a, t))
            counts['padding'] += 1
        for scalar in values:
            result = api.scale(scalar, a)
            exact_record(result, combine((scalar, d)))
            exact_record(api.scale(1, a), expected)
            exact_record(api.scale(0, a), (F(0),))
            for t in points:
                exact(api.evaluate(result, t), scalar*horner(a, t))
            if scalar and d:
                require(api.degree(result) == max(d), 'Nonzero scaling degree changed')
            else:
                reject(api.degree, result)
            counts['scalings'] += 1
        mutable = list(a)
        original = mutable.copy()
        api.normalize(mutable)
        api.evaluate(mutable, F(1, 2))
        api.scale(-1, mutable)
        require(mutable == original, 'Polynomial API mutated input')
        counts['input_immutability'] += 1
    small = records(3)
    for a, b in product(small, repeat=2):
        da, db = sparse(a), sparse(b)
        expected = combine((F(1), da), (F(1), db))
        result = api.add(a, b)
        exact_record(result, expected)
        exact_record(api.subtract(a, b), combine((F(1), da), (F(-1), db)))
        require(api.same_polynomial(a, b) is (da == db), 'Coefficient equality differs')
        exact_record(api.add(b, a), expected)
        ds = sparse(expected)
        if da and db and ds:
            require(api.degree(result) <= max(max(da), max(db)), 'Sum degree bound failed')
        if da and db and max(da) != max(db):
            require(ds and api.degree(result) == max(max(da), max(db)),
                    'Unequal-degree addition lost highest nonzero coefficient')
        for t in points:
            exact(api.evaluate(result, t), horner(a, t)+horner(b, t))
            counts['evaluation_linearity'] += 1
        for scalar in values:
            target = combine((scalar, da), (scalar, db))
            exact_record(api.scale(scalar, result), target)
            exact_record(api.add(api.scale(scalar, a), api.scale(scalar, b)), target)
        counts['pairs'] += 1
    for a, b, c in product(records(2), repeat=3):
        target = combine((F(1), sparse(a)), (F(1), sparse(b)), (F(1), sparse(c)))
        exact_record(api.add(api.add(a, b), c), target)
        exact_record(api.add(a, api.add(b, c)), target)
        counts['triples'] += 1
    for a in small:
        for s, t in product(values, repeat=2):
            exact_record(api.scale(s, api.scale(t, a)), combine((s*t, sparse(a))))
            target = combine((s+t, sparse(a)))
            exact_record(api.scale(s+t, a), target)
            exact_record(api.add(api.scale(s, a), api.scale(t, a)), target)
        exact_record(api.add(a, api.scale(-1, a)), (F(0),))
    for bad in [[], (), None, 1, '1', {0: 1}, {1}, iter([1]), [True], [1.0], [F(1), False]]:
        for fn, args in [(api.normalize, (bad,)), (api.coefficient, (bad, 0)),
                         (api.evaluate, (bad, 0)), (api.scale, (0, bad)),
                         (api.add, ((1,), bad)), (api.add, (bad, (1,))),
                         (api.same_polynomial, ((1,), bad))]:
            reject(fn, *args)
            counts['rejected_inputs'] += 1
    for bad in [True, 1.0, F(1), -1, None]:
        reject(api.coefficient, (1,), bad)
        counts['rejected_inputs'] += 1
    for bad in [True, 1.0, None, '1']:
        reject(api.evaluate, (0,), bad)
        reject(api.scale, bad, (0,))
        counts['rejected_inputs'] += 2
    reject(api.degree, (0, 0))
    counts['rejected_inputs'] += 1
    require(report['counts'] == counts, 'Polynomial report counts differ from actual API replay')
    examples = [
        {'name': 'tail_zero_normalization', 'input': [1, 0, 2, 0, 0],
         'output': api.normalize((1, 0, 2, 0, 0))},
        {'name': 'zero_normalization', 'input': [0, 0, 0], 'output': api.normalize((0, 0, 0))},
        {'name': 'internal_zero_is_not_tail', 'at': 2,
         'left': api.evaluate((1, 0, 2), 2), 'right': api.evaluate((1, 2), 2)},
        {'name': 'leading_cancellation', 'left': [1, 2], 'right': [3, -2],
         'output': api.add((1, 2), (3, -2))},
        {'name': 'total_cancellation', 'output': api.add((1, 2), (-1, -2))},
        {'name': 'negative_scaling', 'output': api.scale(F(-1, 2), (1, -1, 2))}]
    for i, expected in [(0, canonical(sparse((1, 0, 2, 0, 0)))),
                        (1, canonical({})),
                        (3, combine((F(1), sparse((1, 2))), (F(1), sparse((3, -2))))),
                        (4, combine((F(1), sparse((1, 2))), (F(1), sparse((-1, -2))))),
                        (5, combine((F(-1, 2), sparse((1, -1, 2)))) )]:
        exact_record(examples[i]['output'], expected)
    exact(examples[2]['left'], horner((1, 0, 2), F(2)))
    exact(examples[2]['right'], horner((1, 2), F(2)))
    require(report['examples'] == json.loads(json.dumps(examples, default=str)),
            'Polynomial examples differ from independently checked API results')
    return {'status': 'passed', 'evidence_mode': provenance['mode'],
            'report_sha256': hashes([RATIONAL_POLYNOMIAL_BASIC_REPORT]), 'source_sha256': sources,
            'scope': scope, 'external_oracle': report['oracle'], 'counts': counts,
            'direct_oracle': 'Sparse nonzero coefficient maps, support maxima, and exact Horner evaluation',
            'examples': report['examples'],
            'limits': 'Finite implementation evidence only; no polynomial multiplication, zero degree or proof by sampling.'}


def rational_polynomial_product_report_check(manifest):
    """Replay finite checks with constant-plus-shift recursion, never convolution."""
    from fractions import Fraction as F
    from itertools import product
    import rational_polynomial_basic as basic
    import rational_polynomial_product as api

    report = json.loads(RATIONAL_POLYNOMIAL_PRODUCT_REPORT.read_text())
    sources = hashes([ROOT / 'tools' / name for name in
                      ['linear_equation_solvers.py', 'rational_powers_sums.py',
                       'rational_polynomial_basic.py', 'rational_polynomial_product.py',
                       'validate_rational_polynomial_product.py']])
    require(report.get('schema_version') == 1 and report.get('status') == 'passed'
            and report.get('source_sha256') == sources, 'Polynomial product report is stale or failed')
    require(datetime.fromisoformat(report['validated_at']).tzinfo is not None,
            'Polynomial product report lacks a timezone-aware validation time')
    provenance = manifest['rational_polynomial_product_validation']
    require(provenance['report_sha256'] == hashes([RATIONAL_POLYNOMIAL_PRODUCT_REPORT])
            and provenance['source_sha256'] == sources,
            'Polynomial product evidence differs from build')
    require(report['oracle'] == 'SymPy 1.14.0 Poly over QQ', 'Polynomial product external oracle changed')
    scope = {'coefficient_values': ['-1', '0', '1/2', '2'], 'record_lengths': [1, 3],
             'triple_coefficient_values': ['-1', '0', '1/2'], 'triple_lengths': [1, 2],
             'points': ['-2', '-1/2', '0', '1', '2']}
    require(report['scope'] == scope, 'Polynomial product finite scope changed')
    values = (F(-1), F(0), F(1, 2), F(2))
    points = (F(-2), F(-1, 2), F(0), F(1), F(2))
    records = [a for n in range(1, 4) for a in product(values, repeat=n)]

    def canonical(a):
        support = {i: F(q) for i, q in enumerate(a) if q}
        return tuple(support.get(i, F(0)) for i in range(max(support, default=0)+1))

    def plus(a, b):
        return canonical(tuple((a[i] if i < len(a) else F(0))
                               + (b[i] if i < len(b) else F(0))
                               for i in range(max(len(a), len(b)))))

    def scaled(s, a):
        return canonical(tuple(s*q for q in a))

    def shifted(a):
        return canonical((F(0),)+a)

    @lru_cache(maxsize=None)
    def recursive_product(a, b):
        # b = constant(b[0]) + shift(b[1:]); the one-item case never
        # normalizes an empty tail. No coefficient-pair convolution here.
        constant_part = scaled(b[0], a)
        if len(b) == 1:
            return constant_part
        return plus(constant_part, shifted(recursive_product(a, b[1:])))

    def horner(a, t):
        result = F(0)
        for q in reversed(a):
            result = result*t+q
        return result

    def exact(actual, expected):
        require(type(actual) is F and actual == expected,
                'Polynomial product exact value differs from independent oracle')

    def exact_record(actual, expected):
        require(type(actual) is tuple and len(actual) == len(expected),
                'Polynomial product canonical record shape differs')
        for a, b in zip(actual, expected):
            exact(a, b)

    def reject(fn, *args):
        try:
            fn(*args)
        except (TypeError, ValueError):
            return
        raise ValueError('Polynomial product API accepted invalid input: '+fn.__name__)

    counts = dict.fromkeys(['records', 'pairs', 'evaluations', 'padding', 'scalings',
                            'triples', 'rejections', 'immutability'], 0)
    for a in records:
        expected = canonical(a)
        exact_record(api.shift(a), shifted(a))
        exact_record(api.multiply(a, (1,)), expected)
        exact_record(api.multiply((0,), a), (F(0),))
        for t in points:
            exact(basic.evaluate(api.shift(a), t), t*horner(a, t))
        for k in range(3):
            exact_record(api.shift(a+(F(0),)*k), shifted(a))
        mutable = list(a)
        original = mutable.copy()
        api.shift(mutable)
        api.multiply(mutable, mutable)
        require(mutable == original, 'Polynomial product API mutated input')
        counts['immutability'] += 1
        counts['records'] += 1
    for a, b in product(records, repeat=2):
        expected = recursive_product(a, b)
        result = api.multiply(a, b)
        exact_record(result, expected)
        exact_record(api.multiply(b, a), expected)
        exact_record(api.multiply(api.shift(a), b), shifted(expected))
        exact_record(api.multiply(a, api.shift(b)), shifted(expected))
        ca, cb = canonical(a), canonical(b)
        if ca != (F(0),) and cb != (F(0),):
            d = basic.degree(result)
            require(type(d) is int and d == len(ca)+len(cb)-2,
                    'Nonzero product degree differs from independent support maxima')
            exact(result[-1], ca[-1]*cb[-1])
        else:
            exact_record(result, (F(0),))
            reject(basic.degree, result)
        for t in points:
            exact(basic.evaluate(result, t), horner(expected, t))
            exact(basic.evaluate(result, t), horner(a, t)*horner(b, t))
            counts['evaluations'] += 1
        for k in (0, 1, 3):
            exact_record(api.multiply(a+(F(0),)*k, b+(F(0),)*k), expected)
            counts['padding'] += 1
        for scalar in (F(0), F(-1, 2), F(2)):
            target = scaled(scalar, expected)
            exact_record(api.multiply(basic.scale(scalar, a), b), target)
            exact_record(api.multiply(a, basic.scale(scalar, b)), target)
            counts['scalings'] += 1
        counts['pairs'] += 1
    small = [a for n in (1, 2) for a in product((F(-1), F(0), F(1, 2)), repeat=n)]
    for a, b, c in product(small, repeat=3):
        target = recursive_product(recursive_product(a, b), c)
        exact_record(api.multiply(api.multiply(a, b), c), target)
        exact_record(api.multiply(a, api.multiply(b, c)), target)
        exact_record(api.multiply(basic.add(a, b), c), recursive_product(plus(a, b), c))
        exact_record(api.multiply(a, basic.add(b, c)), recursive_product(a, plus(b, c)))
        counts['triples'] += 1
    for bad in [[], (), None, 1, '1', {0: 1}, {1}, iter([1]), [True], [1.0], [F(1), False]]:
        for fn, args in [(api.shift, (bad,)), (api.multiply, (bad, (0,))),
                         (api.multiply, ((0,), bad))]:
            reject(fn, *args)
            counts['rejections'] += 1
    require(report['counts'] == counts, 'Polynomial product counts differ from actual API replay')
    examples = [
        {'name': 'zero_shift', 'output': api.shift((0, 0))},
        {'name': 'coefficient_convolution', 'left': [1, -1, 2], 'right': [0, 3],
         'output': api.multiply((1, -1, 2), (0, 3))},
        {'name': 'square_difference', 'output': api.multiply((-2, 1), (2, 1))},
        {'name': 'fractional_coefficients',
         'output': api.multiply((F(1, 2), 0, F(-1, 3)), (-2, 1))},
        {'name': 'zero_product', 'output': api.multiply((0, 0), (1, 0, 2))},
        {'name': 'tail_zero_representatives', 'output': api.multiply((1, 1, 0, 0), (1, -1, 0))}]
    targets = [shifted((F(0), F(0))),
               recursive_product((F(1), F(-1), F(2)), (F(0), F(3))),
               recursive_product((F(-2), F(1)), (F(2), F(1))),
               recursive_product((F(1, 2), F(0), F(-1, 3)), (F(-2), F(1))),
               recursive_product((F(0), F(0)), (F(1), F(0), F(2))),
               recursive_product((F(1), F(1), F(0), F(0)), (F(1), F(-1), F(0)))]
    for item, target in zip(examples, targets):
        exact_record(item['output'], target)
    require(report['examples'] == json.loads(json.dumps(examples, default=str)),
            'Polynomial product examples differ from independently checked API results')
    return {'status': 'passed', 'evidence_mode': provenance['mode'],
            'report_sha256': hashes([RATIONAL_POLYNOMIAL_PRODUCT_REPORT]), 'source_sha256': sources,
            'scope': scope, 'external_oracle': report['oracle'], 'counts': counts,
            'direct_oracle': 'Constant-plus-shift recursive product, exact Horner evaluation, support maxima',
            'examples': report['examples'],
            'limits': 'Finite implementation checks only; no zero degree, polynomial division, or proof by sampling.'}


def rational_polynomial_linear_division_report_check(manifest):
    """Independent explicit-power quotient sums and coefficient reconstruction."""
    from fractions import Fraction as F
    from itertools import product
    import rational_polynomial_linear_division as api
    import rational_polynomial_basic as basic

    report = json.loads(RATIONAL_POLYNOMIAL_LINEAR_DIVISION_REPORT.read_text())
    sources = hashes([ROOT / 'tools' / name for name in
                      ['linear_equation_solvers.py', 'rational_powers_sums.py',
                       'rational_polynomial_basic.py', 'rational_polynomial_product.py',
                       'rational_polynomial_linear_division.py',
                       'validate_rational_polynomial_linear_division.py']])
    require(report.get('schema_version') == 1 and report.get('status') == 'passed'
            and report.get('source_sha256') == sources, 'Linear polynomial division report is stale or failed')
    require(datetime.fromisoformat(report['validated_at']).tzinfo is not None,
            'Linear polynomial division report lacks a timezone-aware validation time')
    provenance = manifest['rational_polynomial_linear_division_validation']
    require(provenance['report_sha256'] == hashes([RATIONAL_POLYNOMIAL_LINEAR_DIVISION_REPORT])
            and provenance['source_sha256'] == sources, 'Linear polynomial division evidence differs from build')
    require(report['oracle'] == 'SymPy 1.14.0 Poly over QQ, division by X-a',
            'Linear polynomial division external oracle changed')
    scope = {'coefficient_values': ['-1', '0', '1/2'], 'record_lengths': [1, 4],
             'additional_records': [[-6, 11, -6, 1], [1, 0, 2], [0, 0, 0, 0, 0]],
             'points': ['-2', '-1/2', '0', '1', '2']}
    require(report['scope'] == scope, 'Linear polynomial division finite scope changed')
    values = (F(-1), F(0), F(1, 2))
    records = [a for n in range(1, 5) for a in product(values, repeat=n)]
    records += [tuple(map(F, a)) for a in scope['additional_records']]
    points = (F(-2), F(-1, 2), F(0), F(1), F(2))

    def canonical(a):
        support = {i: F(q) for i, q in enumerate(a) if q}
        return tuple(support.get(i, F(0)) for i in range(max(support, default=0)+1))

    def quotient_sum(a, t):
        # Coefficient j is the sum of original coefficients at positions i>j,
        # weighted by t**(i-j-1). This does not replay the descending state loop.
        q = tuple(sum((F(a[i])*t**(i-j-1) for i in range(j+1, len(a))), F(0))
                  for j in range(len(a)-1))
        return canonical(q), sum((F(c)*t**i for i, c in enumerate(a)), F(0))

    def exact(actual, expected):
        require(type(actual) is F and actual == expected,
                'Linear polynomial division exact value differs from independent oracle')

    def exact_record(actual, expected):
        require(type(actual) is tuple and len(actual) == len(expected),
                'Linear polynomial division canonical record shape differs')
        for a, b in zip(actual, expected):
            exact(a, b)

    def verify(a, t):
        result = api.divide_linear(a, t)
        require(type(result) is tuple and len(result) == 2,
                'Linear polynomial division must return the quotient/remainder pair')
        q, r = result
        expected_q, expected_r = quotient_sum(a, t)
        exact_record(q, expected_q)
        exact(r, expected_r)
        # Direct coefficient reconstruction of (X-t)q+r; no production multiply/add.
        rebuilt = [r-t*q[0]]
        rebuilt += [q[i-1]-t*(q[i] if i < len(q) else F(0)) for i in range(1, len(q)+1)]
        exact_record(canonical(rebuilt), canonical(a))
        return q, r

    def reject(*args):
        try:
            api.divide_linear(*args)
        except (TypeError, ValueError):
            return
        raise ValueError('Linear polynomial division API accepted invalid input')

    counts = dict.fromkeys(['records', 'divisions', 'padding', 'suffixes', 'nonconstant_degree',
                            'constant_zero', 'rejections', 'immutability'], 0)
    for a in records:
        counts['records'] += 1
        mutable = list(a)
        original = mutable.copy()
        ca = canonical(a)
        for t in points:
            q, r = verify(mutable, t)
            counts['divisions'] += 1
            if len(ca) == 1:
                exact_record(q, (F(0),))
                counts['constant_zero'] += 1
            else:
                d = basic.degree(q)
                require(type(d) is int and d == len(ca)-2,
                        'Nonconstant linear quotient degree differs from support bound')
                counts['nonconstant_degree'] += 1
            for k in (0, 1, 3):
                padded_q, padded_r = verify(a+(F(0),)*k, t)
                exact_record(padded_q, q)
                exact(padded_r, r)
                counts['padding'] += 1
            for start in range(len(a)):
                verify(a[start:], t)
                counts['suffixes'] += 1
        require(mutable == original, 'Linear polynomial division API mutated input')
        counts['immutability'] += 1
    for bad in [[], (), None, 1, '1', {0: 1}, {1}, iter([1]), [True], [1.0], [F(1), False]]:
        for t in (0, F(-1, 2)):
            reject(bad, t)
            counts['rejections'] += 1
    for bad in [True, False, 1.0, None, '1', complex(1), [1]]:
        for a in [(0,), (1,), (1, 0, 2)]:
            reject(a, bad)
            counts['rejections'] += 1
    require(report['counts'] == counts, 'Linear polynomial division counts differ from actual API replay')
    examples = []
    for name, a, t in [
            ('cubic_root', (-6, 11, -6, 1), F(1)),
            ('nonzero_remainder', (1, 0, 2), F(2)),
            ('constant', (F(-3, 2),), F(-2)),
            ('zero_tail', (0, 0, 0), F(1, 2)),
            ('fractional', (F(1, 2), F(-1, 3), F(2, 3)), F(-1, 2)),
            ('zero_parameter', (2, -3, 4), F(0))]:
        q, r = verify(a, t)
        examples.append({'name': name, 'record': a, 'at': t, 'quotient': q, 'remainder': r})
    require(report['examples'] == json.loads(json.dumps(examples, default=str)),
            'Linear polynomial division examples differ from independently checked API results')
    return {'status': 'passed', 'evidence_mode': provenance['mode'],
            'report_sha256': hashes([RATIONAL_POLYNOMIAL_LINEAR_DIVISION_REPORT]), 'source_sha256': sources,
            'scope': scope, 'external_oracle': report['oracle'], 'counts': counts,
            'direct_oracle': 'Explicit power-weighted quotient sums, direct evaluation and coefficient reconstruction',
            'examples': report['examples'],
            'limits': 'Finite exact linear-divisor checks only; no general division, root enumeration, or universal proof.'}


def rational_quadratics_report_check(manifest):
    """Replay exact APIs with integer isqrt and independent QQ root extraction."""
    from fractions import Fraction as F
    from itertools import product
    from math import isqrt
    import sympy as sp
    import rational_quadratics as api

    report = json.loads(RATIONAL_QUADRATICS_REPORT.read_text())
    sources = hashes([ROOT / 'tools' / name for name in
                      ['linear_equation_solvers.py', 'rational_quadratics.py',
                       'validate_rational_quadratics.py']])
    require(report.get('schema_version') == 1 and report.get('status') == 'passed'
            and report.get('source_sha256') == sources, 'Rational quadratic report is stale or failed')
    require(datetime.fromisoformat(report['validated_at']).tzinfo is not None,
            'Rational quadratic report lacks a timezone-aware validation time')
    provenance = manifest['rational_quadratics_validation']
    require(provenance['report_sha256'] == hashes([RATIONAL_QUADRATICS_REPORT])
            and provenance['source_sha256'] == sources, 'Rational quadratic evidence differs from build')
    require(report['oracle'] == 'Python math.isqrt and SymPy 1.14.0 Poly QQ ground_roots'
            and sp.__version__ == '1.14.0', 'Rational quadratic external oracle changed')
    scope = {'integer_range': [0, 4095], 'large_integer_cases': 6,
             'fraction_numerators': [-80, 80], 'fraction_denominators': [1, 19],
             'quadratic_coefficients': ['-2', '-1', '-3/4', '-1/2', '0', '1/2', '2/3', '1', '2']}
    require(report['scope'] == scope, 'Rational quadratic finite scope changed')
    counts = dict.fromkeys(['integer_bounds', 'rational_squares', 'quadratics', 'all', 'none',
                            'finite_one', 'finite_two', 'rejections'], 0)

    def square(value):
        actual = api.rational_square_root(value)
        expected = None
        if value >= 0:
            m, n = isqrt(value.numerator), isqrt(value.denominator)
            if m*m == value.numerator and n*n == value.denominator:
                expected = F(m, n)
        require(actual == expected and (actual is None or type(actual) is F),
                'Rational square result differs from independent integer oracle')
        if actual is not None:
            require(actual >= 0 and actual*actual == value, 'Rational square witness is invalid')
        return actual

    x = sp.Symbol('x')

    def quadratic(a, b, c):
        actual = api.solve_quadratic(a, b, c)
        a, b, c = map(F, (a, b, c))
        if a == b == c == 0:
            expected = {'kind': 'all'}
        else:
            # Polynomial factor extraction over QQ does not evaluate the API's
            # discriminant formula or call its binary integer-square routine.
            poly = sp.Poly(sum(sp.Rational(q.numerator, q.denominator)*x**i
                               for i, q in enumerate((c, b, a))), x, domain=sp.QQ)
            roots = tuple(sorted(F(int(r.p), int(r.q)) for r in poly.ground_roots()))
            expected = {'kind': 'finite', 'roots': roots} if roots else {'kind': 'none'}
        require(type(actual) is dict and actual == expected,
                'Rational quadratic solution set differs from independent QQ roots')
        if actual['kind'] == 'finite':
            roots = actual['roots']
            require(type(roots) is tuple and len(roots) in (1, 2)
                    and tuple(sorted(set(roots))) == roots
                    and all(type(t) is F and a*t*t+b*t+c == 0 for t in roots),
                    'Rational quadratic roots fail exact type/order/substitution checks')
        return actual

    for n in list(range(4096)) + [10**100+k for k in (-1, 0, 1)] + [(10**60+1)**2+k for k in (-1, 0, 1)]:
        s = api.integer_sqrt(n)
        require(type(s) is int and s == isqrt(n) and s >= 0 and s*s <= n < (s+1)*(s+1),
                'Binary integer square bound differs from independent isqrt')
        counts['integer_bounds'] += 1
    for a, b in product(range(-80, 81), range(1, 20)):
        square(F(a, b))
        counts['rational_squares'] += 1
    for a, b, c in product(map(F, scope['quadratic_coefficients']), repeat=3):
        actual = quadratic(a, b, c)
        kind = actual['kind']
        key = ('finite_one' if len(actual['roots']) == 1 else 'finite_two') if kind == 'finite' else kind
        counts[key] += 1
        counts['quadratics'] += 1

    def reject(function, *args):
        try:
            function(*args)
        except (TypeError, ValueError):
            counts['rejections'] += 1
            return
        raise ValueError('Rational quadratic API accepted invalid input')

    for bad in [True, False, 1.0, F(1), -1, None, '1']:
        reject(api.integer_sqrt, bad)
    for bad in [True, False, 1.0, None, '1', complex(1), [1]]:
        reject(api.rational_square_root, bad)
        for i in range(3):
            args = [0, 0, 0]
            args[i] = bad
            reject(api.solve_quadratic, *args)
    require(report['counts'] == counts, 'Rational quadratic counts differ from actual API replay')
    examples = []
    for name, args in [('square_zero', [F(0)]), ('square_reduced', [F(8, 18)]),
                       ('square_nonsquare', [F(2)])]:
        examples.append({'name': name, 'operation': 'rational_square_root',
                         'inputs': args, 'output': square(*args)})
    for name, args in [('linear', [0, 2, -6]), ('quadratic_two', [F(3, 2), -1, F(-1, 2)]),
                       ('quadratic_repeated', [1, -3, F(9, 4)]), ('quadratic_all', [0, 0, 0]),
                       ('quadratic_negative_leading', [-1, 3, -2])]:
        examples.append({'name': name, 'operation': 'solve_quadratic',
                         'inputs': args, 'output': quadratic(*args)})
    require(report['examples'] == json.loads(json.dumps(examples, default=str)),
            'Rational quadratic examples differ from independently checked API results')
    return {'status': 'passed', 'evidence_mode': provenance['mode'],
            'report_sha256': hashes([RATIONAL_QUADRATICS_REPORT]), 'source_sha256': sources,
            'scope': scope, 'external_oracle': report['oracle'], 'counts': counts,
            'direct_oracle': 'Python math.isqrt; SymPy QQ factor/root extraction; exact substitution',
            'examples': report['examples'],
            'limits': 'Finite exact implementation checks only; not universal proof or real-root computation.'}


def main():
    require(len(UNITS) == 61 and len(PAIRS) == 502 and len(FIGURES) == 21,
            "Batch 30 registration counts must be 61 units, 502 exercise pairs and 21 figures")
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    # Immediately invalidate an earlier acceptance, including if this run later fails.
    REPORT.write_text(json.dumps({"status": "validation_in_progress",
                                  "visual_review": {"status": "pending_actual_image_inspection"}}, indent=2) + "\n")
    manifest = json.loads((BUILD / "build_inputs.json").read_text())
    require(source_hashes() == manifest["source_sha256"], "Build sources changed; rebuild the batch")
    require(artifact_hashes() == manifest["artifact_sha256"], "Build artifacts changed; rebuild the batch")
    legacy = json.loads((BUILD / "legacy_validation_snapshot.json").read_text())
    require(legacy["status"] == "automated_checks_passed", "Missing legacy validation")
    require(hashlib.sha256((BUILD / "legacy_validation_snapshot.json").read_bytes()).hexdigest()
            == manifest["legacy_snapshot_sha256"], "Legacy validation snapshot changed")
    current = artifact_hashes()
    reused = manifest.get("legacy_reuse", {})
    if reused.get("mode") == "validated_snapshot_reuse":
        prior_path = ROOT / reused["prior_manifest_path"]
        require(hashlib.sha256(prior_path.read_bytes()).hexdigest() == reused["prior_manifest_sha256"],
                "Archived prior manifest for incremental reuse changed")
        prior = json.loads(prior_path.read_text())
        require(prior["legacy_snapshot_sha256"] == reused["snapshot_sha256"]
                == manifest["legacy_snapshot_sha256"], "Incremental snapshot chain differs")
        for path, digest in reused["legacy_source_sha256"].items():
            require(prior["source_sha256"].get(path) == digest == manifest["source_sha256"].get(path),
                    "Incremental legacy source chain differs: " + path)
        for path, digest in reused["independent_artifact_sha256"].items():
            require(legacy["artifact_sha256"].get(path) == digest == current.get(path),
                    "Incremental independent artifact chain differs: " + path)
    for path, digest in legacy["artifact_sha256"].items():
        if "综合数学_第一章审阅版" in path or "综合数学_完整数学目录" in path:
            require(current[path] == digest, "Independent legacy artifact changed: " + path)
    SCREEN.mkdir(parents=True, exist_ok=True)
    for old in SCREEN.glob("*.png"):
        old.unlink()
    full = (OUT / "综合数学.md").read_text()
    review = (OUT / (REVIEW_STEM + ".md")).read_text()
    catalog = json.loads((ROOT / "data/catalog_validation.json").read_text())
    require(catalog["catalog_checks"]["heading_counts"] == {"部分": 63, "章": 534, "节": 6006}, "Catalogue validation mismatch")
    require(len(re.findall(r"^## 第\d+部分 ", full, re.M)) == 63, "Catalogue parts mismatch")
    require(len(re.findall(r"^### 第\d+章 ", full, re.M)) == 534, "Catalogue chapters mismatch")
    require(len(re.findall(r"^- 第\d+节 ", full, re.M)) == 6006, "Catalogue sections mismatch")
    for text in [full, review]:
        require(re.findall(r"^# 第(\d+)章 ", text, re.M) == ["1", "26", "526", "529", "528", "529", "528", "526", "528", "527", "242"],
                "Teaching chapter order must follow prerequisites, with chapters 529, 528 and 526 continued")
        require(re.findall(r"^# 第(\d+)部分 ", text, re.M) == ["1", "7", "63", "28"],
                "Teaching parts must follow prerequisites: 1, 7, 63, 28")
        require(re.findall(r"^## 第(\d+)节 ", text, re.M) == [str(i) for i in range(1, 24)], "First chapter section numbering changed")
        require(re.findall(r"^# 附录(二十八|二十七|二十六|二十五|二十四|二十三|二十二|二十一|二十|十九|十八|十七|十六|十五|十四|十三|十二|十一|十|[一二三四五六七八九]) ", text, re.M)
                == ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十", "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十", "二十一", "二十二", "二十三", "二十四", "二十五", "二十六", "二十七", "二十八"],
                "Appendix numbering conflict")
        answers = text.index("# 附录一 ")
        require(all(text.index("{#" + anchor + "}") < answers for _stem, anchor, *_ in UNITS),
                "Answers interleaved with teaching prose")
        require(all(text.index("{#" + q + "}") < answers < text.index("{#" + a + "}") for q, a in PAIRS),
                "Exercise/answer separation failed")
        teaching_order = ["26", "526", "529", "528", "529-continuation", "528-continuation", "526-continuation", "528-real-continuation", "527", "242"]
        chapter_starts = {segment: text.index("{#chapter-" + segment + "}") for segment in teaching_order}
        chapter_ends = {segment: chapter_starts[teaching_order[i + 1]]
                        if i + 1 < len(teaching_order) else answers
                        for i, segment in enumerate(teaching_order)}
        for _stem, anchor, *_ in UNITS:
            position = text.index("{#" + anchor + "}")
            parent = CLASSIFIED_UNITS[anchor]["chapter"] if anchor in CLASSIFIED_UNITS else 26
            segment = "529-continuation" if anchor in ("coord-unit", "affgraph-unit") else str(parent)
            if anchor in ("pow-unit", "sum-unit", "polyrec-unit", "polyops-unit", "polymul-unit", "polyprod-unit", "polydiv-unit", "polyroot-unit", "sqrat-unit", "quad-unit"):
                segment = "528-continuation"
            if anchor in ("qgap-unit", "cut-unit", "cutadd-unit", "cutgroup-unit",
                          "cutprod-unit", "cutprod-laws-unit", "cutsigned-unit", "cutring-unit", "cutinv-unit", "cutdiv-unit", "realarch-unit", "realsqrt-unit", "realabs-unit"):
                segment = "526-continuation"
            if anchor == "realquad-unit":
                segment = "528-real-continuation"
            require(int(segment.split("-")[0]) == parent
                    and chapter_starts[segment] < position < chapter_ends[segment],
                    "Unit assigned to the wrong teaching chapter: " + anchor)
        for phrase in ["第26章、第242章仅有部分单元", "第526章未完成", "第529章未完成", "第528章未完成",
                       "97F80", "97F70", "97I20", "97H30", "97H20", "章号保留原分类目录编号",
                       "同一分类章续写，不新增分类章或节",
                       "第529章续写，不新增分类章或节", "第526章续写，不新增分类章或节", "97F50",
                       "学习顺序说成MSC分类顺序", "没有第2章教学正文", "采用佩亚诺规则", "未形式证明递归原则", "二十一张插图", "六十一个基础桥接单元", "有序交换加法群", "非负分割乘积规律", "有序交换环", "完备有序域", "12J15", "有理像稠密", "非负平方根", "实数绝对值", "实数二次方程", "54E35"]:
            require(phrase in text, "Missing scope/figure disclosure: " + phrase)
        require(rational_gap_figure_source().strip() in text,
                "Rational gap appendix does not contain the current complete figure function")
        require(dedekind_grid_figure_source().strip() in text,
                "Dedekind grid appendix does not contain the current complete figure function")
        require(text.count("{#dedekind-addition-sources}") == 1
                and text.count("{#dedekind-grid-figure-code}") == 1,
                "Dedekind addition references or figure appendix missing/duplicated")
        require(text.count("{#dedekind-multiplication-sources}") == 1,
                "Nonnegative cut product reference anchor missing/duplicated")
        require(text.count("{#dedekind-signed-sources}") == 1,
                "Signed cut multiplication reference anchor missing/duplicated")
        require(text.count("{#dedekind-inverse-sources}") == 1,
                "Cut inverse reference anchor missing/duplicated")
        require(text.count("{#real-arch-sqrt-sources}") == 1,
                "Real Archimedean/square-root reference anchor missing/duplicated")
        require(text.count("{#real-distance-quadratic-sources}") == 1,
                "Real distance/quadratic reference anchor missing/duplicated")
        require(text.count("{#real-plane-metric-sources}") == 1
                and text.count("{#real-plane-figure-code}") == 1,
                "Real plane references/code anchor missing or duplicated")
        require(real_plane_figure_source().strip() in text,
                "Real plane appendix omits current complete drawing function")
        require(text.count("{#real-lines-projection-sources}") == 1
                and text.count("{#real-projection-figure-code}") == 1,
                "Real lines/projection references or code anchor missing/duplicated")
        require(real_projection_figure_source().strip() in text,
                "Projection appendix omits current complete function")
        require(text.count("{#real-sequences-sources}") == 1
                and text.count("{#real-sequence-epsilon-figure-code}") == 1,
                "Real sequences references or code anchor missing/duplicated")
        require(real_sequence_epsilon_figure_source().strip() in text,
                "Sequence appendix omits current complete function")
        require("本轮共发出" not in text and "HTTP 404" not in text, "Research request transcript leaked into book")
    book_reports = {stem: audit_book(stem, len(FIGURES), PAIRS) for stem in NEW_STEMS}
    book_reports["综合数学_第一章审阅版"] = audit_book("综合数学_第一章审阅版", 4, PAIRS[:14])
    arithmetic = finite_arithmetic_checks()
    algorithms = finite_natural_algorithm_checks()
    written = written_arithmetic_report_check(manifest)
    integers = integer_pairs_report_check(manifest)
    euclidean = integer_euclidean_report_check(manifest)
    extended = extended_euclidean_report_check(manifest)
    rational = rational_addition_report_check(manifest)
    multiplication = rational_multiplication_report_check(manifest)
    order = rational_order_report_check(manifest)
    ratios = ratios_units_report_check(manifest)
    functions = finite_functions_report_check(manifest)
    inverses = finite_function_inverses_report_check(manifest)
    linear = linear_equation_solvers_report_check(manifest)
    inequalities = rational_inequalities_report_check(manifest)
    affine = rational_affine_report_check(manifest)
    powers_sums = rational_powers_sums_report_check(manifest)
    polynomial = rational_polynomial_basic_report_check(manifest)
    polynomial_product = rational_polynomial_product_report_check(manifest)
    polynomial_division = rational_polynomial_linear_division_report_check(manifest)
    quadratics = rational_quadratics_report_check(manifest)
    # Executing both figure scripts must reproduce the exact shipped images.
    before_figures = hashes([OUT / "figures" / name for name in FIGURES])
    subprocess.run([sys.executable, "tools/draw_ch01_figures.py"], cwd=ROOT, check=True, capture_output=True)
    for name in FIGURES[:4]:
        require(hashlib.sha256((ROOT / "figures" / name).read_bytes()).hexdigest()
                == before_figures["dist/figures/" + name], "Original figure regeneration differs: " + name)
    subprocess.run([sys.executable, "tools/draw_foundations_batch.py"], cwd=ROOT, check=True, capture_output=True)
    require(hashes([OUT / "figures" / name for name in FIGURES]) == before_figures,
            "New figure regeneration differs from shipped image")
    logs = list((ROOT / "build/review_ch01").glob("*.log")) + list(BUILD.glob("*.log"))
    missing = [f"{p.name}: {line}" for p in logs for line in p.read_text().splitlines()
               if "Missing character" in line or "Missing glyph" in line]
    require(not missing, "Missing glyph warnings: " + repr(missing[:8]))
    overfull = [f"{p.name}: {line}" for p in logs for line in p.read_text().splitlines()
                if "Overfull \\hbox" in line or "Overfull \\vbox" in line]
    require(not overfull, "TeX overflow warnings: " + repr(overfull[:8]))
    pdf_reports = {stem: audit_pdf(stem) for stem in PDF_STEMS}
    require(source_hashes() == manifest["source_sha256"] and artifact_hashes() == current,
            "Inputs or outputs changed during validation; rerun build and validation")
    report = {"schema_version": 1, "status": "automated_checks_passed",
              "validated_at": datetime.now(timezone.utc).isoformat(),
              "command": manifest["build_command"] + " && python tools/validate_learning_batch.py",
              "catalog_counts": {"parts": 63, "chapters": 534, "sections": 6006},
              "scope": {"chapter": "00Axx", "units": [anchor for _stem, anchor, *_ in UNITS],
                        "partial_chapter": "11Axx", "chapter_26_complete": False,
                        "partial_chapters": ["11Axx", "97Fxx", "97Ixx", "97Hxx", "97Gxx", "40Axx"],
                        "chapter_526_complete": False, "chapter_529_complete": False, "chapter_528_complete": False,
                        "teaching_chapter_order": [1, 26, 526, 529, 528, 529, 528, 526, 528, 527, 242],
                        "unique_teaching_chapters": [1, 26, 526, 529, 528, 527, 242],
                        "chapter_527_complete": False, "chapter_242_complete": False,
                        "analysis_unit_sections": {anchor: mapping["section"] for anchor, mapping in ANALYSIS_UNITS.items()},
                        "unit_parent_chapters": {anchor: CLASSIFIED_UNITS[anchor]["code"] if anchor in CLASSIFIED_UNITS else "11Axx"
                                                 for _stem, anchor, *_ in UNITS},
                        "education_unit_sections": {anchor: mapping["section"] for anchor, mapping in EDUCATION_UNITS.items()},
                        "chapter_2_teaching_present": False, "formal_natural_number_construction": False},
              "counts": {"ch01_exercises": 14,
                         **{name + "_exercises": 8 for _stem, _anchor, _prefix, name in UNITS},
                         "total_exercises": len(PAIRS), "figures": len(FIGURES)},
              "checks": {"formula_rendering": True, "images": True, "cross_references": True,
                         "exercise_answer_pairs": True, "answers_after_teaching": True,
                         "figure_code_reproducible": True, "page_boundary_overflow": False,
                         "missing_glyphs": False, "screenshot_inspection": False},
              "finite_arithmetic_checks": arithmetic, "finite_natural_algorithm_checks": algorithms,
              "finite_written_arithmetic_checks": written,
              "finite_integer_pairs_checks": integers,
              "finite_integer_euclidean_checks": euclidean,
              "finite_extended_euclidean_checks": extended,
              "finite_rational_addition_checks": rational,
              "finite_rational_multiplication_checks": multiplication,
              "finite_rational_order_checks": order,
              "finite_ratios_units_checks": ratios,
              "finite_functions_checks": functions,
              "finite_function_inverses_checks": inverses,
              "finite_linear_equation_solvers_checks": linear,
              "finite_rational_inequalities_checks": inequalities,
              "finite_rational_affine_checks": affine,
              "finite_rational_powers_sums_checks": powers_sums,
              "finite_rational_polynomial_basic_checks": polynomial,
              "finite_rational_polynomial_product_checks": polynomial_product,
              "finite_rational_polynomial_linear_division_checks": polynomial_division,
              "finite_rational_quadratics_checks": quadratics,
              "legacy_reuse": manifest.get("legacy_reuse"), "books": book_reports,
              "artifacts": pdf_reports, "missing_glyph_warnings": missing,
              "tex_overflow_warnings": overfull,
              "source_sha256": manifest["source_sha256"], "artifact_sha256": current,
              "screenshot_sha256": hashes(SCREEN.glob("*.png")),
              "visual_review": {"status": "pending_actual_image_inspection", "pages": {},
                                "artifact_sha256": current, "reviewed_at": None, "result": None},
              "limits": "Automated checks, finite arithmetic cross-checks and raster generation do not constitute mathematical proof verification or actual visual inspection."}
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "counts": report["counts"],
                      "pdf_pages": {name: record["pages"] for name, record in pdf_reports.items()},
                      "visual_review": "pending_actual_image_inspection", "report": str(REPORT)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
