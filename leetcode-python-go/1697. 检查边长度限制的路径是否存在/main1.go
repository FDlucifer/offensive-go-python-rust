package main

import (
	"fmt"
	"sort"
)

var p []int

func fr(x int) int {
	if p[x] != x {
		p[x] = fr(p[x])
	}
	return p[x]
}

type ByLength [][]int

func (b ByLength) Len() int {
	return len(b)
}

func (b ByLength) Less(i, j int) bool {
	return b[i][2] < b[j][2]
}

func (b ByLength) Swap(i, j int) {
	b[i], b[j] = b[j], b[i]
}

func distanceLimitedPathsExist(n int, es [][]int, queries [][]int) []bool {
	p = make([]int, n+10)
	for i := 0; i < n; i += 1 {
		p[i] = i
	}
	m := len(queries)
	for i := 0; i < m; i += 1 {
		queries[i] = append(queries[i], i)
	}
	sort.Sort(ByLength(es))
	sort.Sort(ByLength(queries))
	l := -1
	sz := len(es)
	ans := make([]bool, m)
	for _, q := range queries {
		for l+1 < sz && es[l+1][2] < q[2] {
			p[fr(es[l+1][0])] = fr(es[l+1][1])
			l += 1
		}
		ans[q[3]] = fr(q[0]) == fr(q[1])
	}
	return ans
}

func main() {
	n := 3
	edgeList := [][]int{{0, 1, 2}, {1, 2, 4}, {2, 0, 8}, {1, 0, 16}}
	queries := [][]int{{0, 1, 2}, {0, 2, 5}}
	results := distanceLimitedPathsExist(n, edgeList, queries)
	fmt.Println(results)
}
