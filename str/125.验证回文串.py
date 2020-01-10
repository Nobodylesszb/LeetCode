#
# @lc app=leetcode.cn id=125 lang=python
#
# [125] 验证回文串
#
#two points 
# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l,r =0,len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                    l += 1
            while l <r and not s[r].isalnum():
                    r -= 1
            if s[l].lower() != s[r].lower():
                    return False
            l +=1; r -= 1
        return True

        
# @lc code=end

