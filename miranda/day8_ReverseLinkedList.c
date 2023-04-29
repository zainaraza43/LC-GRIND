/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head){
    struct ListNode * current = head;
    struct ListNode * prev = NULL;
    struct ListNode * savedNext = NULL;

    while (current != NULL) {
        savedNext = current->next;
        current->next = prev;
        prev = current;
        current = savedNext;

    }
    head = prev;
    return head;
}
