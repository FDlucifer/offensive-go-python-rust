package main

import (
	"fmt"
)

var (
	dx = []int{1, 0, 0, -1}
	dy = []int{0, 1, -1, 0}
)

func floodFill(image [][]int, sr int, sc int, color int) [][]int {
	currColor := image[sr][sc]
	if currColor != color {
		dfs(image, sr, sc, currColor, color)
	}
	return image
}

func dfs(image [][]int, x, y, currColor, color int) {
	if image[x][y] == currColor {
		image[x][y] = color
		for i := 0; i < 4; i++ {
			mx, my := x+dx[i], y+dy[i]
			if mx >= 0 && mx < len(image) && my >= 0 && my < len(image[0]) {
				dfs(image, mx, my, currColor, color)
			}
		}
	}
}

func main() {
	image := [][]int{{1, 1, 1}, {1, 1, 0}, {1, 0, 1}}
	sr := 1
	sc := 1
	newColor := 2
	results := floodFill(image, sr, sc, newColor)
	fmt.Println(results)
}
