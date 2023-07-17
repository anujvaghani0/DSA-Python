from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        max_length = 1

        for num in arr:
            if num - difference in dp:
                dp[num] = dp[num - difference] + 1
            else:
                dp[num] = 1

            max_length = max(max_length, dp[num])

        return max_length
        # length = len(arr)
        # dp = [[0] * length for _ in range(length)]
        # max_length = 1
        #
        # for i in range(length):
        #     dp[i][i] = 1
        #     start = arr[i]
        #
        #     for j in range(i + 1, length):
        #         if arr[j] == start + difference:
        #             dp[i][j] = dp[i][j - 1] + 1
        #             start = arr[j]
        #         else:
        #             dp[i][j] = dp[i][j - 1]
        #
        #     max_length = max(max_length, dp[i][length - 1])
        #
        # return max_length



sol = Solution()
print(sol.longestSubsequence([1, 2, 3, 4], 1))
