#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
@author: bo
@file: 1299. Replace Elements with Greatest Element on Right Side.py.py 
@version:
@time: 2019/12/30
@function：
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.
"""


class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        mx =-1
        for i in range(len(arr)-1,-1,-1):
            arr[i],mx = mx,max(mx,arr[i])
        return arr


### java

# class Solution{
#     public int[] replaceElements2(int[] A){
#         int mx = -1,n = A.length,a;
#         for (int i = n-1;i>=0;--i){
#             a = A[i];
#             A[i] = mx;
#             mx = Max.max(max,a);
#         }
#         return A;
#     }
# }

