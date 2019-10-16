#
# @lc app=leetcode.cn id=916 lang=python3
#
# [916] 单词子集
#
# https://leetcode-cn.com/problems/word-subsets/description/
#
# algorithms
# Medium (35.70%)
# Likes:    17
# Dislikes: 0
# Total Accepted:    1.3K
# Total Submissions: 3.6K
# Testcase Example:  '["amazon","apple","facebook","google","leetcode"]\n["e","o"]'
#
# 我们给出两个单词数组 A 和 B。每个单词都是一串小写字母。
#
# 现在，如果 b 中的每个字母都出现在 a 中，包括重复出现的字母，那么称单词 b 是单词 a 的子集。 例如，“wrr” 是 “warrior”
# 的子集，但不是 “world” 的子集。
#
# 如果对 B 中的每一个单词 b，b 都是 a 的子集，那么我们称 A 中的单词 a 是通用的。
#
# 你可以按任意顺序以列表形式返回 A 中所有的通用单词。
#
#
#
#
#
#
# 示例 1：
#
# 输入：A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
# 输出：["facebook","google","leetcode"]
#
#
# 示例 2：
#
# 输入：A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
# 输出：["apple","google","leetcode"]
#
#
# 示例 3：
#
# 输入：A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
# 输出：["facebook","google"]
#
#
# 示例 4：
#
# 输入：A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
# 输出：["google","leetcode"]
#
#
# 示例 5：
#
# 输入：A = ["amazon","apple","facebook","google","leetcode"], B =
# ["ec","oc","ceo"]
# 输出：["facebook","leetcode"]
#
#
#
#
# 提示：
#
#
# 1 <= A.length, B.length <= 10000
# 1 <= A[i].length, B[i].length <= 10
# A[i] 和 B[i] 只由小写字母组成。
# A[i] 中所有的单词都是独一无二的，也就是说不存在 i != j 使得 A[i] == A[j]。
#
#
#


# @lc code=start
class Solution:
    def wordSubsets(self, A: list, B: list) -> list:
        universal_words = []
        b_dict = {}
        for b in B:
            tmp_dict = {}
            for y in b:
                tmp_dict.update({y: 1 + tmp_dict.get(y, 0)})
            for each in tmp_dict:
                if each not in b_dict or tmp_dict[each] > b_dict.get(each, 0):
                    b_dict[each] = tmp_dict[each]
        for a in A:
            a_dict = {}
            for x in list(a):
                a_dict.update({x: 1 + a_dict.get(x, 0)})
            # 判断B 是否是a的子集
            flag = True
            for each in b_dict:
                if a_dict.get(each, 0) < b_dict[each]:
                    flag = False
                    break
            if flag is True:
                universal_words.append(a)
        return universal_words


# @lc code=end
