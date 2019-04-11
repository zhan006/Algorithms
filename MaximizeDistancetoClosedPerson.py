'''In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to closest person.'''
class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        leng=len(seats)
        o=[]
        for i in range(leng):
            if seats[i]==1:
                o.append(i)
        
        lo=len(o)
        head=seats[:o[0]]
        #print(head)
        mh=len(head)
        tail=seats[o[lo-1]:]
        #print(tail)
        mt=len(tail)-1
        mid=[]
        lm=len(mid)
        for i in range(len(o)-1):
            mid=seats[o[i]:o[i+1]] if len(seats[o[i]:o[i+1]])>lm else mid
            lm=len(mid)
            #print(mid)
        ml=lm/2
        #print(mid)
        return int(max(ml,mt,mh))
        