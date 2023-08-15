from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for num in range(len(nums)):
            heapq.heappush(pq, nums[num])
            if len(pq) > k:
                heapq.heappop(pq)

        return pq[0]


sol = Solution()
print(sol.findKthLargest([3, 2, 1, 5, 6, 4], 2))
