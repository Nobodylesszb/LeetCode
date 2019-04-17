'''
题目：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''

'''
将输入数组转成字符串，利用cmp比较mn或者nm的大小，进行从小到大的排序
notes:
31ms
5596k
'''

import operator

# -*- coding:utf-8 -*-
from functools import cmp_to_key
class Solution:
    def cmp(self,a,b):
        if a+b>b+a:
            return 1
        if a+b<b+a:
            return -1
        else:
            return 0
    def PrintMinNumber(self,numbers):
        if not numbers:
            return ""
        number = list(map(str,numbers))
        number.sort(key=cmp_to_key(self.cmp))
        return "".join(number).lstrip('0') or '0' 
arr = [3,32,321]
s = Solution()
r = s.PrintMinNumber(arr)
print(r)