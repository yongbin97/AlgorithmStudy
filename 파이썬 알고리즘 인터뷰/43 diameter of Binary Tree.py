# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_length = 0

    def diameterOfBinaryTree_1(self, root: Optional[TreeNode]) -> int:
        def search(node, depth):
            if node.left is None and node.right is None:
                return depth

            left_depth, right_depth = 0, 0
            if node.left is not None:
                left_depth = search(node.left, depth + 1)

            if node.right is not None:
                right_depth = search(node.right, depth + 1)

            return max(left_depth, right_depth)

        if root is None:
            return 0

        left_max_depth = right_max_depth = 0

        if root.left is not None:
            left_max_depth = search(root.left, 1)

        if root.right is not None:
            right_max_depth = search(root.right, 1)

        return left_max_depth + right_max_depth

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(node: TreeNode):
            if node.left is None and node.right is None:
                return 1

            left_depth, right_depth = 0, 0

            if node.left is not None:
                left_depth = dfs(node.left)
            if node.right is not None:
                right_depth = dfs(node.right)

            self.max_length = max(self.max_length, left_depth + right_depth)

            return max(left_depth, right_depth) + 1

        dfs(root)

        return self.max_length
