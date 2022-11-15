package main

import (
	"fmt"
)

func isIdealPermutation(nums []int) bool {
	n := len(nums)
	minSuf := nums[n-1]
	for i := n - 2; i > 0; i-- {
		if nums[i-1] > minSuf {
			return false
		}
		minSuf = min(minSuf, nums[i])
	}
	return true
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}

func main() {
	nums := []int{1, 0, 2}
	results := isIdealPermutation(nums)
	fmt.Println(results)
}
