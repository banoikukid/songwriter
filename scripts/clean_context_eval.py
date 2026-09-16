#!/usr/bin/env python3
"""Run songwriting forward-tests with isolated generator and grader contexts."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path


SCRIPT_SKILL_DIR = Path(__file__).resolve().parents[1]
DEFAULT_SUITE = SCRIPT_SKILL_DIR / "references" / "eval-suite.json"
DEFAULT_OUTPUT_ROOT = SCRIPT_SKILL_DIR.parents[3] / ".songwriting-min-clean-eval-runs"
REFRAME_PATTERNS = (
    r"\bkhông phải\b.{0,80}\bmà (?:là|do|vì)\b",
    r"\btưởng\b.{0,80}\b(?:hóa ra|hoá ra|thì ra)\b",
    r"\btừng\b.{0,80}\b(?:bây giờ|giờ|nay)\b",
    r"\b(?:nhưng|thế mà|vậy mà)\b",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate in fresh contexts, save raw artifacts, then grade separately."
    )
    parser.add_argument("--suite", type=Path, default=DEFAULT_SUITE)
    parser.add_argument(
        "--skill-dir",
        type=Path,
        default=SCRIPT_SKILL_DIR,
        help="Skill snapshot copied into each clean generator context.",
    )
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--case", action="append", dest="case_ids")
    parser.add_argument("--model", help="Optional Codex model override.")
    parser.add_argument(
        "--arm",
        choices=("guided", "direct", "both"),
        default="guided",
        help="Run with the skill, without the skill, or as a paired A/B test.",
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--keep-sandboxes", action="store_true")
    return parser.parse_args()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run_codex(prompt: str, cwd: Path, output_path: Path, model: str | None) -> None:
    command = [
        "codex",
        "exec",
        "--ephemeral",
        "--ignore-user-config",
        "--skip-git-repo-check",
        "--sandbox",
        "read-only",
        "--color",
        "never",
        "-C",
        str(cwd),
        "-o",
        str(output_path),
    ]
    if model:
        command.extend(["--model", model])
    command.append(prompt)
    completed = subprocess.run(command, text=True, encoding="utf-8", errors="replace")
    if completed.returncode != 0:
        raise RuntimeError(f"codex exec failed with exit code {completed.returncode}")


def generator_prompt(case: dict, arm: str) -> str:
    if arm == "direct":
        return (
            "Hãy tự sáng tác trực tiếp theo yêu cầu dưới đây. Không đọc hoặc dùng bất kỳ "
            "skill, rubric, bài mẫu hay output nào khác. Chỉ trả artifact người dùng yêu cầu; "
            "không tự chấm và không giải thích quy trình nội bộ.\n\n"
            f"YÊU CẦU:\n{case['prompt']}\n"
        )
    return (
        "Dùng skill songwriting-min trong thư mục ./songwriting-min để xử lý yêu cầu dưới đây. "
        "Chỉ đọc SKILL.md và các reference mà router của skill yêu cầu cho đúng tác vụ. "
        "Không audit skill, không tự chấm, không giải thích quy trình nội bộ.\n\n"
        f"YÊU CẦU:\n{case['prompt']}\n"
    )


def grader_prompt(case: dict, rubric: str) -> str:
    return (
        "Bạn là grader độc lập. Chỉ đọc ./raw-output.md. Không suy đoán prompt ẩn, "
        "không sửa bài và không thưởng vì bài giống một đáp án mẫu. Chấm từng tiêu chí "
        "đúng theo rubric dưới đây; trích dẫn ngắn từ raw output làm evidence. "
        "Trả về đúng JSON theo schema được cung cấp.\n\n"
        f"CASE ID: {case['id']}\n"
        f"USER BRIEF:\n{case['prompt']}\n\n"
        f"RUBRIC:\n{rubric}\n"
    )


def deterministic_scan(raw: str) -> dict:
    hits = []
    for pattern in REFRAME_PATTERNS:
        matches = re.findall(pattern, raw, flags=re.IGNORECASE | re.DOTALL)
        if matches:
            hits.append({"pattern": pattern, "count": len(matches)})
    return {
        "reframe_marker_hits": hits,
        "reframe_marker_total": sum(item["count"] for item in hits),
        "note": "Marker scan is diagnostic only; semantic reframe is decided by the grader.",
    }


def main() -> int:
    args = parse_args()
    if args.trials < 1:
        raise SystemExit("--trials must be at least 1")

    skill_dir = args.skill_dir.resolve()
    if not (skill_dir / "SKILL.md").is_file():
        raise SystemExit(f"Invalid --skill-dir (missing SKILL.md): {skill_dir}")
    suite = load_json(args.suite.resolve())
    schema_value = suite.get("grader_schema", "eval-grader-schema.json")
    schema_path = Path(schema_value)
    if not schema_path.is_absolute():
        schema_path = args.suite.resolve().parent / schema_path
    schema_path = schema_path.resolve()
    if not schema_path.is_file():
        raise SystemExit(f"Missing grader schema: {schema_path}")
    cases = suite["cases"]
    if args.case_ids:
        wanted = set(args.case_ids)
        cases = [case for case in cases if case["id"] in wanted]
        missing = wanted - {case["id"] for case in cases}
        if missing:
            raise SystemExit(f"Unknown case id(s): {', '.join(sorted(missing))}")

    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = args.output_root.resolve() / run_id
    manifest = {
        "run_id": run_id,
        "suite": str(args.suite.resolve()),
        "suite_sha256": sha256(args.suite.resolve()),
        "grader_schema": str(schema_path),
        "grader_schema_sha256": sha256(schema_path),
        "skill_dir": str(skill_dir),
        "skill_sha256": sha256(skill_dir / "SKILL.md"),
        "model": args.model or "codex-config-default",
        "arm": args.arm,
        "trials_per_case": args.trials,
        "contamination_status": "isolated-generator-and-grader-filesystems",
        "cases": [case["id"] for case in cases],
    }

    if args.dry_run:
        print(json.dumps(manifest, ensure_ascii=False, indent=2))
        return 0

    run_dir.mkdir(parents=True, exist_ok=False)
    (run_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    rubric = suite["grader_rubric"]

    arms = ("direct", "guided") if args.arm == "both" else (args.arm,)

    for case in cases:
        for trial in range(1, args.trials + 1):
            for arm in arms:
                artifact_dir = run_dir / case["id"] / f"trial-{trial:02d}" / arm
                artifact_dir.mkdir(parents=True)
                raw_path = artifact_dir / "raw-output.md"
                grade_path = artifact_dir / "grade.json"

                generator_tmp = Path(tempfile.mkdtemp(prefix="song-gen-"))
                grader_tmp = Path(tempfile.mkdtemp(prefix="song-grade-"))
                try:
                    if arm == "guided":
                        shutil.copytree(
                            skill_dir,
                            generator_tmp / "songwriting-min",
                            ignore=shutil.ignore_patterns(
                                "eval-runs", "songwriting-min-clean-eval-runs", "__pycache__", "*.pyc"
                            ),
                        )
                    run_codex(generator_prompt(case, arm), generator_tmp, raw_path, args.model)
                    raw_text = raw_path.read_text(encoding="utf-8")
                    (artifact_dir / "deterministic.json").write_text(
                        json.dumps(deterministic_scan(raw_text), ensure_ascii=False, indent=2),
                        encoding="utf-8",
                    )

                    shutil.copy2(raw_path, grader_tmp / "raw-output.md")
                    local_schema = grader_tmp / "grader-schema.json"
                    shutil.copy2(schema_path, local_schema)
                    command = [
                    "codex",
                    "exec",
                    "--ephemeral",
                    "--ignore-user-config",
                    "--skip-git-repo-check",
                    "--sandbox",
                    "read-only",
                    "--color",
                    "never",
                    "-C",
                    str(grader_tmp),
                    "--output-schema",
                    str(local_schema),
                    "-o",
                    str(grade_path),
                    ]
                    if args.model:
                        command.extend(["--model", args.model])
                    command.append(grader_prompt(case, rubric))
                    completed = subprocess.run(
                        command, text=True, encoding="utf-8", errors="replace"
                    )
                    if completed.returncode != 0:
                        raise RuntimeError(
                            f"grader failed with exit code {completed.returncode}"
                        )
                    json.loads(grade_path.read_text(encoding="utf-8"))
                finally:
                    if args.keep_sandboxes:
                        (artifact_dir / "sandboxes.txt").write_text(
                            f"generator={generator_tmp}\ngrader={grader_tmp}\n",
                            encoding="utf-8",
                        )
                    else:
                        shutil.rmtree(generator_tmp, ignore_errors=True)
                        shutil.rmtree(grader_tmp, ignore_errors=True)

    print(run_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
