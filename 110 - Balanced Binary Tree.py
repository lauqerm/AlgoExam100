# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def check(self, node):
        if node == None:
            return True
        lh = self.height(node.left)
        rh = self.height(node.right)
        if (abs(lh - rh) <= 1
            and self.check(node.left)
            and self.check(node.right)):
            return True
        return False
 
    def height(self, node):
        if node == None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))
            
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root)