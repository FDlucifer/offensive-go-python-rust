package main

import (
	"fmt"
)

func sortedSquares(nums []int) []int {
	n := len(nums)
	ans := make([]int, n)
	i, j := 0, n-1
	for pos := n - 1; pos >= 0; pos-- {
		if v, w := nums[i]*nums[i], nums[j]*nums[j]; v > w {
			ans[pos] = v
			i++
		} else {
			ans[pos] = w
			j--
		}
	}
	return ans
}

func main() {
	nums := []int{-4, -1, 0, 3, 10}
	results := sortedSquares(nums)
	fmt.Println(results)
}
