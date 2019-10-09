"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
import itertools
class Solution:
  def purmute(self,nums):
    return itertools.permutations(nums)

  def permute2(self,nums):
    """
    自己写回溯法
    """
    res = []
    def _backtrace(nums,pre_list):
      if len(nums) <0:
        res.append(pre_list)
      else:
        for i in nums:
          # 注意copy一份新的调用，否则无法正常循环
          p_list = pre_list.copy()
          p_list.append(i)
          left_nums = nums.copy()
          left_nums.remove(i)
          _backtrace(left_nums, p_list)
      _backtrace(nums,[])
      return res

