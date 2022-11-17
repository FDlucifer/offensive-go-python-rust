package main

import (
	"fmt"
	"sort"
)

func sumSubseqWidths(nums []int) int {
	const mod int = 1e9 + 7
	sort.Ints(nums)
	res, x, y := 0, nums[0], 2
	for _, num := range nums[1:] {
		res = (res + num*(y-1) - x) % mod
		x = (x*2 + num) % mod
		y = y * 2 % mod
	}
	return (res + mod) % mod
}

func main() {
	nums := []int{2, 1, 3}
	results := sumSubseqWidths(nums)
	fmt.Println(results)
}
