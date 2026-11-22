"""Command line interface for algodrill. All output is plain ASCII."""

from __future__ import annotations

import argparse
import sys

from algodrill.catalog import Problem, filter_catalog, load_catalog
from algodrill.tracker import DEFAULT_PROGRESS, ProgressStore


def _add_progress(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--progress",
        default=argparse.SUPPRESS,
        help=f"progress JSON file (default: {DEFAULT_PROGRESS})",
    )


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="algodrill",
        description="Track a self-directed algorithm practice checklist.",
    )
    _add_progress(parser)
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="list catalog problems")
    _add_progress(p_list)
    p_list.add_argument("--category", help="filter by category (case-insensitive)")
    p_list.add_argument("--difficulty", help="filter by Easy/Medium/Hard")
    p_list.add_argument("--limit", type=int, help="show at most N problems")

    p_stats = sub.add_parser("stats", help="show progress statistics")
    _add_progress(p_stats)

    p_solve = sub.add_parser("solve", help="mark a problem solved")
    _add_progress(p_solve)
    p_solve.add_argument("slug", help="problem slug")

    p_unsolve = sub.add_parser("unsolve", help="mark a problem unsolved")
    _add_progress(p_unsolve)
    p_unsolve.add_argument("slug", help="problem slug")

    p_next = sub.add_parser("next", help="suggest the next unsolved problem")
    _add_progress(p_next)

    return parser


def _format_problem(problem: Problem) -> str:
    return (
        f"{problem.slug:<38} {problem.difficulty:<6}  {problem.title} "
        f"[{problem.category} / {problem.pattern}]"
    )


def _find(catalog: tuple[Problem, ...], slug: str) -> Problem | None:
    return next((p for p in catalog if p.slug == slug), None)


def _cmd_list(args: argparse.Namespace, catalog: tuple[Problem, ...]) -> int:
    problems = filter_catalog(
        catalog,
        category=args.category,
        difficulty=args.difficulty,
        limit=args.limit,
    )
    print(f"Catalog: {len(catalog)} problems, showing {len(problems)}")
    print("-" * 78)
    for problem in problems:
        print(_format_problem(problem))
    return 0


def _cmd_stats(args: argparse.Namespace, catalog: tuple[Problem, ...], progress: str) -> int:
    store = ProgressStore(progress)
    result = store.stats(catalog)
    print(
        f"Progress: {result['solved_count']}/{result['total_count']} solved "
        f"({result['percent']:.1f}%)"
    )
    if result["unknown_solved"]:
        print(f"Note: {result['unknown_solved']} solved slug(s) not in catalog")

    print("")
    print("By difficulty:")
    for name in ("Easy", "Medium", "Hard"):
        bucket = result["by_difficulty"].get(name, {"solved": 0, "total": 0})
        print(f"  {name:<8} {bucket['solved']:>3}/{bucket['total']}")

    print("")
    print("By category:")
    for name in sorted(result["by_category"]):
        bucket = result["by_category"][name]
        print(f"  {name:<30} {bucket['solved']:>3}/{bucket['total']}")
    return 0


def _cmd_solve(args: argparse.Namespace, catalog: tuple[Problem, ...], progress: str) -> int:
    problem = _find(catalog, args.slug)
    if problem is None:
        print(f"Unknown slug: {args.slug}", file=sys.stderr)
        return 1
    added = ProgressStore(progress).mark_solved(args.slug)
    state = "Marked solved" if added else "Already solved"
    print(f"{state}: {problem.slug} - {problem.title}")
    return 0


def _cmd_unsolve(args: argparse.Namespace, catalog: tuple[Problem, ...], progress: str) -> int:
    problem = _find(catalog, args.slug)
    if problem is None:
        print(f"Unknown slug: {args.slug}", file=sys.stderr)
        return 1
    removed = ProgressStore(progress).mark_unsolved(args.slug)
    state = "Marked unsolved" if removed else "Not marked solved"
    print(f"{state}: {problem.slug} - {problem.title}")
    return 0


def _cmd_next(args: argparse.Namespace, catalog: tuple[Problem, ...], progress: str) -> int:
    store = ProgressStore(progress)
    candidate = next((p for p in catalog if not store.is_solved(p.slug)), None)
    if candidate is None:
        print(f"All {len(catalog)} problems are solved.")
        return 0
    print(f"Next up: {candidate.title}")
    print(f"  slug:       {candidate.slug}")
    print(f"  category:   {candidate.category}")
    print(f"  difficulty: {candidate.difficulty}")
    print(f"  pattern:    {candidate.pattern}")
    return 0


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    catalog = load_catalog()
    progress = getattr(args, "progress", DEFAULT_PROGRESS)
    if args.command == "list":
        return _cmd_list(args, catalog)
    if args.command == "stats":
        return _cmd_stats(args, catalog, progress)
    if args.command == "solve":
        return _cmd_solve(args, catalog, progress)
    if args.command == "unsolve":
        return _cmd_unsolve(args, catalog, progress)
    return _cmd_next(args, catalog, progress)
