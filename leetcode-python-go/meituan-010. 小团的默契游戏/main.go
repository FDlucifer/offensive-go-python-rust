package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var n, m int

func main() {
	in := bufio.NewReader(os.Stdin)
	fmt.Fscan(in, &n, &m)
	nums := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &nums[i])
	}
	var res int
	for l := 1; l <= m; l++ {
		r := sort.Search(m+1, func(x int) bool {
			if x < l {
				return false
			}
			var pre int
			for i := 0; i < n; i++ {
				if nums[i] < l || nums[i] > x {
					if nums[i] >= pre {
						pre = nums[i]
					} else {
						return false
					}
				}
			}
			return true
		})
		res += m - r + 1

	}
	fmt.Println(res)
}
