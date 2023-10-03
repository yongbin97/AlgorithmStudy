# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    range_sum = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root:
            if low <= root.val <= high:
                self.range_sum += root.val

            if low <= root.val:
                self.rangeSumBST(root.left, low, high)
            if high >= root.val:
                self.rangeSumBST(root.right, low, high)

        return self.range_sum
