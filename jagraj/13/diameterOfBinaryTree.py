from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    d: int = 0

    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        heightLeft = self.maxHeight(root.left)
        heightRight = self.maxHeight(root.right)
        self.d = max(self.d, heightLeft + heightRight)
        return 1 + max(heightRight, heightLeft)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxHeight(root)
        return self.d
