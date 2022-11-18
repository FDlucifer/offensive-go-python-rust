package main

import (
	"fmt"
)

func largestAltitude(gain []int) (ans int) {
	total := 0
	for _, x := range gain {
		total += x
		ans = max(ans, total)
	}
	return
}

func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}

func main() {
	gain := []int{-5, 1, 5, 0, -7}
	results := largestAltitude(gain)
	fmt.Println(results)
}
