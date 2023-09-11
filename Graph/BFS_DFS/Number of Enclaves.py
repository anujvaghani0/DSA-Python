from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        nrow = [-1, 0, +1, 0]
        ncol = [0, 1, 0, -1]
        visited = [[0 for _ in range(m)] for _ in range(n)]
        # row top and bottom
        for j in range(m):
            if visited[0][j] == 0 and grid[0][j] == 1:
                self.dfs(0, j, visited, grid, nrow, ncol)

            if visited[n - 1][j] == 0 and grid[n - 1][j] == 1:
                self.dfs(n - 1, j, visited, grid, nrow, ncol)

        # col left and right
        for i in range(n):
            if visited[i][0] == 0 and grid[i][0] == 1:
                self.dfs(i, 0, visited, grid, nrow, ncol)

            if visited[i][m - 1] == 0 and grid[i][m - 1] == 1:
                self.dfs(i, m - 1, visited, grid, nrow, ncol)

        #  count the number of 1s
        count = 0
        for i in range(n):
            for k in range(m):
                if visited[i][k] == 0 and grid[i][k] == 1:
                    count += 1
        return count

    def dfs(self, row, col, visited, board, drow, dcol):
        visited[row][col] = 1
        n = len(board)
        m = len(board[0])

        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if n > nrow >= 0 == visited[nrow][ncol] and 0 <= ncol < m and board[nrow][ncol] == 1:
                self.dfs(nrow, ncol, visited, board, drow, dcol)


sol = Solution()
print(sol.numEnclaves([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
