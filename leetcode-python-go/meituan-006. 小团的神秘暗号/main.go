package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var n int
var T string

func main() {
	in := bufio.NewReader(os.Stdin)
	fmt.Fscan(in, &n, &T)
	PM := strings.Index(T, "M")
	PT := strings.Index(T[PM:], "T") + PM
	ST := strings.LastIndex(T, "T")
	SM := strings.LastIndex(T[:ST], "M")
	fmt.Println(T[PT+1 : SM])
}
