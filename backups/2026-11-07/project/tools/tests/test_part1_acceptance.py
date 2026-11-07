"""Offline regression tests for source gates, not textbook acceptance evidence.

Every full-scope fixture is explicitly synthetic and lives in a TemporaryDirectory.
The two Crossref tests read stored evidence only and never promote a whole section.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import sys
from tempfile import TemporaryDirectory
from types import SimpleNamespace
import unittest
import zipfile

import fitz
from PIL import Image


REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "tools"))
from validate_part1_acceptance import (  # noqa: E402
    BUILD_CHECKS,
    COMMON,
    VISUAL_CHECKS,
    Validator,
)


class EvidenceFixture:
    """Construct complete synthetic evidence without running historical scripts."""

    DATE = "2026-11-05"
    DOCUMENT_HASH = "a" * 64
    BOUND_RECORDS = (
        "math.json", "pedagogy.json", "build.json", "visual.json", "sources.json",
    )

    def __init__(self, root: Path):
        self.root = root
        self.args = SimpleNamespace(
            plan="plan.json", math_review="math.json", pedagogy_review="pedagogy.json",
            build_review="build.json", visual_review="visual.json", source_review="sources.json",
        )
        taxonomy = json.loads((REPO_ROOT / "data/msc_taxonomy.json").read_text())
        self.write("data/msc_taxonomy.json", taxonomy)
        entries = [entry for entry in taxonomy["entries"]
                   if entry["level"] in {"general_leaf", "subject_leaf"}
                   and entry["parent_code"] in {"00-XX", "00Axx", "00Bxx"}]
        self.write("body.md", "\n".join(
            "## Synthetic section {#sec-" + entry["code"] + "}" for entry in entries
        ) + "\n## References {#refs}\n## Question {#question}\n## Answer {#answer}\n")
        self.write("build.py", "# Synthetic test tooling; not a real build.\n")
        sections = [{
            "code": entry["code"], "parent_code": entry["parent_code"], "depth": "G",
            "body_source": "body.md", "anchor": "sec-" + entry["code"],
            "objectives": [{"id": entry["code"] + "-1", "text": "Synthetic fixture target"}],
            "prerequisites": [], "adopted_rules": [], "excluded_topics": ["All real teaching"],
            "reference_entries": ["body.md#refs"], "exercise_answer_pairs": [],
            "source_requirements": [{
                "id": entry["code"] + "-topic-source", "topic": "Synthetic fixture topic",
                "objective_ids": [entry["code"] + "-1"], "relevance": "topic_specific",
            }],
            "topic_source_status": "verified",
        } for entry in entries]
        self.write("plan.json", {
            **COMMON, "authors": ["author"], "chapter_codes": ["00Axx", "00Bxx"],
            "source_files": ["body.md"], "sections": sections,
        })
        sources = {"body.md": self.digest("body.md")}
        binding = {"plan_sha256": self.digest("plan.json"), "source_sha256": sources}
        for kind in ("math", "pedagogy"):
            self.write(kind + ".md", "SYNTHETIC FIXTURE ONLY; not an actual editorial review.")
            self.write(kind + ".json", {
                **COMMON, **binding, "review_kind": kind, "status": "accepted", "reviewer": kind,
                "reviewed_at": self.DATE, "independent_of_authors": True, "blocking_issues": [],
                "evidence": [self.evidence(kind + ".md")],
                "sections": [{
                    "code": section["code"], "depth": "G",
                    "objective_ids": [section["objectives"][0]["id"]],
                    "status": "accepted", "blocking_issues": [],
                } for section in sections],
            })
        with fitz.open() as pdf:
            pdf.new_page()
            pdf.save(root / "book.pdf")
        self.write("book.html", "<html>Synthetic fixture only</html>")
        self.write("book.md", "Synthetic fixture only")
        with zipfile.ZipFile(root / "source.zip", "w") as archive:
            archive.write(root / "body.md", "body.md")
        artifacts = {name: self.digest(name)
                     for name in ("book.pdf", "book.html", "book.md", "source.zip")}
        self.write("build.md", "Synthetic build fixture; no actual textbook was built.")
        self.write("build.json", {
            **COMMON, **binding, "status": "automated_checks_passed",
            "command": "synthetic fixture", "built_at": self.DATE, "blocking_issues": [],
            "build_input_sha256": {**sources, "build.py": self.digest("build.py")},
            "evidence": [self.evidence("build.md")],
            "section_codes": [section["code"] for section in sections],
            "artifact_sha256": artifacts, "pdf_page_counts": {"book.pdf": 1},
            "checks": dict.fromkeys(sorted(BUILD_CHECKS), True),
        })
        Image.new("RGB", (20, 20), "white").save(root / "page.png")
        self.write("visual.md", "Synthetic screenshot fixture; not real visual review.")
        self.write("visual.json", {
            **COMMON, **binding, "status": "accepted", "reviewer": "visual",
            "reviewed_at": self.DATE, "artifact_sha256": artifacts,
            "build_review_sha256": self.digest("build.json"), "blocking_issues": [],
            "evidence": [self.evidence("visual.md")],
            "pages": [{"pdf": "book.pdf", "pages": [1], **self.evidence("page.png"), "inspected": True}],
            "checks": dict.fromkeys(sorted(VISUAL_CHECKS), True),
        })
        self.write("access.json", {
            "status": "retrieved", "document_sha256": self.DOCUMENT_HASH,
            "notice": "SYNTHETIC access fixture; no network request occurred.",
        })
        self.write("content.md", "SYNTHETIC content review; not an actual source claim.")
        source = {
            "id": "synthetic", "title": "Synthetic source", "author_or_publisher": "Fixture",
            "version": "test", "public_url": "https://example.org/fixture",
            "access": {
                "status": "retrieved", "method": "public_https", "retrieved_at": self.DATE,
                "document_sha256": self.DOCUMENT_HASH, "evidence": [self.evidence("access.json")],
            },
            "content_review": {
                "status": "verified", "reviewer": "fixture_reader", "reviewed_at": self.DATE,
                "document_sha256": self.DOCUMENT_HASH, "evidence": [self.evidence("content.md")],
                "coverage": [{
                    "section_code": section["code"],
                    "requirement_id": section["source_requirements"][0]["id"],
                    "objective_ids": [section["objectives"][0]["id"]], "relevance": "topic_specific",
                    "source_location": "fixture paragraph", "verified_claim": "Synthetic scenario only",
                    "limitations": "No real textbook claim",
                } for section in sections],
            },
        }
        self.write("sources.json", {
            **COMMON, **binding, "status": "verified", "sources": [source],
            "sections": [{
                "code": section["code"], "topic_source_status": "verified",
                "requirements": [{
                    "requirement_id": section["source_requirements"][0]["id"],
                    "status": "verified", "source_ids": ["synthetic"],
                }],
            } for section in sections],
        })

    def write(self, name, value):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n"
                        if isinstance(value, dict) else value)

    def read(self, name):
        return json.loads((self.root / name).read_text())

    def digest(self, name):
        return hashlib.sha256((self.root / name).read_bytes()).hexdigest()

    def evidence(self, name):
        return {"path": name, "sha256": self.digest(name)}

    def rebind(self):
        """Keep unrelated gates valid when deliberately changing the source plan."""
        for name in self.BOUND_RECORDS:
            document = self.read(name)
            document["plan_sha256"] = self.digest("plan.json")
            self.write(name, document)
        visual = self.read("visual.json")
        visual["build_review_sha256"] = self.digest("build.json")
        self.write("visual.json", visual)

    def mutate(self, name, change):
        document = self.read(name)
        change(document)
        self.write(name, document)
        self.rebind()

    def original_work(self, depth):
        plan = self.read("plan.json")
        section = plan["sections"][0]
        section.update(depth=depth, source_requirements=[],
                       topic_source_status="original_work_reviewed_separately")
        if depth == "T":
            section["exercise_answer_pairs"] = [{"question": "body.md#question", "answer": "body.md#answer"}]
        self.write("plan.json", plan)
        sources = self.read("sources.json")
        sources["status"] = "requirements_satisfied"
        sources["sections"][0].update(
            topic_source_status="original_work_reviewed_separately", requirements=[])
        self.write("sources.json", sources)
        for name in ("math.json", "pedagogy.json"):
            review = self.read(name)
            review["sections"][0]["depth"] = depth
            self.write(name, review)
        self.rebind()
        return section

    def mixed_work(self):
        plan = self.read("plan.json")
        section = plan["sections"][0]
        section["depth"] = "S"
        section["objectives"].append({"id": section["code"] + "-original-extra",
                                      "text": "An independently reviewed original derivation"})
        requirement = section["source_requirements"][0]
        section["external_source_claims"] = [{
            "claim": "Synthetic externally sourced fact", "requirement_id": requirement["id"],
            "objective_ids": requirement["objective_ids"],
        }]
        self.write("plan.json", plan)
        for name in ("math.json", "pedagogy.json"):
            review = self.read(name)
            review["sections"][0].update(
                depth="S", objective_ids=[objective["id"] for objective in section["objectives"]])
            self.write(name, review)
        self.rebind()


class SourceGateTests(unittest.TestCase):
    """Nineteen scenarios migrated from the source-gate and exemption checks."""

    def setUp(self):
        directory = TemporaryDirectory(prefix="part1_acceptance_test_")
        self.addCleanup(directory.cleanup)
        self.fixture = EvidenceFixture(Path(directory.name))

    def assert_gate(self, expected, reason=None, missing_math=False):
        fixture = self.fixture
        result = Validator(fixture.root).validate(fixture.args)
        self.assertEqual(result["status"], expected, result["blocking_issues"])
        self.assertEqual(result["full_scope_accepted"], expected == "accepted")
        checks = result["completion_checks"]
        self.assertTrue(checks["scope_plan_valid"], result["blocking_issues"])
        for stage in ("math", "pedagogy", "build", "visual"):
            self.assertEqual(checks["full_scope_" + stage + "_accepted"],
                             not (stage == "math" and missing_math), result["blocking_issues"])
        self.assertEqual(checks["full_scope_sources_accepted"], expected == "accepted" or missing_math)
        self.assertEqual(result["author_review"]["status"], "pending")
        self.assertFalse(result["push_succeeded"])
        if reason:
            messages = json.dumps(result["blocking_issues"]) + json.dumps(result["source_review"]["sections"])
            self.assertIn(reason, messages)
        return result

    def test_complete_source_attestations(self):
        self.assert_gate("accepted")

    def test_missing_source_ledger(self):
        (self.fixture.root / "sources.json").unlink()
        self.assert_gate("pending", "sources.json")

    def test_missing_source_requirements(self):
        self.fixture.mutate("plan.json", lambda d: d["sections"][0].pop("source_requirements"))
        self.assert_gate("pending", "Explicit source_requirements missing")

    def test_g_cannot_request_only_general_method(self):
        self.fixture.mutate("plan.json", lambda d: d["sections"][0]["source_requirements"][0].update(relevance="general_method"))
        self.assert_gate("pending", "G requires topic-specific sources")

    def test_general_source_cannot_substitute_for_topic(self):
        self.fixture.mutate("sources.json", lambda d: d["sources"][0]["content_review"]["coverage"][0].update(relevance="general_method"))
        self.assert_gate("pending", "General method source cannot replace topic-specific evidence")

    def test_http_success_without_content_review(self):
        self.fixture.mutate("sources.json", lambda d: d["sources"][0].update(content_review={"status": "pending"}))
        self.assert_gate("pending", "Actual source content review missing")

    def test_content_review_document_hash_mismatch(self):
        self.fixture.mutate("sources.json", lambda d: d["sources"][0]["content_review"].update(document_sha256="b" * 64))
        self.assert_gate("pending", "different retrieved document")

    def test_access_metadata_is_not_content_review(self):
        self.fixture.mutate("sources.json", lambda d: d["sources"][0]["content_review"].update(evidence=[self.fixture.evidence("access.json")]))
        self.assert_gate("pending", "Access metadata cannot serve as its own content review")

    def test_exact_source_location_is_required(self):
        self.fixture.mutate("sources.json", lambda d: d["sources"][0]["content_review"]["coverage"][0].update(source_location=""))
        self.assert_gate("pending", "Source content review missing source_location")

    def test_pending_scope_source_status(self):
        self.fixture.mutate("plan.json", lambda d: d["sections"][0].update(topic_source_status="pending"))
        self.assert_gate("pending", "Scope plan topic_source_status is not verified")

    def test_source_objectives_must_match_requirement(self):
        self.fixture.mutate("sources.json", lambda d: d["sources"][0]["content_review"]["coverage"][0].update(objective_ids=["not-declared"]))
        self.assert_gate("pending", "Source content coverage does not match required objectives")

    def test_blocked_content_is_not_verified(self):
        self.fixture.mutate("sources.json", lambda d: d["sources"][0]["access"].update(status="blocked_by_environment_proxy"))
        self.assert_gate("pending", "Source content has not been obtained")

    def test_source_ledger_must_cover_all_sections(self):
        self.fixture.mutate("sources.json", lambda d: d["sections"].pop())
        self.assert_gate("pending", "topic source coverage must cover exactly all 33 sections")

    def assert_original_work(self, depth):
        section = self.fixture.original_work(depth)
        result = self.assert_gate("accepted")
        source_result = result["source_review"]["sections"][section["code"]]
        self.assertEqual(source_result["status"], "original_work_reviewed_separately")
        self.assertFalse(source_result["external_sources_verified"])
        self.assertEqual(result["source_review"]["status"], "requirements_satisfied")

    def test_original_t_work_needs_no_external_source(self):
        self.assert_original_work("T")

    def test_original_s_work_needs_no_external_source(self):
        self.assert_original_work("S")

    def test_g_cannot_use_original_work_exemption(self):
        self.fixture.original_work("G")
        self.assert_gate("pending", "G requires nonempty topic-specific source requirements")

    def test_external_fact_cannot_use_original_work_exemption(self):
        section = self.fixture.original_work("S")
        self.fixture.mutate("plan.json", lambda d: d["sections"][0].update(external_source_claims=[{
            "claim": "An external historical fact", "requirement_id": "missing",
            "objective_ids": [section["objectives"][0]["id"]],
        }]))
        self.assert_gate("pending", "External source claims cannot use the original-work exemption")

    def test_mixed_s_sources_only_cover_external_goal(self):
        self.fixture.mixed_work()
        self.assert_gate("accepted")

    def test_original_goal_still_requires_independent_math_review(self):
        self.fixture.mixed_work()
        (self.fixture.root / "math.json").unlink()
        self.assert_gate("pending", "math.json", missing_math=True)


class StoredCrossrefEvidenceTests(unittest.TestCase):
    """Two limited source-unit tests; no live network or whole-section acceptance."""

    def setUp(self):
        directory = TemporaryDirectory(prefix="part1_crossref_test_")
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        access_path = "research/production/part1_revision_sources.json"
        content_path = "research/production/part1_revision_sources.md"
        for name in (access_path, content_path):
            destination = self.root / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REPO_ROOT / name, destination)
        record = json.loads((self.root / access_path).read_text())
        request = next(item for item in record["requests"] if item["id"] == "CROSSREF-FORMAT")
        fact = next(item["fact_zh"] for item in record["crossref"]["source_content_facts"]
                    if item["section"] == "Work / Contributor")
        def evidence(name):
            return {"path": name, "sha256": hashlib.sha256((self.root / name).read_bytes()).hexdigest()}
        self.requirement = {
            "id": "metadata-role-test", "topic": "Crossref Work/Contributor role fields",
            "objective_ids": ["metadata-role-only"], "relevance": "topic_specific",
        }
        self.source = {
            "id": "crossref-real", "title": "Crossref Metadata API JSON Format",
            "author_or_publisher": "Crossref", "version": "v3 (2018-05-15), deprecated document",
            "public_url": request["url"],
            "access": {
                "status": "retrieved", "method": "public_https",
                "retrieved_at": request["checked_at_utc"], "document_sha256": request["sha256"],
                "evidence": [evidence(access_path)],
            },
            "content_review": {
                "status": "verified", "reviewer": "/root/part1_sources",
                "reviewed_at": record["reviewed_at_utc"], "document_sha256": request["sha256"],
                "evidence": [evidence(content_path)],
                "coverage": [{
                    "section_code": "00B10", "requirement_id": "metadata-role-test",
                    "objective_ids": ["metadata-role-only"], "relevance": "topic_specific",
                    "source_location": "Work / Contributor: author, editor, translator, family, given",
                    "verified_claim": fact,
                    "limitations": "Only the stored role-field review; no actual article, philosophy, or literature claim.",
                }],
            },
        }

    def test_stored_crossref_role_field_review_is_valid(self):
        Validator(self.root).verified_topic_source(self.source, "00B10", self.requirement)

    def test_crossref_does_not_meet_philosophy_requirement(self):
        with self.assertRaisesRegex(ValueError, "Source does not address this section's topic requirement"):
            Validator(self.root).verified_topic_source(
                self.source, "00A30", {**self.requirement, "id": "00A30-topic-source"})


if __name__ == "__main__":
    unittest.main()
