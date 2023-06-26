class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        meargedString = ""
        for i in range(min(len(word1), len(word2))):
            meargedString += word1[i] + word2[i]
        if len(word1) > len(word2):
            meargedString += word1[len(word2):]
        elif len(word2) > len(word1):
            meargedString += word2[len(word1):]
        return meargedString


solution = Solution()
word1 = "abc"
word2 = "pqr"
print(solution.mergeAlternately(word1, word2))
