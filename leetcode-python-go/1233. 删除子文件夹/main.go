package main

import (
	"fmt"
	"sort"
	"strings"
)

func removeSubfolders(folder []string) (ans []string) {
	sort.Strings(folder)
	ans = append(ans, folder[0])
	for _, f := range folder[1:] {
		last := ans[len(ans)-1]
		if !strings.HasPrefix(f, last) || f[len(last)] != '/' {
			ans = append(ans, f)
		}
	}
	return
}

func main() {
	folder := []string{"/a/b/c", "/a/b/ca", "/a/b/d"}
	results := removeSubfolders(folder)
	fmt.Println(results)
}
