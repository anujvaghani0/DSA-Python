from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        curr_sum, max_len = 0, 0
        i = 0
        found = False
        for j in range(len(nums)):
            curr_sum += nums[j]
            while i <= j and curr_sum > target:
                curr_sum -= nums[i]
                i += 1
            if curr_sum == target:
                found = True
                max_len = max(max_len, j - i + 1)

        return len(nums) - max_len if found else -1


sol = Solution()
# print(sol.minOperations([5,6,7,8,9], 4))
print(sol.minOperations([1, 1, 4, 2, 3], 5))