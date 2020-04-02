"""
We can use the standard two-pointer approach 
that starts at the left and right of the string and move inwards. Whenever there is a mismatch, we can either exclude the character at the left or the right pointer. We then take the two remaining substrings and compare against its reversed and see if either one is a palindrome.
"""

class Solution:
    def validPalindrome(self,s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True
