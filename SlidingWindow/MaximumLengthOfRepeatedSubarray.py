from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        strnum2 = "".join([chr(x) for x in nums2])
        strmax = ''
        ans = 0
        for num in nums1:
            strmax += chr(num)
            if strmax in strnum2:
                ans = max(ans, len(strmax))
            else:
                strmax = strmax[1:]

        return ans


sol = Solution()
print(sol.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))

