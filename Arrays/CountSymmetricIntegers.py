class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high + 1):
            if self.isSymmetric(i):
                count += 1
        return count

    def isSymmetric(self, num: int) -> bool:
        numStr = str(num)
        temp1 = 0
        n = len(numStr)
        if n % 2 != 0:
            return False
        for i in range(n // 2):
            temp1 += int(numStr[i])
        temp2 = 0
        for i in range(n // 2, n):
            temp2 += int(numStr[i])
        if temp1 != temp2:
            return False
        return True


sol = Solution()
print(sol.countSymmetricIntegers(1, 100))
