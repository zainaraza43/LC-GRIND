/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    // O(n) time, O(n) space
    public boolean isSameTree(TreeNode p, TreeNode q) {
        return depthFirstCheckSame(p, q);
    }

    public boolean depthFirstCheckSame(TreeNode p, TreeNode q) {
        if (p == null && q == null) return true;
        else if (p == null || q == null) return false;

        if (p.val != q.val) return false;

        return depthFirstCheckSame(p.left, q.left) && depthFirstCheckSame(p.right, q.right);
    }
}
