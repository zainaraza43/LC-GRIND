# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def idenTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]):
        if root == None and subRoot == None:
            return True
        
        if root == None or subRoot == None:
            return False
        
        return root.val == subRoot.val and self.idenTree(root.left, subRoot.left) and self.idenTree(root.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None or subRoot == None:
            return False
        
        if self.idenTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
