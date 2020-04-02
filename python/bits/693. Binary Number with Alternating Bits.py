"""
Given a positive integer, 
check whether it has alternating bits: namely, 
if two adjacent bits will always have different values.
"""

class Soluton:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (((n ^ (n >> 1)) + 1) & n) == 0
