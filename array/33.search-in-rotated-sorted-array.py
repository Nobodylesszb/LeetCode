"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

"""
这是一个我在网上看到的前端头条技术终面的一个算法题。

题目要求时间复杂度为logn，因此基本就是二分法了。 这道题目不是直接的有序数组，不然就是easy了。

首先要知道，我们随便选择一个点，将数组分为前后两部分，其中一部分一定是有序的。

具体步骤：

我们可以先找出mid，然后根据mid来判断，mid是在有序的部分还是无序的部分
假如mid小于start，则mid一定在右边有序部分。 假如mid大于等于start， 则mid一定在左边有序部分。

注意等号的考虑

然后我们继续判断target在哪一部分， 我们就可以舍弃另一部分了
我们只需要比较target和有序部分的边界关系就行了。 
比如mid在右侧有序部分，即[mid, end] 那么我们只需要判断 target >= mid && target <= end 就能知道target在右侧有序部分，
我们就 可以舍弃左边部分了(start = mid + 1)， 反之亦然。
"""


class Solution:
    def search(self,nums,target):
        lo,hi =0, len(nums)
        while lo<hi:
            mid = (lo +hi)/2
            if (nums[mid]<nums[0] == (target<nums[0])):
                if nums[mid] < target:
                    lo = mid +1
                elif nums[mid] > target:
                    hi = mid
                else:
                    return mid
        return -1
