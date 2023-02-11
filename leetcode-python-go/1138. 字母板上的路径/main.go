package main

import (
	"fmt"
	"strings"
)

func alphabetBoardPath(target string) string {
	ans := []byte{}
	x, y := 0, 0
	for _, c := range target {
		nx, ny := int(c-'a')/5, int(c-'a')%5                      // 目标位置
		v := strings.Repeat(string("UD"[b2i(nx > x)]), abs(nx-x)) // 竖直
		h := strings.Repeat(string("LR"[b2i(ny > y)]), abs(ny-y)) // 水平
		if c == 'z' {
			v, h = h, v
		}
		ans = append(ans, v+h+"!"...)
		x, y = nx, ny
	}
	return string(ans)
}

func b2i(b bool) int {
	if b {
		return 1
	}
	return 0
}
func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	target := "code"
	results := alphabetBoardPath(target)
	fmt.Println(results)
}
