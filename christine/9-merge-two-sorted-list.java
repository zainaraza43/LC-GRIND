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
    //use recursive definition
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null){
            return list2;
        }
        else if (list2 == null){
            return list1;
        }
        else {
            if (list1.val < list2.val){
                list1.next = mergeTwoLists(list1.next, list2); //sort & merge the elements after this one
                return list1; //this element is sorted in the list
            }

            list2.next = mergeTwoLists(list2.next, list1); // list1.val >= list2.val
            return list2;
        }
    }
}