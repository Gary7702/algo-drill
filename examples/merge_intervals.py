"""Merge Intervals: combine overlapping closed intervals."""


def merge(intervals: list[list[int]]) -> list[list[int]]:
    """Approach: sort by start, then extend the last result when ranges overlap.

    Time O(n log n), space O(n) for the returned list.
    """
    if not intervals:
        return []
    ordered = sorted(intervals, key=lambda pair: pair[0])
    merged: list[list[int]] = [list(ordered[0])]
    for start, end in ordered[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
