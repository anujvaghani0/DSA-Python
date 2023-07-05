from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_length = 0  # variable to store the maximum length of subarray
        count = 0  # variable to count the number of 1's in the current subarray
        prev_count = 0  # variable to store the count of previous subarray
        has_zero = False  # flag to indicate if a zero has been encountered

        for num in nums:
            if num == 1:
                count += 1
                prev_count += 1
            else:
                has_zero = True
                max_length = max(max_length, prev_count)  # update max_length
                prev_count = count
                count = 0

        # If the array ends with 1 and there is no zero encountered
        if not has_zero:
            return count - 1

        # If the array ends with 1 and there is a zero encountered
        return max(max_length, prev_count)


solution = Solution()
nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
print(solution.longestSubarray(nums))
