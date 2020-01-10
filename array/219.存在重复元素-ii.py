#
# @lc app=leetcode.cn id=219 lang=python
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for index,num in enumerate(nums):
            if num in d and  index - d[num] <= k:
                return True
            d[num] = index
        return False
        
# @lc code=end

