/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *reverseList(struct ListNode *head)
{
    struct ListNode *result = NULL, *tmp;
    while (head)
    {
        tmp = head->next;
        head->next = result;
        result = head;
        head = tmp;
    }
    return result;
}