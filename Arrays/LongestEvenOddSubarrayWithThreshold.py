from typing import List


class Solution:
    def longestAlternatingSubarray(self, n: List[int], threshold: int) -> int:
        res = 0
        cnt = 0
        for l in range(len(n)):
            if n[l] <= threshold:
                if cnt:
                    cnt = 0 if n[l] % 2 == n[l - 1] % 2 else cnt + 1
                if cnt == 0:
                    cnt = 0 if n[l] % 2 == 0 else 1
            else:
                cnt = 0
            res = max(res, cnt)
        return res


solution = Solution()
n = [3, 2, 5, 4]
threshold = 5
print(solution.longestAlternatingSubarray(n, threshold))
