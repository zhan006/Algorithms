'''Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.'''
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for i in s:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
            elif i==']':
                if len(stack)==0:
                    stack.append(i)
                elif len(stack)!=0 and stack[-1]=='[':
                    stack.pop()
                else:
                    stack.append(i)

            elif i=='}':
                if len(stack)==0:
                    stack.append(i)
                elif len(stack)!=0 and stack[-1]=='{':
                    stack.pop()
                else:
                    stack.append(i)
            elif i==')':
                if len(stack)==0:
                    stack.append(i)
                elif len(stack)!=0 and stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(i)
                
        if len(stack)==0:
            return True
        else:
            return False
                