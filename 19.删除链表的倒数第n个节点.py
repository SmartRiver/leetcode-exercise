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
        # if head is None or head.next is None:
        #     return None
        # p = head
        # node_list = []
        # while p:
        #     node_list.append(p)
        #     p = p.next
        # if n == len(node_list):
        #     return node_list[1]
        # elif n == 1:
        #     node_list[-2].next = None
        # else:
        #     node_list[-n-1].next = node_list[-n+1]
        # return node_list[0]
        
        # 官方题解
        # 利用双指针第一个指针从列表的开头向前移动 n+1 步，而第二个指针将从列表
        # 的开头出发。现在，这两个指针被 nn 个结点分开。
        # 我们通过同时移动两个指针向前来保持这个恒定的间隔，
        # 直到第一个指针到达最后一个结点。
        # 此时第二个指针将指向从最后一个结点数起的第 n 个结点。
        # 我们重新链接第二个指针所引用的结点的 next 指针指向该结点的下下个结点。
        empty_node = ListNode(0)
        empty_node.next = head
        first_point = empty_node
        second_point = empty_node
        for _ in range(n+1):
            first_point = first_point.next
        while first_point is not None:
            first_point = first_point.next
            second_point = second_point.next
        second_point.next = second_point.next.next
        return  empty_node.next
             
# @lc code=end
