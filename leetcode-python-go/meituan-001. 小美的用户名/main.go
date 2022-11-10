package main

import (
	"fmt"
	"unicode"
)

func check(s string) string {
	d := false
	for i, c := range s {
		if i == 0 {
			if !unicode.IsLetter(c) {
				return "Wrong"
			}
		}
		if !unicode.IsLetter(c) && !unicode.IsNumber(c) {
			return "Wrong"
		} else if unicode.IsNumber(c) {
			d = true
		}
	}
	if d {
		return "Accept"
	} else {
		return "Wrong"
	}
}

func main() {
	var T int
	var s string
	fmt.Scanln(&T)
	for i := 0; i < T; i++ {
		fmt.Scanln(&s)
		fmt.Printf("%s\n", check(s))
	}
}
