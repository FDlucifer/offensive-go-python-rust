package main

import (
	"bufio"
	. "fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n int
	Fscan(in, &n)
	w := make([]int, n)
	for i := range w {
		Fscan(in, &w[i])
	}
	q := make([]int, n)
	for i := range q {
		Fscan(in, &q[i])
	}
	fa := make([]int, n+1)
	for i := range fa {
		fa[i] = i
	}
	sum := make([]int, n+1)
	var find func(int) int
	find = func(x int) int {
		if fa[x] != x {
			fa[x] = find(fa[x])
		}
		return fa[x]
	}

	ans := make([]int, n)
	for i := n - 1; i > 0; i-- {
		x := q[i] - 1
		to := find(x + 1)
		fa[x] = to // 合并 x 和 x+1
		sum[to] += sum[x] + w[x]
		ans[i-1] = max(ans[i], sum[to])
	}
	for _, v := range ans {
		Fprintln(out, v)
	}
}

func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
