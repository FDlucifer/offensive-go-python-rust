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
	max := 0
	for _, line := range bytes.Split(c, []byte("\n")) {
		if len(line) == 0 {
			continue
		}
		lineStr := string(line)
		left := 0
		right := 127
		for _, c := range lineStr[:7] {
			middle := (right + left + 1) / 2
			if c == 'B' {
				left = middle
			} else {
				right = middle - 1
			}
		}
		row := left
		left = 0
		right = 7
		for _, c := range lineStr[:7] {
			middle := (right + left + 1) / 2
			if c == 'R' {
				left = middle
			} else {
				right = middle - 1
			}
		}
		col := left
		seatID := row*8 + col
		if seatID > max {
			max = seatID
		}
	}
	log.Println(max)
}
