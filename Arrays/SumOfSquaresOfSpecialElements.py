from typing import List
import math


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):
            if n % i == 0:
                ans += int(math.pow(nums[i - 1], 2))
        return ans


sol = Solution()
print(sol.sumOfSquares([2, 7, 1, 19, 18, 3]))
