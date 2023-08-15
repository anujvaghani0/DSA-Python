from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = end + (start - end) // 2
            if nums[mid] == target or nums[start] == target or nums[end] == target:
                return True
            if target > nums[mid] and target < nums[end]:
                start = mid + 1
                continue
            elif target < nums[mid] and target > nums[start]:
                end = mid - 1
                continue
            start += 1
            end -= 1
        return False


sol = Solution()
print(sol.search([2, 5, 6, 0, 0, 1, 2], 0))
