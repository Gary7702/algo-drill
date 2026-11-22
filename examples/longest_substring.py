"""Longest Substring Without Repeating Characters."""


def length_of_longest_substring(s: str) -> int:
    """Approach: sliding window with last-seen indices; jump left past a repeat.

    Time O(n), space O(min(n, alphabet)).
    """
    last_seen: dict[str, int] = {}
    best = 0
    left = 0
    for right, char in enumerate(s):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1
        last_seen[char] = right
        best = max(best, right - left + 1)
    return best
