# algodrill

A tiny command-line tracker for a self-directed algorithms practice plan.
It ships a deterministic checklist of 180 canonical problems, local JSON
progress tracking, and 10 short teaching examples. No network, no accounts,
no external dependencies.

## Honesty note

- The catalog is a **curated practice checklist**, not scraped content and not
  a claim about what the author has solved. It contains stable slugs and
  English titles only — **no numeric problem IDs**.
- The `examples/` files are **teaching demos** written to illustrate an
  approach and its complexity. They are **not** the author's own submissions.
- The project scaffolding was **AI-assisted in November 2026**.
- **No claim** is made that any of these problems were solved by the author.
  Progress starts at zero and is recorded only when *you* run `solve`.
- There is no LeetCode branding, logo, or copied problem statement.

## Requirements

Python 3.10 or newer. Standard library only at runtime.

## Install

From the project root:

```bash
python -m pip install -e ".[dev]"
```

Offline without build isolation (uses the already-installed setuptools):

```bash
python -m pip install -e ".[dev]" --no-build-isolation
```

After installation, `python -m algodrill ...` works. An `algodrill` console
script is also installed (add your Python `Scripts/` directory to `PATH` if it
is not already there). Without installing, run from the project root with
`PYTHONPATH=src python -m algodrill ...`.

## Usage

```bash
python -m algodrill list --limit 3
python -m algodrill list --category tree --difficulty easy --limit 5
python -m algodrill stats
python -m algodrill next
python -m algodrill solve two-sum
python -m algodrill unsolve two-sum
python -m algodrill --progress ./my-progress.json stats
```

`--progress` is accepted before or after the subcommand and defaults to
`.algodrill-progress.json` in the current directory. A missing or corrupt file
is treated as empty progress.

### Real CLI output (captured from a run)

`python -m algodrill list --limit 3`

```text
Catalog: 180 problems, showing 3
------------------------------------------------------------------------------
two-sum                                Easy    Two Sum [Array & String / hash-map]
best-time-to-buy-and-sell-stock        Easy    Best Time to Buy and Sell Stock [Array & String / one-pass]
contains-duplicate                     Easy    Contains Duplicate [Array & String / hash-set]
```

`python -m algodrill stats`

```text
Progress: 0/180 solved (0.0%)

By difficulty:
  Easy       0/62
  Medium     0/100
  Hard       0/18

By category:
  Array & String                   0/18
  Binary Search & Sorting          0/18
  Dynamic Programming              0/18
  Graph                            0/18
  Hash Map & Set                   0/18
  Linked List                      0/18
  Math & Bit Manipulation          0/18
  Stack & Queue                    0/18
  Tree                             0/18
  Two Pointers & Sliding Window    0/18
```

`python -m algodrill next`

```text
Next up: Two Sum
  slug:       two-sum
  category:   Array & String
  difficulty: Easy
  pattern:    hash-map
```

`python -m algodrill solve two-sum --progress <temp-file>` followed by
`python -m algodrill stats --progress <temp-file>`

```text
Marked solved: two-sum - Two Sum
Progress: 1/180 solved (0.6%)

By difficulty:
  Easy       1/62
  Medium     0/100
  Hard       0/18

By category:
  Array & String                   1/18
  Binary Search & Sorting          0/18
  Dynamic Programming              0/18
  Graph                            0/18
  Hash Map & Set                   0/18
  Linked List                      0/18
  Math & Bit Manipulation          0/18
  Stack & Queue                    0/18
  Tree                             0/18
  Two Pointers & Sliding Window    0/18
```

## Project layout

```text
algo-drill/
├── src/algodrill/
│   ├── __init__.py       public imports
│   ├── __main__.py       python -m algodrill
│   ├── catalog.py        180 deterministic Problem entries
│   ├── cli.py            argparse commands
│   └── tracker.py        JSON-backed progress store
├── examples/             10 worked teaching functions
│   ├── two_sum.py
│   ├── valid_parentheses.py
│   ├── reverse_linked_list.py
│   ├── max_depth_tree.py
│   ├── climb_stairs.py
│   ├── merge_intervals.py
│   ├── binary_search.py
│   ├── longest_substring.py
│   ├── course_schedule.py
│   └── coin_change.py
├── tests/                pytest suite
├── .github/workflows/ci.yml
├── pyproject.toml
├── LICENSE
└── .gitignore
```

## Development

```bash
python -m ruff check .
python -m ruff format --check .
python -m pytest
python -m coverage run -m pytest
python -m coverage report
python -m build --no-isolation --outdir dist
```

CI runs lint, format check, tests and coverage on Python 3.10–3.13.

## License

MIT — Copyright (c) 2026 Gary7702.
