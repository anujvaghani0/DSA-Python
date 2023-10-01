from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 2:
            return True

        direction = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                if direction == 0:
                    direction = 1
                elif direction == -1:
                    return False
            elif nums[i] < nums[i - 1]:
                if direction == 0:
                    direction = -1
                elif direction == 1:
                    return False

        return True


sol = Solution()
print(sol.isMonotonic([6, 5, 7, 4, 4]))
