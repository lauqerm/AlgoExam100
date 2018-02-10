# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    a = {}
    def travel(self, node):
        if node == None:
            return
        if not node.val in self.a:
            self.a[node.val] = 1
        else:
            self.a[node.val] += 1
        if not node.left == None:
            self.travel(node.left)
        if not node.right == None:
            self.travel(node.right)
        
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.a.clear()
        d = []
        self.travel(root)
        mx = 0
        for i in self.a:
            if self.a[i] > mx:
                mx = self.a[i]
        print(mx)
        for i in self.a:
            print(i, self.a[i])
            if mx == self.a[i]:
                d.append(i)
                print(d)
        return d