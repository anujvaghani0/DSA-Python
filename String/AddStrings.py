class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = ""
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1

        while i >= 0 or j >= 0:
            n1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            n2 = ord(num2[j]) - ord('0') if j >= 0 else 0

            temp = n1 + n2 + carry
            carry = temp // 10
            ans = str(temp % 10) + ans

            i -= 1
            j -= 1

        if carry:
            ans = str(carry) + ans

        return ans


solution = Solution()
num1 = "999"
num2 = "123"
print(solution.addStrings(num1, num2))