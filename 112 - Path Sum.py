# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        
    def travel(self, node, value, sum):
        value += node.val
        #print(value)
        if not (node.left == None):
            #print("Go left")
            if self.travel(node.left, value, sum) == True:
                return True
        if not (node.right == None):
            #print("Go right")
            if self.travel(node.right, value, sum) == True:
                return True
        if node.left == None and node.right == None:
            if value == sum:
                #print("Survive end")
                return True
            else:
                #print("Dead end")
                return False
        else:
            #print("Middle 2 end")
            return False
                
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        return self.travel(root, 0, sum)
            
        
        