# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def set_node(self, l1, l2, current_node, extra_value=0):
        if l1 is None and l2 is None and extra_value == 0:
            return

        current_value = extra_value + getattr(l1, "val", 0) + getattr(l2, "val", 0)
        current_node.next = ListNode(val=current_value % 10)
        point = current_node.next

        self.set_node(getattr(l1, "next", None), getattr(l2, "next", None), point, current_value // 10)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        self.set_node(l1, l2, answer)

        return answer.next



