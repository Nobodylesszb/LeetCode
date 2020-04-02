class Solution():
    def longest_palindrome_prefix(self,s):
        if not s:
            return 0
        s = s + '#' + s[::-1] + '$'
        i = 0
        j = -1
        nt = [0] * len(s)
        nt[0] = -1
        while i < len(s) - 1:
            if j == -1 or s[i] == s[j]:
                i += 1
                j += 1
                nt[i] = j
            else:
                j = nt[j]
        return nt[len(s) - 1]
    def longest_palindrome_prefix2(self,s):
        index =[]
        if not s:
            return 0
        l = len(s)
        for i in range(l):
            index = s.index(s[i:],s[i])
            


string = 'abbabbc'
print (string.index(string[1:],'a'))
# s = Solution()
# r = s.longest_palindrome_prefix(string)
# print(string[:r])