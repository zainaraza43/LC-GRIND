/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

struct TreeNode* invertTree(struct TreeNode* root){
    if (!root)
        return root;
    struct TreeNode *c = root->left;
    root->left = root->right;
    root->right = c;
    invertTree(root->left);
    invertTree(root->right);
    return root;
}