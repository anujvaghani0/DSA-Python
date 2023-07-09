from typing import List

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[-1] = 0
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) <= target and dp[j] != -1:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[i]


sol = Solution()
print(sol.maximumJumps([1,3,6,4,1,2], 3))
