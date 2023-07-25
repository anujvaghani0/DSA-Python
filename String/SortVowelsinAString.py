class Solution:
    def sortVowels(self, s: str) -> str:
        ans = ""
        ans1 = [c for c in s if c not in "aeiouAEIOU"]
        ans2 = sorted([c for c in s if c in "aeiouAEIOU"])

        for i in s:
            if i in ans1:
                ans += i
            else:
                ans += ans2.pop(0)
        return ans


sol = Solution()
print(sol.sortVowels("lEetcOde"))
