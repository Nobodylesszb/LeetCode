class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return([i for i in A if i %2==0]+[i for i in A if i %2!=0])
        