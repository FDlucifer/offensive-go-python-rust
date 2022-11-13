package main

import (
	"bufio"
	"fmt"
	"os"
)

var a, b, c, d, e, f, g int

func main() {
	in := bufio.NewReader(os.Stdin)
	fmt.Fscan(in, &a, &b, &c, &d, &e, &f, &g)
	var res int
	var x int
	for d > 0 && (a > 0 || b > 0 || c > 0) {
		if a > 0 && e >= f && e >= g {
			x = min(a, d)
			res += e * x
			a -= x
			d -= x
			e = -1
		} else if b > 0 && f >= e && f >= g {
			x = min(b, d)
			res += f * x
			b -= x
			d -= x
			f = -1
		} else if c > 0 && g >= e && g >= f {
			x = min(c, d)
			res += g * x
			c -= x
			d -= x
			g = -1
		}
	}
	fmt.Println(res)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
