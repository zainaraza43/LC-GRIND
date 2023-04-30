from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        p1: Optional[ListNode] = head
        p2: Optional[ListNode] = head.next

        while p1 is not None and p2 is not None and p2.next is not None:
            p1 = p1.next
            p2 = p2.next.next

            if p1 == p2:
                return True

        return False
