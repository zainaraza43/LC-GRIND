# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def utils(root):

            if root == None:
                return 0

            left = utils(root.left)

            if left == -1:
                return -1 

            right = utils(root.right)

            if right == -1 or abs(right-left) > 1:
                return -1
            else:
                return max(right, left) + 1

        return False if utils(root) == -1 else True