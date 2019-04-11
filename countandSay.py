'''The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.'''
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==0:
            return -1
        elif n==1:
            return "1"
        else:
            
            return self.it(self.countAndSay(n-1))
    def it(self,seq):
        s=list(str(seq))
        #print(s)
        sli=[]
        bl=[]
        for i in range(len(s)-1):
            if s[i]!=s[i+1]:
                sli.append(i+1)
        #print(sli)
        if len(sli)==0:
            
            bl.append(len(s))
            bl.append(s[0])
            a=list(map(str,bl))
            bl=''.join(a)
            return bl
        else:
            beef=s[:sli[0]]
            num=len(beef)
            bl.append(num)
            bl.append(beef[0])
            for i in range(len(sli)-1):
                beef=s[sli[i]:sli[i+1]]
                num=len(beef)
                bl.append(num)
                bl.append(beef[0])
            beef=s[sli[len(sli)-1]:]
            num=len(beef)
            bl.append(num)
            bl.append(beef[0])
            a=list(map(str,bl))
            bl=''.join(a)
            return bl