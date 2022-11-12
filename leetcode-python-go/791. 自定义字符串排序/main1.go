package main

import (
	"fmt"
	"strings"
)

func customSortString(order, s string) string {
	freq := [26]int{}
	for _, c := range s {
		freq[c-'a']++
	}
	t := &strings.Builder{}
	for _, c := range order {
		if freq[c-'a'] > 0 {
			t.WriteString(strings.Repeat(string(c), freq[c-'a']))
			freq[c-'a'] = 0
		}
	}
	for i, k := range freq {
		if k > 0 {
			t.WriteString(strings.Repeat(string('a'+i), k))
		}
	}
	return t.String()
}

func main() {
	order := "cba"
	s := "abcd"
	results := customSortString(order, s)
	fmt.Println(results)
}
