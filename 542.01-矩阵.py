#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#
# https://leetcode-cn.com/problems/01-matrix/description/
#
# algorithms
# Medium (35.06%)
# Likes:    111
# Dislikes: 0
# Total Accepted:    6.8K
# Total Submissions: 18.6K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# 给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
# 
# 两个相邻元素间的距离为 1 。
# 
# 示例 1: 
# 输入:
# 
# 
# 0 0 0
# 0 1 0
# 0 0 0
# 
# 
# 输出:
# 
# 
# 0 0 0
# 0 1 0
# 0 0 0
# 
# 
# 示例 2: 
# 输入:
# 
# 
# 0 0 0
# 0 1 0
# 1 1 1
# 
# 
# 输出:
# 
# 
# 0 0 0
# 0 1 0
# 1 2 1
# 
# 
# 注意:
# 
# 
# 给定矩阵的元素个数不超过 10000。
# 给定矩阵中至少有一个元素是 0。
# 矩阵中的元素只在四个方向上相邻: 上、下、左、右。
# 
# 
#

# @lc code=start
class Solution:
    def updateMatrix(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        update_mat = [[0 for col in range(cols)] for row in range(rows)]
        q = []
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] > 0:
                    update_mat[row][col] = 10001
                else:
                    q.append([row, col])
        while q:
            q_len = len(q)
            while q_len > 0:
                self.neighboor(q, update_mat, q.pop(0), rows, cols)
                q_len -= 1
        return update_mat
                    
    
    def neighboor(self, q, update_mat, node, rows, cols):
        neighboor_nodes = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        dis_min = update_mat[node[0]][node[1]]
        for neighboor_node in neighboor_nodes:
            x = node[0] + neighboor_node[0]
            y = node[1] + neighboor_node[1]
            if x >= 0 and y >= 0 and x < rows and y < cols:
                dis_min = min(update_mat[x][y] + 1, dis_min)
                if update_mat[x][y] == 10001:
                    q.append([x, y])
        update_mat[node[0]][node[1]] = dis_min
                    
# @lc code=end
