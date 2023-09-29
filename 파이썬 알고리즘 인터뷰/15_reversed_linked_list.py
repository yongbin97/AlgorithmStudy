# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        first_node, _ = self.reverse(head)
        return first_node

    def reverse(self, node: ListNode):
        if node.next is None:
            reverse_first = ListNode(node.val)
            return reverse_first, reverse_first

        reverse_first, prev = self.reverse(node.next)
        current_node = ListNode(node.val)
        prev.next = current_node

        return reverse_first, current_node

