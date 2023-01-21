package main

import (
	"fmt"
	"math"
)

func minSideJumps(obstacles []int) int {
	d := [3]int{1, 0, 1}
	for _, x := range obstacles[1:] {
		minCnt := math.MaxInt / 2
		for j := 0; j < 3; j++ {
			if j == x-1 {
				d[j] = math.MaxInt / 2
			} else {
				minCnt = min(minCnt, d[j])
			}
		}
		for j := 0; j < 3; j++ {
			if j != x-1 {
				d[j] = min(d[j], minCnt+1)
			}
		}
	}
	return min(min(d[0], d[1]), d[2])
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}

func main() {
	obstacles := []int{0, 1, 1, 3, 3, 0}
	results := minSideJumps(obstacles)
	fmt.Println(results)
}
