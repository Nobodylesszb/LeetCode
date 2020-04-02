class Solution:
    def reverseBits(self, n):
            res = 0
            for _ in range(32):
                res = (res<<1) + (n&1) # 右移动
                n>>=1 # 左移
            return res



s =Solution()
b = s.reverseBits(101010111)
print(b)

