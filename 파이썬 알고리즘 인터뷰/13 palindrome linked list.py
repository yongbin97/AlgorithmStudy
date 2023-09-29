from typing import Optional
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        dq = deque()
        while head is not None:
            dq.append(head.val)
            head = head.next

        while len(dq) > 1:
            if dq.popleft() != dq.pop():
                return False

        return True


solution = Solution()

head = [1,2,2,1]
print(solution.isPalindrome(head))

head_2 = [1,2]
print(solution.isPalindrome(head_2))