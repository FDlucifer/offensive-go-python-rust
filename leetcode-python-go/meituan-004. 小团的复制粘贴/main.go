package main

import (
	"bufio"
	"fmt"
	"os"
)

var n, m int
var t, k, x, y int

type Order struct {
	No    int
	Price int
}

func main() {
	in := bufio.NewReader(os.Stdin)
	fmt.Fscan(in, &n)
	A := make([]int, n)
	B := make([]int, n)
	for i := range A {
		fmt.Fscan(in, &A[i])
		B[i] = -1
	}
	fmt.Fscan(in, &m)
	for ; m > 0; m-- {
		fmt.Fscan(in, &t)
		if t == 1 {
			fmt.Fscan(in, &k, &x, &y)
			copy(B[y-1:], A[x-1:x-1+k])
		} else {
			fmt.Fscan(in, &x)
			fmt.Println(B[x-1])
		}
	}
}
