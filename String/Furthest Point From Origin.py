
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        countL = 0
        countR = 0
        for i in moves:
            if i == 'L' or i == '_':
                countL += 1
            elif i == 'R':
                countR += 1
        return abs(countL - countR)


sol = Solution()
str = "_R__LL_"
print(sol.furthestDistanceFromOrigin(str))
