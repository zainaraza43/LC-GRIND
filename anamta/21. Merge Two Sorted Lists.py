# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        if list1 and list2:
                temp1 = list1
                temp2 = list2

                if (temp1.val < temp2.val):
                    head = temp1
                    temp1 = temp1.next
                else:
                    head = temp2
                    temp2 = temp2.next
                
                curr = head
                while (temp1 or temp2):
                    if (temp1 and temp2):
                        if (temp1.val < temp2.val):
                            curr.next = temp1
                            temp1 = temp1.next
                        else:
                            curr.next = temp2
                            temp2 = temp2.next
                    elif (temp1):
                        curr.next = temp1
                        temp1 = temp1.next      
                    else:
                        curr.next = temp2
                        temp2 = temp2.next 
                    if(curr):
                        curr = curr.next
                
                return head
        if list1:
            return list1

        if list2:
            return list2
