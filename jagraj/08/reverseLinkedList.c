struct ListNode {
  int val;
  struct ListNode *next;
};

struct ListNode *reverseList(struct ListNode *head) {

  if (!head || !head->next) {
    return head;
  }
  struct ListNode *current = head, *next = head->next;


  head->next = 0;
  while (next) {
    struct ListNode *tmp = next->next;
    next->next = current;
    current = next;
    next = tmp;
  }

  return current;
}


