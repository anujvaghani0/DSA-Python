# Definition for a binary tree node.
from typing import List, Optional
from functools import lru_cache


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @lru_cache(None)
        def helper(start, end):
            if start > end:
                return [None]
            if start == end:
                return [TreeNode(start)]

            ans = []

            for i in range(start, end + 1):
                left_trees = helper(start, i - 1)
                right_trees = helper(i + 1, end)
                for l in left_trees:
                    for r in right_trees:
                        ans.append(TreeNode(i, l, r))
            return ans

        return helper(1, n)


sol = Solution()
print(sol.generateTrees(3))
