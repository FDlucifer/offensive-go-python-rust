package main

import (
	"bufio"
	"fmt"
	"os"
)

var n, m, xs, ys, xt, yt int

func main() {
	in := bufio.NewReader(os.Stdin)
	fmt.Fscan(in, &n, &m, &xs, &ys, &xt, &yt)
	xs--
	ys--
	xt--
	yt--
	a := make([][]int, n)
	for i := 0; i < n; i++ {
		a[i] = make([]int, m)
		for j := 0; j < m; j++ {
			fmt.Fscan(in, &a[i][j])
		}
	}
	b := make([][]int, n)
	for i := 0; i < n; i++ {
		b[i] = make([]int, m)
		for j := 0; j < m; j++ {
			fmt.Fscan(in, &b[i][j])
		}
	}
	vis := make([][]bool, n)
	for i := 0; i < n; i++ {
		vis[i] = make([]bool, m)
	}
	var t int
	type Pair struct {
		x, y int
	}
	stack := []*Pair{{xs, ys}}
	vis[xs][ys] = true
	for {
		length := len(stack)
		for i := 0; i < length; i++ {
			x := stack[i].x
			y := stack[i].y
			if x == xt && y == yt {
				fmt.Println(t)
				return
			}
			if t%(a[x][y]+b[x][y]) < a[x][y] {
				if x > 0 && vis[x-1][y] == false {
					vis[x-1][y] = true
					stack = append(stack, &Pair{x - 1, y})
				}
				if x < n-1 && vis[x+1][y] == false {
					vis[x+1][y] = true
					stack = append(stack, &Pair{x + 1, y})
				}
			}
			if t >= a[x][y] && (t-a[x][y])%(a[x][y]+b[x][y]) < b[x][y] {
				if y > 0 && vis[x][y-1] == false {
					vis[x][y-1] = true
					stack = append(stack, &Pair{x, y - 1})
				}
				if y < m-1 && vis[x][y+1] == false {
					vis[x][y+1] = true
					stack = append(stack, &Pair{x, y + 1})
				}
			}
		}
		t++
	}
}
