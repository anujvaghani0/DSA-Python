class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        s = sum([ord(_) for _ in s1]) + sum([ord(_) for _ in s2])
        n1, n2 = len(s1), len(s2)
        dp = [[0 for _ in range(n1 + 1)] for _ in range(n2 + 1)]
        maximumscore = 0
        for i in range(1, n2 + 1):
            for j in range(1, n1 + 1):
                if s2[i - 1] == s1[j - 1]:
                    dp[i][j] = max(dp[i - 1][j - 1] + ord(s1[j - 1]), dp[i - 1][j], dp[i][j - 1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                maximumscore = max(maximumscore, dp[i][j])
        print(dp, s)
        return s - maximumscore * 2


sol = Solution()
print(sol.minimumDeleteSum('sea', 'eat'))
