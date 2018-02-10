# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        p1 = l1
        p2 = l2
        head = None
        curr = None
        while not (p1 == None and p2 == None):
            if p1.val >= p2.val:
                if curr == None:
                    head = p2
                    curr = p2
                else:
                    curr.next = p2
                    curr = curr.next
                #print("Add", curr.val)
                p2 = p2.next
                if p2 == None:
                    break
            else:
                if curr == None:
                    head = p1
                    curr = p1
                else:
                    curr.next = p1
                    curr = curr.next
                #print("Add", curr.val)
                p1 = p1.next
                if p1 == None:
                    break
        if p1 == None:
            curr.next = p2
        elif p2 == None:
            curr.next = p1
        return head