class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        n = len(coins)
        dp = [amount + 1 for _ in range(amount+1)]
        dp[0] = 0
        for curr in range(1, amount+1):
            for coin in coins:
                if coin <= curr:
                    dp[curr] = min(dp[curr], dp[curr-coin]+1)
        return -1 if dp[amount] > amount else dp[amount]
