from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        target = len(set(nums))
        n = len(nums)
        ans = 0
        for i in range(n):
            unique = set()
            for j in range(i, n):
                unique.add(nums[j])
                if len(unique) == target:
                    ans += n - j
                    break
        return ans


sol = Solution()
print(sol.countCompleteSubarrays([1, 2, 1, 2, 3]))
