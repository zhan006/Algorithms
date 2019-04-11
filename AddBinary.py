'''Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.'''
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        length=max(len(a),len(b))
        a=self.initlist(length,a)
        b=self.initlist(length,b)
        res=[]
        up=0
        for i in range(length):
            summa=a[i]+b[i]+up
            if summa>=2:
                summa-=2
                up=1
                res.append(summa)
            else:
                up=0
                res.append(summa)
        if up==1:
            res.append(up)
        res.reverse()
        res=''.join(list(map(str,res)))
        return res
    def initlist(self,capa,string):
        lst=[0 for i in range(capa)]
        number=list(string)
        for i in range(len(number)):
            lst[i]=number.pop()
        lst=list(map(int,lst))
        return lst