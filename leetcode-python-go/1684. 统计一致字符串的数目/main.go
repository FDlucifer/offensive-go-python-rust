package main

import (
	"fmt"
	"sort"
	"strings"
)

func in(target string, str_array []string) bool {
	for _, element := range str_array {
		if target == element {
			return true
		}
	}
	return false
}

func isExistV1(matrix [][]string, target []string) bool {
	// fmt.Println("target: ", target)
	for _, element := range matrix {
		res := strings.Join(element, "")
		// fmt.Println("isExistV1 element: ", res)
		res1 := strings.Join(target, "")
		// fmt.Println("isExistV1 	target: ", res1)
		if res1 == res {
			return true
		}
	}
	return false
}

func subsets(A []string) [][]string { // 算出所有子集二维数组
	// write code here
	var set [][]string
	var subSet []string
	subSet = append(subSet, A[0])
	set = append(set, subSet)
	for i := 1; i < len(A); i++ {
		num := len(set)
		for j := 0; j < num; j++ {
			var subSet []string
			subSet = append(subSet, set[j]...)
			subSet = append(subSet, A[i])
			set = append(set, subSet)
		}
		var subSet []string
		subSet = append(subSet, A[i])
		set = append(set, subSet)
	}
	set = append(set, []string{})
	return set
}

func countConsistentStrings(allowed string, words []string) int {
	count := 0
	sort.Strings(words)
	for _, value := range words {
		var result []string
		word := string(value)
		// fmt.Println("word: ", word)
		for i := 0; i < len(word); i++ {
			w := string(word[i])
			if in(w, result) {
				continue
			}
			result = append(result, w)
			sort.Strings(result)
			// fmt.Printf("%s\n", result)
		}
		// fmt.Printf("result: %s\n", result)
		var result1 []string
		for i1 := 0; i1 < len(allowed); i1++ {
			w1 := string(allowed[i1])
			result1 = append(result1, w1)
			sort.Strings(result1)
			// fmt.Printf("%s\n", result1)
		}
		// fmt.Printf("result1: %s\n", result1)
		subsets1 := subsets(result1)
		if len(result) > len(result1) {
			continue
		}
		if isExistV1(subsets1, result) {
			count++
		}
	}
	return count
}

func main() {
	allowed := "ujwvpzgrictsonka"
	words := []string{"o", "utoopn", "s", "trovszt", "viovnggza", "rwikini", "kvzpr", "kingkcu", "dghdypcdc", "unjpauiku", "gzsn", "rtsio", "mibsy", "o", "nnv", "wzssjn", "bhlayqkntz", "stwrii", "scuaucv", "ozsou", "t", "succspou", "khwihjjsf", "rvovnrkz", "bfakgfw", "sugaopnw", "cd", "uzjpwivu", "rpgcwzjz", "jgrctrar", "ns", "zhekexu", "vvcsoj", "g", "wirt", "iwtcn", "cigga", "nrrunca", "vs", "gwk", "wrp", "zcjwpnwr", "iziiiirurj", "co", "xiliwwzvv", "crjj", "rj", "ot", "uzat", "n", "ikjrrwgkzv", "j", "gsugivi", "hpz", "vefsycu", "kwcjnzjvs", "cwoczgt", "jk", "qmomynvptk", "rnig", "gkgasvz", "hwjwuqsg", "dyv", "g", "icajjskik", "cza", "zpjigip", "xfbomkpqmf", "gc", "tpoz", "guj", "r", "ngowssucu", "upanupuv", "ucjuaju", "saj", "wg", "nwngs", "cnpc", "zwipctkugc"}
	results := countConsistentStrings(allowed, words)
	fmt.Println(results)
}
