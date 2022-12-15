package main

import (
	"fmt"
	"strconv"
)

func getLucky(s string, k int) int {
	t := []byte{}
	for _, c := range s {
		t = append(t, strconv.Itoa(int(c-'a'+1))...)
	}
	digits := string(t)
	for i := 1; i <= k && len(digits) > 1; i++ {
		sum := 0
		for _, c := range digits {
			sum += int(c - '0')
		}
		digits = strconv.Itoa(sum)
	}
	ans, _ := strconv.Atoi(digits)
	return ans
}

func main() {
	s := "leetcode"
	k := 2
	results := getLucky(s, k)
	fmt.Println(results)
}
