# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None

        start = ListNode()
        curr = start

        while list1 is not None and list2 is not None:
            if list1 is None:
                new_node = ListNode(list2.val)
                list2 = list2.next

            elif list2 is None:
                new_node = ListNode(list1.val)
                list1 = list1.next

            elif list1.val > list2.val:
                new_node = ListNode(list2.val)
                list2 = list2.next
            else:
                new_node = ListNode(list1.val)
                list1 = list1.next

            curr.next = new_node
            curr = curr.next

        return start.next
