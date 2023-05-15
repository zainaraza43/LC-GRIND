/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
// #include <stdlib.h>
int bb(struct TreeNode* root)
{
    if (!root) return 0;
    int l = bb(root->left);
    int r = bb(root->right);
    if (abs(l - r) > 1 || l < 0 || r < 0)
        return -1;
    return (l < r ? r : l) + 1;
}
bool isBalanced(struct TreeNode* root){
    return bb(root) >= 0;
}