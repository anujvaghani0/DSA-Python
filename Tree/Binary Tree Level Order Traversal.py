from typing import List
from collections import deque
from typing import Optional

# construct a binary tree from a list
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self,root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans

        queue = deque([root])
        while queue:
            n = len(queue)
            temp = []
            for i in range(n):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(temp)
        return ans


sol = Solution()
print(sol.levelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
