"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
import itertools

class Solution:
    def permuteUnique(self,nums):

        """"
         与46题一样，当然也可以直接调用itertools的函数，然后去重
        """
        return list(set(itertools.permutations(nums)))

    def permuteUnique1(self,nums):
        """
        需要去重
        """
        nums.sort()
        res = []
        def _backtrace(nums,pre_list):
            if len(nums)<=0:
                res.append(pre_list)
            else:
                for i in range(len(nums)):
                    # 如果是同样的数字，则之前一定生成对应可能
                    if i > 0 and nums[i] ==nums[i-i]:
                        continue
                    p_list = pre_list.copy()
                    p_list.append(nums[i])
                    left_nums = nums.copy()
                    left_nums.pop(i)
                    _backtrace(left_nums,p_list)
        _backtrace(nums,[])
        return res
        
        
