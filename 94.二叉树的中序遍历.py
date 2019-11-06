#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (68.39%)
# Likes:    311
# Dislikes: 0
# Total Accepted:    72.2K
# Total Submissions: 105.1K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的中序 遍历。
# 
# 示例:
# 
# 输入: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# 输出: [1,3,2]
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
        # 递归
        # res = []
        # if root is None:
        #     return []
        # res.extend(self.inorderTraversal(root.left))
        # res.append(root.val)
        # res.extend(self.inorderTraversal(root.right))
        # return res
        
        # 迭代
        p = root
        res = []
        node_stack = []
        while p or node_stack:
            while p:
                node_stack.append(p)
                p = p.left
            p = node_stack.pop(0)
            res.append(p.val)
            p = p.right
        return res
                
# @lc code=end
