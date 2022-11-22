package main

import (
	"fmt"
)

func countBalls(lowLimit, highLimit int) (ans int) {
	count := map[int]int{}
	for i := lowLimit; i <= highLimit; i++ {
		sum := 0
		for x := i; x > 0; x /= 10 {
			sum += x % 10
		}
		count[sum]++
		ans = max(ans, count[sum])
	}
	return
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	lowLimit := 1
	highLimit := 10
	results := countBalls(lowLimit, highLimit)
	fmt.Println(results)
}
