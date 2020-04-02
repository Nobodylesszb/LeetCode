#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
@author: bo
@file: 1304. Find N Unique Integers Sum up to Zero.py 
@version:
@time: 2019/12/30
@function： 
"""


class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [i for i in range(n - 1)]
        result.append(-sum(result))
        return result
