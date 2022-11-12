package main

import (
	"bufio"
	"fmt"
	"os"
)

var n, m int

const MOD = 998244353

func main() {
	in := bufio.NewReader(os.Stdin)
	fmt.Fscan(in, &n, &m)
	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, n+1)
	}
	for i := 1; i <= n; i++ {
		dp[0][i] = 1
	}
	for i := 0; i < m-1; i++ {
		for j := 1; j <= n; j++ {
			for k := 1; j*k <= n; k++ {
				dp[i+1][j*k] = (dp[i+1][j*k] + dp[i][j]) % MOD
			}
		}
	}
	var res int
	for i := 1; i <= n; i++ {
		res = (res + dp[m-1][i]) % MOD
	}
	fmt.Println(res)
}
