#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
@author: bo
@file: 1295.FindNumberswithEvenNumberofDigits.py
@version:
@time: 2019/12/30
@function： 
"""


class Solution:
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        for num in nums:
            if (num >= 10 and num < 100) or (num >= 1000 and num < 10000):
                s += 1

        return s

    def findNumbers_two(self, nums):
        return len([i for i in nums if len(str(i)) % 2 == 0])
