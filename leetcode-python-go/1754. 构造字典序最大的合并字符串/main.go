package main

import (
	"fmt"
)

func largestMerge(word1, word2 string) string {
	merge := []byte{}
	i, j, n, m := 0, 0, len(word1), len(word2)
	for i < n || j < m {
		if i < n && word1[i:] > word2[j:] {
			merge = append(merge, word1[i])
			i += 1
		} else {
			merge = append(merge, word2[j])
			j += 1
		}
	}
	return string(merge)
}
func main() {
	word1 := "abcabc"
	word2 := "abdcaba"
	results := largestMerge(word1, word2)
	fmt.Println(results)
}
