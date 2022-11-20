package main

import (
	"fmt"
)

func soupServings(n int) float64 {
	n = (n + 24) / 25
	if n >= 179 {
		return 1
	}
	dp := make([][]float64, n+1)
	for i := range dp {
		dp[i] = make([]float64, n+1)
	}
	dp[0][0] = 0.5
	for i := 1; i <= n; i++ {
		dp[0][i] = 1
	}
	for i := 1; i <= n; i++ {
		for j := 1; j <= n; j++ {
			dp[i][j] = (dp[max(0, i-4)][j] + dp[max(0, i-3)][max(0, j-1)] +
				dp[max(0, i-2)][max(0, j-2)] + dp[max(0, i-1)][max(0, j-3)]) / 4
		}
	}
	return dp[n][n]
}

func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}

func main() {
	n := 50
	results := soupServings(n)
	fmt.Println(results)
}
