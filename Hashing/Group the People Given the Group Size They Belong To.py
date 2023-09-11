from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        result = []
        for i, size in enumerate(groupSizes):
            if size not in groups:
                groups[size] = []
            groups[size].append(i)

            if len(groups[size]) == size:
                result.append(groups[size])
                groups[size] = []

        return result


sol = Solution()
print(sol.groupThePeople([3, 3, 3, 3, 3, 1, 3]))
