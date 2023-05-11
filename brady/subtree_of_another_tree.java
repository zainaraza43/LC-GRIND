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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        // find value at subRoot in root's tree using breadth-first-search
        Queue<TreeNode> bfsQueue = new LinkedList<>();
        bfsQueue.add(root);
        while (!bfsQueue.isEmpty()) {
            TreeNode node = bfsQueue.poll();
            if (node.val == subRoot.val && isSameTree(node, subRoot)) return true;

            // Adding nodes to the LinkedList is O(1) since Java LinkedLists are Deques
            if (node.left != null) bfsQueue.add(node.left);
            if (node.right != null) bfsQueue.add(node.right);
        }

        return false;
    }

    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) return true;
        else if (p == null || q == null) return false;

        if (p.val != q.val) return false;

        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}
