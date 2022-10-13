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
		qs := make(map[rune]int)
		for _, person := range bytes.Split(group, []byte("\n")) {
			for _, c := range string(person) {
				qs[c]++
			}
		}
		for _, c := range qs {
			if c == len(bytes.Split(group, []byte("\n"))) {
				tot++
			}
		}
	}
	log.Println(tot)
}
