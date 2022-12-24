package main

import (
	"fmt"
	"strings"
)

func largestMerge(word1 string, word2 string) string {
	l1 := len(word1)
	l2 := len(word2)
	i1, i2 := 0, 0
	var res strings.Builder
	res.Grow(l1 + l2)
	for i1 < l1 && i2 < l2 {
		if word2[i2] < word1[i1] || word2[i2:] <= word1[i1:] {
			res.WriteByte(word1[i1])
			i1++
		} else {
			res.WriteByte(word2[i2])
			i2++
		}
	}
	if i1 < l1 {
		res.WriteString(word1[i1:])
	}
	if i2 < l2 {
		res.WriteString(word2[i2:])
	}
	return res.String()
}

func main() {
	word1 := "abcabc"
	word2 := "abdcaba"
	results := largestMerge(word1, word2)
	fmt.Println(results)
}
