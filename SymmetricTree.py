'''Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def isMirror(left,right):
            if not left and not right:
                return True
            if (not left and right) or (left and not right):
                return False
            if left.val!=right.val:
                return False
            else:
                return isMirror(left.left,right.right) and isMirror(left.right,right.left)
        return isMirror(root.left,root.right)