class Solution:
    def pivotInteger(self, n: int) -> int:
        lst = []
        for i in range(1, n + 1):
            lst.append(i)
        for i in range(len(lst)):
            if sum(lst[:i]) == sum(lst[i + 1:]):
                return lst[i]
        return -1


solution = Solution()
n = 8
print(solution.pivotInteger(n))
