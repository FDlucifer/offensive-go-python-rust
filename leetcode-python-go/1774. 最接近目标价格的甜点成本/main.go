package main

import (
	"fmt"
)

func closestCost(baseCosts []int, toppingCosts []int, target int) int {
	ans := baseCosts[0]
	for _, c := range baseCosts {
		ans = min(ans, c)
	}
	var dfs func(int, int)
	dfs = func(p, curCost int) {
		if abs(ans-target) < curCost-target {
			return
		} else if abs(ans-target) >= abs(curCost-target) {
			if abs(ans-target) > abs(curCost-target) {
				ans = curCost
			} else {
				ans = min(ans, curCost)
			}
		}
		if p == len(toppingCosts) {
			return
		}
		dfs(p+1, curCost+toppingCosts[p]*2)
		dfs(p+1, curCost+toppingCosts[p])
		dfs(p+1, curCost)
	}
	for _, c := range baseCosts {
		dfs(0, c)
	}
	return ans
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}

func main() {
	baseCosts := []int{1, 7}
	toppingCosts := []int{3, 4}
	target := 10
	results := closestCost(baseCosts, toppingCosts, target)
	fmt.Println(results)
}
