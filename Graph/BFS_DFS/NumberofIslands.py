from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(grid, i, j)
        return count

    def dfs(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
            return
        grid[i][j] = "0"
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)


sol = Solution()
print(sol.numIslands([["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]))
