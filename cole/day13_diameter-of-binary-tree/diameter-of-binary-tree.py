# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def d(self, root: Optional[TreeNode]) -> tuple[int]:
        if not root:
            return 0, 0
        ld, lP = self.d(root.left)
        rd, rP = self.d(root.right)
        d = max(ld, rd, lP + rP)
        P = max(lP, rP) + 1
        return d, P

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.d(root)[0]
