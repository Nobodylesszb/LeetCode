
class Solution:
    def moveZeros(self,nums):
        last0 = 0
        for i in range (0,len(nums)):
            if nums[i] != 0:
                nums[i],nums[last0] = nums[last0],nums[i]
                last0 +=1 # 指向0的位置




a = [1,0,3,12]

s = Solution()
s.moveZeros(a)