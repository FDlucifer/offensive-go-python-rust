package main

import (
	"bytes"
	"io/ioutil"
	"log"
	"sort"
)

func main() {
	c, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	seats := []int{}
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
		seats = append(seats, seatID)
	}
	sort.Ints(seats)
	prev := seats[0]
	for i := 1; i < len(seats); i++ {
		if seats[i] != prev+1 {
			log.Println(prev + 1)
			break
		}
		prev = seats[i]
	}
}
