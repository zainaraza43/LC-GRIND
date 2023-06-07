# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return max(self.treeDiameter(root))

        
    def treeDiameter(self, root):
        if root == None:
            return (-1, 0)

        left_max, whole_left_max = self.treeDiameter(root.left)
        right_max, whole_right_max = self.treeDiameter(root.right)

        side_max = max(left_max, right_max) + 1
        whole_max = max(whole_left_max, whole_right_max, left_max + right_max + 2)

        return (side_max, whole_max)