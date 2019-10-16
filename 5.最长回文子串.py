#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_list = list(s)
        if len(s_list) < 1:
            return ''
        start = end = 0
        for i in range(len(s_list)):
            len1 = self.expandAroundCenter(s_list, i, i)
            len2 = self.expandAroundCenter(s_list, i, i+1)
            i_max_len = max(len1, len2)
            if i_max_len > (end - start):
                start = i - (i_max_len - 1) // 2
                end = i + i_max_len // 2
        return ''.join(s_list[start:end+1])
        
    def expandAroundCenter(self, s_list: list, left: int, right: int) ->int:
        L = left
        R = right
        while L>= 0 and R < len(s_list) and s_list[L] == s_list[R]:
            L -= 1
            R += 1
        return R - L - 1
        
# @lc code=end
