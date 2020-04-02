"""
Given an array nums of n integers, 
are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
"""
"""
Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

"""
我们采用分治的思想. 想要找出三个数相加等于0，我们可以数组依次遍历， 每一项a[i]我们都认为它是最终能够用组成0中的一个数字，那么我们的目标就是找到 剩下的元素（除a[i]）两个相加等于-a[i].

通过上面的思路，我们的问题转化为了给定一个数组，找出其中两个相加等于给定值， 这个问题是比较简单的， 我们只需要对数组进行排序，然后双指针解决即可。 加上我们需要外层遍历依次数组，因此总的时间复杂度应该是O(N^2)。
在这里之所以要排序解决是因为， 我们算法的瓶颈在这里不在于排序，而在于O(N^2)，如果我们瓶颈是排序，就可以考虑别的方式了

如果找某一个特定元素，一个指针就够了。如果是找两个元素满足一定关系（比如求和等于特定值），需要双指针， 当然前提是数组有序
"""


class Solution:
  def threeSum(self,nums):
    res = []
    nums.sort()
    for i in range(len(nums)-2):
      if i > 0 and nums[i] == nums[i-1]:
        continue
      l, r = i +1 ,len(nums)-1
      while l < r:
        s = nums[i] + nums[l] + nums[r]
        if s < 0:
          l += 1
        elif s>0:
          r -= 1
        else:
          res.append((nums[i],nums[l],nums[r]))
          while l < r and nums[l] == nums[l+1]:
            l += 1
          while l < r and nums[r] == nums[r-l]:
            r -= 1
          l +=1
          r -= 1
    return res

