class Solution:
    def searching2DArray(slef, target, nums):
        m = len(nums)
        n = len(nums[0])
        row, col = 0, 0

        while row < m and col < n:
            if target == nums[row][col]:
                return True
            if target > nums[row][n - 1]:
                row += 1
            else:
                col += 1

        return False


solution = Solution()
nums = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
print(solution.searching2DArray(target, nums))
