package main

import (
	"fmt"
)

func minOperations(nums []int) (ans int) {
	n := len(nums)

	pre := 0

	for i := 1; i < n; i++ {
		cur := 0
		if nums[i] > pre+nums[i-1] {
			cur = 0
		} else {
			cur = pre + nums[i-1] - nums[i] + 1
		}
		ans += cur
		pre = cur
	}

	return
}

func main() {
	nums := []int{1, 5, 2, 4, 1}
	results := minOperations(nums)
	fmt.Println(results)
}
