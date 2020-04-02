'''
题目：一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法
'''

'''
因为n级台阶，第一步有n种跳法：跳1级、跳2级、到跳n级
跳1级，剩下n-1级，则剩下跳法是f(n-1)
跳2级，剩下n-2级，则剩下跳法是f(n-2)
所以f(n)=f(n-1)+f(n-2)+...+f(1)
因为f(n-1)=f(n-2)+f(n-3)+...+f(1)
所以f(n)=2*f(n-1)
然后求解这个无穷级数的和，正确答案应该是：每次至少跳一个，至多跳n个，一共有f(n)=2n-1种跳法
29ms
5632k
'''

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        if number <2:
            return number
        # write code here
        return 2*self.jumpFloorII(number-1)