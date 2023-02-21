package main

import (
	"fmt"
	"math"
	"sort"
)

func minTaps(n int, ranges []int) int {
	intervals := [][2]int{}
	for i, r := range ranges {
		start := max(0, i-r)
		end := min(n, i+r)
		intervals = append(intervals, [2]int{start, end})
	}
	sort.Slice(intervals, func(i, j int) bool {
		a, b := intervals[i], intervals[j]
		return a[0] < b[0]
	})

	dp := make([]int, n+1)
	for i := range dp {
		dp[i] = math.MaxInt
	}
	dp[0] = 0
	for _, p := range intervals {
		start, end := p[0], p[1]
		if dp[start] == math.MaxInt {
			return -1
		}
		for j := start; j <= end; j++ {
			dp[j] = min(dp[j], dp[start]+1)
		}
	}
	return dp[n]
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
