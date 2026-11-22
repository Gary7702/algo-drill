"""Maximum Depth of Binary Tree: recursive depth-first search."""

from __future__ import annotations


class TreeNode:
    """Minimal binary tree node."""

    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode | None) -> int:
    """Approach: depth = 1 + max(depth(left), depth(right)); empty is 0.

    Time O(n), space O(h) for the recursion stack (h = tree height).
    """
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
