package main

//给你二叉搜索树的根节点 root ，该树中的 恰好 两个节点的值被错误地交换。请在不改变其结构的情况下，恢复这棵树 。
//
// 
//
// 示例 1： 
//
// 
//输入：root = [1,3,null,null,2]
//输出：[3,1,null,null,2]
//解释：3 不能是 1 的左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。
// 
//
// 示例 2： 
//
// 
//输入：root = [3,1,4,null,null,2]
//输出：[2,1,4,null,null,3]
//解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。 
//
// 
//
// 提示： 
//
// 
// 树上节点的数目在范围 [2, 1000] 内 
// -2³¹ <= Node.val <= 2³¹ - 1 
// 
//
// 
//
// 进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用 O(1) 空间的解决方案吗？ 
// Related Topics 树 深度优先搜索 二叉搜索树 二叉树 👍 699 👎 0

//leetcode submit region begin(Prohibit modification and deletion)


// TreeNode Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func recoverTree(root *TreeNode) {
	// 构造序列 nums
	nums := []int{}
	inorder(root, nums)
	// 找出序列中被错误交换的点，可能一个/二个
	x, y := findErrorPos(nums)
	// 恢复交换的点
	swapErrorPos(root, 2, x, y)
}

func inorder(node *TreeNode, nums []int) {
	if node == nil {
		return
	}
	inorder(node.Left, nums)
	nums = append(nums, node.Val)
	inorder(node.Right, nums)
}

func findErrorPos(nums []int) (x, y int) {
	index1, index2 := -1, -1
	for index := 0; index < len(nums)-1; index++ {
		if nums[index] > nums[index+1] {
			index2 = index + 1
			if index1 == -1 {
				index1 = index
			} else {
				break
			}
		}
	}
	x, y = nums[index1], nums[index2]
	return
}

func swapErrorPos(node *TreeNode, count, x, y int) {
	if node.Val == x {
		node.Val = y
		count--
	}
	if node.Val == y {
		node.Val = x
		count--
	}
	if count == 0 {
		return
	}
	swapErrorPos(node.Left, count, x, y)
	swapErrorPos(node.Right, count, x, y)
}

//leetcode submit region end(Prohibit modification and deletion)
