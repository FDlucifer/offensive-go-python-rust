package main

import (
	"fmt"
)

func numSubarrayBoundedMax(nums []int, left int, right int) int {
	count := func(lower int) (res int) {
		cur := 0
		for _, x := range nums {
			if x <= lower {
				cur++
			} else {
				cur = 0
			}
			res += cur
		}
		return
	}
	return count(right) - count(left-1)
}

func main() {
	nums := []int{2, 1, 4, 3}
	left := 2
	right := 3
	results := numSubarrayBoundedMax(nums, left, right)
	fmt.Println(results)
}
