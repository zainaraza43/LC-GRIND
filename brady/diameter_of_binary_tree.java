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
    public int diameterOfBinaryTree(TreeNode root) {
        
        if (root == null) return 0;

        int[] diameter = new int[1];
        findDiameter(root, diameter);

        return diameter[0];
    }

    // Returns the height of the tree rooted at "root", and updates the diameter object if necessary
    public int findDiameter(TreeNode root, int[] diameter) {
        if (root == null) return 0;

        int leftDepth = findDiameter(root.left, diameter);
        int rightDepth = findDiameter(root.right, diameter);

        diameter[0] = Math.max(diameter[0], leftDepth + rightDepth);

        return Math.max(leftDepth, rightDepth) + 1;
    }
}
