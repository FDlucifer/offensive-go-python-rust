package main

import (
	"fmt"
	"strings"
)

func halvesAreAlike(s string) bool {
	cnt := 0
	for _, c := range s[:len(s)/2] {
		if strings.ContainsRune("aeiouAEIOU", c) {
			cnt++
		}
	}
	for _, c := range s[len(s)/2:] {
		if strings.ContainsRune("aeiouAEIOU", c) {
			cnt--
		}
	}
	return cnt == 0
}

func main() {
	s := "textbook"
	results := halvesAreAlike(s)
	fmt.Println(results)
}
