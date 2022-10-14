package main

import "fmt"

func main() {
	fmt.Println(find("crazy brown fx", "own"))
	fmt.Println(find("crazy brown fox", "fox"))
	fmt.Println(find("crazy brown fx", "fox"))
	fmt.Println(find("cccccccccccasdvsdfbvsdfgbdfgb34tgesrdfrvsad", "34t"))
}

func find(text, pattern string) int {
	badCharTable := [256]int{}
	// initialise dedfault values for bad char table
	for i := range badCharTable {
		badCharTable[i] = len(pattern)
	}
	// creating the bad char table based on the pattern
	// using the formula len(pattern) - 1; i++
	for i := 0; i < len(pattern)-1; i++ {
		badCharTable[pattern[i]] = len(pattern) - i - 1
	}
	// i is the index for text
	i := len(pattern) - 1
	// scan all the text
	for i < len(text) {
		j := len(pattern) - 1
		for j >= 0 && pattern[j] == text[i] {
			j--
			i--
		}
		if j < 0 {
			return i + 1
		}
		// shift the pattern based on badchar table
		i = i + badCharTable[text[i]]
	}
	// nothing has been found
	return -1
}
