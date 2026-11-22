"""Coin Change: find the fewest coins needed to form an amount."""


def coin_change(coins: list[int], amount: int) -> int:
    """Approach: bottom-up unbounded-knapsack DP over amounts.

    Time O(amount * len(coins)), space O(amount). Returns -1 if unreachable.
    """
    if amount < 0:
        return -1
    unreachable = amount + 1
    dp = [0] + [unreachable] * amount
    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value:
                dp[value] = min(dp[value], dp[value - coin] + 1)
    return dp[amount] if dp[amount] < unreachable else -1
