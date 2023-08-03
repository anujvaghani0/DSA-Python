from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        list = [i for i in range(1, n + 1)]
        self.backtrack(ans, k, list, [], 0)
        return ans

    def backtrack(self, ans, k, list, temp, param1):
        if len(temp) == k:
            ans.append(temp[:])
            return

        for i in range(param1, len(list)):
            temp.append(list[i])
            self.backtrack(ans, k, list, temp, i + 1)
            temp.pop()


sol = Solution()
print(sol.combine(4, 2))