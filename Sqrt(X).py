'''Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.'''
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<2:
            return x
        else:
            return int(self.binary(x,0,x))
    def binary(self,x,left,right):
        mid=int((left+right)/2)

        if mid**2<=x and (mid+1)**2>x:
            return mid
        elif mid**2<x:
            left=mid
            return self.binary(x,left,right)
        elif mid**2>x:
            right=mid
            return self.binary(x,left,right)
            