package main

import (
	"fmt"
	"sort"
)

func distanceLimitedPathsExist(n int, edgeList [][]int, queries [][]int) []bool {
	sort.Slice(edgeList, func(i, j int) bool { return edgeList[i][2] < edgeList[j][2] })

	// 并查集模板
	fa := make([]int, n)
	for i := range fa {
		fa[i] = i
	}
	var find func(int) int
	find = func(x int) int {
		if fa[x] != x {
			fa[x] = find(fa[x])
		}
		return fa[x]
	}
	merge := func(from, to int) {
		fa[find(from)] = find(to)
	}

	for i := range queries {
		queries[i] = append(queries[i], i)
	}
	// 按照 limit 从小到大排序，方便离线
	sort.Slice(queries, func(i, j int) bool { return queries[i][2] < queries[j][2] })

	ans := make([]bool, len(queries))
	k := 0
	for _, q := range queries {
		for ; k < len(edgeList) && edgeList[k][2] < q[2]; k++ {
			merge(edgeList[k][0], edgeList[k][1])
		}
		ans[q[3]] = find(q[0]) == find(q[1])
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
