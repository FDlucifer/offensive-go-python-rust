package main

import (
	"fmt"
	"sort"
)

func maximumUnits(boxTypes [][]int, truckSize int) (ans int) {
	sort.Slice(boxTypes, func(i, j int) bool { return boxTypes[i][1] > boxTypes[j][1] })
	for _, p := range boxTypes {
		if p[0] >= truckSize {
			ans += truckSize * p[1]
			break
		}
		truckSize -= p[0]
		ans += p[0] * p[1]
	}
	return
}

func main() {
	truckSize := 4
	boxTypes := [][]int{{1, 3}, {2, 2}, {3, 1}}
	results := maximumUnits(boxTypes, truckSize)
	fmt.Println(results)
}
