// https://adventofcode.com/2020/day/1
// part 1

package main

import (
	"bytes"
	"io/ioutil"
	"log"
	"strconv"
)

func main() {
	d, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	m := make(map[int]int, 0)
	for _, line := range bytes.Split(d, []byte("\n")) {
		for _, line1 := range bytes.Split(line, []byte("\r")) {
			n, err := strconv.Atoi(string(line1))
			//fmt.Println(n)
			if err != nil {
				log.Println(err)
				continue
			}
			m[n]++
		}
	}
	for y, _ := range m {
		x := 2020 - y
		if _, ok := m[x]; ok {
			log.Printf("%d+%d=2020 / %d*%d=%d", x, y, x, y, x*y)
			return
		}
	}
}
