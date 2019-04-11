'''Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.'''
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst=list(s)
        summa=0
        lastnumber=0
        for i in range(len(lst)):
            number=self.toint(lst.pop())
            if (lastnumber==5 or lastnumber==10) and number==1:
                summa=summa-number
            elif (lastnumber==50 or lastnumber==100) and number==10:
                summa=summa-number
            elif (lastnumber==500 or lastnumber==1000) and number==100:
                summa=summa-number
            else:
                summa=number+summa
            lastnumber=number
        return summa
    def toint(self,s):
        if s=='V':
            return 5
        elif s=='I':
            return 1         
        elif s=='X':
            return 10
        elif s=='L':
            return 50
        elif s=='C':
            return 100
        elif s=='D':
            return 500
        elif s=='M':
            return 1000
        else:
            return None
        
