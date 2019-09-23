#Count the number of prime numbers less than a non-negative number, n.
import math
class Solution(object):
    def countPrimes(self, n):
        if n<=2:
            return 0
        res= [True]*n
        res[0]= res[1]=False
        
        k=int(math.sqrt(n))+1
        
        for p in range(2,k,1):
            if res[p]==True:
                for i in range(p*2, n,p):
                    res[i]=False
                    
        return sum(res)