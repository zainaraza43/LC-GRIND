/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    struct ListNode * fast = head;
    struct ListNode * slow = head;

    while (fast != NULL  && fast->next != NULL && 
            fast->next->next!= NULL && slow != NULL) {
        slow = slow->next;
        fast = fast->next->next;

        if (fast == slow) {
            return true;
        }
    }

    return false;
}