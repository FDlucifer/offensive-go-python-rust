// https://adventofcode.com/2020/day/2
// part 1
// code running on go version go1.13.8 linux/amd64 or windows

package main

import (
	"bytes"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

func main() {
	c, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	// 1-2 a: abc
	valid := 0
	for _, line := range bytes.Split(c, []byte("\n")) {
		parts := strings.Split(string(line), " ")
		if len(parts) < 3 {
			log.Println("parts less than 3 ", string(line))
			continue
		}
		lh := strings.Split(parts[0], "-")
		if len(lh) < 2 {
			log.Println("parts less than 2")
			continue
		}
		low, _ := strconv.Atoi(lh[0])
		high, _ := strconv.Atoi(lh[1])
		pattern := []rune(strings.ReplaceAll(parts[1], ":", ""))
		pwd := []rune(parts[2])

		i := 0
		for _, c := range pwd {
			if c == pattern[0] {
				i++
			}
		}
		if i <= high && i >= low {
			valid++
		}
	}
	log.Println(valid)
}
