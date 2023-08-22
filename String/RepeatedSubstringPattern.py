class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        temp = s + s
        str1 = temp[1:len(temp) - 1]
        if s in str1:
            return True
        else:
            return False


sol = Solution()
print(sol.repeatedSubstringPattern("abacb"))
