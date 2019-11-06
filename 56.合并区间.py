#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
# https://leetcode-cn.com/problems/merge-intervals/description/
#
# algorithms
# Medium (38.86%)
# Likes:    199
# Dislikes: 0
# Total Accepted:    32.9K
# Total Submissions: 84.6K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# 给出一个区间的集合，请合并所有重叠的区间。
# 
# 示例 1:
# 
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 
# 
# 示例 2:
# 
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
# 
#

# @lc code=start
class Solution:
    def merge(self, intervals):
        """
        Arguments:
            intervals {List[List[int]]}
        """
        if len(intervals) < 2:
            return intervals
        result = []
        intervals.sort()
        left = intervals[0][0]
        right = intervals[0][1] 
        for i in range(1, len(intervals)):
            if intervals[i][0] <= right:
                if intervals[i][1] > right:
                    right = intervals[i][1]
            else:
                result.append([left, right])
                left = intervals[i][0]
                right = intervals[i][1]
        result.append([left, right])
        return result
        
# @lc code=end


