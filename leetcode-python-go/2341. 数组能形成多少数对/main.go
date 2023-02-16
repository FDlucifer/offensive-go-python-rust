package main

import (
	"fmt"
)

func numberOfPairs(nums []int) []int {
	cnt := map[int]bool{}
	res := 0
	for _, num := range nums {
		cnt[num] = !cnt[num]
		if !cnt[num] {
			res++
		}
	}
	return []int{res, len(nums) - 2*res}
}

func main() {
	nums := []int{1, 3, 2, 1, 3, 2, 2}
	results := numberOfPairs(nums)
	fmt.Println(results)
}
