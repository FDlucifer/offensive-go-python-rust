package main

import (
	"fmt"
)

func countConsistentStrings(allowed string, words []string) (res int) {
	mask := 0
	for _, c := range allowed {
		mask |= 1 << (c - 'a')
	}
	for _, word := range words {
		mask1 := 0
		for _, c := range word {
			mask1 |= 1 << (c - 'a')
		}
		if mask1|mask == mask {
			res++
		}
	}
	return
}

func main() {
	allowed := "ujwvpzgrictsonka"
	words := []string{"o", "utoopn", "s", "trovszt", "viovnggza", "rwikini", "kvzpr", "kingkcu", "dghdypcdc", "unjpauiku", "gzsn", "rtsio", "mibsy", "o", "nnv", "wzssjn", "bhlayqkntz", "stwrii", "scuaucv", "ozsou", "t", "succspou", "khwihjjsf", "rvovnrkz", "bfakgfw", "sugaopnw", "cd", "uzjpwivu", "rpgcwzjz", "jgrctrar", "ns", "zhekexu", "vvcsoj", "g", "wirt", "iwtcn", "cigga", "nrrunca", "vs", "gwk", "wrp", "zcjwpnwr", "iziiiirurj", "co", "xiliwwzvv", "crjj", "rj", "ot", "uzat", "n", "ikjrrwgkzv", "j", "gsugivi", "hpz", "vefsycu", "kwcjnzjvs", "cwoczgt", "jk", "qmomynvptk", "rnig", "gkgasvz", "hwjwuqsg", "dyv", "g", "icajjskik", "cza", "zpjigip", "xfbomkpqmf", "gc", "tpoz", "guj", "r", "ngowssucu", "upanupuv", "ucjuaju", "saj", "wg", "nwngs", "cnpc", "zwipctkugc"}
	results := countConsistentStrings(allowed, words)
	fmt.Println(results)
}
