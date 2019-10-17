#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (47.46%)
# Likes:    228
# Dislikes: 0
# Total Accepted:    22.5K
# Total Submissions: 47.5K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
# 
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
# 
# 示例:
# 
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        idx = 0
        dumpNode = ListNode(-1)
        dumpNode.next = head
        cur = dumpNode
        startNode = None
        endNode = None
        reversePart = None
        while cur:
            if idx == m - 1:
                startNode = cur
            elif idx >= m:
                if idx == m:
                    endNode = ListNode(cur.val)
                    reversePart = endNode
                elif idx == n+1:
                    endNode.next = cur
                    break
                else:
                    tmp = ListNode(cur.val)
                    tmp.next = reversePart
                    reversePart = tmp
            idx += 1
            cur = cur.next
        startNode.next = reversePart
        return dumpNode.next
                
            
    
            
# @lc code=end
