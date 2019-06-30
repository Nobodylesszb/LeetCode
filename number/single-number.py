"""
Given a non-empty array of integers, 
every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""
"""关键点
异或的性质 两个数字异或的结果a^b是将 a 和 b 的二进制每一位进行运算，得出的数字。 运算的逻辑是 如果同一位的数字相同则为 0，不同则为 1

异或的规律

任何数和本身异或则为0

任何数和 0 异或是本身

很多人只是记得异或的性质和规律，但是缺乏对其本质的理解，导致很难想到这种解法（我本人也没想到）

bit 运算

"""
class Solution(object):
    def singNum(self,nums):
        res = 0
        for num in nums:
            res ^= num
            print(num,'____________',res)
        return res
    

c = [1,2,3,5,4,5,4,3,1]

s = Solution()

b = s.singNum(c)
print(b)


