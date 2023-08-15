from typing import List


class Solution:
    # @staticmethod
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        dp = [[0] * (amount + 1) for _ in range(N + 1)]

        for i in range(amount + 1):
            dp[0][i] = 0
        for i in range(N + 1):
            dp[i][0] = 1

        for i in range(1, N + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] <= j:
                    dp[i][j] = dp[i][j - coins[i - 1]] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        # print(dp)
        return dp[N][amount]


sol = Solution()
# print(sol.change(,5, [1, 2, 5]))
print(sol.change(5, [1, 2, 5]))
