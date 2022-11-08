package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"strings"
)

func main() {
	buf, _ := ioutil.ReadFile("input.txt")

	ans := countValidTriangles(string(buf), 1)
	fmt.Println("Part1: ", ans)

	ans1 := countValidTriangles(string(buf), 2)
	fmt.Println("Part2: ", ans1)
}

func countValidTriangles(input string, part int) int {
	triangleEdges := parseInput(input)

	if part == 2 {
		triangleEdges = transformTriangles(triangleEdges)
	}

	var valid int
	for _, tri := range triangleEdges {
		// lazy, just check the three scenarios
		if tri[0]+tri[1] <= tri[2] {
			continue
		}
		if tri[0]+tri[2] <= tri[1] {
			continue
		}
		if tri[1]+tri[2] <= tri[0] {
			continue
		}
		valid++
	}

	return valid
}

var multipleSpaces = regexp.MustCompile("[\\s]{2,}")

func parseInput(input string) (ans [][3]int) {
	lines := strings.Split(input, "\n")
	for _, l := range lines {
		l = multipleSpaces.ReplaceAllString(l, " ")
		var triangleEdges [3]int
		fmt.Sscanf(l, " %d %d %d", &triangleEdges[0], &triangleEdges[1], &triangleEdges[2])
		ans = append(ans, triangleEdges)
	}
	return ans
}

// for part 2 where rows are in columns of 3 for some stupid reason
func transformTriangles(triangles [][3]int) [][3]int {
	var newTriangles [][3]int
	for i := 0; i < len(triangles); i += 3 {
		for col := 0; col < 3; col++ {
			var edge [3]int
			for row := 0; row < 3; row++ {
				edge[row] = triangles[i+row][col]
			}
			newTriangles = append(newTriangles, edge)
		}
	}
	return newTriangles
}
