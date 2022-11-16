package main

import (
	"fmt"
)

func numMatchingSubseq(s string, words []string) (ans int) {
	type pair struct{ i, j int }
	ps := [26][]pair{}
	for i, w := range words {
		ps[w[0]-'a'] = append(ps[w[0]-'a'], pair{i, 0})
	}
	for _, c := range s {
		q := ps[c-'a']
		ps[c-'a'] = nil
		for _, p := range q {
			p.j++
			if p.j == len(words[p.i]) {
				ans++
			} else {
				w := words[p.i][p.j] - 'a'
				ps[w] = append(ps[w], p)
			}
		}
	}
	return
}

func main() {
	s := "abcde"
	words := []string{"a", "bb", "acd", "ace"}
	results := numMatchingSubseq(s, words)
	fmt.Println(results)
}
