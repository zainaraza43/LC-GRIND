/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int maxDepth(struct TreeNode* root){
    if (root == NULL) {
        return 0;
    }

    int rightMax = maxDepth(root->right);
    int leftMax = maxDepth(root->left);

    return 1 + (rightMax > leftMax ? rightMax : leftMax);
}