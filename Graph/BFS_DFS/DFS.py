class Solution:
    def dfsOfGraph(self, V, adj):
        visited = [False] * V
        visited[0] = True
        ans = []
        self.dfs(0, adj, visited, ans)
        return ans

    def dfs(self, node, adj, visited, ans):
        ans.append(node)
        for i in adj[node]:
            if not visited[i]:
                visited[i] = True
                self.dfs(i, adj, visited, ans)


sol = Solution()
# print(sol.dfsOfGraph(4, [[1, 2, 3], [0], [0], [0]]))
print(sol.dfsOfGraph(7, [[1, 2], [0, 3, 4], [0, 5, 6], [1], [1], [2], [2]]))
