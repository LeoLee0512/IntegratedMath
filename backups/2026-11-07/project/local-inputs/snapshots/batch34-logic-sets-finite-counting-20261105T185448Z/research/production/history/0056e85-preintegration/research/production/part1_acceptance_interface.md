# 第一部分全范围验收接口 v1

日期：2026-11-05。对应独立工具 `tools/validate_part1_acceptance.py`。该工具验证范围、证据完整性和文件身份，不自动判定数学真理，不替代实际审读或查看页面。

## 调用与结果

```bash
python tools/validate_part1_acceptance.py \
  --plan research/production/part1_scope_plan.json \
  --math-review research/production/part1_math_review.json \
  --pedagogy-review research/production/part1_pedagogy_review.json \
  --build-review research/production/part1_build_review.json \
  --visual-review research/production/part1_visual_review.json \
  --output research/production/part1_acceptance.json
```

以上也是各参数默认值。`--root` 默认为仓库根目录。`--output -` 仅打印，不写回执。accepted退出0；缺文件、过期hash、错范围、待处理问题等输出pending并退出1。只写指定输出文件，不修改源稿或全量台账。输出含 `status`、`full_scope_accepted`、`completion_checks`、`depth_counts`、`section_results`、`chapter_results`、`source_sha256`、`plan_sha256`、`evidence`、`blocking_issues`。`author_review.status`始终pending；`push_succeeded`始终false。本回执是编辑生产验收，不冒充作者审阅或推送回执。

## 路径与共同字段

路径均为仓库内规范相对路径，不允许绝对路径、`..`、符号链接逃逸。SHA-256为64位小写十六进制。`{path,sha256}`记录必须逐字节匹配当前文件。日期采用ISO日期或时间。所有文档均要求 `schema_version: 1`、`target_type: "part"`、`target_id: "00-XX"`、`scope: "complete_part"`。

## 范围计划

```json
{
  "schema_version": 1,
  "target_type": "part", "target_id": "00-XX", "scope": "complete_part",
  "authors": ["正文作者的稳定代理身份"],
  "chapter_codes": ["00Axx", "00Bxx"],
  "source_files": ["manuscript/review_ch01/part_opening.md", "其他正文、答案、附录和必要算法文件"],
  "sections": [{
    "code": "00A06", "parent_code": "00Axx", "depth": "T",
    "body_source": "manuscript/review_ch01/chapter.md",
    "anchor": "sec-00A06",
    "objectives": [{"id": "00A06-1", "text": "候选、代回与唯一性的具体学习目标"}],
    "prerequisites": ["manuscript/review_ch01/chapter.md#sec-00A05"],
    "adopted_rules": ["第3节明示采用的运算规则"],
    "excluded_topics": ["数系公理化构造"],
    "reference_entries": ["manuscript/review_ch01/appendices.md#sources"],
    "exercise_answer_pairs": [{"question": "manuscript/review_ch01/chapter.md#question-01", "answer": "manuscript/review_ch01/answers.md#answer-01"}]
  }]
}
```

sections必须恰好覆盖原分类33节且无重复，parent_code逐项保持。source_files必须包括所有正文、答案、附录、先修/参考入口实际引用的文件；工具核对本地锚点存在，并验证先修节图无环。每节有非空目标、排除范围；G必须有参考入口；T必须有题答；S/G允许没有独立题答，是否充分由教学审阅明确判断。`adopted_rules`可空。正文作者不得作为math/ped独立审阅者。计划不写完成状态；声明范围不等于内容已完成。

## 数学与教学审阅JSON（各一份）

共同字段之外：

```json
{
  "review_kind": "math",
  "status": "accepted", "reviewer": "独立审阅者稳定身份",
  "reviewed_at": "2026-11-05T00:00:00+00:00", "independent_of_authors": true,
  "plan_sha256": "计划文件hash", "source_sha256": {"所有计划source_files": "当前hash"},
  "blocking_issues": [],
  "evidence": [{"path": "research/production/part1_math_review.md", "sha256": "实际报告hash"}],
  "sections": [{"code": "00A06", "depth": "T", "objective_ids": ["00A06-1"], "status": "accepted", "blocking_issues": []}]
}
```

教学报告 `review_kind` 为 `pedagogy`；两种报告reviewer必须不同，且不在authors中。两报告都必须覆盖33节全部目标，source_sha256恰好等于计划全部源文件当前hash；不能只抽读T节或新写第2章。Markdown实质报告应逐项给出推导、范围、先修、来源和题答的审读结论及限制。工具只能校验显式签署，不能从姓名字符串推断独立性的现实真实性。

## 构建记录JSON

共同字段之外：`status: "automated_checks_passed"`、非空 `command`、`built_at`、`plan_sha256`、精确 `source_sha256`、`build_input_sha256`（包括所有source_files及实际构建/校验脚本、样式、分类数据等输入的当前hash）、`blocking_issues: []`、`evidence`（至少一份实际构建/校验记录的path/hash）。

`section_codes`须恰好33节。`artifact_sha256`映射至少包含实际存在的PDF、HTML、Markdown、ZIP各一个；`pdf_page_counts`恰好列出所有PDF及正整数页数，工具用PyMuPDF重新读取核实。ZIP中的路径必须安全，全部计划source_files须按原相对路径（允许统一外层目录）存在，且解包字节hash与当前审读源稿一致。`checks`须显式为true：`scope_33_sections`、`formula_rendering`、`images`、`cross_references`、`exercise_answer_pairs`、`offline_html`、`source_bundle`、`page_boundaries`。将自动检查之外的实际视觉判断留给下一份报告。

## 实际视觉记录JSON

共同字段之外：`status: "accepted"`、`reviewer`、`reviewed_at`、`plan_sha256`、精确 `source_sha256`、与构建相同的 `artifact_sha256`、`build_review_sha256`（上一JSON文件hash）、`blocking_issues: []`、`evidence`（实际查看记录的path/hash）。

`pages`为数组：每项 `{"pdf":"dist/某文件.pdf", "pages":[1,2], "path":"build/某联系表.png", "sha256":"图片hash", "inspected":true}`。单页或联系表均可；全部PDF每页至少被一个实际查看的记录覆盖，工具核页码范围和图像可读性。不得只生成图片就填写inspected。可另附放大检查记录，不强制固定抽样数量。`checks`须显式为true：`formulas`、`chinese`、`figures`、`toc`、`pagination`。

## 接入全量台账时的边界

1. 只有当前工具重验accepted，且回执plan/source/artifact/evidence仍匹配，才能提升33节及2章的“按声明深度完成”。
2. T/S/G数量分别报告。G完成只意味着导读目标兑现；章或部分完成不表示穷尽MSC领域。
3. 缺一节、缺一种独立审阅、文件修改或缺实际视觉证据即pending，不能沿用历史accepted。
4. 作者审阅与GitHub推送是独立状态。本工具不联网、不提交、不推送，也不为这些动作产生成功证据。

`tools/part1_ledger.py`是全量生成器的最小接入辅助模块：读取明确计划注册00-XX两个章与33节，并在每次生成时重新调用Validator。不会把已有回执的accepted当作当前验收结果。计划不完整/文件尚未齐全时保留pending；其他部分记录不受该helper修改。该辅助模块自身不写文件。
