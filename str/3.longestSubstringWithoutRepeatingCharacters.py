"""
Given a string, find the length of the 
longest substring without repeating characters.
"""

"""
用一个hashmap来建立字符和其出现位置之间的映射。

维护一个滑动窗口，窗口内的都是没有重复的字符，去尽可能的扩大窗口的大小，窗口不停的向右滑动。

（1）如果当前遍历到的字符从未出现过，那么直接扩大右边界；

（2）如果当前遍历到的字符出现过，则缩小窗口（左边索引向右移动），然后继续观察当前遍历到的字符；

（3）重复（1）（2），直到左边索引无法再移动；

（4）维护一个结果res，每次用出现过的窗口大小来更新结果res，最后返回res获取结果。


"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        used = {}
        max_length = start = 0
        for i,c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c]+1
            else:
                max_length = max(max_length,i-start+1)
            used[c] = i
        return max_length

str = "abcabcbb"

s =Solution()
s.lengthOfLongestSubstring(str)