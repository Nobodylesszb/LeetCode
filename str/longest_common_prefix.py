class Solution(object):
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
            
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)

strs = ["flower","flow","flight"]
print(list(zip(*strs)))

s = Solution()
t= s.longestCommonPrefix(strs)
print(t)