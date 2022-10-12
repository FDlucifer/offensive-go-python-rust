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

	tot1 := walkDown(1, 1, m)
	tot2 := walkDown(3, 1, m)
	tot3 := walkDown(5, 1, m)
	tot4 := walkDown(7, 1, m)
	tot5 := walkDown(1, 2, m)
	log.Println(tot1 * tot2 * tot3 * tot4 * tot5)
}

func walkDown(rightStep, downStep int, m [][]rune) int {
	down := downStep
	right := rightStep
	tot := 0
	for down < len(m) {
		row := m[down]
		if row[right%len(row)] == '#' {
			tot++
		}
		down += downStep
		right += rightStep
	}
	return tot
}
