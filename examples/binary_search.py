"""Binary Search: locate a target in a sorted array."""


def binary_search(nums: list[int], target: int) -> int:
    """Approach: halve the inclusive range until the target is found or it empties.

    Time O(log n), space O(1). Returns -1 when the target is absent.
    """
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
