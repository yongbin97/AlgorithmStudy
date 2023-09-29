# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def set_node(self, head, idx, odd_pointer, even_pointer):
        if head is None:
            return even_pointer

        if idx % 2 == 0:
            even_pointer.next = ListNode(val=head.val)
            even_pointer = even_pointer.next
        else:
            odd_pointer.next = ListNode(val=head.val)
            odd_pointer = odd_pointer.next

        even_pointer = self.set_node(head.next, idx + 1, odd_pointer, even_pointer)
        return even_pointer

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_start, even_start = ListNode(), ListNode()
        even_pointer = self.set_node(head, 0, odd_start, even_start)

        even_pointer.next = odd_start.next
        return even_start.next

