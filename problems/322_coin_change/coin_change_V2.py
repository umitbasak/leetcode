from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # If the coins list is empty or None, it's impossible to form the amount
        if coins is None or len(coins) == 0:
            return -1

        # Initialize the dp array where dp[i] will hold the minimum number of coins to make up amount i.
        # We fill it with a value greater than any possible minimum (amount + 1) to represent infinity.
        dp = [amount + 1] * (amount + 1)
        # Base case: A total amount of 0 requires 0 coins.
        dp[0] = 0

        # Build up the dp table from 1 to amount.
        for i in range(1, amount + 1):
            # Check each coin to see if it can be used to build up the current amount i.
            for coin in coins:
                if coin <= i:
                    # Update dp[i] to be the minimum of its current value or
                    # 1 coin + the minimum number of coins required for (i - coin)
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # If the dp[amount] value is still greater than amount, it means it's impossible to form that amount.
        if dp[amount] == amount + 1:
            return -1

        # Otherwise, return the minimum number of coins required.
        return dp[amount]
