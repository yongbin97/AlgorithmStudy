# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def search(node, idx):
            if node.left is None and node.right is None:
                return idx

            left_idx, right_idx = 0, 0
            if node.left is not None:
                left_idx = search(node.left, idx + 1)

            if node.right is not None:
                right_idx = search(node.right, idx + 1)

            return max(left_idx, right_idx)

        if root is None:
            return 0
        return search(root, 1)

    def maxDepth(root: Optional[TreeNode]):
        # 데크를 이용해 root노드를 담아준다.
        q = deque([root])

        # 깊이 초기화
        depth = 0

        while q:
            depth += 1
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

        return depth