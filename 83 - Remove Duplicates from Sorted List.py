# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return []
        curr = head
        while not curr.next == None:
            if curr.next.val == curr.val:
                if curr.next.next == None:
                    curr.next = None
                else:
                    curr.next = curr.next.next
            else:
                curr = curr.next
        return head