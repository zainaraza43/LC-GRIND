/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int * search(struct TreeNode * root) {
    int * values = malloc(sizeof(int)*2);

    if (root == NULL) {
        values[0] = 1;
        values[1] = 0;
        return values;
    }

    int * right = search(root->right);
    int * left = search(root->left);

    int diff = abs(right[1] - left[1]);

    if(diff <= 1 && right[0] == 1 && left[0] == 1) {
        //balanced
        values[0] = 1;
    } else {
        //not balanced
        values[0] = 0;
    }

    //update height
    int max = right[1] > left[1] ? right[1] : left[1];
    values[1] = 1 + max;

    return values;
}

bool isBalanced(struct TreeNode* root){
    int values[] = {1, 0};
    int * ret = search(root);

    bool isBalanced = ret[0];
    return isBalanced;

}