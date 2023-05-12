/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reversal(ListNode* prev, ListNode* head) {
        if(head->next == nullptr) {
            head->next = prev;
            return head;
        }

        ListNode * nextNode = head->next;
        head->next = prev;
        return reversal(head, nextNode);
    }

    ListNode* reverseList(ListNode* head) {
        if (head != nullptr) {
            return reversal(nullptr, head);
        }
        return head;
    }

};