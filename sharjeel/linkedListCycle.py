class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head is None or head.next is None: return False

        # Two Pointer Solution
        slow = head
        fast = head.next.next

        while fast and fast.next:
            if fast == slow and slow: return True
            fast = fast.next.next
            slow = slow.next

        return False