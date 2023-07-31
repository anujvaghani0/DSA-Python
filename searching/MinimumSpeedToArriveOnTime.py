from typing import List
import math


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        start = 0
        end = 10000000
        ans = -1
        while start <= end:
            mid = start + (end - start) // 2
            if self.isValid(dist, hour, mid):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans

    def isValid(self, dist, hour, speed):
        if speed == 0:
            return False

        time = 0
        for i in range(len(dist) - 1):
            time += math.ceil(dist[i] * 1.0 / speed)
        time -= math.ceil(dist[-1] * 1.0 / speed)
        time += dist[-1] * 1.0 / speed
        return time <= hour


sol = Solution()
print(sol.minSpeedOnTime([1, 3, 2], 6))
print(5 // 2)
