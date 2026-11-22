"""Climb Stairs: count distinct ways to reach the top."""


def climb_stairs(n: int) -> int:
    """Approach: Fibonacci computed with rolling variables instead of an array.

    Time O(n), space O(1).
    """
    if n <= 0:
        return 0
    one_step_back, two_steps_back = 1, 1
    for _ in range(2, n + 1):
        one_step_back, two_steps_back = one_step_back + two_steps_back, one_step_back
    return one_step_back
