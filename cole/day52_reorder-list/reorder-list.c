/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
void reorderList(struct ListNode* head) {
    // if the list is empty or has only one element, there is nothing to do
    if (!head->next) return;

    struct ListNode* p1, * p2, * tmp;
    p1 = p2 = head;

    // first, find the middle of the list
    p2 = p2->next;
    while ((p1 = p1->next) && (p1 = p1->next)) p2 = p2->next;

    // p2 now points to the first element in the second half
    // now, reverse the sublist p2 -> end in-place
    tmp = NULL;
    while (p2->next) {
        p1 = p2->next;
        p2->next = tmp;
        tmp = p2;
        p2 = p1;
    }
    p2->next = tmp;

    // now, merge the two lists
    p1 = head;
    while (p2 && p1->next != p2) {
        tmp = p2->next;
        p2->next = p1->next;
        p1->next = p2;
        p1 = p2->next;
        p2 = tmp;
    }
    // if there are an odd number of elements, p1 should be the last element, as the first half will be longer
    if (p2 == NULL) p1->next = NULL;
}