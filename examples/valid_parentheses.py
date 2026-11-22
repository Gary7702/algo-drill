"""Valid Parentheses: check that brackets are balanced and correctly nested."""

_PAIRS = {")": "(", "]": "[", "}": "{"}


def is_valid(s: str) -> bool:
    """Approach: push openings on a stack and match closings against the top.

    Time O(n), space O(n).
    """
    stack: list[str] = []
    for char in s:
        if char in _PAIRS:
            if not stack or stack[-1] != _PAIRS[char]:
                return False
            stack.pop()
        elif char in "([{":
            stack.append(char)
    return not stack
