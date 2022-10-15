package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
)

// Each line gives the password policy and then the password.
// The password policy indicates the lowest and highest number of times
// a given letter must appear for the password to be valid.

// 1-3 a: aabacd
// 4-4 b: bbaaacd
// ...

// For example, '1-3 a' means that the password must contain
// 'a' at least 1 time and at most 3 times.

func main() {
	contents, err := ioutil.ReadFile("1.txt")
	if err != nil {
		panic(err)
	}
	fmt.Print(solve(contents))
}

func solve(contents []byte) int {
	valid := 0
	for _, line := range bytes.Split(contents, []byte("\n")) {
		lineStr := string(line)
		layout := regexp.MustCompile(`([0-9]+)-([0-9]+)\s(\w){1}:\s([a-z]+)$`)
		matches := layout.FindStringSubmatch(lineStr)
		if len(matches) < 5 {
			continue
		}
		min, _ := strconv.Atoi(matches[1])
		max, _ := strconv.Atoi(matches[2])
		pattern := []rune(matches[3])
		data := string(matches[4])
		x := 0
		for _, c := range data {
			if c == pattern[0] {
				x++
			}
		}
		if x > max || x < min {
			continue
		}
		valid++
	}
	return valid
}
