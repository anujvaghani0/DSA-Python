from typing import List
import heapq


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        total = 0
        i, j = candidates, len(costs) - candidates - 1
        if len(costs) <= 2 * candidates:
            heap = [(x, 0) for x in costs]
        else:
            heap = [(x, 0) for x in costs[:candidates]] + [(x, 1) for x in costs[len(costs) - candidates:]]
        heapq.heapify(heap)

        for _ in range(k):
            cost, direction = heapq.heappop(heap)
            total += cost

            if i <= j:
                if direction:
                    heapq.heappush(heap, (costs[j], 1))
                    j -= 1
                else:
                    heapq.heappush(heap, (costs[i], 0))
                    i += 1

        return total


solution = Solution()
costs = [31, 25, 72, 79, 74, 65, 84, 91, 18, 59, 27, 9, 81, 33, 17, 58]
k = 11
candidates = 2
print(solution.totalCost(costs, k, candidates))
