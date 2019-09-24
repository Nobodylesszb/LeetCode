"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
#由于题目对于交易次数有限制，只能交易一次，
# 因此问题的本质其实就是求相邻波峰浪谷的差值的最大值。
class Solution:
    def maxProfit(self, prices):
        if len(prices) <=1:
            return 0 
        min_ = prices[0]
        max_ = 0

        for i in range(1,len(prices)):
            if prices[i] <min_:
                min_ = prices[i]
            diff = prices[i] - min_
            if diff > max_:
                max_ = diff
            return max_

class Solution1:
    def maxProfit(self,prices):
        if not prices:
            return 0
        min_price = 0
        max_profit = 0
        for price in prices:
            if prices <min_price:
                min_price = price
            elif max_profit < price - min_price:
                max_profit = price - min_price
        return max_profit
