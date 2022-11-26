package main

import (
	"fmt"
)

func sortedSquares(nums []int) []int {
	n := len(nums)
	lastNegIndex := -1
	for i := 0; i < n && nums[i] < 0; i++ {
		lastNegIndex = i
	}

	ans := make([]int, 0, n)
	for i, j := lastNegIndex, lastNegIndex+1; i >= 0 || j < n; {
		if i < 0 {
			ans = append(ans, nums[j]*nums[j])
			j++
		} else if j == n {
			ans = append(ans, nums[i]*nums[i])
			i--
		} else if nums[i]*nums[i] < nums[j]*nums[j] {
			ans = append(ans, nums[i]*nums[i])
			i--
		} else {
			ans = append(ans, nums[j]*nums[j])
			j++
		}
	}

	return ans
}

func main() {
	nums := []int{-4, -1, 0, 3, 10}
	results := sortedSquares(nums)
	fmt.Println(results)
}
