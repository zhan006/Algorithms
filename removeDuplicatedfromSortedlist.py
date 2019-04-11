'''Given a sorted linked list, delete all duplicates such that each element appear only once.'''
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
        if head:
            cur=head
            while cur.next:
                if cur.val==cur.next.val:
                    cur.next=cur.next.next
                else:
                    cur=cur.next
            return head
