package main

import (
	"fmt"
)

func maxHappyGroups(batchSize int, groups []int) (ans int) {
	const kWidth = 5
	const kWidthMask = 1<<kWidth - 1

	cnt := make([]int, batchSize)
	for _, x := range groups {
		cnt[x%batchSize]++
	}

	start := 0
	for i := batchSize - 1; i > 0; i-- {
		start = start<<kWidth | cnt[i]
	}

	memo := map[int]int{}
	var dfs func(int) int
	dfs = func(mask int) (best int) {
		if mask == 0 {
			return
		}
		if res, ok := memo[mask]; ok {
			return res
		}

		total := 0
		for i := 1; i < batchSize; i++ {
			amount := mask >> ((i - 1) * kWidth) & kWidthMask
			total += i * amount
		}

		for i := 1; i < batchSize; i++ {
			amount := mask >> ((i - 1) * kWidth) & kWidthMask
			if amount > 0 {
				result := dfs(mask - 1<<((i-1)*kWidth))
				if (total-i)%batchSize == 0 {
					result++
				}
				best = max(best, result)
			}
		}
		memo[mask] = best
		return
	}
	return dfs(start) + cnt[0]
}

func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}

func main() {
	batchSize := 4
	groups := []int{1, 3, 2, 5, 2, 2, 1, 6}
	results := maxHappyGroups(batchSize, groups)
	fmt.Println(results)
}
