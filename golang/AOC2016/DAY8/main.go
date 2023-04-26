package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"path"
	"runtime"
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

	count, finalString := twoFA(ReadFile("./input.txt"), 6, 50)
	if part == 1 {
		fmt.Println("Output:", count)
	} else {
		fmt.Println("Output:")
		fmt.Println(finalString)
	}
}

func twoFA(input string, height, width int) (int, string) {
	instructions := strings.Split(input, "\n")
	var grid [][]bool
	for i := 0; i < height; i++ {
		grid = append(grid, make([]bool, width))
	}

	for _, inst := range instructions {
		if strings.HasPrefix(inst, "rect") {
			var row, col int
			fmt.Sscanf(inst, "rect %dx%d", &col, &row)
			for r := 0; r < row; r++ {
				for c := 0; c < col; c++ {
					grid[r][c] = true
				}
			}
		} else if strings.HasPrefix(inst, "rotate row") {
			var row, by int
			_, err := fmt.Sscanf(inst, "rotate row y=%d by %d", &row, &by)
			if err != nil {
				panic("parsing error on instruction: " + err.Error())
			}
			for count := 0; count < by; count++ {
				store := grid[row][width-1]
				for i := width - 1; i > 0; i-- {
					grid[row][i] = grid[row][i-1]
				}
				grid[row][0] = store
			}
		} else if strings.HasPrefix(inst, "rotate column") {
			var col, by int
			_, err := fmt.Sscanf(inst, "rotate column x=%d by %d", &col, &by)
			if err != nil {
				panic("parsing error on instruction: " + err.Error())
			}
			for count := 0; count < by; count++ {
				store := grid[height-1][col]
				for r := height - 1; r > 0; r-- {
					grid[r][col] = grid[r-1][col]
				}
				grid[0][col] = store
			}
		} else {
			panic("unhandled instruction: " + inst)
		}
	}

	var count int
	var finalState string
	// count on pixels
	for _, row := range grid {
		for _, v := range row {
			if v {
				finalState += "#"
				count++
			} else {
				finalState += " "
			}
		}
		finalState += "\n"
	}

	return count, finalState
}
