'''Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.'''
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=str(x)
        l=len(s)
        for i in range(l):
            if s[i]!=s[l-i-1]:
                return False
        return True
            
        