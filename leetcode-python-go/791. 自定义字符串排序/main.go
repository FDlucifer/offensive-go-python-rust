package main

import (
	"fmt"
	"sort"
)

func customSortString(order, s string) string {
	val := map[byte]int{}
	for i, c := range order {
		val[byte(c)] = i + 1
	}
	t := []byte(s)
	sort.Slice(t, func(i, j int) bool { return val[t[i]] < val[t[j]] })
	return string(t)
}

func main() {
	order := "cba"
	s := "abcd"
	results := customSortString(order, s)
	fmt.Println(results)
}
