package main

import (
	"fmt"
)

func splitArraySameAverage(nums []int) bool {
	sum := 0
	for _, x := range nums {
		sum += x
	}

	n := len(nums)
	m := n / 2
	isPossible := false
	for i := 1; i <= m; i++ {
		if sum*i%n == 0 {
			isPossible = true
			break
		}
	}
	if !isPossible {
		return false
	}

	dp := make([]map[int]bool, m+1)
	for i := range dp {
		dp[i] = map[int]bool{}
	}
	dp[0][0] = true
	for _, num := range nums {
		for i := m; i >= 1; i-- {
			for x := range dp[i-1] {
				curr := x + num
				if curr*n == sum*i {
					return true
				}
				dp[i][curr] = true
			}
		}
	}
	return false
}

func main() {
	nums := []int{1, 2, 3, 4, 5, 6, 7, 8}
	results := splitArraySameAverage(nums)
	fmt.Println(results)
}
