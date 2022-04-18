package main

import "fmt"

// TreeNode Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func recoverTree(root *TreeNode) {
	// 构造序列 nums
	nums := []int{}

	var inorder func(node *TreeNode)
	inorder = func(node *TreeNode) {
		if node == nil {
			return
		}
		inorder(node.Left)
		nums = append(nums, node.Val)
		inorder(node.Right)
	}

	inorder(root)
	// 找出序列中被错误交换的点，可能一个/二个
	x, y := findErrorPos(nums)
	// 恢复交换的点
	swapErrorPos(root, 2, x, y)
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
	if node == nil {
		return
	}
	if node.Val == x || node.Val == y {
		if node.Val == x {
			node.Val = y
		}else {
			node.Val = x
		}
		count--
		if count == 0 {
			return
		}
	}
	swapErrorPos(node.Left, count, x, y)
	swapErrorPos(node.Right, count, x, y)
}

func main() {
	root := &TreeNode{
		Val: 1,
		Left: &TreeNode{
			Val: 3,
			Left: nil,
			Right: &TreeNode{
				Val: 2,
				Left: nil,
				Right: nil,
			},
		},
		Right: nil,
	}
	recoverTree(root)
}