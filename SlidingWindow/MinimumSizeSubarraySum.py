from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        ans = float('inf')
        i, sum = 0, 0
        for j in range(len(nums)):
            sum += nums[j]
            while sum >= target:
                ans = min(ans, j - i + 1)
                sum -= nums[i]
                i += 1
        return ans if ans <= len(nums) else 0


sol = Solution()
print(sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
