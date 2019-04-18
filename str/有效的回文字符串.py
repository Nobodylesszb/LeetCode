"""
给一个字符串，判断他是否是回文的
"""
"""
方法一采用双指针形式
"""
class Solution(object):
    def isParlidrome(self,s):
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l <r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l +=1; r -= 1   
        return True

"""
利用列表表达式
"""
class Solution2(object):
    def isPalindrome(self, s):
        chk = [ch.lower() for ch in s if ch.isalnum()]
        return chk == chk[::-1]


            
        
        

