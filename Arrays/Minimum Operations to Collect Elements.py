from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        # list
        temp = []
        for i in range(1, k + 1):
            temp.append(i)

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in temp:
                temp.remove(nums[i])
            elif len(temp) == 0:
                break
            count += 1
        return count


sol = Solution()
print(sol.minOperations([3, 1, 5, 4, 2], 2))
