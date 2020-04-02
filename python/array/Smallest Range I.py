#Smallest Range I

#Given an array A of integers, for each integer A[i] we may choose any x with -K <= x <= K, and add x to A[i].

#After this process, we have some array B.

#return the smallest possible difference between the maximum value of B and the minimum value of B.

#Intuition:
# If min(A) + K < max(A) - K, then return max(A) - min(A) - 2 * K
# If min(A) + K >= max(A) - K, then return 0
class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return max(0, max(A) - min(A) - 2 * K)