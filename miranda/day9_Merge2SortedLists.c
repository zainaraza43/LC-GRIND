/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    struct ListNode * mergedList;
    struct ListNode * current = mergedList;
    struct ListNode * temp;

    if(list1==NULL) {
        return list2;
    } 
    if(list2==NULL){
        return list1;
    }

    //initalize list
    if (list1->val <= list2->val) {
        mergedList = list1;
        current = list1;
        list1 = list1->next;
    } else {
        mergedList = list2;
        current = list2;
        list2 = list2->next;
    }

    while ((list1 != NULL) && (list2 != NULL)) {
        if (list1->val <= list2->val) {
            //add element from list 1 
            temp = list1->next;
            current->next = list1;
            current = current -> next;
            list1 = temp;
        } else {
            printf("list1: %d, list2: %d\n", list1->val, list2->val);
            //add element from list 2
            temp = list2->next;
            current->next = list2;
            current = current -> next;
            list2 = temp;
        }
    }

    if (list1 != NULL) {
        current->next = list1;
    }
    if (list2 != NULL) {
        current->next = list2;
    }
    return mergedList;

}