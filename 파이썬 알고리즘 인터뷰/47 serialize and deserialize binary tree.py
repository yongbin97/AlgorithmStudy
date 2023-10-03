# Definition for a binary tree node.
from collections import deque
from typing import Optional

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root) -> str:
        answer = []
        dq = deque([root])
        while dq:
            node = dq.popleft()

            if node is None:
                answer.append(None)
            else:
                answer.append(node.val)
                dq.append(node.left)
                dq.append(node.right)

        return ' '.join(str(x) for x in answer)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        data_list = deque(None if x == "None" else int(x) for x in data.split())
        root_v = data_list.popleft()
        if root_v is None:
            return None

        root = TreeNode(root_v)
        node_q = deque([root])

        while node_q and data_list:
            node = node_q.popleft()
            left_val = data_list.popleft()
            right_val = data_list.popleft()

            if left_val is not None:
                left_node = TreeNode(left_val)
                node.left = left_node
                node_q.append(left_node)

            if right_val is not None:
                right_node = TreeNode(right_val)
                node.right = right_node
                node_q.append(right_node)

        return root