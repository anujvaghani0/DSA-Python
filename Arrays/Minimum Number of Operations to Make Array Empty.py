from typing import List
import math
from collections import defaultdict


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        hashmap = {}

        for i in range(len(nums)):
            temp = nums[i]
            if temp in hashmap:
                hashmap[temp] += 1
            else:
                hashmap[temp] = 1
        count = 0
        m = defaultdict(int)
        n = len(nums)

        for key, count in hashmap.items():
            if count == 1:
                return -1
            count += math.ceil(count / 3.0)

        return count


sol = Solution()
print(sol.minOperations([19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19]))
