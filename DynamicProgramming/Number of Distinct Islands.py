from typing import List


class Solution:
    def countDistinctIslands(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[0 for _ in range(m)] for _ in range(n)]
        st = set()
        for i in range(n):
            for j in range(m):
                if visited[i][j] == 0 and grid[i][j] == 1:
                    temp = set()  # Change temp to a set
                    self.dfs(i, j, visited, grid, temp, i, j)
                    st.add(frozenset(temp))  # Use frozenset to store in the set

        return len(st)

    def dfs(self, row, col, visited, grid, temp, i, j):
        visited[row][col] = 1
        temp.add(self.convert(row - i, col - j))
        n = len(grid)
        m = len(grid[0])
        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]

        for k in range(4):
            nrow = row + drow[k]
            ncol = col + dcol[k]
            if 0 <= nrow < n and 0 <= ncol < m and visited[nrow][ncol] == 0 and grid[nrow][ncol] == 1:
                self.dfs(nrow, ncol, visited, grid, temp, i,
                         j)  # Remove the condition "n > nrow >= 0 == visited[nrow][ncol]"

    def convert(self, row, col):
        return str(row) + " " + str(col)  # Add a space between row and col


sol = Solution()
print(sol.countDistinctIslands([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]))
