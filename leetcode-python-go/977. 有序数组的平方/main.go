package main

import (
	"fmt"
	"sort"
)

func sortedSquares(nums []int) []int {
	ans := make([]int, len(nums))
	for i, v := range nums {
		ans[i] = v * v
	}
	sort.Ints(ans)
	return ans
}

func main() {
	nums := []int{-4, -1, 0, 3, 10}
	results := sortedSquares(nums)
	fmt.Println(results)
}
