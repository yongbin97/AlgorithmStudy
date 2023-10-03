# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node1, node2):
            if node1 is None and node2 is None:
                return None

            if node1 is None:
                node1 = TreeNode()
            if node2 is None:
                node2 = TreeNode()

            left = dfs(node1.left, node2.left)
            right = dfs(node1.right, node2.right)

            return TreeNode(val=node1.val + node2.val, left=left, right=right)

        root = dfs(root1, root2)
        return root