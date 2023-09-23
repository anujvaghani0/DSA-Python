
class Solution:
    def armstrongNumber(self, n: int) -> bool:
        temp=n
        if n < 0:
            return False
        digits = []
        while n > 0:
            digits.append(n % 10)
            n //= 10
        k = len(digits)
        return sum([digit ** k for digit in digits]) == temp

solution = Solution()
n=int(input("Enter a number: "))
print(solution.armstrongNumber(int(n)))