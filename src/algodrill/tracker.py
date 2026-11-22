"""JSON-backed progress tracking. No global state: every store owns one path."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from algodrill.catalog import Problem

DEFAULT_PROGRESS = ".algodrill-progress.json"
_VERSION = 1


class ProgressStore:
    """Read and write solved-problem state for a single JSON file."""

    def __init__(self, path: str | Path):
        self.path = Path(path)

    def _read(self) -> dict[str, Any]:
        """Load the file, treating a missing or corrupt file as empty progress."""
        try:
            with self.path.open(encoding="utf-8") as handle:
                data = json.load(handle)
        except (OSError, ValueError):
            return {"version": _VERSION, "solved": {}}

        if not isinstance(data, dict):
            return {"version": _VERSION, "solved": {}}
        solved = data.get("solved")
        if not isinstance(solved, dict):
            return {"version": _VERSION, "solved": {}}

        clean: dict[str, Any] = {}
        for slug, record in solved.items():
            if isinstance(slug, str) and slug:
                clean[slug] = record if isinstance(record, dict) else {"solved_at": None}
        return {"version": _VERSION, "solved": clean}

    def _write(self, data: dict[str, Any]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        ordered = {
            "version": _VERSION,
            "solved": {slug: data["solved"][slug] for slug in sorted(data["solved"])},
        }
        with self.path.open("w", encoding="utf-8", newline="\n") as handle:
            json.dump(ordered, handle, indent=2, ensure_ascii=True, sort_keys=False)
            handle.write("\n")

    def mark_solved(self, slug: str, note: str = "") -> bool:
        """Mark a slug as solved. Returns True if it was newly added."""
        if not isinstance(slug, str) or not slug.strip():
            raise ValueError("slug must be a non-empty string")
        slug = slug.strip()
        data = self._read()
        if slug in data["solved"]:
            return False
        record: dict[str, Any] = {
            "solved_at": datetime.now(timezone.utc).isoformat(timespec="seconds")
        }
        if note:
            record["note"] = note
        data["solved"][slug] = record
        self._write(data)
        return True

    def mark_unsolved(self, slug: str) -> bool:
        """Remove a slug from solved state. Returns True if it was present."""
        if not isinstance(slug, str) or not slug.strip():
            raise ValueError("slug must be a non-empty string")
        data = self._read()
        if slug.strip() not in data["solved"]:
            return False
        del data["solved"][slug.strip()]
        self._write(data)
        return True

    def is_solved(self, slug: str) -> bool:
        return slug in self._read()["solved"]

    def solved_slugs(self) -> list[str]:
        """Return solved slugs in stable sorted order."""
        return sorted(self._read()["solved"])

    def stats(self, problems: tuple[Problem, ...] | list[Problem]) -> dict[str, Any]:
        """Summarize progress against the given catalog."""
        solved = set(self.solved_slugs())
        valid = {p.slug for p in problems}
        matched = solved & valid

        by_category: dict[str, dict[str, int]] = {}
        by_difficulty: dict[str, dict[str, int]] = {}
        for problem in problems:
            for bucket, key in (
                (by_category, problem.category),
                (by_difficulty, problem.difficulty),
            ):
                entry = bucket.setdefault(key, {"solved": 0, "total": 0})
                entry["total"] += 1
                if problem.slug in matched:
                    entry["solved"] += 1

        total = len(problems)
        return {
            "solved_count": len(matched),
            "total_count": total,
            "percent": round(100.0 * len(matched) / total, 1) if total else 0.0,
            "unknown_solved": len(solved - valid),
            "by_category": dict(by_category),
            "by_difficulty": dict(by_difficulty),
        }


def mark_solved(path: str | Path, slug: str, note: str = "") -> bool:
    return ProgressStore(path).mark_solved(slug, note)


def mark_unsolved(path: str | Path, slug: str) -> bool:
    return ProgressStore(path).mark_unsolved(slug)


def solved_slugs(path: str | Path) -> list[str]:
    return ProgressStore(path).solved_slugs()


def stats(path: str | Path, problems: tuple[Problem, ...] | list[Problem]) -> dict[str, Any]:
    return ProgressStore(path).stats(problems)
