/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *popSmaller(struct ListNode **p1, struct ListNode **p2);
void setNext(struct ListNode **p1, struct ListNode *p2);

// O(m+n) time, O(1) space, where m and n are the sizes of list1 and list2 respectively
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    if (list1 == NULL) return list2;
    else if (list2 == NULL) return list1;

    struct ListNode *p = popSmaller(&list1, &list2);
    struct ListNode *head = p;

    while (list1 != NULL && list2 != NULL) {
        if (list1->val < list2->val) {
            setNext(&p, list1);
            list1 = list1->next;
        } else {
            setNext(&p, list2);
            list2 = list2->next;
        }
    }

    if (list1 == NULL) setNext(&p, list2);
    else setNext(&p, list1);

    return head;
}

struct ListNode *popSmaller(struct ListNode **p1, struct ListNode **p2) {
    struct ListNode *ret;
    if ((*p1)->val < (*p2)->val) {
        ret = *p1;
        *p1 = (*p1)->next;
    } else {
        ret = *p2;
        *p2 = (*p2)->next;
    }
    return ret;
}

void setNext(struct ListNode **p1, struct ListNode *p2) {
    (*p1)->next = p2;
    *p1 = (*p1)->next;
}
