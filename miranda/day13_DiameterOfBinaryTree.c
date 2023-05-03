/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int maxDiameter;

int dfs(struct TreeNode * root) {
    if (root == NULL) {
        return -1;
    }
    int right = dfs(root->right);
    int left = dfs(root->left);
    int diameter = 2 + right + left;

    if (diameter > maxDiameter) {
        maxDiameter = diameter;
    }

    int height = 1 + (right > left ? right : left);
    return height;
}

int diameterOfBinaryTree(struct TreeNode* root){
    maxDiameter = 0;
    dfs(root);
    return maxDiameter;
}