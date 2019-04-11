'''You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.'''
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        minstep=math.ceil(n/2)
        curstep=n
        res=0
        while curstep>minstep:
            res+=self.step(curstep)/(self.step(n-curstep)*self.step(curstep-n+curstep))
            curstep-=1
        if n/2==minstep:
            return int(res+1)
        else:
            return int(res+minstep)
    def step(self,x):
        fac=1
        while x>1:
            fac*=x
            x-=1
        return fac
