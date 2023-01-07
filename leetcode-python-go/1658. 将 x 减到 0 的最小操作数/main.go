package main

import (
	"fmt"
)

func minOperations(nums []int, x int) int {
	n := len(nums)
	sum := 0
	for _, num := range nums {
		sum += num
	}
	if sum < x {
		return -1
	}

	right := 0
	lsum := 0
	rsum := sum
	ans := n + 1

	for left := -1; left < n; left++ {
		if left != -1 {
			lsum += nums[left]
		}
		for right < n && lsum+rsum > x {
			rsum -= nums[right]
			right++
		}
		if lsum+rsum == x {
			ans = min(ans, (left+1)+(n-right))
		}
	}
	if ans > n {
		return -1
	}
	return ans
}

func min(a, b int) int {
	if b < a {
		return b
	}
	return a
}

func main() {
	nums := []int{5, 6, 7, 8, 9}
	x := 4
	results := minOperations(nums, x)
	fmt.Println(results)
}
