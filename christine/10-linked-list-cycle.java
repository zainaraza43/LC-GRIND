/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        ListNode next;

        while(curr != null){
            next = curr.next; //inside loop in case curr/head is null
            curr.next = prev;
            prev = curr; //reverse the link relationship "arrow"
            curr = next;
        }

        return prev;
    }
}