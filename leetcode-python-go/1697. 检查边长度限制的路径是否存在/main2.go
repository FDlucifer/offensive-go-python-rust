package main

import (
	"fmt"
	"sort"
)

func distanceLimitedPathsExist(n int, edgeList [][]int, queries [][]int) []bool {
	sort.Slice(edgeList, func(i, j int) bool {
		return edgeList[i][2] < edgeList[j][2]
	})
	idxs := make([]int, len(queries))
	for i := range idxs {
		idxs[i] = i
	}
	sort.Slice(idxs, func(i, j int) bool { return queries[idxs[i]][2] < queries[idxs[j]][2] })
	fa := make([]int, n)
	for i := range fa {
		fa[i] = i
	}
	var find func(int) int
	find = func(i int) int {
		if fa[i] != i {
			fa[i] = find(fa[i])
		}
		return fa[i]
	}

	merge := func(fo, to int) {
		fa[find(fo)] = find(to)
	}
	res := make([]bool, len(queries))
	j := 0
	for _, v := range idxs {
		for j < len(edgeList) && edgeList[j][2] < queries[v][2] {
			merge(edgeList[j][0], edgeList[j][1])
			j++
		}
		if find(queries[v][0]) == find(queries[v][1]) {
			res[v] = true
		}
	}
	return res
}

func main() {
	n := 3
	edgeList := [][]int{{0, 1, 2}, {1, 2, 4}, {2, 0, 8}, {1, 0, 16}}
	queries := [][]int{{0, 1, 2}, {0, 2, 5}}
	results := distanceLimitedPathsExist(n, edgeList, queries)
	fmt.Println(results)
}
