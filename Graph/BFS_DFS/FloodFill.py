from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] != color:
            self.dfs(image, sr, sc, image[sr][sc], color)
        return image

    def dfs(self, image, row, col, start, color):
        if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] != start:
            return
        image[row][col] = color
        self.dfs(image, row + 1, col, start, color)
        self.dfs(image, row - 1, col, start, color)
        self.dfs(image, row, col + 1, start, color)
        self.dfs(image, row, col - 1, start, color)


sol = Solution()
print(sol.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
