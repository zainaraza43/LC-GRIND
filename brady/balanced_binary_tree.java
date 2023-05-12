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
    public boolean isBalanced(TreeNode root) {
        int[] res = heightAndWhetherBalanced(root);

        return res[1] == 0;
    }

    // Second value in the array will be a 1 if the recursive calls found a height difference > 1, 0 otherwise
    public int[] heightAndWhetherBalanced(TreeNode root) {
        if (root == null) return new int[]{0, 0};

        int[] leftRes = heightAndWhetherBalanced(root.left);
        int[] rightRes = heightAndWhetherBalanced(root.right);
        int heightDifference = Math.abs(leftRes[0]-rightRes[0]);
        int foundImbalance = (leftRes[1] == 1 || rightRes[1] == 1 || heightDifference > 1) ? 1 : 0;

        return new int[]{Math.max(leftRes[0], rightRes[0])+1, foundImbalance};
    }
}
