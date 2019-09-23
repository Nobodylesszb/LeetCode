"""
Given an array of integers and an integer k, 
find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] 
and the absolute difference between i and j is at most k.
"""

"""
由于题目没有对空间复杂度有求，用一个hashmap 存储已经访问过的数字即可, 每次访问都会看hashmap中是否有这个元素，有的话拿出索引进行比对，
是否满足条件（相隔不大于k），如果满足返回true即可。
"""
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        for i,v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False

    

nums = [1,2,3,1]
k = 3

s= Solution()
s.containsNearbyDuplicate(nums,k)




