package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

var x, y int

func main() {
	in := bufio.NewReader(os.Stdin)
	fmt.Fscan(in, &x, &y)
	if x == y {
		fmt.Printf("%s%s", strings.Repeat("A", x), strings.Repeat("B", y))
		return
	}
	n := x + y
	nums1 := make([]int, n)
	nums2 := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &nums1[i])
	}
	copy(nums2, nums1)
	sort.Ints(nums2)
	m1 := "A"
	m2 := "B"
	var midNum int
	if x > y {
		midNum = nums2[x]
		m1, m2 = m2, m1
	} else {
		midNum = nums2[y]
	}
	for _, num := range nums1 {
		if num >= midNum {
			fmt.Printf(m1)
		} else {
			fmt.Printf(m2)
		}
	}
}
