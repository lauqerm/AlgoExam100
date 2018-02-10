# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    sm = 0
    def travel(self, node, choose):
        if choose and node.left == None and node.right == None:
            self.sm += node.val
        if not node.left == None:
            self.travel(node.left, True)
        if not node.right == None:
            self.travel(node.right, False)
        
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.travel(root, False)
        return self.sm