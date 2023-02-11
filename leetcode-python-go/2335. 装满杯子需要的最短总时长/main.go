package main

import (
	"fmt"
	"sort"
)

func fillCups(amount []int) int {
	sort.Ints(amount)
	if amount[2] > amount[1]+amount[0] {
		return amount[2]
	}
	return (amount[0] + amount[1] + amount[2] + 1) / 2
}

func main() {
	amount := []int{5, 4, 4}
	results := fillCups(amount)
	fmt.Println(results)
}
