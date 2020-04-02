#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
@author: bo
@file: 1252. Cells with Odd Values in a Matrix Easy.py 
@version:
@time: 2019/12/30
@function： 
"""


class Solution:
    def oddCells(self, n, m, indices):

        matrix = [[0 for x in range(m)] for y in range(n)]

        for index in indices:
            for row in range(n):
                matrix[row][index[1]] += 1
            for col in range(m):
                matrix[index[0]][col] += 1

        odd_count =0
        for row in range(n):
            for col in range(m):
                if matrix[row][col] % 2 != 0:
                    odd_count += 1

        return odd_count


if __name__ == '__main__':
    n = 2
    m = 3
    indices = [[0, 1], [1, 1]]
    s = Solution()
    print(s.oddCells(n, m, indices))