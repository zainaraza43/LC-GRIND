// another 100%

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *mergeTwoLists(struct ListNode *list1, struct ListNode *list2)
{
    // obvious cases
    switch (((list2 != NULL) << 1) | (list1 != NULL))
    {
    case 0:
        return NULL;
    case 1:
        return list1;
    case 2:
        return list2;
    }
    // initialize output list
    struct ListNode *out, *l, *tmp;
    if (list1->val < list2->val)
    {
        out = list1;
        l = list1;
        list1 = list1->next;
    }
    else
    {
        out = list2;
        l = list2;
        list2 = list2->next;
    }
    // generate output in-place
    while (list1 && list2)
    {
        if (list1->val < list2->val)
        {
            tmp = list1->next;
            l->next = list1;
            l = l->next;
            list1 = tmp;
        }
        else
        {
            tmp = list2->next;
            l->next = list2;
            l = l->next;
            list2 = tmp;
        }
    }
    l->next = list1 ? list1 : list2;
    return out;
}