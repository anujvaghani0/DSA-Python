class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0: return 0
        if n <= 3: return 1
        s, index = [1, 2, 2], 2
        while len(s) < n:
            s += [3 - s[-1]] * s[index]
            index += 1
        return s[:n].count(1)


solution = Solution()
n = 6
print(solution.magicalString(n))
