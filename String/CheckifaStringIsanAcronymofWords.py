from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words) != len(s):
            return False

        for i in range(len(words)):
            if words[i][0] != s[i]:
                return False
        return True


sol = Solution()
print(sol.isAcronym(["alice", "bob", "charlie"], "abc"))
