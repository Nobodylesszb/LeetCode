'''
题目：输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
'''

'''
思路1，这一题应用堆排序算法复杂度只有O(nlog k)，堆是完全二叉树的一种，最大堆就是最上面的数是最大的
该方法基于二叉树或者堆来实现，首先把数组前k个数字构建一个最大堆，然后从第k+1个数字开始遍历数组，如果遍历到的
元素小于堆顶的数字，那么久将换两个数字，重新构造堆，继续遍历，最后剩下的堆就是最小的k个数，时间复杂度O(nlog k)。
思路2：排序
'''
import heapq

class Solution(object):
    def get_least_numbers(self,tinput,k):
        if tinput == None or len(tinput) < k or len(tinput) <= 0 or k <= 0:
            return []
        return heapq.nsmallest(k,tinput)

class Solution2:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here、
        import heapq
        if tinput == None or len(tinput) < k or len(tinput) <= 0 or k <= 0:
            return []

        return sorted(tinput)[:k]
