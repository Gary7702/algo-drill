"""Tests for the argparse CLI and the module entry point."""

import os
import runpy
import subprocess
import sys
from pathlib import Path

import pytest

from algodrill.catalog import load_catalog
from algodrill.cli import main
from algodrill.tracker import ProgressStore

SRC_DIR = Path(__file__).resolve().parents[1] / "src"


def _path(tmp_path):
    return str(tmp_path / "progress.json")


def test_list_limit(capsys, tmp_path):
    code = main(["list", "--limit", "3", "--progress", _path(tmp_path)])
    out = capsys.readouterr().out
    assert code == 0
    lines = [line for line in out.splitlines() if line.strip()]
    assert lines[0] == "Catalog: 180 problems, showing 3"
    assert len(lines) == 5
    assert "two-sum" in lines[2]


def test_list_filters(capsys, tmp_path):
    code = main(
        [
            "list",
            "--category",
            "tree",
            "--difficulty",
            "easy",
            "--limit",
            "2",
            "--progress",
            _path(tmp_path),
        ]
    )
    out = capsys.readouterr().out
    assert code == 0
    assert "showing 2" in out
    assert "maximum-depth-of-binary-tree" in out
    assert "invert-binary-tree" in out


def test_stats_empty(capsys, tmp_path):
    code = main(["stats", "--progress", _path(tmp_path)])
    out = capsys.readouterr().out
    assert code == 0
    assert "Progress: 0/180 solved (0.0%)" in out
    assert "By difficulty:" in out
    assert "By category:" in out
    assert "Array & String" in out


def test_solve_then_stats(capsys, tmp_path):
    path = _path(tmp_path)
    assert main(["solve", "two-sum", "--progress", path]) == 0
    assert "Marked solved: two-sum - Two Sum" in capsys.readouterr().out

    assert main(["solve", "two-sum", "--progress", path]) == 0
    assert "Already solved: two-sum" in capsys.readouterr().out

    assert main(["stats", "--progress", path]) == 0
    assert "Progress: 1/180 solved (0.6%)" in capsys.readouterr().out


def test_next_and_unsolve(capsys, tmp_path):
    path = _path(tmp_path)
    assert main(["next", "--progress", path]) == 0
    first = capsys.readouterr().out
    assert "Next up: Two Sum" in first
    assert "slug:       two-sum" in first
    assert "difficulty: Easy" in first

    main(["solve", "two-sum", "--progress", path])
    capsys.readouterr()
    main(["next", "--progress", path])
    assert "Next up: Best Time to Buy and Sell Stock" in capsys.readouterr().out

    assert main(["unsolve", "two-sum", "--progress", path]) == 0
    assert "Marked unsolved: two-sum" in capsys.readouterr().out
    main(["unsolve", "two-sum", "--progress", path])
    assert "Not marked solved: two-sum" in capsys.readouterr().out


def test_unknown_slug_writes_stderr(capsys, tmp_path):
    code = main(["solve", "does-not-exist", "--progress", _path(tmp_path)])
    captured = capsys.readouterr()
    assert code == 1
    assert "Unknown slug: does-not-exist" in captured.err
    assert captured.out == ""


def test_progress_before_subcommand(capsys, tmp_path):
    path = _path(tmp_path)
    main(["--progress", path, "solve", "two-sum"])
    assert "Marked solved" in capsys.readouterr().out
    main(["--progress", path, "stats"])
    assert "Progress: 1/180" in capsys.readouterr().out


def test_unsolve_unknown_slug_writes_stderr(capsys, tmp_path):
    code = main(["unsolve", "does-not-exist", "--progress", _path(tmp_path)])
    captured = capsys.readouterr()
    assert code == 1
    assert "Unknown slug: does-not-exist" in captured.err


def test_stats_reports_unknown_solved_slug(capsys, tmp_path):
    path = _path(tmp_path)
    ProgressStore(path).mark_solved("not-in-catalog")
    main(["stats", "--progress", path])
    assert "Note: 1 solved slug(s) not in catalog" in capsys.readouterr().out


def test_next_when_all_solved(capsys, tmp_path):
    path = _path(tmp_path)
    store = ProgressStore(path)
    for problem in load_catalog():
        store.mark_solved(problem.slug)
    assert main(["next", "--progress", path]) == 0
    assert "All 180 problems are solved." in capsys.readouterr().out


def test_module_entry_point(tmp_path):
    env = os.environ.copy()
    env["PYTHONPATH"] = str(SRC_DIR) + os.pathsep + env.get("PYTHONPATH", "")
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "algodrill",
            "list",
            "--limit",
            "1",
            "--progress",
            _path(tmp_path),
        ],
        capture_output=True,
        text=True,
        env=env,
        check=False,
    )
    assert result.returncode == 0
    assert "Catalog: 180 problems, showing 1" in result.stdout


def test_runpy_main_module(monkeypatch, capsys, tmp_path):
    monkeypatch.setattr(sys, "argv", ["algodrill", "stats", "--progress", _path(tmp_path)])
    with pytest.raises(SystemExit) as exc:
        runpy.run_module("algodrill", run_name="__main__")
    assert exc.value.code == 0
    assert "Progress: 0/180 solved (0.0%)" in capsys.readouterr().out
