package main

import (
	"bufio"
	"fmt"
	"os"
)

var n int

func main() {
	in := bufio.NewReader(os.Stdin)
	fmt.Fscan(in, &n)
	a := make([][]int, n)
	for i := range a {
		a[i] = make([]int, n)
	}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			fmt.Fscan(in, &a[i][j])
		}
	}
	b := make([]bool, n+1)
	var ans []int
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if b[a[i][j]] == false {
				b[a[i][j]] = true
				ans = append(ans, a[i][j])
				break
			}
		}
	}
	for _, x := range ans {
		fmt.Printf("%d ", x)
	}
}
