class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        ans = ""
        n = len(s)
        difference = 2 * (numRows - 1)
        second_index = 0
        index = 0
        for i in range(numRows):
            index = i
            while index < n:
                ans += s[index]
                if i != 0 and i != numRows - 1:
                    diagonal_diff = difference - 2 * i
                    second_index = index + diagonal_diff
                    if second_index < n:
                        ans += s[second_index]
                index += difference
        return ans


solution = Solution()
s = "PAYPALISHIRING"
numRows = 3
print(solution.convert(s, numRows))
