# Given an integer array nums, 
# find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
# If you have figured out the O(n) solution, 
# try coding another solution using the divide and conquer approach, which is more subtle.
import sys

class Solution:
    def maxSubArray(self,nums):
        n = len(nums)
        maxSum = nums[0]
        minSum = sum = 0
        for i in  range(n):
            sum +=nums[i]
            maxSum = max(maxSum,sum-minSum)
            minSum = min(minSum,sum)
        return maxSum


#动态规划
class Solution1:
    def maxSubArray(self,nums):
        n = len(nums)
        max_sum_ending_curr_index = max_sum = nums[0]
        for i in range(1,n):
            max_sum_ending_curr_index = max(max_sum_ending_curr_index + nums[i], nums[i])
            max_sum = max(max_sum_ending_curr_index, max_sum)

        return max_sum


#暴力破解
class Solution2:
    def maxSubArray(self,nums):
        n = len(nums)
        maxSum = -sys.maxsize
        sum = 0
        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum += nums[j]
                maxSum = max(maxSum, sum)
        
        return maxSum