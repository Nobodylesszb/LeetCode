"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

"""

"""
解决这类问题的核心思想就是两个字“延伸”，具体来说

如果一个字符串是回文串，那么在它左右分别加上一个相同的字符，那么它一定还是一个回文串
如果一个字符串不是回文串，或者在回文串左右分别加不同的字符，得到的一定不是回文串
事实上，上面的分析已经建立了大问题和小问题之间的关联， 基于此，我们可以建立动态规划模型。

我们可以用 dp[i][j] 表示 s 中从 i 到 j（包括 i 和 j）是否可以形成回文， 状态转移方程只是将上面的描述转化为代码即可：

if (s[i] === s[j] && dp[i + 1][j - 1]) {
  dp[i][j] = true;
}
"""

# class Solution:
#     def longestPalindrome(self,s):
#         res = ''
#         for i in range(len(s)):
#             # odd case like 'abc'
#             tmp = self.helper(s,i,i)
#             if len(tmp) >len(res):
#                 res = tmp
#             #even case , like 'abba'
#             tmp = self.helper(s,i,i+1)
#             if len(tmp) > len(res):
#                 res = tmp
#         return res

#     def helper(self,s,l,r):
#         while l >= 0 and r < len(s) and s[l] == s[r]:
#             l -= 1; r += 1
#         return s[l+1:r]


class Solution:
    def longestPalindrome(self,s):
        if len(s) == 0:
            return 0

        maxLen = 0
        start = 0
        for i in range(len(s)):
            if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
        		start=i-maxLen-1
        		maxLen+=2
        		continue

        	if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
        		start=i-maxLen
        		maxLen+=1
        return s[start,start+maxLen]

