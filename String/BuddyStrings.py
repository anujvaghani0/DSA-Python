class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(s)
        if s == goal:
            temp = set(s)
            return len(temp) < len(goal)

        i = 0
        j = n - 1

        while i < j and s[i] == goal[i]:
            i += 1

        while i < j and s[j] == goal[j]:
            j -= 1

        if i < j:
            s_list = list(s)
            s_list[i], s_list[j] = s_list[j], s_list[i]
            s = ''.join(s_list)

        return s == goal


solution = Solution()
s = "aab"
goal = "ab"
print(solution.buddyStrings(s, goal))
