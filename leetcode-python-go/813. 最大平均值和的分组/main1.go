package main

import (
	"fmt"
	"math"
)

func largestSumOfAverages(nums []int, k int) float64 {
	n := len(nums)
	prefix := make([]float64, n+1)
	for i, x := range nums {
		prefix[i+1] = prefix[i] + float64(x)
	}
	dp := make([]float64, n+1)
	for i := 1; i <= n; i++ {
		dp[i] = prefix[i] / float64(i)
	}
	for j := 2; j <= k; j++ {
		for i := n; i >= j; i-- {
			for x := j - 1; x < i; x++ {
				dp[i] = math.Max(dp[i], dp[x]+(prefix[i]-prefix[x])/float64(i-x))
			}
		}
	}
	return dp[n]
}

func main() {
	nums := []int{9, 1, 2, 3, 9}
	k := 3
	results := largestSumOfAverages(nums, k)
	fmt.Println(results)
}
