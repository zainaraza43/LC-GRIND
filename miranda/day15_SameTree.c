/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool isSameTree(struct TreeNode* p, struct TreeNode* q){
    if (p == NULL && q == NULL) {
        return true;
    }

    if ((p == NULL && q !=NULL || (p != NULL && q== NULL))) {
        return false;
    }

    if (p->val != q->val) {
        return false;
    }

    bool isRightTreeSame = isSameTree(p->right, q->right);
    bool isLeftTreeSame = isSameTree(p->left, q->left);

    return isRightTreeSame && isLeftTreeSame;

}