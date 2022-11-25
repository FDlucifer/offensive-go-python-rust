package main

import (
	"fmt"
)

func expand(s, t string) bool {
	n, m := len(s), len(t)
	i, j := 0, 0
	for i < n && j < m {
		if s[i] != t[j] {
			return false
		}
		ch := s[i]
		cntI := 0
		for i < n && s[i] == ch {
			cntI++
			i++
		}
		cntJ := 0
		for j < m && t[j] == ch {
			cntJ++
			j++
		}
		if cntI < cntJ || cntI > cntJ && cntI < 3 {
			return false
		}
	}
	return i == n && j == m
}

func expressiveWords(s string, words []string) (ans int) {
	for _, word := range words {
		if expand(s, word) {
			ans++
		}
	}
	return
}

func main() {
	S := "heeellooo"
	words := []string{"hello", "hi", "helo"}
	results := expressiveWords(S, words)
	fmt.Println(results)
}
