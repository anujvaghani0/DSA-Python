from collections import defaultdict
from typing import List  # Import the List module


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = defaultdict(dict)
        n = len(nums)
        ans = 1

        for i in range(n):
            for j in range(i):
                difference = nums[i] - nums[j]
                dp[i][difference] = dp[j].get(difference, 1) + 1
                ans = max(ans, dp[i][difference])

        return ans


# Example usage:
solution = Solution()
nums = [9, 4, 7, 2, 10]  # Arithmetic subsequence: [4, 7, 10]
print(solution.longestArithSeqLength(nums))  # Output: 3
