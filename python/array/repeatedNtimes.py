class Solution:
    def repeatedNtimes(self, a):
        return int(sum(a)- sum(set(a)))