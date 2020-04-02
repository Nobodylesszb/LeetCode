"""
Given an array of size n, find the majority element. 
The majority element is the element that appears more than 
⌊ n/2 ⌋ times.
You may assume that the array is non-empty 
and the majority element always exist in the array.
"""

class Solution():
    def majorityElement(self, nums):
        num_set = set(nums)
        for num in num_set:
            if nums.count(num) > (len(nums)/2):
                return num

class Solution2:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]