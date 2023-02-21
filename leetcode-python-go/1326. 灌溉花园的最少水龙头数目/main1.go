package main

import (
	"fmt"
)

func minTaps(n int, ranges []int) int {
	rightMost := make([]int, n+1)
	for i := range rightMost {
		rightMost[i] = i
	}
	for i, r := range ranges {
		start := max(0, i-r)
		end := min(n, i+r)
		rightMost[start] = max(rightMost[start], end)
	}

	last, ret, pre := 0, 0, 0
	for i := 0; i < n; i++ {
		last = max(last, rightMost[i])
		if i == last {
			return -1
		}
		if i == pre {
			ret++
			pre = last
		}
	}
	return ret
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}

func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}

func main() {
	n := 5
	ranges := []int{3, 4, 1, 1, 0, 0}
	results := minTaps(n, ranges)
	fmt.Println(results)
}
