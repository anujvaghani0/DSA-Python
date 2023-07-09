from typing import List


class Solution:
    @staticmethod
    def longestOnes(nums: List[int], k: int) -> int:
        ones = 0
        ans = 0
        left = 0
        for right in range(len(nums)):
            ones += nums[right]
            if right - left + 1 - ones > k:
                ones -= nums[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans


# sol = Solution()
print(Solution.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
