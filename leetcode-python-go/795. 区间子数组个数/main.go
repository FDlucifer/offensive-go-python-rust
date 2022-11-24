package main

import (
	"fmt"
)

func numSubarrayBoundedMax(nums []int, left int, right int) (res int) {
	last2, last1 := -1, -1
	for i, x := range nums {
		if left <= x && x <= right {
			last1 = i
		} else if x > right {
			last2 = i
			last1 = -1
		}
		if last1 != -1 {
			res += last1 - last2
		}
	}
	return
}

func main() {
	nums := []int{2, 1, 4, 3}
	left := 2
	right := 3
	results := numSubarrayBoundedMax(nums, left, right)
	fmt.Println(results)
}
