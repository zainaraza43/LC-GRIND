/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* invertTree(struct TreeNode* root){
    if (root == NULL) {
        return NULL;
    }

    struct node * tempNode = root->right;
    root->right = root->left;
    root->left = tempNode;

    invertTree(root->right);
    invertTree(root->left);

    return root;
}