package main

import (
	"bufio"
	"fmt"
	"os"
)

var n int
var s string

func main() {
	in := bufio.NewReader(os.Stdin)
	fmt.Fscan(in, &n, &s)
	var cnt int
	var res int
	for i := 0; i < n; i++ {
		if s[i] == 'E' {
			cnt++
		} else if cnt > 0 {
			cnt--
		}
		res = max(res, cnt)
	}
	fmt.Println(res)
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
