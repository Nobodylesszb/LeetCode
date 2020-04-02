"""
giving a string,find the first non_repeating char in it and 
it's index , if it doesn't exit,return -1
"""
import collections
class Solution(object):
    def firstUniqChar(self, s):
        return min([s.find(c) for c,v in collections.Counter(s).iteritems() if v==1] or [-1])