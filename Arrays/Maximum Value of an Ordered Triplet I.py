from typing import List


@staticmethod
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        N = len(nums)

        prefix = [0] * N
        mx = 0

        for i in range(N):
            mx = max(mx, nums[i])
            prefix[i] = mx

        suffix = [0] * N
        mx = 0

        for i in range(N - 1, -1, -1):
            mx = max(mx, nums[i])
            suffix[i] = mx

        for i in range(1, N - 1):
            cand = (prefix[i - 1] - nums[i]) * suffix[i + 1]
            ans = max(ans, cand)

        return ans


sol = Solution()
print(sol.maximumTripletValue([12, 6, 1, 2, 7]))
