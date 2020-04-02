"""
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), 
and its complement is 010. So you need to output 2.
"""


"""
The core is ^
111 ^ 101 = 010
Then the concern is to let the '0' in num complement to '1', because all the '1' in num will be complemented to "0" with ^.
So how to find the '0's in num
find another number that is one bit left than num and do minus 1.
e.g. 1000 (8) - 1 = 111 (7)
which will be the largest one in that bit-length, only having '1's.
With help of ^, '0' in num now will be complemented to '1'
""" 
class Solution(object):
    def findComplement(self, num):
        i = 1
        while i <= num:
            i = i << 1
        return (i - 1) ^ num

    
s =Solution()
r = s.findComplement(5)

print(r)