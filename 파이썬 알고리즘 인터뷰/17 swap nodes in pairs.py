# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swap(self, head: Optional[ListNode]):
        if head.next is None or head.next.next is None:
            return

        next = head.next
        next_next = head.next.next

        head.next = next_next
        next.next = next_next.next
        next_next.next = next

        self.swap(next)

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode()
        start.next = head
        self.swap(start)
        return start.next