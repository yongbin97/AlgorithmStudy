# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree_1(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(pre_order, in_order):
            if not pre_order:
                return None

            mid = pre_order[0]
            mid_idx = in_order.index(mid)
            left_inorder = in_order[:mid_idx]
            right_inorder = in_order[mid_idx+1:]

            left_preorder = pre_order[1:len(left_inorder)+1]
            right_preorder = pre_order[len(left_inorder)+1:]

            left_node = dfs(left_preorder, left_inorder)
            right_node = dfs(right_preorder, right_inorder)

            return TreeNode(val=mid, left=left_node, right=right_node)

        return dfs(preorder, inorder)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            index = inorder.index(preorder.pop(0))

            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildTree(preorder, inorder[index+1:])

            return node




solution = Solution()
print(solution.buildTree([3,9,20,15,7], [9,3,15,20,7]))


