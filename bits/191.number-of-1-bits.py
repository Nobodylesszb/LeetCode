"""
Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).
"""
class Solution:
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """       
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c


s =Solution()
s.hammingWeight(5)