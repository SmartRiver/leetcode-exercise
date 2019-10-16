#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (35.93%)
# Likes:    550
# Dislikes: 0
# Total Accepted:    82.5K
# Total Submissions: 229.5K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
# 
# 示例：
# 
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
# 
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 
# 
# 说明：
# 
# 给定的 n 保证是有效的。
# 
# 进阶：
# 
# 你能尝试使用一趟扫描实现吗？
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None or head.next is None:
            return None
        p = head
        node_list = []
        while p:
            node_list.append(p)
            p = p.next
        if n == len(node_list):
            return node_list[1]
        elif n == 1:
            node_list[-2].next = None
        else:
            node_list[-n-1].next = node_list[-n+1]
        return node_list[0]
            
        
# @lc code=end
