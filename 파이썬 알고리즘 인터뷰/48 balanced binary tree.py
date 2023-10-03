# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    depth = 0

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.depth = max(self.depth, abs(left-right))

            return max(left, right) + 1

        dfs(root)
        return self.depth < 2
