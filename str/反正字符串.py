"""
给一个字符串每隔2k个字符反转k个
"""

class Solution:
    def reverseStr(self, s, k):
    s = list(s)
    for i in xrange(0, len(s), 2*k):
        s[i:i+k] = reversed(s[i:i+k])
    return "".join(s)