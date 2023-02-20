package main

import (
	"bytes"
	"fmt"
)

func bestHand(ranks []int, suits []byte) string {
	if bytes.Count(suits, suits[:1]) == 5 {
		return "Flush"
	}
	cnt, pair := map[int]int{}, false
	for _, r := range ranks {
		cnt[r]++
		if cnt[r] == 3 {
			return "Three of a Kind"
		}
		if cnt[r] == 2 {
			pair = true
		}
	}
	if pair {
		return "Pair"
	}
	return "High Card"
}

func main() {
	ranks := []int{4, 4, 2, 4, 4}
	suits := []byte{byte("d"[0]), byte("a"[0]), byte("a"[0]), byte("b"[0]), byte("c"[0])}
	results := bestHand(ranks, suits)
	fmt.Println(results)
}
