from typing import List
from queue import Queue
import math

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = Queue()
        visited = [[0 for i in range(n)] for j in range(m)]
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.put((i, j, 0))
                    visited[i][j] = 2

                if grid[i][j] == 1:
                    fresh += 1

        time = 0
        rows = [-1, 0, 1, 0]
        cols = [0, 1, 0, -1]
        while not queue.empty():
            r, c, t = queue.get()
            time = max(time, t)
            for i in range(4):
                new_row = r + rows[i]
                new_col = c + cols[i]

                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == 1 and visited[new_row][new_col] == 0:
                    queue.put((new_row, new_col, time + 1))
                    visited[new_row][new_col] = 2
                    fresh -= 1

        if fresh != 0:
            return -1

        return time

sol = Solution()
print(sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
