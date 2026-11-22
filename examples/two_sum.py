"""Two Sum: find indices of two values that add up to a target."""


def two_sum(nums: list[int], target: int) -> list[int]:
    """Approach: one pass with a value -> index hash map.

    Time O(n), space O(n). Returns an empty list if no pair exists.
    """
    seen: dict[int, int] = {}
    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], index]
        seen[value] = index
    return []
