package main

import (
	"fmt"
	"unicode"
)

var dirs = []struct{ x, y int }{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

func shortestPathAllKeys(grid []string) int {
	m, n := len(grid), len(grid[0])
	sx, sy := 0, 0
	keyToIdx := map[rune]int{}
	for i, row := range grid {
		for j, c := range row {
			if c == '@' {
				sx, sy = i, j
			} else if unicode.IsLower(c) {
				if _, ok := keyToIdx[c]; !ok {
					keyToIdx[c] = len(keyToIdx)
				}
			}
		}
	}

	dist := make([][][]int, m)
	for i := range dist {
		dist[i] = make([][]int, n)
		for j := range dist[i] {
			dist[i][j] = make([]int, 1<<len(keyToIdx))
			for k := range dist[i][j] {
				dist[i][j][k] = -1
			}
		}
	}
	dist[sx][sy][0] = 0
	q := [][3]int{{sx, sy, 0}}
	for len(q) > 0 {
		p := q[0]
		q = q[1:]
		x, y, mask := p[0], p[1], p[2]
		for _, d := range dirs {
			nx, ny := x+d.x, y+d.y
			if 0 <= nx && nx < m && 0 <= ny && ny < n && grid[nx][ny] != '#' {
				c := rune(grid[nx][ny])
				if c == '.' || c == '@' {
					if dist[nx][ny][mask] == -1 {
						dist[nx][ny][mask] = dist[x][y][mask] + 1
						q = append(q, [3]int{nx, ny, mask})
					}
				} else if unicode.IsLower(c) {
					t := mask | 1<<keyToIdx[c]
					if dist[nx][ny][t] == -1 {
						dist[nx][ny][t] = dist[x][y][mask] + 1
						if t == 1<<len(keyToIdx)-1 {
							return dist[nx][ny][t]
						}
						q = append(q, [3]int{nx, ny, t})
					}
				} else {
					idx := keyToIdx[unicode.ToLower(c)]
					if mask>>idx&1 > 0 && dist[nx][ny][mask] == -1 {
						dist[nx][ny][mask] = dist[x][y][mask] + 1
						q = append(q, [3]int{nx, ny, mask})
					}
				}
			}
		}
	}
	return -1
}

func main() {
	grid := []string{"@.a.#", "###.#", "b.A.B"}
	results := shortestPathAllKeys(grid)
	fmt.Println(results)
}
