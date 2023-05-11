/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

 #include <stack>

class Solution {
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        // find a possible root

        std::stack<TreeNode*> stck;
        TreeNode *current;

        stck.push(root);

        while(!stck.empty()) {
            current = stck.top();

            if (current->val == subRoot->val) {
                if (isSameTree(current, subRoot)) return true;
            }

            stck.pop();

            if (current->left != nullptr) stck.push(current->left);
            if (current->right != nullptr) stck.push(current->right);
        }

        return false;
    }



    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (p == nullptr && q == nullptr) return true;
        if (p == nullptr || q == nullptr || p->val != q->val) return false;

        return (!isSameTree(p->left, q->left) || !isSameTree(p->right, q->right)) ? false : true;
    }
};