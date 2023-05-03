package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"math"
	"path"
	"regexp"
	"runtime"
	"strconv"
	"strings"
)

func ToInt(arg interface{}) int {
	var val int
	switch arg.(type) {
	case string:
		var err error
		val, err = strconv.Atoi(arg.(string))
		if err != nil {
			panic("error converting string to int " + err.Error())
		}
	default:
		panic(fmt.Sprintf("unhandled type for int casting %T", arg))
	}
	return val
}

func ReadFile(pathFromCaller string) string {
	// Docs: https://golang.org/pkg/runtime/#Caller
	_, filename, _, ok := runtime.Caller(1)
	if !ok {
		panic("Could not find Caller of util.ReadFile")
	}

	// parse directory with pathFromCaller (which could be relative to Directory)
	absolutePath := path.Join(path.Dir(filename), pathFromCaller)

	// read the entire file & return the byte slice as a string
	content, err := ioutil.ReadFile(absolutePath)
	if err != nil {
		panic(err)
	}
	// trim off new lines and tabs at end of input files
	strContent := string(content)
	return strings.TrimRight(strContent, "\n")
}

func main() {
	var part int
	flag.IntVar(&part, "part", 1, "part 1 or 2")
	flag.Parse()
	fmt.Println("Running part", part)

	ans := cleaningRobot(ReadFile("./input.txt"), part)
	fmt.Println("Output:", ans)
}

func cleaningRobot(input string, part int) int {
	var grid [][]string
	for _, l := range strings.Split(input, "\n") {
		grid = append(grid, strings.Split(l, ""))
	}

	// bfs from every numbered cell to every other
	// generate a weighted graph
	var graph [][]int
	for r, row := range grid {
		for c, cell := range row {
			if regexp.MustCompile("[0-9]").MatchString(cell) {
				poi := cell
				distancesFromPOI := bfsGetEdgeWeights(grid, [2]int{r, c})
				// initialize graph size
				if graph == nil {
					for i := 0; i < len(distancesFromPOI); i++ {
						graph = append(graph, make([]int, len(distancesFromPOI)))
					}
				}
				graph[ToInt(poi)] = distancesFromPOI
			}
		}
	}

	// then a recursive, backtracking dfs on that weighted graph to determine
	// the shortest total path
	returnToZero := part != 1
	return dfs(graph, 0, map[int]bool{0: true}, returnToZero)
}

type bfsNode struct {
	row, col int // 0,0 is top left
	distance int
}

// allows passing through points of interest
func bfsGetEdgeWeights(grid [][]string, start [2]int) []int {
	// points of interest to distance to reach them from the starting coord
	poiToDistance := map[string]int{
		grid[start[0]][start[1]]: 0,
	}
	// run until all nodes have been seen...
	queue := []bfsNode{
		{start[0], start[1], 0},
	}
	visited := map[[2]int]bool{}
	for len(queue) > 0 {
		front := queue[0]
		queue = queue[1:]

		if visited[[2]int{front.row, front.col}] {
			continue
		}
		visited[[2]int{front.row, front.col}] = true

		if regexp.MustCompile("[0-9]").MatchString(grid[front.row][front.col]) {
			poiToDistance[grid[front.row][front.col]] = front.distance
		}
		for _, d := range dirs {
			nextRow, nextCol := front.row+d[0], front.col+d[1]
			// don't need to check for going out of bounds because there are walls
			// surrounding everything
			if grid[nextRow][nextCol] != "#" {
				queue = append(queue, bfsNode{
					row:      nextRow,
					col:      nextCol,
					distance: front.distance + 1,
				})
			}
		}

	}

	distances := make([]int, len(poiToDistance))
	for numStr, dist := range poiToDistance {
		distances[ToInt(numStr)] = dist
	}
	return distances
}

var dirs = [][2]int{
	{0, -1},
	{0, 1},
	{1, 0},
	{-1, 0},
}

func MinInt(nums ...int) int {
	minNum := nums[0]
	for _, v := range nums {
		if v < minNum {
			minNum = v
		}
	}
	return minNum
}

func dfs(graph [][]int, entryIndex int, visited map[int]bool, returnToZero bool) (minWeightSum int) {
	// if all nodes have been visited, return zero for part 1, or the distance
	// from the entryIndex to the zero POI
	if len(graph) == len(visited) {
		if returnToZero {
			return graph[entryIndex][0]
		}
		return 0
	}

	// get the minimum distance from a recursive call
	minDistance := math.MaxInt32
	for i, val := range graph[entryIndex] {
		if !visited[i] {
			visited[i] = true

			dist := val + dfs(graph, i, visited, returnToZero)
			minDistance = MinInt(minDistance, dist)

			delete(visited, i)
		}
	}

	return minDistance
}
