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
	tot := 0
	for _, group := range bytes.Split(c, []byte("\n\n")) {
		qs := make(map[rune]struct{})
		for _, line := range bytes.Split(group, []byte("\n")) {
			for _, c := range string(line) {
				qs[c] = struct{}{}
			}
		}
		tot += len(qs)
	}
	log.Println(tot)
}
