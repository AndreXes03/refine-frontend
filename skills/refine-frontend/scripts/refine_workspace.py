#!/usr/bin/env python3
"""Create and validate a persistent Functional → Refined workspace."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


WORKSPACE = ".visual-refactor"
CONTRACT = "visual-contract.json"
FEEDBACK = "visual-feedback.json"
LEDGER = "change-ledger.md"
LEVELS = {"high", "medium", "low"}
DEPTHS = {"foundations", "surface", "system"}
STATUSES = {"accepted", "modified", "rejected", "reverted"}
QUALITY_STATUSES = {"pass", "not-applicable"}
QUALITY_CHECKS = {
    "structureAndComprehension",
    "typographyAndZoom",
    "contrastAndColor",
    "keyboardAndFocus",
    "targetsStatesAndFeedback",
    "formsErrorsAndRecovery",
    "responsiveAndOverflow",
    "densityGroupingAndData",
}


def timestamp() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def workspace(project: str) -> Path:
    return Path(project).expanduser().resolve() / WORKSPACE


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"missing {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path}: {exc}") from exc


def contract_template(surface: str) -> dict[str, Any]:
    return {
        "schemaVersion": 1,
        "surface": {
            "name": surface,
            "primaryTask": "TODO",
            "routes": [],
            "states": ["default"],
        },
        "classification": {
            "interactionLoad": "medium",
            "informationDensity": "medium",
            "brandExpressionNeed": "low",
            "refinementDepth": "surface",
            "rationale": "TODO",
        },
        "patternSelection": {
            "taskTopology": "TODO",
            "dominantArtifact": "TODO",
            "nativePattern": "TODO",
            "navigationModel": "TODO",
            "compositionModel": "TODO",
            "existingPrimitives": [],
            "productSpecificSignals": [],
            "alternativePattern": "TODO",
            "rejectedDefaults": [],
            "mobileTransformation": "TODO",
            "convergenceRisk": "medium",
            "rationale": "TODO",
        },
        "invariants": [],
        "constraints": {
            "framework": "TODO",
            "styling": "TODO",
            "newDependencies": False,
            "maxChangedFiles": None,
        },
        "foundations": {
            "typography": {},
            "spacing": {},
            "colorRoles": {},
            "surfaces": {},
            "shape": {},
            "layout": {},
            "states": {},
            "responsive": {},
        },
        "qualityFloor": {
            "checks": {
                check: {"status": "TODO", "evidence": []}
                for check in sorted(QUALITY_CHECKS)
            }
        },
        "signature": {
            "enabled": False,
            "channel": None,
            "rule": None,
            "exclusions": [],
        },
        "verification": {
            "viewports": [
                {"name": "mobile", "width": 390, "height": 844},
                {"name": "desktop", "width": 1440, "height": 900},
            ],
            "commands": [],
            "scenarios": [],
        },
    }


def command_init(args: argparse.Namespace) -> int:
    root = workspace(args.project)
    root.mkdir(parents=True, exist_ok=True)
    (root / "before").mkdir(exist_ok=True)
    (root / "after").mkdir(exist_ok=True)

    contract_path = root / CONTRACT
    feedback_path = root / FEEDBACK
    ledger_path = root / LEDGER

    if contract_path.exists() and not args.force:
        print(f"preserved {contract_path}")
    else:
        write_json(contract_path, contract_template(args.surface))
        print(f"created {contract_path}")

    if feedback_path.exists() and not args.force:
        print(f"preserved {feedback_path}")
    else:
        write_json(feedback_path, {"schemaVersion": 1, "updatedAt": timestamp(), "decisions": []})
        print(f"created {feedback_path}")

    if ledger_path.exists() and not args.force:
        print(f"preserved {ledger_path}")
    else:
        ledger_path.write_text(
            "# Visual refinement change ledger\n\n"
            "Record observed problems, material decisions, affected files, and verification evidence.\n",
            encoding="utf-8",
        )
        print(f"created {ledger_path}")
    return 0


def require_mapping(value: Any, label: str, errors: list[str]) -> dict[str, Any]:
    if not isinstance(value, dict):
        errors.append(f"{label} must be an object")
        return {}
    return value


def validate_contract(value: Any, *, strict: bool = False) -> list[str]:
    errors: list[str] = []
    root = require_mapping(value, "contract", errors)
    if root.get("schemaVersion") != 1:
        errors.append("contract.schemaVersion must be 1")

    surface = require_mapping(root.get("surface"), "contract.surface", errors)
    if not isinstance(surface.get("name"), str) or not surface.get("name", "").strip():
        errors.append("contract.surface.name must be a non-empty string")
    if not isinstance(surface.get("states"), list):
        errors.append("contract.surface.states must be an array")

    classification = require_mapping(root.get("classification"), "contract.classification", errors)
    for key in ("interactionLoad", "informationDensity", "brandExpressionNeed"):
        if classification.get(key) not in LEVELS:
            errors.append(f"contract.classification.{key} must be high, medium, or low")
    if classification.get("refinementDepth") not in DEPTHS:
        errors.append("contract.classification.refinementDepth must be foundations, surface, or system")

    pattern_selection = root.get("patternSelection")
    if strict and pattern_selection is None:
        errors.append("contract.patternSelection is required for strict validation")
    if pattern_selection is not None:
        pattern_selection = require_mapping(pattern_selection, "contract.patternSelection", errors)
        required_strings = [
            "taskTopology",
            "nativePattern",
            "navigationModel",
            "compositionModel",
            "rationale",
        ]
        if strict:
            required_strings.extend(("dominantArtifact", "alternativePattern", "mobileTransformation"))
        for key in required_strings:
            if not isinstance(pattern_selection.get(key), str) or not pattern_selection.get(key, "").strip():
                errors.append(f"contract.patternSelection.{key} must be a non-empty string")
            elif strict and pattern_selection[key].strip().upper() == "TODO":
                errors.append(f"contract.patternSelection.{key} must replace the TODO placeholder")
        required_arrays = ["existingPrimitives", "rejectedDefaults"]
        if strict:
            required_arrays.append("productSpecificSignals")
        for key in required_arrays:
            if not isinstance(pattern_selection.get(key), list):
                errors.append(f"contract.patternSelection.{key} must be an array")
        if strict and isinstance(pattern_selection.get("productSpecificSignals"), list):
            if len(pattern_selection["productSpecificSignals"]) < 2:
                errors.append("contract.patternSelection.productSpecificSignals must include at least two items")
        if strict and isinstance(pattern_selection.get("rejectedDefaults"), list):
            if not pattern_selection["rejectedDefaults"]:
                errors.append("contract.patternSelection.rejectedDefaults must include at least one item")
        if pattern_selection.get("convergenceRisk") not in LEVELS:
            errors.append("contract.patternSelection.convergenceRisk must be high, medium, or low")

    invariants = root.get("invariants")
    if not isinstance(invariants, list):
        errors.append("contract.invariants must be an array")

    foundations = require_mapping(root.get("foundations"), "contract.foundations", errors)
    required_foundations = {
        "typography", "spacing", "colorRoles", "surfaces", "shape", "layout", "states", "responsive"
    }
    missing = sorted(required_foundations - foundations.keys())
    if missing:
        errors.append("contract.foundations is missing: " + ", ".join(missing))

    quality_floor = root.get("qualityFloor")
    if strict and quality_floor is None:
        errors.append("contract.qualityFloor is required for strict validation")
    if quality_floor is not None:
        quality_floor = require_mapping(quality_floor, "contract.qualityFloor", errors)
        checks = require_mapping(quality_floor.get("checks"), "contract.qualityFloor.checks", errors)
        if strict:
            missing_checks = sorted(QUALITY_CHECKS - checks.keys())
            if missing_checks:
                errors.append(
                    "contract.qualityFloor.checks is missing: " + ", ".join(missing_checks)
                )
        for check_id, result in checks.items():
            label = f"contract.qualityFloor.checks.{check_id}"
            if check_id not in QUALITY_CHECKS:
                errors.append(f"{label} is not a supported quality-floor check")
                continue
            result = require_mapping(result, label, errors)
            status = result.get("status")
            if strict and status not in QUALITY_STATUSES:
                errors.append(f"{label}.status must be pass or not-applicable")
            elif not strict and status not in QUALITY_STATUSES | {"TODO"}:
                errors.append(f"{label}.status must be TODO, pass, or not-applicable")
            evidence = result.get("evidence")
            if not isinstance(evidence, list):
                errors.append(f"{label}.evidence must be an array")
            elif strict:
                usable_evidence = [
                    item for item in evidence if isinstance(item, str) and item.strip()
                ]
                if not usable_evidence:
                    errors.append(f"{label}.evidence must include at least one concrete item")

    signature = require_mapping(root.get("signature"), "contract.signature", errors)
    if not isinstance(signature.get("enabled"), bool):
        errors.append("contract.signature.enabled must be a boolean")
    if signature.get("enabled"):
        if signature.get("channel") not in {"typography", "composition", "color", "motion", "imagery"}:
            errors.append("enabled signature.channel must be typography, composition, color, motion, or imagery")
        if not isinstance(signature.get("rule"), str) or not signature.get("rule", "").strip():
            errors.append("enabled signature.rule must be a non-empty string")

    verification = require_mapping(root.get("verification"), "contract.verification", errors)
    viewports = verification.get("viewports")
    if not isinstance(viewports, list) or len(viewports) < 2:
        errors.append("contract.verification.viewports must include at least mobile and desktop")
    else:
        for index, viewport in enumerate(viewports):
            if not isinstance(viewport, dict):
                errors.append(f"contract.verification.viewports[{index}] must be an object")
                continue
            for dimension in ("width", "height"):
                if not isinstance(viewport.get(dimension), int) or viewport[dimension] <= 0:
                    errors.append(
                        f"contract.verification.viewports[{index}].{dimension} must be a positive integer"
                    )
    return errors


def validate_feedback(value: Any) -> list[str]:
    errors: list[str] = []
    root = require_mapping(value, "feedback", errors)
    if root.get("schemaVersion") != 1:
        errors.append("feedback.schemaVersion must be 1")
    decisions = root.get("decisions")
    if not isinstance(decisions, list):
        errors.append("feedback.decisions must be an array")
        return errors
    seen: set[str] = set()
    for index, item in enumerate(decisions):
        if not isinstance(item, dict):
            errors.append(f"feedback.decisions[{index}] must be an object")
            continue
        decision_id = item.get("id")
        if not isinstance(decision_id, str) or not decision_id.strip():
            errors.append(f"feedback.decisions[{index}].id must be a non-empty string")
        elif decision_id in seen:
            errors.append(f"feedback decision id is duplicated: {decision_id}")
        else:
            seen.add(decision_id)
        if item.get("status") not in STATUSES:
            errors.append(f"feedback.decisions[{index}].status is invalid")
    return errors


def command_validate(args: argparse.Namespace) -> int:
    root = workspace(args.project)
    errors: list[str] = []
    try:
        errors.extend(validate_contract(load_json(root / CONTRACT), strict=args.strict))
    except ValueError as exc:
        errors.append(str(exc))
    try:
        errors.extend(validate_feedback(load_json(root / FEEDBACK)))
    except ValueError as exc:
        errors.append(str(exc))
    if not (root / LEDGER).is_file():
        errors.append(f"missing {root / LEDGER}")
    for evidence_dir in ("before", "after"):
        if not (root / evidence_dir).is_dir():
            errors.append(f"missing {root / evidence_dir}/")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"valid refinement workspace: {root}")
    return 0


def command_feedback(args: argparse.Namespace) -> int:
    root = workspace(args.project)
    path = root / FEEDBACK
    try:
        value = load_json(path)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    if validate_feedback(value):
        print("ERROR: existing feedback file is invalid; run validate", file=sys.stderr)
        return 1

    entry = {"id": args.id, "status": args.status, "note": args.note, "recordedAt": timestamp()}
    decisions = value["decisions"]
    existing = next((item for item in decisions if item.get("id") == args.id), None)
    if existing:
        existing.update(entry)
        action = "updated"
    else:
        decisions.append(entry)
        action = "recorded"
    value["updatedAt"] = timestamp()
    write_json(path, value)
    print(f"{action} feedback {args.id} as {args.status}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="create a .visual-refactor workspace")
    init_parser.add_argument("--project", default=".")
    init_parser.add_argument("--surface", required=True)
    init_parser.add_argument("--force", action="store_true", help="replace contract, feedback, and ledger")
    init_parser.set_defaults(func=command_init)

    validate_parser = subparsers.add_parser("validate", help="validate the workspace structure and JSON")
    validate_parser.add_argument("--project", default=".")
    validate_parser.add_argument(
        "--strict",
        action="store_true",
        help="reject placeholders and require completed specificity and quality-floor evidence",
    )
    validate_parser.set_defaults(func=command_validate)

    feedback_parser = subparsers.add_parser("feedback", help="record or update a human decision")
    feedback_parser.add_argument("--project", default=".")
    feedback_parser.add_argument("--id", required=True)
    feedback_parser.add_argument("--status", required=True, choices=sorted(STATUSES))
    feedback_parser.add_argument("--note", required=True)
    feedback_parser.set_defaults(func=command_feedback)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
