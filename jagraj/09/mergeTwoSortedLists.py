# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2

        if list2 is None:
            return list1

        result: ListNode = ListNode()
        tail: ListNode = result

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                tail.next = ListNode(list1.val)
                tail = tail.next
                list1 = list1.next
            else:
                tail.next = ListNode(list2.val)
                tail = tail.next
                list2 = list2.next

        while list1 is not None:
            tail.next = ListNode(list1.val)
            tail = tail.next
            list1 = list1.next

        while list2 is not None:
            tail.next = ListNode(list2.val)
            tail = tail.next
            list2 = list2.next

        return result.next
