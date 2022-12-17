package main

import (
	"fmt"
)

func canChoose(groups [][]int, nums []int) bool {
next:
	for _, g := range groups {
		for len(nums) >= len(g) {
			if equal(nums[:len(g)], g) {
				nums = nums[len(g):]
				continue next
			}
			nums = nums[1:]
		}
		return false
	}
	return true
}

func equal(a, b []int) bool {
	for i, x := range a {
		if x != b[i] {
			return false
		}
	}
	return true
}

func main() {
	groups := [][]int{{1, -1, -1}, {3, -2, 0}}
	nums := []int{1, -1, 0, 1, -1, -1, 3, -2, 0}
	results := canChoose(groups, nums)
	fmt.Println(results)
}
