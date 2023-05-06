# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

class Solution(object):
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
      
# Explanation
# I defined one slow pointer and one fast pointer
# While both pointers we're not null, slow is initialized to the next element and fast is initialized to two elements ahead.
# If they are equal to each other we return true, if not we return False.
# Example: 3->2->0->-4->(goes to 2)
# Slow and Fast start at 3
# Slow goes up 1 to 2, fast goes up 2 to 0
# Slow goes up 1 to 0, fast goes up 2 to 2
# Slow goes up 1 to -4, fast goes up 2 to -4
# This will always work because if there is a cycle, the faster pointer will always catch up to the slower one.
