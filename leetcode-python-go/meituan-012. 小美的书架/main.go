package main

import (
	"bufio"
	"fmt"
	"os"
)

var N, M, Q int
var t, x, y int

func main() {
	in := bufio.NewReader(os.Stdin)
	fmt.Fscan(in, &M, &N, &Q)
	// false: 没上锁；true：已上锁
	lockStatus := make([]bool, N+1)
	// -1：在小团手里；0：在小美手里，未上架；>0：在小美手里，已上架
	bookStatus := make([]int, M+1)
	for ; Q > 0; Q-- {
		fmt.Fscan(in, &t)
		switch t {
		case 1:
			fmt.Fscan(in, &x, &y)
			bs := bookStatus[x]
			if bs == -1 || lockStatus[y] == true || (bs > 0 && lockStatus[bs] == true) {
				continue
			}
			bookStatus[x] = y
		case 2:
			fmt.Fscan(in, &y)
			lockStatus[y] = true
		case 3:
			fmt.Fscan(in, &y)
			lockStatus[y] = false
		case 4:
			fmt.Fscan(in, &x)
			bs := bookStatus[x]
			if bs == -1 || bs == 0 || (bs > 0 && lockStatus[bs] == true) {
				fmt.Println(-1)
			} else {
				fmt.Println(bs)
				bookStatus[x] = -1
			}
		case 5:
			fmt.Fscan(in, &x)
			bs := bookStatus[x]
			if bs == -1 {
				bookStatus[x] = 0
			}
		}
	}
}
