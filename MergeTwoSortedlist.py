'''Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.'''
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
        dummy=ListNode(-1)
        cur=dummy
        a=l1
        b=l2
        while l1 or l2:
            if l1==None and l2!=None:
                cur.next=l2
                break
            elif l2==None and l1!=None:
                cur.next=l1
                break
            elif l1.val>=l2.val:
                cur.next=l2
                l2=l2.next
                cur=cur.next
            else:
                cur.next=l1
                l1=l1.next
                cur=cur.next
        re=dummy.next
        return re
