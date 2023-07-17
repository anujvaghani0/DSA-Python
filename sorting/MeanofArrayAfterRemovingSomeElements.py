from typing import List
import math


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        five_percent = math.floor(n * 0.05)
        arr = arr[five_percent:n - five_percent]
        return sum(arr) / len(arr)


solution = Solution()
arr = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]
print(solution.trimMean(arr))
