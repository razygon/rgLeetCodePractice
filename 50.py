'''
50. Pow(x, n)  
Implement pow(x, n).
'''
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ans = x
        
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
        d = abs(n/2)
        r = abs(n%2)
        if r and n<0:
            d = d-1
        print d,r,x
        rem = []
        if r:
            rem.append(ans)
        while(d!=0):
            
            ans = ans*ans
            m = d
            d = m/2
            if d and m%2:
                rem.append(ans)
        print rem
        for r in rem:
            ans = ans*r
        if n<0:
            print ans
            ans = 1/ans
            
        return ans
