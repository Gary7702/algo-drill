"""Tests for the deterministic practice catalog."""

from collections import Counter

from algodrill.catalog import DIFFICULTIES, categories, filter_catalog, load_catalog


def test_catalog_has_180_unique_slugs():
    catalog = load_catalog()
    assert len(catalog) == 180
    counts = Counter(p.slug for p in catalog)
    assert len(counts) == 180
    assert [slug for slug, count in counts.items() if count > 1] == []


def test_entries_are_well_formed():
    for problem in load_catalog():
        assert problem.slug and problem.slug == problem.slug.strip()
        assert problem.title and problem.title == problem.title.strip()
        assert problem.category and problem.pattern
        assert problem.difficulty in DIFFICULTIES


def test_ten_categories_with_eighteen_each():
    names = categories()
    assert len(names) == 10
    assert len(set(names)) == 10
    assert set(names) == {p.category for p in load_catalog()}
    for name in names:
        assert len(filter_catalog(category=name)) == 18


def test_catalog_is_deterministic():
    first = load_catalog()
    assert first == load_catalog()
    assert first is load_catalog()


def test_filter_by_difficulty_is_case_insensitive():
    easy = filter_catalog(difficulty="easy")
    assert easy
    assert all(p.difficulty == "Easy" for p in easy)
    assert len(easy) == len(filter_catalog(difficulty="EASY"))
    assert len(easy) == len(filter_catalog(difficulty="Easy"))


def test_filter_by_pattern_and_category_combined():
    result = filter_catalog(category="tree", pattern="DFS")
    assert result
    assert all(p.category == "Tree" and p.pattern == "dfs" for p in result)


def test_filter_limit():
    assert len(filter_catalog(limit=5)) == 5
    assert len(filter_catalog(limit=1000)) == 180
    assert filter_catalog(limit=0) == ()
    assert filter_catalog(limit=-3) == ()


def test_filter_custom_source():
    catalog = load_catalog()
    assert filter_catalog(catalog[:5], limit=2) == catalog[:2]


def test_unknown_filters_return_empty():
    assert filter_catalog(category="no-such-category") == ()
    assert filter_catalog(difficulty="Impossible") == ()
    assert filter_catalog(pattern="teleportation") == ()
