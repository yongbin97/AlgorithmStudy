# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, val: int, sort_head: ListNode):
        if sort_head.next is None:
            sort_head.next = ListNode(val)
        else:
            prev, curr = sort_head, sort_head.next
            while curr and val >= curr.val:
                prev, curr = curr, curr.next

            prev.next = ListNode(val, curr)

    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sort_head = ListNode()

        while head:
            self.insert(head.val, sort_head)
            head = head.next

        return sort_head.next

    def insertionSortList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = parent = ListNode()
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next

            if head and cur.val > head.val:
                cur = parent

        return parent.next
