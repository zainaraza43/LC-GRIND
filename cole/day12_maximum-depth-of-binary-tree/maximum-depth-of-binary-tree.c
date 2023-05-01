/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int maxDepth(struct TreeNode *root)
{
    int a, b;
    return root ? ((a = maxDepth(root->left)) > (b = maxDepth(root->right)) ? a : b) + 1 : 0;
}