# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def b(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l, r = self.b(root.left), self.b(root.right)
        if abs(l - r) > 1 or l < 0 or r < 0:
            return -1
        return max(l, r) + 1
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.b(root) >= 0