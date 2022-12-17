package main

import (
	"fmt"
)

func allPathsSourceTarget(graph [][]int) (ans [][]int) {
	stk := []int{0}
	var dfs func(int)
	dfs = func(x int) {
		if x == len(graph)-1 {
			ans = append(ans, append([]int(nil), stk...))
			return
		}
		for _, y := range graph[x] {
			stk = append(stk, y)
			dfs(y)
			stk = stk[:len(stk)-1]
		}
	}
	dfs(0)
	return
}

func main() {
	graph := [][]int{{4, 3, 1}, {3, 2, 4}, {3}, {4}, {}}
	results := allPathsSourceTarget(graph)
	fmt.Println(results)
}
