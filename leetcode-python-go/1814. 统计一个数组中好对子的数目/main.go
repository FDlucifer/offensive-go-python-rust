package main

import (
	"fmt"
)

func countNicePairs(nums []int) (ans int) {
	cnt := map[int]int{}
	for _, num := range nums {
		rev := 0
		for x := num; x > 0; x /= 10 {
			rev = rev*10 + x%10
		}
		ans += cnt[num-rev]
		cnt[num-rev]++
	}
	return ans % (1e9 + 7)
}

func main() {
	nums := []int{42, 11, 1, 97}
	results := countNicePairs(nums)
	fmt.Println(results)
}
