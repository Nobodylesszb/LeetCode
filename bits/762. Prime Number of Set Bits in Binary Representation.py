"""
Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.

(Recall that the number of set bits an integer has is the number of 1s present when written in binary. For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)
"""

"""
The most intuitive way to count for 1's in the binary expression of a number, is counting the 1's. Luckily, python can do that using .count() method.

So all we have to do is convert the number to binary, and do a count(). However, how do we know if a count is prime?

We could solve for the prime, but that would take forever, instead, we can opt for a reference table of prime numbers. Therefore we create a set containing all primes from 0~19, (since 20 bits is the limit due to OP stating max number there is 10^6, which can have up to 20 bits)

From them on, it's a simple comparison.
"""
class Solution:
    def countPrimeSetBits(self, L, R):
        prime_set = {2, 3, 5, 7, 11, 13, 17, 19}
        
        ret = 0
        for i in range(L, R+1):
            one_count = bin(i).count('1')
            if one_count in prime_set:
                ret +=1
        
        return ret