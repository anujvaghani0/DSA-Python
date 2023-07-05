from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        maxVal = 0
        for i in strs:
            if i.isdigit():
                maxVal = max(maxVal, int(i))
            else:
                maxVal = max(maxVal, len(i))
        return maxVal


solution = Solution()
strs = ["alic3", "bob", "3", "4", "00000"]
print(solution.maximumValue(strs))
