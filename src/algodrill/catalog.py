"""Deterministic catalog of canonical algorithm practice problems.

The entries are a curated practice checklist: stable slugs and English titles
only. No numeric problem IDs or scraped content are included.
"""

from __future__ import annotations

from dataclasses import dataclass

DIFFICULTIES = ("Easy", "Medium", "Hard")


@dataclass(frozen=True, slots=True)
class Problem:
    """One practice problem in the catalog."""

    slug: str
    title: str
    category: str
    difficulty: str
    pattern: str


# Each group holds (slug, title, difficulty, pattern) tuples.
_RAW: dict[str, tuple[tuple[str, str, str, str], ...]] = {
    "Array & String": (
        ("two-sum", "Two Sum", "Easy", "hash-map"),
        ("best-time-to-buy-and-sell-stock", "Best Time to Buy and Sell Stock", "Easy", "one-pass"),
        ("contains-duplicate", "Contains Duplicate", "Easy", "hash-set"),
        ("missing-number", "Missing Number", "Easy", "math"),
        ("single-number", "Single Number", "Easy", "bit-manipulation"),
        ("plus-one", "Plus One", "Easy", "array"),
        ("remove-element", "Remove Element", "Easy", "two-pointers"),
        ("merge-sorted-array", "Merge Sorted Array", "Easy", "two-pointers"),
        ("majority-element", "Majority Element", "Easy", "boyer-moore"),
        ("rotate-array", "Rotate Array", "Medium", "reversal"),
        ("set-matrix-zeroes", "Set Matrix Zeroes", "Medium", "in-place"),
        ("product-except-self", "Product of Array Except Self", "Medium", "prefix-sum"),
        ("longest-consecutive-sequence", "Longest Consecutive Sequence", "Medium", "hash-set"),
        ("valid-sudoku", "Valid Sudoku", "Medium", "hash-set"),
        ("spiral-matrix", "Spiral Matrix", "Medium", "simulation"),
        ("sum-of-two-integers", "Sum of Two Integers", "Medium", "bit-manipulation"),
        ("trapping-rain-water", "Trapping Rain Water", "Hard", "two-pointers"),
        ("first-missing-positive", "First Missing Positive", "Hard", "in-place"),
    ),
    "Hash Map & Set": (
        ("group-anagrams", "Group Anagrams", "Medium", "hash-map"),
        ("isomorphic-strings", "Isomorphic Strings", "Easy", "hash-map"),
        ("word-pattern", "Word Pattern", "Easy", "hash-map"),
        ("valid-anagram", "Valid Anagram", "Easy", "frequency-count"),
        ("intersection-of-two-arrays", "Intersection of Two Arrays", "Easy", "hash-set"),
        (
            "intersection-of-two-arrays-ii",
            "Intersection of Two Arrays II",
            "Easy",
            "frequency-count",
        ),
        ("top-k-frequent-elements", "Top K Frequent Elements", "Medium", "heap"),
        ("longest-harmonious-subsequence", "Longest Harmonious Subsequence", "Easy", "hash-map"),
        ("find-all-anagrams", "Find All Anagrams in a String", "Medium", "sliding-window"),
        ("subarray-sum-equals-k", "Subarray Sum Equals K", "Medium", "prefix-sum"),
        ("contiguous-array", "Contiguous Array", "Medium", "prefix-sum"),
        ("fraction-to-recurring-decimal", "Fraction to Recurring Decimal", "Medium", "hash-map"),
        ("lucky-number-in-a-matrix", "Lucky Numbers in a Matrix", "Easy", "hash-set"),
        ("word-subsets", "Word Subsets", "Medium", "frequency-count"),
        ("longest-arithmetic-subsequence", "Longest Arithmetic Subsequence", "Medium", "dp"),
        ("largest-difference", "Largest Difference Between Consecutive Digits", "Easy", "math"),
        ("array-with-duplicates", "Array With Duplicates", "Easy", "frequency-count"),
        ("count-pairs-with-equal-sum", "Count Pairs With Equal Sum", "Medium", "hash-map"),
    ),
    "Two Pointers & Sliding Window": (
        (
            "longest-substring-without-repeating",
            "Longest Substring Without Repeating Characters",
            "Medium",
            "sliding-window",
        ),
        (
            "longest-repeating-char-replacement",
            "Longest Repeating Character Replacement",
            "Medium",
            "sliding-window",
        ),
        ("minimum-window-substring", "Minimum Window Substring", "Hard", "sliding-window"),
        (
            "longest-substring-k-repeating",
            "Longest Substring with At Least K Repeating Characters",
            "Medium",
            "divide-and-conquer",
        ),
        (
            "longest-subarray-abs-diff",
            "Longest Continuous Subarray with Absolute Diff <= k",
            "Medium",
            "sliding-window",
        ),
        ("longest-nice-substring", "Longest Nice Substring", "Easy", "divide-and-conquer"),
        ("two-sum-ii-sorted", "Two Sum II - Input Array Is Sorted", "Medium", "two-pointers"),
        ("3sum", "3Sum", "Medium", "two-pointers"),
        ("3sum-closest", "3Sum Closest", "Medium", "two-pointers"),
        ("4sum", "4Sum", "Medium", "two-pointers"),
        ("container-with-most-water", "Container With Most Water", "Medium", "two-pointers"),
        ("valid-palindrome", "Valid Palindrome", "Easy", "two-pointers"),
        ("palindrome-number", "Palindrome Number", "Easy", "math"),
        ("reverse-string", "Reverse String", "Easy", "two-pointers"),
        ("reverse-vowels", "Reverse Vowels of a String", "Easy", "two-pointers"),
        ("string-compression", "String Compression", "Medium", "two-pointers"),
        ("is-subsequence", "Is Subsequence", "Easy", "two-pointers"),
        ("sort-colors", "Sort Colors", "Medium", "dutch-flag"),
    ),
    "Linked List": (
        ("reverse-linked-list", "Reverse Linked List", "Easy", "pointer-manipulation"),
        ("merge-two-sorted-lists", "Merge Two Sorted Lists", "Easy", "two-pointers"),
        ("linked-list-cycle", "Linked List Cycle", "Easy", "fast-slow-pointers"),
        ("linked-list-cycle-ii", "Linked List Cycle II", "Medium", "fast-slow-pointers"),
        ("middle-of-linked-list", "Middle of the Linked List", "Easy", "fast-slow-pointers"),
        (
            "remove-nth-node-from-end",
            "Remove Nth Node From End of List",
            "Medium",
            "fast-slow-pointers",
        ),
        ("add-two-numbers", "Add Two Numbers", "Medium", "math"),
        (
            "intersection-of-two-linked-lists",
            "Intersection of Two Linked Lists",
            "Easy",
            "two-pointers",
        ),
        ("palindrome-linked-list", "Palindrome Linked List", "Easy", "fast-slow-pointers"),
        (
            "delete-node-in-linked-list",
            "Delete Node in a Linked List",
            "Easy",
            "pointer-manipulation",
        ),
        ("swap-nodes-in-pairs", "Swap Nodes in Pairs", "Medium", "pointer-manipulation"),
        ("rotate-list", "Rotate List", "Medium", "pointer-manipulation"),
        ("reverse-nodes-in-k-group", "Reverse Nodes in k-Group", "Hard", "pointer-manipulation"),
        ("merge-k-sorted-lists", "Merge k Sorted Lists", "Hard", "heap"),
        ("reorder-list", "Reorder List", "Medium", "fast-slow-pointers"),
        (
            "remove-linked-list-elements",
            "Remove Linked List Elements",
            "Easy",
            "pointer-manipulation",
        ),
        ("odd-even-linked-list", "Odd Even Linked List", "Medium", "pointer-manipulation"),
        ("copy-list-with-random-pointer", "Copy List with Random Pointer", "Medium", "hash-map"),
    ),
    "Stack & Queue": (
        ("valid-parentheses", "Valid Parentheses", "Easy", "stack"),
        ("min-stack", "Min Stack", "Easy", "stack"),
        ("implement-stack-using-queues", "Implement Stack using Queues", "Easy", "queue"),
        ("implement-queue-using-stacks", "Implement Queue using Stacks", "Easy", "stack"),
        ("evaluate-reverse-polish-notation", "Evaluate Reverse Polish Notation", "Medium", "stack"),
        ("basic-calculator", "Basic Calculator", "Hard", "stack"),
        ("basic-calculator-ii", "Basic Calculator II", "Medium", "stack"),
        ("longest-valid-parentheses", "Longest Valid Parentheses", "Hard", "stack"),
        ("remove-invalid-parentheses", "Remove Invalid Parentheses", "Hard", "bfs"),
        ("daily-temperatures", "Daily Temperatures", "Medium", "monotonic-stack"),
        ("next-greater-element-i", "Next Greater Element I", "Easy", "monotonic-stack"),
        ("next-greater-element-ii", "Next Greater Element II", "Medium", "monotonic-stack"),
        (
            "largest-rectangle-in-histogram",
            "Largest Rectangle in Histogram",
            "Hard",
            "monotonic-stack",
        ),
        ("sliding-window-maximum", "Sliding Window Maximum", "Hard", "monotonic-deque"),
        ("design-circular-queue", "Design Circular Queue", "Medium", "queue"),
        ("moving-average-from-data-stream", "Moving Average from Data Stream", "Easy", "queue"),
        ("validate-stack-sequences", "Validate Stack Sequences", "Medium", "stack"),
        ("sum-of-subarray-minimums", "Sum of Subarray Minimums", "Medium", "monotonic-stack"),
    ),
    "Tree": (
        ("maximum-depth-of-binary-tree", "Maximum Depth of Binary Tree", "Easy", "dfs"),
        ("invert-binary-tree", "Invert Binary Tree", "Easy", "dfs"),
        ("symmetric-tree", "Symmetric Tree", "Easy", "dfs"),
        ("binary-tree-level-order", "Binary Tree Level Order Traversal", "Medium", "bfs"),
        (
            "binary-tree-zigzag-level-order",
            "Binary Tree Zigzag Level Order Traversal",
            "Medium",
            "bfs",
        ),
        ("validate-binary-search-tree", "Validate Binary Search Tree", "Medium", "dfs"),
        ("binary-search-tree-iterator", "Binary Search Tree Iterator", "Medium", "stack"),
        ("kth-smallest-in-bst", "Kth Smallest Element in a BST", "Medium", "dfs"),
        ("lowest-common-ancestor", "Lowest Common Ancestor of a Binary Tree", "Medium", "dfs"),
        ("binary-tree-maximum-path-sum", "Binary Tree Maximum Path Sum", "Hard", "dfs"),
        (
            "construct-tree-preorder-inorder",
            "Construct Binary Tree from Preorder and Inorder Traversal",
            "Medium",
            "dfs",
        ),
        ("path-sum", "Path Sum", "Easy", "dfs"),
        ("path-sum-ii", "Path Sum II", "Medium", "dfs"),
        ("sum-root-to-leaf-numbers", "Sum Root to Leaf Numbers", "Medium", "dfs"),
        ("count-complete-tree-nodes", "Count Complete Tree Nodes", "Medium", "binary-search"),
        ("diameter-of-binary-tree", "Diameter of Binary Tree", "Medium", "dfs"),
        (
            "serialize-deserialize-binary-tree",
            "Serialize and Deserialize Binary Tree",
            "Hard",
            "bfs",
        ),
        ("balanced-binary-tree", "Balanced Binary Tree", "Easy", "dfs"),
    ),
    "Graph": (
        ("number-of-islands", "Number of Islands", "Medium", "dfs"),
        ("max-area-of-island", "Max Area of Island", "Medium", "dfs"),
        ("course-schedule", "Course Schedule", "Medium", "bfs"),
        ("course-schedule-ii", "Course Schedule II", "Medium", "dfs"),
        ("clone-graph", "Clone Graph", "Medium", "bfs"),
        ("pacific-atlantic-water-flow", "Pacific Atlantic Water Flow", "Medium", "dfs"),
        ("surrounded-regions", "Surrounded Regions", "Medium", "dfs"),
        (
            "number-of-connected-components",
            "Number of Connected Components",
            "Medium",
            "union-find",
        ),
        ("graph-valid-tree", "Graph Valid Tree", "Medium", "union-find"),
        ("redundant-connection", "Redundant Connection", "Medium", "union-find"),
        ("word-ladder", "Word Ladder", "Hard", "bfs"),
        ("word-ladder-ii", "Word Ladder II", "Hard", "bfs"),
        ("shortest-path-binary-matrix", "Shortest Path in Binary Matrix", "Medium", "bfs"),
        ("rotate-image", "Rotate Image", "Medium", "in-place"),
        ("walls-and-gates", "Walls and Gates", "Medium", "bfs"),
        ("all-paths-source-to-target", "All Paths From Source to Target", "Medium", "dfs"),
        (
            "cheapest-flights-within-k-stops",
            "Cheapest Flights Within K Stops",
            "Medium",
            "bellman-ford",
        ),
        ("network-delay-time", "Network Delay Time", "Medium", "dijkstra"),
    ),
    "Dynamic Programming": (
        ("climb-stairs", "Climb Stairs", "Easy", "dp"),
        ("min-cost-climbing-stairs", "Min Cost Climbing Stairs", "Easy", "dp"),
        ("house-robber", "House Robber", "Medium", "dp"),
        ("house-robber-ii", "House Robber II", "Medium", "dp"),
        ("longest-increasing-subsequence", "Longest Increasing Subsequence", "Medium", "dp"),
        ("longest-common-subsequence", "Longest Common Subsequence", "Medium", "dp"),
        ("longest-common-substring", "Longest Common Substring", "Medium", "dp"),
        ("coin-change", "Coin Change", "Medium", "dp"),
        ("coin-change-ii", "Coin Change II", "Medium", "dp"),
        ("word-break", "Word Break", "Medium", "dp"),
        ("word-break-ii", "Word Break II", "Hard", "dp"),
        ("unique-paths", "Unique Paths", "Medium", "dp"),
        ("unique-paths-ii", "Unique Paths II", "Medium", "dp"),
        ("minimum-path-sum", "Minimum Path Sum", "Medium", "dp"),
        ("edit-distance", "Edit Distance", "Medium", "dp"),
        ("palindrome-partitioning-ii", "Palindrome Partitioning II", "Hard", "dp"),
        ("maximum-subarray", "Maximum Subarray", "Medium", "kadane"),
        ("best-time-buy-sell-stock-iii", "Best Time to Buy and Sell Stock III", "Hard", "dp"),
    ),
    "Binary Search & Sorting": (
        ("binary-search", "Binary Search", "Easy", "binary-search"),
        ("search-insert-position", "Search Insert Position", "Easy", "binary-search"),
        ("first-bad-version", "First Bad Version", "Easy", "binary-search"),
        ("guess-number-higher-or-lower", "Guess Number Higher or Lower", "Easy", "binary-search"),
        (
            "find-first-and-last-position",
            "Find First and Last Position of Element in Sorted Array",
            "Medium",
            "binary-search",
        ),
        ("search-a-2d-matrix", "Search a 2D Matrix", "Medium", "binary-search"),
        (
            "search-in-rotated-sorted-array",
            "Search in Rotated Sorted Array",
            "Medium",
            "binary-search",
        ),
        (
            "find-minimum-rotated-sorted-array",
            "Find Minimum in Rotated Sorted Array",
            "Medium",
            "binary-search",
        ),
        (
            "peak-index-in-a-mountain-array",
            "Peak Index in a Mountain Array",
            "Easy",
            "binary-search",
        ),
        ("kth-largest-element", "Kth Largest Element in an Array", "Medium", "quickselect"),
        ("sort-an-array", "Sort an Array", "Medium", "merge-sort"),
        ("merge-intervals", "Merge Intervals", "Medium", "sorting"),
        ("insert-interval", "Insert Interval", "Medium", "sorting"),
        ("non-overlapping-intervals", "Non-overlapping Intervals", "Medium", "greedy"),
        ("meeting-rooms", "Meeting Rooms", "Easy", "sorting"),
        ("meeting-rooms-ii", "Meeting Rooms II", "Medium", "heap"),
        ("find-peak-element", "Find Peak Element", "Medium", "binary-search"),
        ("median-of-two-sorted-arrays", "Median of Two Sorted Arrays", "Hard", "binary-search"),
    ),
    "Math & Bit Manipulation": (
        ("reverse-integer", "Reverse Integer", "Medium", "math"),
        ("integer-to-roman", "Integer to Roman", "Medium", "simulation"),
        ("roman-to-integer", "Roman to Integer", "Easy", "simulation"),
        ("power-of-two", "Power of Two", "Easy", "bit-manipulation"),
        ("power-of-three", "Power of Three", "Easy", "math"),
        ("power-of-four", "Power of Four", "Easy", "bit-manipulation"),
        ("factorial-trailing-zeroes", "Factorial Trailing Zeroes", "Medium", "math"),
        ("sqrt-x", "Sqrt(x)", "Easy", "binary-search"),
        ("superpow", "Super Pow", "Medium", "math"),
        ("single-number-ii", "Single Number II", "Medium", "bit-manipulation"),
        ("single-number-iii", "Single Number III", "Medium", "bit-manipulation"),
        (
            "bitwise-and-of-numbers-range",
            "Bitwise AND of Numbers Range",
            "Medium",
            "bit-manipulation",
        ),
        ("number-of-1-bits", "Number of 1 Bits", "Easy", "bit-manipulation"),
        ("counting-bits", "Counting Bits", "Easy", "dp"),
        ("reverse-bits", "Reverse Bits", "Easy", "bit-manipulation"),
        ("maximum-product-of-three-numbers", "Maximum Product of Three Numbers", "Easy", "sorting"),
        ("ugly-number", "Ugly Number", "Easy", "math"),
        ("happy-number", "Happy Number", "Easy", "hash-set"),
    ),
}


def _build() -> tuple[Problem, ...]:
    problems: list[Problem] = []
    for category, entries in _RAW.items():
        for slug, title, difficulty, pattern in entries:
            problems.append(Problem(slug, title, category, difficulty, pattern))
    return tuple(problems)


_CATALOG: tuple[Problem, ...] = _build()


def load_catalog() -> tuple[Problem, ...]:
    """Return the immutable catalog in a stable, deterministic order."""
    return _CATALOG


def categories() -> tuple[str, ...]:
    """Return category names in catalog order."""
    return tuple(dict.fromkeys(p.category for p in _CATALOG))


def filter_catalog(
    problems: tuple[Problem, ...] | list[Problem] | None = None,
    *,
    category: str | None = None,
    difficulty: str | None = None,
    pattern: str | None = None,
    limit: int | None = None,
) -> tuple[Problem, ...]:
    """Filter problems by category, difficulty and/or pattern, then apply a limit.

    String filters are case-insensitive. A ``limit`` of 0 or less yields an
    empty tuple; ``None`` means no limit.
    """
    source = load_catalog() if problems is None else problems
    selected = tuple(
        p
        for p in source
        if (category is None or p.category.casefold() == category.casefold())
        and (difficulty is None or p.difficulty.casefold() == difficulty.casefold())
        and (pattern is None or p.pattern.casefold() == pattern.casefold())
    )
    if limit is None:
        return selected
    if limit <= 0:
        return ()
    return selected[:limit]
