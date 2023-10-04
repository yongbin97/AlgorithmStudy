# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList_2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next

        val_list.sort()

        head = ListNode()
        node = head
        for v in val_list:
            node.next = ListNode(v)
            node = node.next
        return head.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head

        # runner algorithm
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, slow.next.next
        half.next = None

        # divide
        l1 = self.sortList(head)
        l2 = self.sortList(half)

        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1 or l2
