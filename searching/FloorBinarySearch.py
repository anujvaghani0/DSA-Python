from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        # if it's find the floor value then return the left index
        # if it's find the ceil value then return the right index
        return left


Solution = Solution()
nums = [-1, 0, 3, 5, 9, 12]
target = 11
print(Solution.search(nums, target))