#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#
# https://leetcode-cn.com/problems/palindrome-number/description/
#
# algorithms
# Easy (56.66%)
# Likes:    769
# Dislikes: 0
# Total Accepted:    181.1K
# Total Submissions: 319.6K
# Testcase Example:  '121'
#
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# 
# 示例 1:
# 
# 输入: 121
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 
# 
# 示例 3:
# 
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
# 
# 
# 进阶:
# 
# 你能不将整数转为字符串来解决这个问题吗？
# 
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 我的做法
        # if x < 0:
        #     return False
        # rev_x = 0
        # origin_x = x
        # while x > 0:
        #     a = x % 10
        #     x = x // 10
        #     rev_x = rev_x * 10 + a
        # if rev_x == origin_x:
        #     return True
        # return False
        
        # 官方给出的是只比较一半数值
        if x < 0 or ( x != 0 and x % 10 ==0):
            return False
        rev_x = 0
        while x > rev_x:
            rev_x = rev_x * 10 + x % 10
            x //= 10
        return rev_x == x or rev_x // 10 == x
        
          
# @lc code=end
