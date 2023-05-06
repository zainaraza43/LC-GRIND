/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
#define MAX(a, b) (a > b ? a : b)
int *d(struct TreeNode *root, int dP[2])
{
    if (!root)
        return dP;
    int l[] = {0, 0}, r[] = {0, 0};
    d(root->left, l);
    d(root->right, r);
    dP[0] = MAX(MAX(l[0], r[0]), l[1] + r[1]);
    dP[1] = MAX(l[1], r[1]) + 1;
    return dP;
}

int diameterOfBinaryTree(struct TreeNode *root)
{
    int dP[] = {0, 0};
    return d(root, dP)[0];
}