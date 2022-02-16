package main

import (
	"fmt"
	"math"
	"sort"
)

func findClosestNum(nums []int, target int) int {

	closest := nums[0] - target
	minAbs := math.Abs(float64(closest))
	for i, num := range nums {
		if i == 0 {
			continue
		}
		if num > target {
			if math.Abs(float64(num-target)) < minAbs {
				closest = num - target
			}
			break
		} else {
			closest = num - target
			minAbs = math.Abs(float64(closest))
		}

	}
	return closest
}

func twoSumClosest(nums []int, target int) int {
	var r, closest int
	var minAbs float64
	var lessNums []int
	copyNums := make([]int, len(nums))
	for i, num := range nums {
		copy(copyNums, nums)
		lessNums = append(copyNums[:i], copyNums[i+1:]...)
		r = findClosestNum(lessNums, target-num)
		if closest == 0 {
			closest = r
			minAbs = math.Abs(float64(r))
		} else {
			if r == 0 {
				closest = r
				break
			}
			if math.Abs(float64(r)) < minAbs {
				minAbs = math.Abs(float64(r))
				closest = r
			}
		}
		if closest == 0 {
			break
		}
	}
	return closest
}

func threeSumClosest(nums []int, target int) int {
	sort.Ints(nums)
	var r, closest int
	var minAbs float64
	var lessNums []int
	copyNums := make([]int, len(nums))
	for i, num := range nums {
		copy(copyNums, nums)
		lessNums = append(copyNums[:i], copyNums[i+1:]...)
		r = twoSumClosest(lessNums, target-num)
		if closest == 0 {
			closest = r
			minAbs = math.Abs(float64(r))
		} else {
			if r == 0 {
				closest = r
				break
			}
			if math.Abs(float64(r)) < minAbs {
				minAbs = math.Abs(float64(r))
				closest = r
			}
		}
		if closest == 0 {
			break
		}
	}
	return closest + target
}

func main() {
	//nums := []int{-111,-111,3,6,7,16,17,18,19}
	nums := []int{-1, 2, 1, -4}
	fmt.Print(threeSumClosest(nums, 1))
}
