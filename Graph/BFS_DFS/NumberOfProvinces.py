from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)

        visited = [0] * n
        count = 0

        for i in range(n):
            if not visited[i]:
                self.dfs(i, graph, visited)
                count += 1

        return count

    def dfs(self, node, graph, visited):
        visited[node] = 1
        for i in graph[node]:
            if not visited[i]:
                self.dfs(i, graph, visited)


sol = Solution()
print(sol.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
