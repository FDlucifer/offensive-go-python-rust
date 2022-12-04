package main

import (
	"fmt"
)

func closestCost(baseCosts []int, toppingCosts []int, target int) int {
	x := baseCosts[0]
	for _, c := range baseCosts {
		x = min(x, c)
	}
	if x > target {
		return x
	}
	can := make([]bool, target+1)
	ans := 2*target - x
	for _, c := range baseCosts {
		if c <= target {
			can[c] = true
		} else {
			ans = min(ans, c)
		}
	}
	for _, c := range toppingCosts {
		for count := 0; count < 2; count++ {
			for i := target; i > 0; i-- {
				if can[i] && i+c > target {
					ans = min(ans, i+c)
				}
				if i-c > 0 {
					can[i] = can[i] || can[i-c]
				}
			}
		}
	}
	for i := 0; i <= ans-target; i++ {
		if can[target-i] {
			return target - i
		}
	}
	return ans
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
