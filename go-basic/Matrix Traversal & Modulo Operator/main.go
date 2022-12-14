package main

import (
	"bytes"
	"io/ioutil"
	"log"
)

func main() {
	c, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	m := make([][]rune, 0)
	for _, line := range bytes.Split(c, []byte("\n")) {
		if len(line) == 0 {
			continue
		}
		row := make([]rune, 0)
		for _, c := range string(line) {
			row = append(row, c)
		}
		m = append(m, row)
	}

	tot := 0
	right := 3
	down := 1
	for down < len(m) {
		row := m[down]
		if row[right%len(row)] == '#' {
			tot++
		}
		down++
		right += 3
	}
	log.Println(tot)
}
