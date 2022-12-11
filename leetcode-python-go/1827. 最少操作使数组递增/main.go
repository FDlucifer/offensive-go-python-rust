package main

import (
	"fmt"
)

func minOperations(nums []int) (ans int) {
	pre := nums[0] - 1
	for _, x := range nums {
		pre = max(pre+1, x)
		ans += pre - x
	}
	return
}

func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}

func main() {
	nums := []int{1, 5, 2, 4, 1}
	results := minOperations(nums)
	fmt.Println(results)
}
