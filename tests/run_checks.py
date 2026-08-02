#!/usr/bin/env python3
"""Run repository, skill, public-safety, and integration checks."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "refine-frontend"
UTILITY = SKILL / "scripts" / "refine_workspace.py"
BUILDER = ROOT / "scripts" / "build_release.py"


def run(*args: str) -> None:
    subprocess.run(args, cwd=ROOT, check=True)


def validate_skill() -> None:
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        raise AssertionError("SKILL.md frontmatter is missing")
    frontmatter = yaml.safe_load(match.group(1))
    if set(frontmatter) != {"name", "description"}:
        raise AssertionError("SKILL.md frontmatter must contain name and description only")
    if frontmatter["name"] != "refine-frontend":
        raise AssertionError("Unexpected skill name")
    if len(frontmatter["description"]) < 160:
        raise AssertionError("Skill description is not sufficiently descriptive")
    if len(text.splitlines()) > 500:
        raise AssertionError("SKILL.md exceeds the progressive-disclosure limit")

    agent = yaml.safe_load((SKILL / "agents" / "openai.yaml").read_text(encoding="utf-8"))
    interface = agent.get("interface", {})
    if not 25 <= len(interface.get("short_description", "")) <= 64:
        raise AssertionError("openai.yaml short_description must be 25–64 characters")
    if "$refine-frontend" not in interface.get("default_prompt", ""):
        raise AssertionError("openai.yaml default_prompt must invoke the skill")

    required_references = {
        "research-and-rules.md",
        "visual-contract.md",
        "verification.md",
    }
    actual_references = {path.name for path in (SKILL / "references").glob("*.md")}
    if actual_references != required_references:
        raise AssertionError("Unexpected reference set")


def scan_public_tree() -> None:
    fragments = [
        "/" + "Users" + "/",
        "gh" + "o_",
        "BEGIN " + "PRIVATE KEY",
        "p8" + "Ty",
        "Ci" + "v0",
        "Rhein" + "metall",
        "Spen" + "cer",
    ]
    email_pattern = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
    failures: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in {".git", "dist", "__pycache__"} for part in path.parts):
            continue
        if path == Path(__file__).resolve():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for fragment in fragments:
            if fragment.lower() in text.lower():
                failures.append(f"{path.relative_to(ROOT)} contains forbidden marker")
        for _address in email_pattern.findall(text):
            failures.append(f"{path.relative_to(ROOT)} contains an email address")
    if failures:
        raise AssertionError("\n".join(failures))


def integration_checks() -> None:
    with tempfile.TemporaryDirectory() as temporary:
        project = Path(temporary) / "synthetic-product"
        project.mkdir()
        run(sys.executable, str(UTILITY), "init", "--project", str(project), "--surface", "Settings")
        run(sys.executable, str(UTILITY), "validate", "--project", str(project))
        run(
            sys.executable,
            str(UTILITY),
            "feedback",
            "--project",
            str(project),
            "--id",
            "VR-TYPE-001",
            "--status",
            "rejected",
            "--note",
            "Synthetic feedback test.",
        )
        run(sys.executable, str(UTILITY), "validate", "--project", str(project))
        feedback = json.loads(
            (project / ".visual-refactor" / "visual-feedback.json").read_text(encoding="utf-8")
        )
        if feedback["decisions"][0]["status"] != "rejected":
            raise AssertionError("Feedback was not persisted")


def packaging_check() -> None:
    run(sys.executable, str(BUILDER))
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    archive = ROOT / "dist" / f"refine-frontend-skill-v{version}.zip"
    with zipfile.ZipFile(archive) as package:
        names = set(package.namelist())
    required = {
        "refine-frontend/SKILL.md",
        "refine-frontend/agents/openai.yaml",
        "refine-frontend/scripts/refine_workspace.py",
        "refine-frontend/references/research-and-rules.md",
        "refine-frontend/references/visual-contract.md",
        "refine-frontend/references/verification.md",
    }
    if not required.issubset(names):
        raise AssertionError("Release archive is incomplete")
    if any("__pycache__" in name or name.endswith(".pyc") for name in names):
        raise AssertionError("Release archive contains Python cache files")


def main() -> int:
    validate_skill()
    scan_public_tree()
    integration_checks()
    packaging_check()
    print("PASS: repository checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
