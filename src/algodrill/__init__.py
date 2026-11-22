"""algodrill: a small, honest algorithm practice tracker."""

from algodrill.catalog import Problem, categories, filter_catalog, load_catalog
from algodrill.tracker import DEFAULT_PROGRESS, ProgressStore

__all__ = [
    "DEFAULT_PROGRESS",
    "Problem",
    "ProgressStore",
    "categories",
    "filter_catalog",
    "load_catalog",
]
__version__ = "0.1.0"
