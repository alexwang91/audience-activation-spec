#!/usr/bin/env python3
"""Validate evidence-aware Audience Activation Spec markdown outputs.

This validator intentionally uses only the Python standard library. It performs
lightweight structural and safety checks for v1 markdown fixtures.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Iterable, List


REQUIRED_HEADINGS = [
    "## 1. Activation brief",
    "## 2. Market and channel assumptions",
    "## 3. Mainstream reach-channel map",
    "## 4. Research-signal-to-platform mapping",
    "## 5. Channel execution specs",
    "## 6. Experiment matrix",
    "## 7. Measurement and instrumentation",
    "## 8. Prioritized launch plan",
    "## 9. Quality checks",
]

REQUIRED_TABLE_HEADERS = [
    "| Channel | Role in funnel | Why it fits this audience | Reach mechanism | Execution priority |",
    "| Research signal | Evidence label | Consumer meaning | Platform proxy | Channels where usable | Required validation | Caveats |",
    "| Test cell | Channel | Audience proxy | Creative angle | KPI | Success threshold | Next action |",
]

DETERMINISTIC_TARGETING_PATTERNS = [
    r"\bdeterministically reach\b",
    r"\bperfectly identify\b",
    r"\bguaranteed to reach\b",
    r"\breach every person\b",
    r"\bexactly identify every\b",
    r"\ball users who are interested\b",
]

REAL_BEHAVIOR_MISUSE_PATTERNS = [
    r"\b(?:synthetic|llm)[^\n\.]{0,120}\b(?:real consumer behavior|actual consumer behavior|observed consumer behavior|observed purchase behavior)\b",
    r"\b(?:real consumer behavior|actual consumer behavior|observed consumer behavior|observed purchase behavior)\b[^\n\.]{0,120}\b(?:synthetic|llm)\b",
]

CAUSAL_HETERO_TERMS = ["causal hte", "causal_hte"]
SYNTHETIC_TERMS = ["synthetic", "llm_interview", "llm interview", "llm-generated", "expert_or_team_assumption"]
REAL_CAUSAL_EVIDENCE_TERMS = [
    "experiment",
    "treatment",
    "control",
    "randomized",
    "randomised",
    "quasi-experiment",
    "quasi experimental",
    "holdout",
]


def normalize_table_line(line: str) -> str:
    return re.sub(r"\s+", " ", line.strip())


def contains_header(text: str, header: str) -> bool:
    wanted = normalize_table_line(header)
    return any(normalize_table_line(line) == wanted for line in text.splitlines())


def split_review_units(text: str) -> Iterable[str]:
    """Split into lines and sentence-like units for local risk checks."""
    for line in text.splitlines():
        stripped = line.strip()
        if stripped:
            yield stripped
    for unit in re.split(r"(?<=[.!?])\s+|\n{2,}", text):
        stripped = unit.strip()
        if stripped:
            yield stripped


def has_causal_hte_misuse(text: str) -> List[str]:
    errors: List[str] = []
    for unit in split_review_units(text):
        lower = unit.lower()
        has_causal = any(term in lower for term in CAUSAL_HETERO_TERMS)
        if not has_causal:
            continue

        has_synthetic = any(term in lower for term in SYNTHETIC_TERMS)
        has_real_design = any(term in lower for term in REAL_CAUSAL_EVIDENCE_TERMS)

        if has_synthetic and not has_real_design:
            errors.append(
                "causal_hte misuse: synthetic / LLM / assumption evidence is labeled or described as causal HTE without real causal design evidence."
            )
            continue

        # A table row or YAML-like claim that asserts causal_hte should carry a nearby design basis.
        is_assertive_claim = (
            "|" in unit
            or "evidence_label:" in lower
            or "evidence label" in lower
            or "is causal" in lower
            or "as causal" in lower
            or "proves causal" in lower
        )
        if is_assertive_claim and not has_real_design and "only with" not in lower and "does not" not in lower and "without" not in lower:
            errors.append(
                "causal_hte claim lacks experiment, treatment/control, randomized, holdout, or quasi-experiment evidence in the same claim."
            )
    return errors


def validate_markdown(text: str) -> List[str]:
    errors: List[str] = []
    lower_text = text.lower()

    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            errors.append(f"missing required heading: {heading}")

    for header in REQUIRED_TABLE_HEADERS:
        if not contains_header(text, header):
            errors.append(f"missing required table header: {header}")

    if "## 9. Quality checks" in text:
        quality_section = text.split("## 9. Quality checks", 1)[1]
        checklist_count = len(re.findall(r"^\s*- \[[ xX]\]", quality_section, flags=re.MULTILINE))
        if checklist_count < 5:
            errors.append("quality checks section must include at least five markdown checklist items")
    else:
        errors.append("quality checks section not found")

    if "## 6. Experiment matrix" not in text:
        errors.append("experiment matrix section not found")

    if "## 7. Measurement and instrumentation" not in text:
        errors.append("measurement and instrumentation section not found")

    for pattern in DETERMINISTIC_TARGETING_PATTERNS:
        if re.search(pattern, lower_text):
            errors.append(f"banned deterministic targeting language matched: {pattern}")

    for pattern in REAL_BEHAVIOR_MISUSE_PATTERNS:
        if re.search(pattern, lower_text):
            errors.append("synthetic / LLM signal is described as real or observed consumer behavior")
            break

    errors.extend(has_causal_hte_misuse(text))

    if "synthetic" in lower_text or "llm" in lower_text:
        hypothesis_terms = ["hypothesis", "hypothesis-generating", "validate", "validation"]
        if not any(term in lower_text for term in hypothesis_terms):
            errors.append("synthetic / LLM signals appear without hypothesis or validation language")

    return errors


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate an Audience Activation Spec markdown file.")
    parser.add_argument("path", type=Path, help="Markdown file to validate")
    parser.add_argument("--expect-fail", action="store_true", help="Pass only if validation fails")
    args = parser.parse_args(argv)

    if not args.path.exists():
        print(f"ERROR: file not found: {args.path}", file=sys.stderr)
        return 2

    text = args.path.read_text(encoding="utf-8")
    errors = validate_markdown(text)

    if args.expect_fail:
        if errors:
            print("PASS: validation failed as expected")
            for error in errors:
                print(f"- {error}")
            return 0
        print("FAIL: expected validation failure, but file passed")
        return 1

    if errors:
        print("FAIL: validation errors found")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS: activation spec is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
