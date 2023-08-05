from typing import List


class Solution:
    @staticmethod
    def wordBreak(s: str, wordDict: List[str]) -> bool:
        words_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words_set:
                    dp[i] = True
                    break
        return dp[n]


sol = Solution()
print(sol.wordBreak("leetcode", ["leet", "code"]))
