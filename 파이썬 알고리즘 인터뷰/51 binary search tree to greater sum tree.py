# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, node, greater_sum=0):
        if node is None:
            return 0

        if node.right is not None:
            greater_sum = self.dfs(node.right, greater_sum)

        node.val += greater_sum

        if node.left is not None:
            return self.dfs(node.left, node.val)

        return node.val

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.dfs(root)
        return root


class Solution2:
    val: int = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)

        return root
