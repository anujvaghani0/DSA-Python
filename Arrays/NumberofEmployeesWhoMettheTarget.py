from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for i in range(len(hours)):
            if hours[i] >= target:
                count += 1

        return count


sol = Solution()
print(sol.numberOfEmployeesWhoMetTarget([8, 2, 4, 7, 1], 6))
