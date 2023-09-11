from typing import List


class Solution:
    @staticmethod
    def findNumberOfLIS(nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        count = [1] * n
        maxLen = 1
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    count[i] = count[j]
                elif dp[j] + 1 == dp[i]:
                    count[i] += count[j]
            maxLen = max(maxLen, dp[i])
        ans = 0
        for i in range(n):
            if dp[i] == maxLen:
                ans += count[i]
        return ans

sol = Solution()
print(sol.findNumberOfLIS([1, 3, 5, 4, 7]))

