#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
@author: bo
@file: 1266. Minimum Time Visiting All Points.py 
@version:
@time: 2019/12/30
@function：
On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.

You can move according to the next rules:

In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
You have to visit the points in the same order as they appear in the array.
"""


class Solution:
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        # initialize count
        count = 0

        # loop through points
        for point_idx in range(len(points) - 1):
            # grab current and next point
            first_point = points[point_idx]
            second_point = points[point_idx + 1]

            # get the difference in x/y coordinates

            diff_x = abs(second_point[0] - first_point[0])
            diff_y = abs(second_point[1] - first_point[1])

            # return
            if diff_x == diff_y:
                count += diff_x
            else:
                count += max(diff_x, diff_y)

        return count
        