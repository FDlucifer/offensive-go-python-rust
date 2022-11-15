package main

import (
	"fmt"
)

func isIdealPermutation(nums []int) bool {
	for i, x := range nums {
		if abs(x-i) > 1 {
			return false
		}
	}
	return true
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	nums := []int{1, 0, 2}
	results := isIdealPermutation(nums)
	fmt.Println(results)
}
