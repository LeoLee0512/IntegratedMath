"""Explicit Part 1 plan registration and fresh full-scope acceptance import.

This helper never writes a ledger or receipt. Only the two chapters and 33
sections belonging to 00-XX are mutable; all other production records stay put.
"""
import json
from pathlib import PurePosixPath
from types import SimpleNamespace

from validate_part1_acceptance import COMMON, Validator, digest, require


PLAN = "research/production/part1_scope_plan.json"


def local_existing(root, name):
    if not isinstance(name, str):
        return False
    p = PurePosixPath(name)
    if p.is_absolute() or ".." in p.parts or str(p) != name:
        return False
    resolved = (root / name).resolve()
    return resolved.is_relative_to(root.resolve()) and resolved.is_file() and resolved.stat().st_size > 0


def file_refs(section):
    result = {section["body_source"]}
    for pair in section.get("exercise_answer_pairs", []):
        result.update(pair[k].split("#", 1)[0] for k in ["question", "answer"])
    for ref in section.get("reference_entries", []):
        result.add(ref.split("#", 1)[0])
    return result


def register_record(root, target, specifications, planned_files):
    files = sorted(set(target["source_files"]) | planned_files)
    target["planned_source_files"] = files
    target["source_files"] = [p for p in files if local_existing(root, p)]
    target["source_snapshot"] = [{"path": p, "sha256": digest(root / p)} for p in target["source_files"]]
    bodies = sorted({s["body_source"] for s in specifications
                     if local_existing(root, s["body_source"])
                     and "{#" + s["anchor"] + "}" in (root / s["body_source"]).read_text()})
    target["body_source_files"] = bodies
    target["stage"] = "draft" if bodies else "unwritten"
    target["stages"]["unwritten"]["status"] = "false" if bodies else "true"
    target["stages"]["draft"] = {"status": "declared_scope_draft" if bodies else "not_started",
                                   "evidence": [{"path": p, "sha256": digest(root / p)} for p in bodies]}
    target["coverage"].update(scope="declared_objectives" if bodies else "none", completed=False,
                              unwritten_topics="按范围计划逐项目标验收；尚未通过完整第一部分验收。排除主题不属于本次完成声明。",
                              excluded_topics={s["code"]: s["excluded_topics"] for s in specifications})
    target["learning_objectives"] = {"status": "defined", "items": [
        {"section_code": s["code"], **o} for s in specifications for o in s["objectives"]]}
    target["depth_plan"] = {"status": "defined", "per_objective_depth": [
        {"section_code": s["code"], "objective_id": o["id"], "depth": s["depth"]}
        for s in specifications for o in s["objectives"]],
        "policy": "按声明深度和目标完成；G完成不等于完整数学教学，不宣称穷尽MSC领域。"}
    target["learning_entry"].update(status="explicit_entry",
        prerequisite_definition_anchors=sorted({r for s in specifications for r in s["prerequisites"]}),
        adopted_assumptions=sorted({r for s in specifications for r in s["adopted_rules"]}))
    pairs = [pair for s in specifications for pair in s["exercise_answer_pairs"]]
    target["exercise_answer_separation"].update(
        status="registered_pending_verification" if pairs else "not_required_for_declared_scope",
        exercise_files=sorted({p["question"].split("#")[0] for p in pairs}),
        answer_files=sorted({p["answer"].split("#")[0] for p in pairs}),
        paired_ids_verified=False, pairs=pairs)
    target["author_review"] = {"status": "pending"}


def refresh_part1(root, chapters, sections):
    """Register an explicit complete plan even while referenced drafts are absent.

    Promotion uses a fresh Validator evaluation, never a pre-existing acceptance
    JSON. A missing, malformed, incomplete or stale input leaves completion false.
    """
    if not (root / PLAN).is_file():
        return {"status": "pending", "blocking_issues": [{"stage": "plan", "reason": "Part 1 plan missing"}]}
    try:
        plan = json.loads((root / PLAN).read_text())
        require(all(plan.get(k) == v for k, v in COMMON.items()), "Invalid Part 1 plan header")
        targets = {r["code"]: r for r in sections if r["part_code"] == "00-XX"}
        specs = plan["sections"]
        require(isinstance(specs, list) and len(specs) == 33, "Exactly 33 planned sections required")
        require({s["code"] for s in specs} == set(targets), "Plan scope differs from original classification")
        registered = set(plan["source_files"])
        for spec in specs:
            require(spec["parent_code"] == targets[spec["code"]]["parent_code"], "Plan attribution mismatch")
            require(spec["depth"] in {"T", "S", "G"} and spec["objectives"], "Depth/objectives missing")
            require(file_refs(spec) <= registered, "Section sources missing from plan source registry")
            # Check all expected keys before mutating any production record.
            for key in ["anchor", "excluded_topics", "prerequisites", "adopted_rules", "exercise_answer_pairs"]:
                require(key in spec, "Missing planned section field: " + key)
        for spec in specs:
            register_record(root, targets[spec["code"]], [spec], file_refs(spec))
        for chapter in chapters:
            if chapter["part_code"] != "00-XX":
                continue
            owned = [s for s in specs if s["parent_code"] == chapter["code"]]
            register_record(root, chapter, owned, set().union(*(file_refs(s) for s in owned)))
    except Exception as exc:
        return {"status": "pending", "blocking_issues": [{"stage": "plan_registration", "reason": str(exc)}]}
    args = SimpleNamespace(plan=PLAN,
        math_review="research/production/part1_math_review.json",
        pedagogy_review="research/production/part1_pedagogy_review.json",
        build_review="research/production/part1_build_review.json",
        visual_review="research/production/part1_visual_review.json")
    result = Validator(root).validate(args)
    accepted = result["status"] == "accepted"
    for target in chapters + sections:
        if target["part_code"] != "00-XX":
            continue
        target["full_scope_acceptance"] = {
            "status": result["status"], "plan_sha256": result["plan_sha256"],
            "evidence": result["evidence"], "blocking_issues": result["blocking_issues"],
            "freshly_revalidated": True}
        if accepted:
            target["stage"] = "build-verified"
            target["coverage"].update(completed=True, scope="completed_at_declared_depth",
                unwritten_topics="声明目标已完成；明确排除的方向仍未覆盖，不宣称穷尽MSC领域。")
            for stage, category in [("math-reviewed", "math"), ("pedagogy-reviewed", "pedagogy"),
                                    ("build-verified", "build")]:
                record = {"scope": "complete_part", "target_id": "00-XX",
                          "plan_sha256": result["plan_sha256"], "evidence": result["evidence"]}
                target["stages"][stage] = {"status": "passed", "evidence": [record]}
                target["review_evidence"][category].append(record)
            target["exercise_answer_separation"]["paired_ids_verified"] = True
            target["exercise_answer_separation"]["status"] = "verified_for_declared_scope"
    return result


def finish_part1_record(document, result):
    """Attach only the just-revalidated result to the existing parts document."""
    part = next(r for r in document["entries"] if r["code"] == "00-XX")
    accepted = result.get("status") == "accepted"
    part["full_scope_acceptance"] = {
        "status": "accepted" if accepted else "pending",
        "evidence": result.get("evidence", []), "plan_sha256": result.get("plan_sha256"),
        "blocking_issues": result.get("blocking_issues", []),
        "freshly_revalidated": True, "unit_reviews_do_not_promote_part": True}
    part["depth_counts"] = result.get("depth_counts", {})
    part["author_review"] = {"status": "pending"}
    part["completion_checks"].update({k: v for k, v in result.get("completion_checks", {}).items()
                                      if k in part["completion_checks"]})
    part["coverage"].update(completed=accepted,
        note="仅按33节逐项声明的T/S/G深度完成；G不是完整教学。" if accepted
             else "完整第一部分证据尚未齐全；草稿、单元审阅和历史产物不授予完成。")
    if accepted:
        part["stage"] = "completed_at_declared_depth"
        if part["push"]["status"] != "verified":
            part["push"].update(status="due", reason="完整第一部分当前范围验收通过；尚未执行或核验推送")
    document["checks"]["completed_parts"] = sum(bool(p["coverage"]["completed"]) for p in document["entries"])
    return document
