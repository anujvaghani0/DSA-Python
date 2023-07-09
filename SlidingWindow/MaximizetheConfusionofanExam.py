
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        return max(self.maxConsecutive(answerKey, k, 'T'), self.maxConsecutive(answerKey, k, 'F'))

    def maxConsecutive(self, string, k, target):
            left = 0
            ans = 0
            count = 0
            for i in range(len(string)):
                if string[i] == target:
                    count += 1
                while count > k:
                    if string[left] == target:
                        count -= 1
                    left += 1
                ans = max(ans, i - left + 1)
            return ans


sol = Solution()
print(sol.maxConsecutiveAnswers("TTFTTFTT", 1))
