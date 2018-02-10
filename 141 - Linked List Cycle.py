# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        sp = head
        fp = head.next
        while True:
            if sp is fp:
                return True
            sp = sp.next
            if fp.next == None:
                return False
            else:
                fp = fp.next
            if fp.next == None:
                return False
            else:
                fp = fp.next