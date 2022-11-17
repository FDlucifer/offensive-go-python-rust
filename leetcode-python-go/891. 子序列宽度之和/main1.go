package main

import (
	"fmt"
	"sort"
)

func sumSubseqWidths(nums []int) int {
	sort.Ints(nums)
	const M int64 = 1000000007
	n := len(nums)
	var ans int64 = 0
	power := make([]int64, 100010)
	power[0] = 1
	for i := 1; i <= n; i++ {
		power[i] = power[i-1] * int64(2) % M
	}
	for i := 0; i < n; i++ {
		l := i
		r := n - 1 - i
		ans = (ans + (power[l]-power[r])*int64(nums[i])%M + M) % M
	}
	return int(ans)
}

func main() {
	nums := []int{2, 1, 3}
	results := sumSubseqWidths(nums)
	fmt.Println(results)
}
