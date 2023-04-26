package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"path"
	"runtime"
	"strconv"
	"strings"
)

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

	ans := bfs(ReadFile("./input.txt"), [2]int{31, 39}, part)
	fmt.Println("Output:", ans)
}

var dirs = [][2]int{
	{-1, 0},
	{1, 0},
	{0, 1},
	{0, -1},
}

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

func bfs(input string, destination [2]int, part int) int {
	inputNum := ToInt(input)

	// bfs queue
	queue := [][3]int{[3]int{1, 1, 0}} // x,y, DIST
	// to not re-visit cells
	visited := map[[2]int]bool{}

	// for part 2
	uniqueVisitsUnder50 := map[[2]int]bool{}

	for len(queue) > 0 {
		front := queue[0]
		queue = queue[1:]

		currentX, currentY := front[0], front[1]
		currentDist := front[2]

		// part 1 return
		if part == 1 && currentX == destination[0] && currentY == destination[1] {
			return currentDist
		}
		// if already visited, skip
		if !visited[[2]int{currentX, currentY}] {
			// for part 2, check if distance is 50 or less
			if currentDist <= 50 {
				uniqueVisitsUnder50[[2]int{currentX, currentY}] = true
			}

			if part == 2 && currentDist > 50 {
				break
			}

			for _, diff := range dirs {
				nextX, nextY := currentX+diff[0], currentY+diff[1]
				if nextX >= 0 && nextY >= 0 {
					if isOpenSpace(nextX, nextY, inputNum) {
						queue = append(queue, [3]int{nextX, nextY, currentDist + 1})
					}
				}
			}
		}
		visited[[2]int{currentX, currentY}] = true
	}

	return len(uniqueVisitsUnder50)
}

func isOpenSpace(x, y, inputNum int) bool {
	num := x*x + 3*x + 2*x*y + y + y*y + inputNum
	binStr := fmt.Sprintf("%b", num)
	var ones int
	for _, char := range binStr {
		if char == '1' {
			ones++
		}
	}

	return ones%2 == 0
}
