/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == nullptr) return false;
        
        ListNode *slow = head, *fast = head;

        do {
            if (fast->next != nullptr && fast->next->next != nullptr) {
                fast = fast->next->next;
            } else {
                return false;
            }
            
            slow = slow->next;
        } while(slow != fast);
        
        return true;
    }
};