"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""

class Solution:
    def merge(self,num1,m, num2, n):
        l1,l2,end = m-1,n-1,m+n-1
        while l1 >=0 and l2 >=0:
            if num2[l2] > num1[l1]:
                num1[end] = num2[l2]
                l2 -= 1
            else:
                num1[end] = num1[l1]
                l1 -= 1
            end -=1
        if l1 < 0:
            nums1[:l2+1] = nums2[:l2+1]



nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]    
n = 3

s = Solution
s.merge(nums1,m,nums2,n)
print(nums1)



#
# @lc app=leetcode.cn id=88 lang=python
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while m >0 and n > 0:
            if nums1[m-1] >=nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

        
# @lc code=end


if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3   
    nums2 = [2,5,6]
    n = 3
    S = Solution()
    S.merge(nums1,m,nums2,n)