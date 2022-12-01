package main

import (
	"fmt"
	"math"
)

func nearestValidPoint(x, y int, points [][]int) int {
	ans := -1
	minDist := math.MaxInt32
	for i, p := range points {
		if p[0] == x || p[1] == y {
			dist := abs(p[0]-x) + abs(p[1]-y)
			if dist < minDist {
				minDist = dist
				ans = i
			}
		}
	}
	return ans
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	x := 3
	y := 4
	points := [][]int{{1, 2}, {3, 1}, {2, 4}, {2, 3}, {4, 4}}
	results := nearestValidPoint(x, y, points)
	fmt.Println(results)
}
