package main

import (
	"fmt"
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func check(n int) int {
	ans := 0
	for n > 0 {
		ans += n % 10
		n /= 10
	}
	return ans
}

func countBalls(l int, r int) int {
	maps := make(map[int]int)
	for i := l; i <= r; i++ {
		maps[check(i)]++
	}
	ans := 0
	for _, v := range maps {
		ans = max(ans, v)
	}
	return ans
}

func main() {
	lowLimit := 1
	highLimit := 10
	results := countBalls(lowLimit, highLimit)
	fmt.Println(results)
}
