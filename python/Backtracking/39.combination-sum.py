"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

"""
这道题目是求集合，并不是求极值，因此动态规划不是特别切合，因此我们需要考虑别的方法。

这种题目其实有一个通用的解法，就是回溯法。 网上也有大神给出了这种回溯法解题的 通用写法，这里的所有的解法使用通用方法解答。 除了这道题目还有很多其他题目可以用这种通用解法，具体的题目见后方相关题目部分。

我们先来看下通用解法的解题思路，我画了一张图：
"""


class Solution:

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return
        if target == 0:
            return
        for i in range(index, len(nums)):
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)

    def combinationsSum(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res


class Solution1:
    def combinationsSum(self, condidates, target):
        """
        回溯法，层层递减，得到符合条件的路径就加入结果集，超出则剪枝
        主要注意一些细节，避免重复
        """
        size = len(candidates)
        if size <= 0:
            return
        candidates.sort()
        path = []
        res = []
        self._find_path(target, path, res, candidates, 0, size)
        return res
    def _find_path(self,target,path,res,candidates,begin,size):
      """
      沿着路径往下走
      """
      if target ==0:
        res.append(path.copy())
      else:
        for i in range(begin,size):
          left_num = target - candidates[i]
          if left_num < 0:#如果剩余数为负数，说明超过了。剪枝
            break
          #否则把当前值加入路径
          path.append(candidates[i])
          self._find_path(left_num,path,res,candidates,i,size)
          path.pop()


candidates = [2, 3, 6, 7]
target = 8

s = Solution()
s.combinationsSum(candidates, target)
