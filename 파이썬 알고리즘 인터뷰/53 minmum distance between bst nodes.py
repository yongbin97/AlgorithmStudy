# Definition for a binary tree node.
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    min_value = sys.maxsize

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            l_min = r_max = node.val

            if node.left is not None:
                l_min, l_max = dfs(node.left)
                self.min_value = min(self.min_value, abs(node.val - l_max))

            if node.right is not None:
                r_min, r_max = dfs(node.right)
                self.min_value = min(self.min_value, abs(r_min-node.val))

            return l_min, r_max

        dfs(root)
        return self.min_value
