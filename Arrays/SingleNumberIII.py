from typing import List
from collections import Counter


class Solution:
    @staticmethod
    def singleNumber(nums: List[int]) -> List[int]:
        a = []
        for i, j in Counter(nums).items():
            if j == 1:
                a.append(i)
        return a


solution = Solution()
nums = [1, 2, 1, 3, 2, 5]
print(solution.singleNumber(nums))
