from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        visited = [[0] * m for _ in range(n)]
        distance = [[0] * m for _ in range(n)]

        qu = deque()

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    qu.append((i, j, 0))
                    visited[i][j] = 1

        drow = [-1, 1, 0, 0]
        dcol = [0, 0, -1, 1]

        while qu:
            nrow, ncol, step = qu.popleft()
            distance[nrow][ncol] = step
            for i in range(4):
                row = nrow + drow[i]
                col = ncol + dcol[i]

                if m > col >= 0 == visited[row][col] and 0 <= row < n:
                    visited[row][col] = 1
                    qu.append((row, col, step + 1))

        return distance


sol = Solution()
print(sol.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
