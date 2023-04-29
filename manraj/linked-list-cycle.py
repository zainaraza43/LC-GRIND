class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if head.val == "seen":
                return True
            head.val = "seen"
            head = head.next
