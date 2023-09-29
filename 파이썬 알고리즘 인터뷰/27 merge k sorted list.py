# Definition for singly-linked list.
from typing import Optional, List
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 or all(node is None for node in lists):
            return

        values = []
        for node in lists:
            while node is not None:
                heapq.heappush(values, node.val)
                node = node.next

        new = ListNode()
        node = new
        while values:
            node.next = ListNode(val=heapq.heappop(values))
            node = node.next
        return new.next

