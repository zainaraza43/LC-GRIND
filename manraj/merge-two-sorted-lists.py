class Solution:
    def appendList(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        list1.next = self.appendList(list1.next, list2)
        return list1

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = None

        if not list1 and not list2:
            return None

        while list1 and list2:
            if list1.val < list2.val:
                list3 = self.appendList(list3, ListNode(list1.val, None))
                list1 = list1.next
            else:
                list3 = self.appendList(list3, ListNode(list2.val, None))
                list2 = list2.next

        if list1:
            list3 = self.appendList(list3, list1)
        elif list2:
            list3 = self.appendList(list3, list2)
        
        return list3
        
