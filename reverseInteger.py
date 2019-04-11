'''Given a 32-bit signed integer, reverse digits of an integer.'''
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        stack=list(str(x))
        o=[]
        for i in range(len(stack)):
            o.append(stack.pop())
        if o[-1]=='-':
            re=int('-'+''.join(o[:-1]))
        else:
            re=int(''.join(o))
        if re>=-2**31 and re<2**31:
            return re
        else:
            return 0
        