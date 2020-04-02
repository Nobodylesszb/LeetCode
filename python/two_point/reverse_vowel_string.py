"""
The idea is really simple.
Convert string to list then convert back
Pointer processing is verbose.

"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left].lower() not in vowels:
                left += 1
            elif s[right].lower() not in vowels:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left, right = left + 1, right - 1
        
        return ''.join(s)