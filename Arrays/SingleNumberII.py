from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums)) // 2


solution = Solution()
nums = [2, 2, 3, 2]
print(solution.singleNumber(nums))
