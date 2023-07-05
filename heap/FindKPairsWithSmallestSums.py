import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        pq = []

        for x in nums1:
            heapq.heappush(pq, [x + nums2[0], 0])

        while k > 0 and pq:
            pair = heapq.heappop(pq)
            s, pos = pair[0], pair[1]  # Get the smallest sum and the index of the second element in nums2

            ans.append([s - nums2[pos], nums2[pos]])  # Add the pair to the result list

            # If there are more elements in nums2, push the next pair into the priority queue
            if pos + 1 < len(nums2):
                heapq.heappush(pq, [s - nums2[pos] + nums2[pos + 1], pos + 1])

            k -= 1  # Decrement k

        return ans  # Return the k smallest pairs


solution = Solution()
nums1 = [1, 7, 11]
nums2 = [2, 4, 6]
k = 3

print(solution.kSmallestPairs(nums1, nums2, k))
