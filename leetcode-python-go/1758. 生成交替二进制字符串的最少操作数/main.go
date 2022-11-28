package main

import (
	"fmt"
)

func minOperations(s string) int {
	cnt := 0
	for i, c := range s {
		if i%2 != int(c-'0') {
			cnt++
		}
	}
	return min(cnt, len(s)-cnt)
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}

func main() {
	s := "0100"
	results := minOperations(s)
	fmt.Println(results)
}
