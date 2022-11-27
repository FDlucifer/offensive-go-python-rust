package main

import (
	"fmt"
)

func check(nums []int) bool {
	cnt := 0
	for i, v := range nums {
		if v > nums[(i+1)%len(nums)] {
			cnt++
		}
	}
	return cnt <= 1
}

func main() {
	nums := []int{3, 4, 5, 1, 2}
	results := check(nums)
	fmt.Println(results)
}
