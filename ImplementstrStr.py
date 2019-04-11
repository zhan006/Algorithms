'''Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystac'''
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle=='':
            return 0
        import re
        a=re.search(needle,haystack)
        if a:
            return a.span()[0]
        else:
            return -1