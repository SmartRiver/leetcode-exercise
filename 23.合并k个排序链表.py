#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (47.58%)
# Likes:    359
# Dislikes: 0
# Total Accepted:    49.4K
# Total Submissions: 103.7K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
# 
# 示例:
# 
# 输入:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists) -> ListNode:
        # 特殊case会超时
        # if not lists:
        #     return None
        # if len(lists) == 1:
        #     return lists[0]
        
        # first_node = lists.pop(0)
        # while lists:
        #     l1 = lists.pop(0)
        #     first_node = self.mergeTwoLists(first_node, l1)
            
        # return first_node
        
        # 官方题解，使用分治
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None

            
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dump_node = ListNode(0)
        cur = dump_node
        
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            cur = cur.next
            
        cur.next = l1 if l1 is not None else l2
        
        return dump_node.next
        
        
# @lc code=end
