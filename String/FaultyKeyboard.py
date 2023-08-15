class Solution:
    def finalString(self, s: str) -> str:
        temp = []
        for i in range(len(s)):
            if s[i] == 'i':
                temp.reverse()
            else:
                temp.append(s[i])

        return ''.join(temp)

sol = Solution()
print(sol.finalString("poiinter"))
