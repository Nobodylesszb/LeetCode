#
# @lc app=leetcode.cn id=26 lang=python
#
# [26] 删除排序数组中的重复项
#

#使用快慢指针来记录遍历的坐标。

# 开始时这两个指针都指向第一个数字

# 如果两个指针指的数字相同，则快指针向前走一步

# 如果不同，则两个指针都向前走一步

# 当快指针走完整个数组后，慢指针当前的坐标加1就是数组中不同数字的个数

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            slow = 0
            for fast in range(1,len(nums)):
                if nums[fast] != nums[slow]:
                    slow +=1
                    nums[slow] = nums[fast]
            return slow +1
        return 0
            
        
# @lc code=end

