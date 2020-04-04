#
# @lc app=leetcode.cn id=53 lang=python
#
# [53] 最大子序和
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxSum = nums[0]
        minSum = sum = 0
        for i in range(n):
            sum += nums[i]
            maxSum = max(maxSum, sum - minSum)
            minSum = min(minSum, sum)
        return maxSum
        
# @lc code=end

## 
# import sys

# class Solution:
#     def maxSubArray(self,nums):
#         n = len(nums)
#         maxSum = - sys.maxsize
#         sum = 0
#         for i in range(n):
#             sum = 0
#             for j in range(i,n):
#                 sum += nums[j]
#                 maxSum = max(maxSum,sum)
#         return maxSum