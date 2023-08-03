from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        str_ = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = []
        store = []
        if not digits:
            return ans

        self.helper(0, digits, ans, store, str_)
        return ans

    def helper(self, index, digits, ans, store, str_):
        if index == len(digits):
            ans.append("".join(store))
            return

        tempI = int(digits[index])
        tempStr = str_[tempI]
        for i in range(len(tempStr)):
            store.append(tempStr[i])
            self.helper(index + 1, digits, ans, store, str_)
            store.pop()


sol = Solution()
print(sol.letterCombinations("23"))
