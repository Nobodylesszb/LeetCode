"""
Given n non-negative integers a1, a2, ..., an , 
where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, 
such that the container contains the most water.
"""

"""
符合直觉的解法是，我们可以对两两进行求解，计算可以承载的水量。 然后不断更新最大值，
最后返回最大值即可。 这种解法，需要两层循环，时间复杂度是O(n^2)
"""
class Solution:
    def maxArea(self,height):
        max_area = area = 0
        left, right = 0,len(height) -1
        while left < right:
            l,r = height[left],height[right]
            if l < r:
                area = (right -left) * l
                while height[left] <= l:
                    left +=1
            else:
                area = (right- left) * r
                while height[right] <= r and right:
                    right -= 1
            if area > max_area:
                max_area = area
        return max_area
