'''Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only'''
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        import re
        if len(s)==0:
            return 0
        pattern=r'\b[a-zA-Z]+\b'
        res=re.findall(pattern,s)
        if res:
            return len(res[-1])
        else:
            return 0