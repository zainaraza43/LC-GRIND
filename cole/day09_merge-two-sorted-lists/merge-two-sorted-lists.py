# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # initialize
        out, l = None, None
        if not list1 and not list2:
            return None
        elif list1 and list2:
            if list1.val < list2.val:
                out = list1
                list1 = list1.next
                l = out
            else:
                out = list2
                list2 = list2.next
                l = out
        elif list1:
            return list1
        else:
            return list2
        # merge
        while list1 and list2:
            if list1.val < list2.val:
                tmp = list1.next
                l.next = list1
                list1 = tmp
                l = l.next
            else:
                tmp = list2.next
                l.next = list2
                list2 = tmp
                l = l.next
        if list1:
            l.next = list1
        else:
            l.next = list2
        return out
