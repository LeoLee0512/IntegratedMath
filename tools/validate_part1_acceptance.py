"""Validate hash-bound, full-scope Part 1 attestations; never perform a push.

See research/production/part1_acceptance_interface.md. Accepted means completion
at declared T/S/G depth, not exhaustive mathematical coverage or author approval.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys
from urllib.parse import urlsplit
import zipfile


COMMON = {"schema_version": 1, "target_type": "part", "target_id": "00-XX",
          "scope": "complete_part"}
BUILD_CHECKS = {"scope_33_sections", "formula_rendering", "images",
                "cross_references", "exercise_answer_pairs", "offline_html",
                "source_bundle", "page_boundaries"}
VISUAL_CHECKS = {"formulas", "chinese", "figures", "toc", "pagination"}
DEFAULT_SOURCE_REVIEW = "research/production/part1_topic_sources.json"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def strings(value, label, allow_empty=False):
    require(isinstance(value, list) and (allow_empty or bool(value)), label + " must be a list")
    require(all(nonempty(x) for x in value), label + " requires nonempty strings")
    require(len(value) == len(set(value)), label + " contains duplicates")
    return value


def iso_date(value, label):
    require(nonempty(value), label + " is missing")
    datetime.fromisoformat(value.replace("Z", "+00:00"))


class Validator:
    def __init__(self, root):
        self.root = root.resolve()
        self.errors = []
        self.evidence = []
        self.plan = None
        self.plan_hash = None
        self.sources = {}
        self.expected = {}
        self.section_plans = {}
        self.reviews = {}
        self.build = None
        self.build_hash = None
        self.topic_source_results = {}
        self.source_review_path = None
        self.source_review_hash = None

    def path(self, name):
        require(nonempty(name), "Missing file path")
        p = PurePosixPath(name)
        require(not p.is_absolute() and ".." not in p.parts and str(p) == name,
                "Noncanonical repository path: " + name)
        result = (self.root / name).resolve()
        require(result.is_relative_to(self.root) and result.is_file(),
                "Missing or out-of-repository file: " + name)
        return result

    def load(self, name):
        path = self.path(name)
        doc = json.loads(path.read_text())
        require(isinstance(doc, dict), name + " must contain an object")
        for key, value in COMMON.items():
            require(doc.get(key) == value, name + ": wrong " + key)
        self.evidence.append({"path": name, "sha256": digest(path)})
        return doc

    def hash_map(self, values, label):
        require(isinstance(values, dict) and bool(values), label + " is empty")
        for name, expected in values.items():
            require(isinstance(expected, str) and re.fullmatch(r"[0-9a-f]{64}", expected),
                    label + ": invalid SHA-256")
            require(digest(self.path(name)) == expected, label + ": stale file " + name)
        return values

    def reports(self, records):
        require(isinstance(records, list) and records, "Missing substantive evidence reports")
        seen = set()
        for record in records:
            require(isinstance(record, dict), "Invalid evidence record")
            name = record.get("path")
            require(name not in seen, "Duplicate evidence report")
            seen.add(name)
            self.hash_map({name: record.get("sha256")}, "evidence")
            require(self.path(name).stat().st_size > 0, "Empty evidence report")
            self.evidence.append(record)

    def source_binding(self, doc):
        require(self.plan is not None, "Valid scope plan required first")
        require(doc.get("plan_sha256") == self.plan_hash, "Scope plan hash mismatch")
        require(doc.get("source_sha256") == self.sources, "Exact source snapshot mismatch")
        self.hash_map(doc["source_sha256"], "source snapshot")

    def anchor(self, ref):
        require(nonempty(ref) and ref.count("#") == 1, "Expected file#anchor reference")
        name, anchor = ref.split("#")
        require(name in self.sources and bool(anchor), "Unregistered anchor source: " + ref)
        require("{#" + anchor + "}" in self.path(name).read_text(), "Missing anchor: " + ref)
        return ref

    def codes(self, values, label):
        strings(values, label)
        require(set(values) == set(self.expected), label + " must cover exactly all 33 sections")

    def scope_plan(self, name):
        taxonomy_path = "data/msc_taxonomy.json"
        tax = json.loads(self.path(taxonomy_path).read_text())["entries"]
        chapters = {x["code"] for x in tax if x.get("parent_code") == "00-XX"
                    and x.get("level") == "intermediate"}
        self.expected = {x["code"]: x["parent_code"] for x in tax
                         if x.get("level") in {"subject_leaf", "general_leaf"}
                         and x.get("parent_code") in chapters | {"00-XX"}}
        require(chapters == {"00Axx", "00Bxx"} and len(self.expected) == 33,
                "Original taxonomy is not the expected Part 1 scope")
        self.evidence.append({"path": taxonomy_path, "sha256": digest(self.path(taxonomy_path))})
        doc = self.load(name)
        self.plan_hash = digest(self.path(name))
        authors = strings(doc.get("authors"), "authors")
        require(len(authors) > 0, "Authors required for independence check")
        strings(doc.get("chapter_codes"), "chapter_codes")
        require(set(doc["chapter_codes"]) == chapters, "Chapter scope mismatch")
        files = strings(doc.get("source_files"), "source_files")
        self.sources = {p: digest(self.path(p)) for p in files}
        sections = doc.get("sections")
        require(isinstance(sections, list) and all(isinstance(s, dict) for s in sections),
                "sections must be objects")
        self.codes([s.get("code") for s in sections], "plan sections")
        all_ids = set()
        anchor_to_code = {}
        for section in sections:
            code = section["code"]
            require(section.get("parent_code") == self.expected[code], code + ": wrong parent")
            require(section.get("depth") in {"T", "S", "G"}, code + ": undeclared depth")
            ref = self.anchor(section.get("body_source", "") + "#" + section.get("anchor", ""))
            require(ref not in anchor_to_code, "Duplicate section body anchor")
            anchor_to_code[ref] = code
            objectives = section.get("objectives")
            require(isinstance(objectives, list) and objectives, code + ": missing objectives")
            for objective in objectives:
                require(isinstance(objective, dict) and nonempty(objective.get("id"))
                        and nonempty(objective.get("text")), code + ": invalid objective")
                require(objective["id"] not in all_ids, "Repeated objective ID")
                all_ids.add(objective["id"])
            strings(section.get("excluded_topics"), code + " excluded_topics")
            strings(section.get("adopted_rules"), code + " adopted_rules", True)
            for ref in strings(section.get("prerequisites"), code + " prerequisites", True):
                self.anchor(ref)
            for ref in strings(section.get("reference_entries"), code + " references",
                               section["depth"] != "G"):
                self.anchor(ref)
            pairs = section.get("exercise_answer_pairs")
            require(isinstance(pairs, list), code + ": missing exercise/answer registry")
            require(section["depth"] != "T" or bool(pairs), code + ": T requires exercises")
            for pair in pairs:
                require(isinstance(pair, dict), code + ": invalid exercise pair")
                self.anchor(pair.get("question"))
                self.anchor(pair.get("answer"))
                require(pair["question"] != pair["answer"], "Question cannot be its own answer")
            self.section_plans[code] = section
        graph = {s["code"]: [anchor_to_code[r] for r in s["prerequisites"] if r in anchor_to_code]
                 for s in sections}
        active, done = set(), set()
        def visit(code):
            require(code not in active, "Circular section prerequisites: " + code)
            if code in done:
                return
            active.add(code)
            for dependency in graph[code]:
                visit(dependency)
            active.remove(code)
            done.add(code)
        for code in graph:
            visit(code)
        self.plan = doc

    def review(self, name, kind):
        doc = self.load(name)
        self.source_binding(doc)
        require(doc.get("review_kind") == kind, "Wrong review kind")
        require(doc.get("status") == "accepted" and doc.get("blocking_issues") == [],
                kind + " review is not explicitly accepted without blockers")
        require(nonempty(doc.get("reviewer")), "Named reviewer required")
        iso_date(doc.get("reviewed_at"), "reviewed_at")
        require(doc.get("independent_of_authors") is True
                and doc["reviewer"] not in self.plan["authors"], "Independent reviewer required")
        require(all(r["reviewer"] != doc["reviewer"] for r in self.reviews.values()),
                "Math and pedagogy reviewers must be distinct")
        records = doc.get("sections")
        require(isinstance(records, list) and all(isinstance(s, dict) for s in records),
                "Review section records required")
        self.codes([s.get("code") for s in records], kind + " coverage")
        for section in records:
            plan = self.section_plans[section["code"]]
            require(section.get("depth") == plan["depth"], "Review depth mismatch")
            ids = strings(section.get("objective_ids"), "review objective IDs")
            require(set(ids) == {o["id"] for o in plan["objectives"]}, "Incomplete objective review")
            require(section.get("status") == "accepted" and section.get("blocking_issues") == [],
                    "Section review contains unresolved issues: " + section["code"])
        self.reports(doc.get("evidence"))
        self.reviews[kind] = doc

    def verified_topic_source(self, source, code, requirement):
        """Check an explicit content attestation, never infer it from HTTP status.

        Relevance is still a human judgment: the verifier checks a named,
        located, hash-bound claim, not the semantic truth of that claim.
        """
        for field in ["title", "author_or_publisher", "version", "public_url"]:
            require(nonempty(source.get(field)), "Source bibliography missing " + field)
        url = urlsplit(source["public_url"])
        require(url.scheme in {"http", "https"} and bool(url.netloc), "Public source URL missing")
        access = source.get("access")
        require(isinstance(access, dict), "Source access record missing")
        require(access.get("status") in {"retrieved", "available_local"},
                "Source content has not been obtained")
        require(access.get("method") in {"public_https", "local_cache", "user_provided"},
                "Source access method is not declared")
        iso_date(access.get("retrieved_at"), "source retrieved_at")
        content_hash = access.get("document_sha256")
        require(isinstance(content_hash, str) and re.fullmatch(r"[0-9a-f]{64}", content_hash),
                "Obtained content SHA-256 required")
        self.reports(access.get("evidence"))
        review = source.get("content_review")
        require(isinstance(review, dict) and review.get("status") == "verified",
                "Actual source content review missing; URL availability is insufficient")
        require(nonempty(review.get("reviewer")), "Named source content reviewer required")
        iso_date(review.get("reviewed_at"), "source reviewed_at")
        require(review.get("document_sha256") == content_hash,
                "Source content review addresses a different retrieved document")
        self.reports(review.get("evidence"))
        access_paths = {e["path"] for e in access["evidence"]}
        require(all(e["path"] not in access_paths for e in review["evidence"]),
                "Access metadata cannot serve as its own content review")
        coverage = review.get("coverage")
        require(isinstance(coverage, list) and all(isinstance(x, dict) for x in coverage),
                "Source content coverage missing")
        matches = [x for x in coverage if x.get("section_code") == code
                   and x.get("requirement_id") == requirement["id"]]
        require(bool(matches), "Source does not address this section's topic requirement")
        errors = []
        for match in matches:
            try:
                require(match.get("relevance") == requirement["relevance"],
                        "General method source cannot replace topic-specific evidence")
                objectives = strings(match.get("objective_ids"), "source coverage objectives")
                require(set(objectives) == set(requirement["objective_ids"]),
                        "Source content coverage does not match required objectives")
                for field in ["source_location", "verified_claim", "limitations"]:
                    require(nonempty(match.get(field)), "Source content review missing " + field)
                return
            except (ValueError, TypeError) as exc:
                errors.append(str(exc))
        raise ValueError("; ".join(errors))

    def topic_source_section(self, planned, reviewed, sources):
        code = planned["code"]
        requirements = planned.get("source_requirements")
        require(isinstance(requirements, list)
                and all(isinstance(r, dict) for r in requirements),
                "Explicit source_requirements missing")
        external_claims = planned.get("external_source_claims", [])
        require(isinstance(external_claims, list) and all(isinstance(c, dict) for c in external_claims),
                "external_source_claims must be a list of declared external facts")
        if not requirements:
            require(planned["depth"] in {"T", "S"}, "G requires nonempty topic-specific source requirements")
            require(not external_claims, "External source claims cannot use the original-work exemption")
            original_status = "original_work_reviewed_separately"
            require(planned.get("topic_source_status") == original_status
                    and reviewed.get("topic_source_status") == original_status,
                    "Original T/S work must explicitly use the separate math/pedagogy review status")
            require(reviewed.get("requirements") == [], "Original-work record must have no source requirements")
            return {"status": original_status, "source_ids": [], "blocking_issues": [],
                    "review_basis": "independent_math_and_pedagogy_gates",
                    "external_sources_verified": False}
        ids = strings([r.get("id") for r in requirements], "source requirement IDs")
        objective_ids = {o["id"] for o in planned["objectives"]}
        covered_objectives = set()
        for requirement in requirements:
            require(nonempty(requirement.get("topic")), "Source requirement topic missing")
            refs = strings(requirement.get("objective_ids"), "required source objectives")
            require(set(refs) <= objective_ids, "Source requirement points outside this section")
            covered_objectives.update(refs)
            require(requirement.get("relevance") in {"topic_specific", "general_method"},
                    "Source relevance requirement missing")
            require(planned["depth"] != "G" or requirement["relevance"] == "topic_specific",
                    "G requires topic-specific sources; general logic cannot substitute")
        if planned["depth"] == "G":
            require(covered_objectives == objective_ids, "G source requirements omit declared objectives")
        # Original derivations need not occur in an external textbook. Only
        # actual external dependencies of T/S work need source requirements.
        requirement_index = {r["id"]: r for r in requirements}
        for claim in external_claims:
            require(nonempty(claim.get("claim")), "Declared external fact is missing its statement")
            require(claim.get("requirement_id") in requirement_index,
                    "Declared external fact lacks a matching source requirement")
            claim_objectives = strings(claim.get("objective_ids"), "external fact objectives")
            require(set(claim_objectives) <= set(requirement_index[claim["requirement_id"]]["objective_ids"]),
                    "External fact objectives are not covered by its source requirement")
        require(planned.get("topic_source_status") == "verified",
                "Scope plan topic_source_status is not verified")
        require(reviewed.get("topic_source_status") == "verified",
                "Reviewed topic_source_status is not verified")
        records = reviewed.get("requirements")
        require(isinstance(records, list) and all(isinstance(r, dict) for r in records),
                "Per-requirement source review missing")
        actual_ids = strings([r.get("requirement_id") for r in records], "reviewed source requirement IDs")
        require(set(actual_ids) == set(ids), "Reviewed source requirements do not match scope")
        index = {r["requirement_id"]: r for r in records}
        verified_ids = []
        for requirement in requirements:
            record = index[requirement["id"]]
            require(record.get("status") == "verified", "Source requirement is still pending")
            candidates = strings(record.get("source_ids"), "supporting source IDs")
            failures = []
            for identifier in candidates:
                try:
                    require(identifier in sources, "Unknown source ID: " + identifier)
                    self.verified_topic_source(sources[identifier], code, requirement)
                    verified_ids.append(identifier)
                    break
                except Exception as exc:
                    failures.append(identifier + ": " + str(exc))
            else:
                raise ValueError(requirement["id"] + ": " + "; ".join(failures))
        return {"status": "verified", "source_ids": sorted(set(verified_ids)), "blocking_issues": []}

    def source_review(self, name):
        self.source_review_path = name
        doc = self.load(name)
        self.source_review_hash = digest(self.path(name))
        self.source_binding(doc)
        source_list = doc.get("sources")
        require(isinstance(source_list, list) and all(isinstance(s, dict) for s in source_list),
                "Topic source registry missing")
        strings([s.get("id") for s in source_list], "topic source IDs", True)
        sources = {s["id"]: s for s in source_list}
        sections = doc.get("sections")
        require(isinstance(sections, list) and all(isinstance(s, dict) for s in sections),
                "Topic source section records missing")
        self.codes([s.get("code") for s in sections], "topic source coverage")
        records = {s["code"]: s for s in sections}
        for code, planned in self.section_plans.items():
            try:
                self.topic_source_results[code] = self.topic_source_section(planned, records[code], sources)
            except Exception as exc:
                self.topic_source_results[code] = {"status": "pending", "source_ids": [],
                                                   "blocking_issues": [str(exc)]}
        satisfied = {"verified", "original_work_reviewed_separately"}
        pending = [c for c, r in self.topic_source_results.items() if r["status"] not in satisfied]
        require(not pending, "Unverified topic sources in sections: " + ", ".join(pending))
        require(doc.get("status") in {"verified", "requirements_satisfied"},
                "Whole-part source requirements are not satisfied")

    def build_review(self, name):
        doc = self.load(name)
        self.source_binding(doc)
        require(doc.get("status") == "automated_checks_passed" and doc.get("blocking_issues") == [],
                "Build has not passed all automated checks")
        require(nonempty(doc.get("command")), "Actual build command required")
        iso_date(doc.get("built_at"), "built_at")
        self.codes(doc.get("section_codes"), "build scope")
        inputs = self.hash_map(doc.get("build_input_sha256"), "build inputs")
        require(all(inputs.get(p) == h for p, h in self.sources.items()), "Build omits source inputs")
        require(any(p.endswith(".py") for p in inputs), "Build tooling inputs are missing")
        artifacts = self.hash_map(doc.get("artifact_sha256"), "artifacts")
        for extension in [".pdf", ".html", ".md", ".zip"]:
            require(any(p.endswith(extension) for p in artifacts), "Missing " + extension + " deliverable")
        checks = doc.get("checks", {})
        require(isinstance(checks, dict) and all(checks.get(c) is True for c in BUILD_CHECKS),
                "Missing explicit automated build checks")
        pdfs = {p for p in artifacts if p.endswith(".pdf")}
        counts = doc.get("pdf_page_counts")
        require(isinstance(counts, dict) and set(counts) == pdfs, "PDF page counts mismatch")
        import fitz
        for name, count in counts.items():
            require(type(count) is int and count > 0, "Invalid PDF page count")
            with fitz.open(self.path(name)) as pdf:
                require(len(pdf) == count, "Actual PDF page count mismatch")
        bundled_sources = set()
        for name in artifacts:
            if name.endswith(".zip"):
                with zipfile.ZipFile(self.path(name)) as archive:
                    require(archive.testzip() is None and bool(archive.namelist()), "Invalid source archive")
                    for member in archive.infolist():
                        internal = PurePosixPath(member.filename)
                        require(not internal.is_absolute() and ".." not in internal.parts,
                                "Unsafe archive member: " + member.filename)
                        if member.is_dir():
                            continue
                        for source, source_hash in self.sources.items():
                            if member.filename == source or member.filename.endswith("/" + source):
                                require(hashlib.sha256(archive.read(member)).hexdigest() == source_hash,
                                        "Bundled source differs from reviewed source: " + source)
                                bundled_sources.add(source)
        require(bundled_sources == set(self.sources), "Source bundle omits registered source files")
        self.reports(doc.get("evidence"))
        self.build = doc

    def visual_review(self, name):
        require(self.build is not None, "Valid build record required before visual acceptance")
        doc = self.load(name)
        self.source_binding(doc)
        require(doc.get("status") == "accepted" and doc.get("blocking_issues") == [],
                "Actual visual inspection not accepted")
        require(nonempty(doc.get("reviewer")), "Visual reviewer missing")
        iso_date(doc.get("reviewed_at"), "reviewed_at")
        require(doc.get("artifact_sha256") == self.build["artifact_sha256"], "Visual artifact hash mismatch")
        self.hash_map(doc["artifact_sha256"], "visual artifacts")
        require(doc.get("build_review_sha256") == self.build_hash, "Visual build-record hash mismatch")
        checks = doc.get("checks", {})
        require(isinstance(checks, dict) and all(checks.get(c) is True for c in VISUAL_CHECKS),
                "Missing explicit visual inspection checks")
        pages = doc.get("pages")
        require(isinstance(pages, list) and pages, "No actual screenshot inspection records")
        covered = {p: set() for p in self.build["pdf_page_counts"]}
        from PIL import Image
        for record in pages:
            require(isinstance(record, dict) and record.get("inspected") is True,
                    "Screenshot must be explicitly recorded as inspected")
            pdf = record.get("pdf")
            require(pdf in covered, "Screenshot references unknown PDF")
            numbers = record.get("pages")
            require(isinstance(numbers, list) and numbers
                    and all(type(n) is int and 1 <= n <= self.build["pdf_page_counts"][pdf] for n in numbers)
                    and len(set(numbers)) == len(numbers), "Invalid screenshot PDF page numbers")
            self.hash_map({record.get("path"): record.get("sha256")}, "screenshot")
            with Image.open(self.path(record["path"])) as shot:
                shot.verify()
            covered[pdf].update(numbers)
            self.evidence.append({"path": record["path"], "sha256": record["sha256"]})
        for pdf, actual in covered.items():
            require(actual == set(range(1, self.build["pdf_page_counts"][pdf] + 1)),
                    "Uninspected PDF pages: " + pdf)
        self.reports(doc.get("evidence"))

    def step(self, label, function, *args):
        try:
            function(*args)
            return True
        except Exception as exc:
            # Malformed evidence or unavailable parsers can never promote a
            # target. Report the failed stage instead of leaving a stale pass.
            self.errors.append({"stage": label, "reason": str(exc)})
            return False

    def validate(self, args):
        checks = {}
        checks["scope_plan_valid"] = self.step("scope_plan", self.scope_plan, args.plan)
        checks["full_scope_math_accepted"] = self.step("math", self.review, args.math_review, "math")
        checks["full_scope_pedagogy_accepted"] = self.step("pedagogy", self.review, args.pedagogy_review, "pedagogy")
        checks["full_scope_sources_accepted"] = self.step(
            "sources", self.source_review, getattr(args, "source_review", DEFAULT_SOURCE_REVIEW))
        built = self.step("build", self.build_review, args.build_review)
        if built:
            self.build_hash = digest(self.path(args.build_review))
        visual = self.step("visual", self.visual_review, args.visual_review)
        checks["full_scope_build_accepted"] = built
        checks["full_scope_visual_accepted"] = visual
        checks["full_scope_build_and_visual_accepted"] = built and visual
        accepted = all(checks.values())
        checks["all_chapters_completed"] = accepted
        checks["all_direct_sections_completed"] = accepted
        section_results = [{"code": c, "parent_code": p,
                            "depth": self.section_plans.get(c, {}).get("depth"),
                            "topic_source_status": self.topic_source_results.get(c, {}).get("status", "pending"),
                            "status": "completed_at_declared_depth" if accepted else "pending"}
                           for c, p in self.expected.items()]
        return {**COMMON, "status": "accepted" if accepted else "pending",
                "validated_at": datetime.now(timezone.utc).isoformat(),
                "full_scope_accepted": accepted, "completion_checks": checks,
                "depth_counts": dict(Counter(s["depth"] for s in self.section_plans.values())),
                "section_results": section_results,
                "chapter_results": [{"code": c, "completed": accepted,
                                     "completion_basis": "declared_depth_and_objectives"}
                                    for c in ["00Axx", "00Bxx"]],
                "plan_sha256": self.plan_hash, "source_sha256": self.sources,
                "artifact_sha256": self.build["artifact_sha256"] if self.build else {},
                "source_review": {"status": "requirements_satisfied" if checks["full_scope_sources_accepted"] else "pending",
                                  "path": self.source_review_path, "sha256": self.source_review_hash,
                                  "sections": self.topic_source_results,
                                  "boundary": "取得或HTTP成功不等于内容核验；专题相关性仍由实际阅读者负责。"},
                "evidence": self.evidence, "blocking_issues": self.errors,
                "author_review": {"status": "pending", "independent_of_production_acceptance": True},
                "push_succeeded": False,
                "completion_note": "按逐项目标及T/S/G声明深度验收；专题来源缺证阻断全范围通过，其他审阅阶段分别记账。G完成不是完整数学教学，且不宣称穷尽MSC领域。"}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    for option, filename in [("plan", "part1_scope_plan"), ("math-review", "part1_math_review"),
                             ("pedagogy-review", "part1_pedagogy_review"),
                             ("build-review", "part1_build_review"), ("visual-review", "part1_visual_review")]:
        parser.add_argument("--" + option, default="research/production/" + filename + ".json")
    parser.add_argument("--source-review", default=DEFAULT_SOURCE_REVIEW)
    parser.add_argument("--output", default="research/production/part1_acceptance.json")
    args = parser.parse_args(argv)
    validator = Validator(args.root)
    result = validator.validate(args)
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output == "-":
        sys.stdout.write(text)
    else:
        output = (args.root / args.output).resolve()
        require(not Path(args.output).is_absolute() and output.is_relative_to(args.root.resolve()),
                "Output must be inside repository")
        input_paths = {validator.root / getattr(args, field) for field in
                       ["plan", "math_review", "pedagogy_review", "source_review", "build_review", "visual_review"]}
        protected = {p.resolve() for p in input_paths} | {validator.root / p for p in validator.sources}
        protected |= {validator.root / e["path"] for e in validator.evidence}
        if validator.build:
            protected |= {validator.root / p for p in validator.build["artifact_sha256"]}
            protected |= {validator.root / p for p in validator.build["build_input_sha256"]}
        protected.add(Path(__file__).resolve())
        require(output not in protected, "Refusing to overwrite an input or evidence file")
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(text)
        print(json.dumps({"status": result["status"], "output": str(output),
                          "blocking_issue_count": len(result["blocking_issues"])}, ensure_ascii=False))
    return 0 if result["status"] == "accepted" else 1


if __name__ == "__main__":
    raise SystemExit(main())
