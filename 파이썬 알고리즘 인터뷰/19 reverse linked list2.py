# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} "


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        root = start = ListNode()
        root.next = head

        for _ in range(left-1):
            start = start.next
        end = start.next

        for _ in range(right - left):
            tmp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = tmp
        return root.next
