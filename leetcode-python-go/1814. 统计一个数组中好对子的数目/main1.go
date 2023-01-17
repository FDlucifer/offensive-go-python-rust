package main

import (
	"fmt"
)

const M int = 1000000007

func countNicePairs(nums []int) int {
	maps := make(map[int]int, 0)
	for _, v := range nums {
		val := v
		curr := 0
		for v > 0 {
			curr = curr*10 + v%10
			v /= 10
		}
		maps[val-curr] += 1
	}
	ans := 0
	for _, v := range maps {
		ans = (ans + v*(v-1)/2) % M
	}
	return ans
}

func main() {
	nums := []int{42, 11, 1, 97}
	results := countNicePairs(nums)
	fmt.Println(results)
}
