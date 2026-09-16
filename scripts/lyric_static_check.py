#!/usr/bin/env python3
"""Static lyric-sheet diagnostics using only the Python standard library.

This script reports structural signals. It cannot judge meaning, emotion,
tone-to-melody fit, groove, sustain, hook recall, or music quality.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path


SECTION_RE = re.compile(
    r"^(intro|verse(?:\s*\d+)?|pre(?:-chorus)?(?:\s*\d+)?|chorus(?:\s*\d+)?|"
    r"bridge|outro|refrain|post(?:-chorus)?|drop|rap|instrumental)\b",
    re.IGNORECASE,
)
TOKEN_RE = re.compile(r"[0-9A-Za-zÀ-ỹĐđ]+", re.UNICODE)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


def normalize_terminal(line: str) -> str:
    tokens = TOKEN_RE.findall(line.lower())
    return tokens[-1] if tokens else ""


def normalize_line(line: str) -> str:
    return " ".join(TOKEN_RE.findall(line.lower()))


def parse_lyrics(text: str) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = defaultdict(list)
    current: str | None = None

    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#"):
            current = None
            continue
        if line.startswith("- "):
            continue
        if line.startswith("**") and line.endswith("**"):
            continue
        if line.startswith("[") and line.endswith("]"):
            label = line[1:-1].strip()
            current = label if SECTION_RE.match(label) else current
            continue
        if current is None:
            continue
        if line.startswith("(") and line.endswith(")"):
            continue
        sections[current].append(line.rstrip("  "))

    return dict(sections)


def analyze(sections: dict[str, list[str]]) -> dict[str, object]:
    all_lines = [line for lines in sections.values() for line in lines]
    counts = [len(TOKEN_RE.findall(line)) for line in all_lines]
    normalized = [normalize_line(line) for line in all_lines]
    duplicate_counts = Counter(line for line in normalized if line)

    terminal_repeats: list[dict[str, object]] = []
    for section, lines in sections.items():
        for index, (left, right) in enumerate(zip(lines, lines[1:]), start=1):
            terminal = normalize_terminal(left)
            if terminal and terminal == normalize_terminal(right):
                terminal_repeats.append(
                    {
                        "section": section,
                        "line_pair": [index, index + 1],
                        "terminal": terminal,
                    }
                )

    return {
        "scope": (
            "Static diagnostics only; semantic quality and music-fit remain UNKNOWN."
        ),
        "sections": {
            name: {
                "line_count": len(lines),
                "approx_syllables": [len(TOKEN_RE.findall(line)) for line in lines],
            }
            for name, lines in sections.items()
        },
        "total_lyric_lines": len(all_lines),
        "unique_line_lengths": sorted(set(counts)),
        "eight_syllable_share": (
            round(sum(count == 8 for count in counts) / len(counts), 4)
            if counts
            else 0.0
        ),
        "adjacent_terminal_repeats": terminal_repeats,
        "exact_duplicate_lines": [
            {"line": line, "count": count}
            for line, count in duplicate_counts.items()
            if count > 1
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Report static phrase/rhyme signals from a lyric sheet."
    )
    parser.add_argument("lyric_file", type=Path)
    args = parser.parse_args()

    try:
        text = args.lyric_file.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    sections = parse_lyrics(text)
    if not sections:
        print(
            "error: no recognized [Verse]/[Chorus]/... sections found",
            file=sys.stderr,
        )
        return 2

    print(json.dumps(analyze(sections), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
