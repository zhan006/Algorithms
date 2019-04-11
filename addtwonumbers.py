# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself'''
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carries=0
        dummy=ListNode(-1)
        curr=dummy
        while l1 or l2:
            a=l1.val if l1!=None else 0
            b=l2.val if l2!=None else 0
            summa=carries+a+b
            if summa>=10:
                carries=1
                summa=summa-10
            else:
                carries=0
            curr.next=ListNode(summa)
            curr=curr.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        curr.next=ListNode(carries) if carries!=0 else None
        return dummy.next