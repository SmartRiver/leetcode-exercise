package main

import "fmt"

func moveZeroes(nums []int)  {
	n := len(nums)
	l, r := 0, 0
	for r < n {
		if 0 != nums[r] {
			nums[l], nums[r] = nums[r], nums[l]
			l++
		}
		r++
	}
}

func main(){
	nums := []int{4,2,4,0,0,3,0,5,1,0}
	moveZeroes(nums)
	fmt.Print(nums)
}