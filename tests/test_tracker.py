"""Tests for the JSON progress tracker."""

import json

import pytest

from algodrill.catalog import load_catalog
from algodrill.tracker import (
    ProgressStore,
    mark_solved,
    mark_unsolved,
    solved_slugs,
    stats,
)

CATALOG = load_catalog()


def test_missing_file_is_empty(tmp_path):
    store = ProgressStore(tmp_path / "missing.json")
    assert store.solved_slugs() == []
    assert store.is_solved("two-sum") is False
    result = store.stats(CATALOG)
    assert result["solved_count"] == 0
    assert result["total_count"] == 180


def test_mark_and_unmark_persist(tmp_path):
    path = tmp_path / "progress.json"
    store = ProgressStore(path)
    assert store.mark_solved("two-sum") is True
    assert store.mark_solved("two-sum") is False
    assert store.is_solved("two-sum") is True
    assert store.solved_slugs() == ["two-sum"]

    raw = json.loads(path.read_text(encoding="utf-8"))
    assert raw["version"] == 1
    assert "solved_at" in raw["solved"]["two-sum"]

    assert store.mark_unsolved("two-sum") is True
    assert store.mark_unsolved("two-sum") is False
    assert store.is_solved("two-sum") is False


def test_slugs_sorted_and_note_stored(tmp_path):
    store = ProgressStore(tmp_path / "p.json")
    store.mark_solved("two-sum")
    store.mark_solved("binary-search", note="review")
    assert store.solved_slugs() == ["binary-search", "two-sum"]
    raw = json.loads((tmp_path / "p.json").read_text(encoding="utf-8"))
    assert raw["solved"]["binary-search"]["note"] == "review"


def test_corrupt_file_is_handled(tmp_path):
    path = tmp_path / "bad.json"
    path.write_text("{not json", encoding="utf-8")
    store = ProgressStore(path)
    assert store.solved_slugs() == []
    assert store.mark_solved("two-sum") is True
    assert "two-sum" in json.loads(path.read_text(encoding="utf-8"))["solved"]


def test_wrong_shaped_files_are_handled(tmp_path):
    path = tmp_path / "shape.json"
    path.write_text(json.dumps([1, 2, 3]), encoding="utf-8")
    assert ProgressStore(path).solved_slugs() == []

    for bad_solved in (["two-sum", 7, ""], "nope", None, 42):
        path.write_text(json.dumps({"version": 1, "solved": bad_solved}), encoding="utf-8")
        assert ProgressStore(path).solved_slugs() == []

    path.write_text(json.dumps({"version": 1, "solved": {"": {}, "two-sum": {}}}), encoding="utf-8")
    assert ProgressStore(path).solved_slugs() == ["two-sum"]


def test_stats_by_category_and_difficulty(tmp_path):
    store = ProgressStore(tmp_path / "p.json")
    store.mark_solved("two-sum")
    store.mark_solved("climb-stairs")
    result = store.stats(CATALOG)
    assert result["solved_count"] == 2
    assert result["total_count"] == 180
    assert result["percent"] == 1.1
    assert result["by_category"]["Array & String"]["solved"] == 1
    assert result["by_category"]["Dynamic Programming"]["solved"] == 1
    assert result["by_difficulty"]["Easy"]["solved"] == 2
    assert result["by_difficulty"]["Hard"]["solved"] == 0
    assert sum(item["total"] for item in result["by_category"].values()) == 180


def test_unknown_solved_slugs_reported(tmp_path):
    store = ProgressStore(tmp_path / "p.json")
    store.mark_solved("not-in-catalog")
    result = store.stats(CATALOG)
    assert result["solved_count"] == 0
    assert result["unknown_solved"] == 1


@pytest.mark.parametrize("bad_slug", ["", "   ", 123, None])
def test_invalid_slug_rejected(tmp_path, bad_slug):
    store = ProgressStore(tmp_path / "p.json")
    with pytest.raises(ValueError):
        store.mark_solved(bad_slug)
    with pytest.raises(ValueError):
        store.mark_unsolved(bad_slug)


def test_creates_parent_directories(tmp_path):
    path = tmp_path / "nested" / "deep" / "p.json"
    ProgressStore(path).mark_solved("two-sum")
    assert path.exists()


def test_module_level_helpers(tmp_path):
    path = tmp_path / "p.json"
    assert mark_solved(path, "two-sum") is True
    assert solved_slugs(path) == ["two-sum"]
    assert stats(path, CATALOG)["solved_count"] == 1
    assert mark_unsolved(path, "two-sum") is True
    assert solved_slugs(path) == []
