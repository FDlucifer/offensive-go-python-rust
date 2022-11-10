package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var n, m int
var v, w int

type Order struct {
	No    int
	Price int
}

func main() {
	in := bufio.NewReader(os.Stdin)
	fmt.Fscan(in, &n, &m)
	orders := make([]*Order, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &v, &w)
		orders[i] = &Order{i, v + w*2}
	}
	sort.Slice(orders, func(i, j int) bool {
		return orders[i].Price > orders[j].Price || (orders[i].Price == orders[j].Price && orders[i].No < orders[j].No)
	})
	res := make([]int, m)
	for i := 0; i < m; i++ {
		res[i] = orders[i].No
	}
	sort.Ints(res)
	for i := 0; i < m; i++ {
		fmt.Printf("%d ", res[i]+1)
	}
	fmt.Println()
}
