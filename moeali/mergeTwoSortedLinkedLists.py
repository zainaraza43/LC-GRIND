# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        temp = current = ListNode(0)
        
        while(l1 and l2):
            if (l1.val < l2.val):
                current.next = l1
                l1 = l1.next  
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        current.next = l1 or l2
        return temp.next
        
# Explanation
# Initialize two references to a new ListNode (temp is used so we can easily point to the head of the linked list once we are done merging, current is used to iterate
through both lists)
# Note to self: curr is used to iterate through the list, since it eventually ends by being at say the number 15, we can't return it since it's not the head so we use
temp to easily point to the head (first element) of the linked list
# While both lists aren't empty, if the value of l1 is less then the value of l2 (same index in both lists), append l1 to the new list node and do the opposite if l2
is greater than l1. 
# Then we move current to the next node in the list (so we can fill it in the next iteration)
# Finally, after the loop is completed, one of the lists will still have remaining nodes, so we add the rest by assigning current to l1 or l2 
