# Definition for singly-linked list.
     class ListNode:
         def __init__(self, x):
             self.val = x
            self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if (head and head.next):
            temp1 = head
            temp2 = head.next
            while (temp2 and temp2.next):
                temp2 = temp2.next.next
                temp1 = temp1.next
                if (temp1 == temp2):
                    return True
            return False
        return False

