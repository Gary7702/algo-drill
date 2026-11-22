"""Reverse Linked List: iterative pointer reversal."""

from __future__ import annotations


class ListNode:
    """Minimal singly linked list node."""

    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


def reverse(head: ListNode | None) -> ListNode | None:
    """Approach: walk the list with prev/current, redirecting each next link.

    Time O(n), space O(1).
    """
    prev: ListNode | None = None
    current = head
    while current is not None:
        following = current.next
        current.next = prev
        prev = current
        current = following
    return prev
