package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strings"
)

func main() {
	buf, _ := ioutil.ReadFile("input.txt")

	ans := signalsAndNoise(string(buf), 1)
	fmt.Println("Part1: ", ans)

	ans1 := signalsAndNoise(string(buf), 2)
	fmt.Println("Part2: ", ans1)
}

func parseInput(input string) (ans [][]string) {
	for _, line := range strings.Split(strings.TrimSpace(input), "\n") {
		ans = append(ans, strings.Split(strings.TrimSpace(line), ""))
	}
	return ans
}

func signalsAndNoise(input string, part int) string {
	grid := parseInput(input)

	var indexMaps []map[string]int
	for col := 0; col < len(grid[0]); col++ {
		indexMaps = append(indexMaps, map[string]int{})
		for row := 0; row < len(grid); row++ {
			char := grid[row][col]
			indexMaps[col][char]++
		}
	}

	var mostVersion string  // part 1
	var leastVersion string // part 2
	for col := 0; col < len(indexMaps); col++ {
		var (
			mostChar  string
			mostLen   int
			leastChar string
			leastLen  int = math.MaxInt32
		)
		for k, count := range indexMaps[col] {
			if count > mostLen {
				mostLen = count
				mostChar = k
			}
			if count < leastLen {
				leastLen = count
				leastChar = k
			}
		}
		mostVersion += mostChar
		leastVersion += leastChar
	}
	if part == 1 {
		return mostVersion
	}
	return leastVersion
}
