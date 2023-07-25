from typing import List


class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        even = nums[0] - (x if nums[0] % 2 else 0)
        odd = nums[0] - (0 if nums[0] % 2 else x)

        for i in range(1, len(nums)):
            if nums[i] % 2:
                odd = nums[i] + max(odd, even - x)
            else:
                even = nums[i] + max(even, odd - x)

        return max(odd, even)


sol = Solution()
print(sol.maxScore([2, 3, 6, 1, 9, 2], 5))
