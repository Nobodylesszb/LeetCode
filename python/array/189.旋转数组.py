#
# @lc app=leetcode.cn id=189 lang=python
#
# [189] 旋转数组
#

# @lc code=start
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k >=len(nums):
            k %= len(nums)
        for i in range(k-1,-1,-1):
            a = nums[i]
            nums[i] = nums[-1]
            nums.insert(k,a)
            nums.pop()
        return nums
# @lc code=end

