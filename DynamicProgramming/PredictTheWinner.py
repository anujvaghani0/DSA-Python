from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = [[0] * len(nums) for _ in range(len(nums))]
        for s in range(len(nums)):
            for i in range(len(nums) - s):
                j = i + s
                if i == j:
                    dp[i][i] = nums[i]
                else:
                    dp[i][j] = max(nums[j] - dp[i][j - 1], nums[i] - dp[i + 1][j])
        print(dp[0][-1])
        return dp[0][-1] >= 0

    #  second solution using recursion and memoization
    #     n = len(nums)
    #     dp = [[0 for _ in range(n)] for _ in range(n)]
    #     return self.helper(nums, 0, n - 1, dp, 0) >= 0
    #
    # def helper(self, nums, start, end, dp, k):
    #     if start > end:
    #         return 0
    #
    #     if dp[start][end] != -1:
    #         return dp[start][end]
    #
    #     first, last, num = 0, 0, 0
    #     # it's player 1's turn
    #     # player 1 picks the first element
    #     if k % 2 == 0:
    #         first = nums[start] + self.helper(nums, start + 1, end, dp, k + 1)
    #         # player 1 picks the last element
    #         last = nums[end] + self.helper(nums, start, end - 1, dp, k + 1)
    #         ans = max(first, last)
    #     else:
    #         # it's player 2's turn
    #         # player 2 picks the first element
    #         first = -nums[start] + self.helper(nums, start + 1, end, dp, k + 1)
    #         # player 2 picks the last element
    #         last = -nums[end] + self.helper(nums, start, end - 1, dp, k + 1)
    #         ans = min(first, last)
    #
    #     dp[start][end] = ans
    #     return ans


sol = Solution()
print(sol.PredictTheWinner([1, 5, 2]))
