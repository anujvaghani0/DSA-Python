from typing import List
from collections import deque


class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = [False] * V
        for i in range(V):
            if not visited[i]:
                if self.checkOfCycle(i, V, adj, visited):
                    return True
        return False

    def checkOfCycle(self, s: int, V: int, adj: List[List[int]], visited: List[bool]) -> bool:
        visited[s] = True
        queue = deque()
        queue.append((s, -1))
        while queue:
            node, parent = queue.popleft()
            for it in adj[node]:
                if not visited[it]:
                    visited[it] = True
                    queue.append((it, node))
                elif parent != it:
                    return True
        return False


sol = Solution()
V = 5
adj = [[0, 1], [1, 2], [2, 3], [3, 4]]
print(sol.isCycle(V, adj))
