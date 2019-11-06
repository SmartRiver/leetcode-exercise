#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (58.77%)
# Likes:    280
# Dislikes: 0
# Total Accepted:    51.8K
# Total Submissions: 88.2K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
# 示例 1:
#
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
#
#
# 示例 2:
#
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
#
# 说明:
#
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
#
#


# @lc code=start
class Solution:
    def findKthLargest(self, nums, k) -> int:
        """用k长度的有序列表维持k个最大的元素
        
        Arguments:
            nums {List[int]} --
            k {int} --
        
        Returns:
            int -- 第K个最大的元素
        """
        if len(nums) < k:
            return min(nums)
        k_large = [nums[0]]
        for num in nums[1:]:
            if num > k_large[0] or len(k_large) < k:
                for i, k_num in enumerate(k_large):
                    if num < k_num:
                        k_large.insert(i, num)
                        break
                    if i == (len(k_large) - 1):
                        k_large.append(num)
                        break
                if len(k_large) > k:
                    k_large.pop(0)
        return k_large[0]


# @lc code=end
