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
	if currColor == color {
		return image
	}
	n, m := len(image), len(image[0])
	queue := [][]int{}
	queue = append(queue, []int{sr, sc})
	image[sr][sc] = color
	for i := 0; i < len(queue); i++ {
		cell := queue[i]
		for j := 0; j < 4; j++ {
			mx, my := cell[0]+dx[j], cell[1]+dy[j]
			if mx >= 0 && mx < n && my >= 0 && my < m && image[mx][my] == currColor {
				queue = append(queue, []int{mx, my})
				image[mx][my] = color
			}
		}
	}
	return image
}

func main() {
	image := [][]int{{1, 1, 1}, {1, 1, 0}, {1, 0, 1}}
	sr := 1
	sc := 1
	newColor := 2
	results := floodFill(image, sr, sc, newColor)
	fmt.Println(results)
}
