#!/usr/bin/env python3
"""Build a deterministic Functional → Refined skill archive."""

from __future__ import annotations

import hashlib
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "refine-frontend"
DIST = ROOT / "dist"
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
FIXED_TIME = (2026, 1, 1, 0, 0, 0)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()

    output = DIST / f"refine-frontend-skill-v{VERSION}.zip"
    with zipfile.ZipFile(output, "w") as archive:
        for path in sorted(SKILL.rglob("*")):
            if not path.is_file() or "__pycache__" in path.parts:
                continue
            relative = path.relative_to(SKILL)
            info = zipfile.ZipInfo(str(Path("refine-frontend") / relative), FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            executable = path.name == "refine_workspace.py"
            info.external_attr = (0o755 if executable else 0o644) << 16
            archive.writestr(info, path.read_bytes())

    checksum = f"{sha256(output)}  {output.name}\n"
    (DIST / "SHA256SUMS.txt").write_text(checksum, encoding="utf-8")
    print(f"Built {output}")
    print(f"Built {DIST / 'SHA256SUMS.txt'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
