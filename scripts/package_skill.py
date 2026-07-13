#!/usr/bin/env python3
"""Create a deterministic, portable ZIP archive from a Skill directory."""

from __future__ import annotations

import argparse
import stat
import sys
import zipfile
from pathlib import Path, PurePosixPath


EXCLUDED_PARTS = {".DS_Store", "__pycache__", ".git", ".pytest_cache"}
EXCLUDED_SUFFIXES = {".pyc", ".pyo", ".zip"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "skill_dir",
        nargs="?",
        default="skills/eprp-adaptive-tutoring",
        type=Path,
        help="Skill directory to package",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Output ZIP path (default: dist/<skill-name>.zip)",
    )
    return parser.parse_args()


def validate_skill(skill_dir: Path) -> None:
    if not skill_dir.is_dir():
        raise ValueError(f"Skill directory does not exist: {skill_dir}")
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        raise ValueError(f"Missing required file: {skill_file}")
    text = skill_file.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\nname:" not in text or "\ndescription:" not in text:
        raise ValueError("SKILL.md must contain YAML frontmatter with name and description")


def included_files(skill_dir: Path, output: Path) -> list[Path]:
    files: list[Path] = []
    for path in skill_dir.rglob("*"):
        if not path.is_file() or path.resolve() == output.resolve():
            continue
        relative = path.relative_to(skill_dir)
        if any(part in EXCLUDED_PARTS for part in relative.parts):
            continue
        if path.suffix.lower() in EXCLUDED_SUFFIXES:
            continue
        files.append(path)
    return sorted(files, key=lambda item: item.relative_to(skill_dir).as_posix())


def add_file(archive: zipfile.ZipFile, source: Path, archive_name: PurePosixPath) -> None:
    info = zipfile.ZipInfo(str(archive_name), date_time=(1980, 1, 1, 0, 0, 0))
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = (stat.S_IFREG | 0o644) << 16
    info.create_system = 3
    archive.writestr(info, source.read_bytes())


def package_skill(skill_dir: Path, output: Path) -> int:
    skill_dir = skill_dir.resolve()
    output = output.resolve()
    validate_skill(skill_dir)
    files = included_files(skill_dir, output)
    if not files:
        raise ValueError(f"No packageable files found in {skill_dir}")

    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_suffix(output.suffix + ".tmp")
    try:
        with zipfile.ZipFile(temporary, "w") as archive:
            for source in files:
                relative = PurePosixPath(source.relative_to(skill_dir).as_posix())
                add_file(archive, source, PurePosixPath(skill_dir.name) / relative)
        temporary.replace(output)
    finally:
        temporary.unlink(missing_ok=True)
    return len(files)


def main() -> int:
    args = parse_args()
    output = args.output or Path("dist") / f"{args.skill_dir.name}.zip"
    try:
        count = package_skill(args.skill_dir, output)
    except (OSError, ValueError, zipfile.BadZipFile) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    print(f"Packaged {count} files: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
