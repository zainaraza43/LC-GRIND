/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

// O(n) time, O(1) space
bool hasCycle(struct ListNode *head) {
    if (head == NULL) return false;

    struct ListNode *slow = head;
    struct ListNode *fast = head->next;

    // If fast exhausts the list, then there is no cycle. If slow == fast then there is a cycle
    while (fast != NULL && fast->next != NULL) {
        if (slow == fast) return true;
        slow = slow->next;
        fast = fast->next->next;
    }

    return false;
}
