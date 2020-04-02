#Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# 使用快慢指针来记录遍历的坐标。

# 开始时这两个指针都指向第一个数字

# 如果两个指针指的数字相同，则快指针向前走一步

# 如果不同，则两个指针都向前走一步

# 当快指针走完整个数组后，慢指针当前的坐标加1就是数组中不同数字的个数

class Solution:
    def removeDuplicates(self,nums):
        curr_index = 0
        while curr_index < len(nums) -1: #  # iterating through nums list till next-to-last element (curr_idx + 1 always checked)
            if nums[curr_index] == nums[curr_index +1]: # if current and next element are the same
                del nums[curr_index] # # current element is deleted
                curr_index -=1  # to stay at the same place in list, we have to dicrease 1 (1 will be added in the next step)
            curr_index += 1   # going further in the list
        return len(nums)
