package main

import (
	"bytes"
	"io/ioutil"
	"log"
	"strings"
)

var validationFuncs = map[string]func(string) bool{
	"byr": func(v string) bool {
		return true
	},
}

func main() {
	c, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	passports := make([]map[string]string, 0)
	for _, line := range bytes.Split(c, []byte("\n\n")) {
		if len(line) == 0 {
			continue
		}
		p := make(map[string]string)
		for _, subline := range bytes.Split(line, []byte("\n")) {
			if len(subline) == 0 {
				continue
			}
			for _, kv := range bytes.Split(subline, []byte(" ")) {
				parts := strings.Split(string(kv), ":")
				p[parts[0]] = parts[1]
			}
		}
		passports = append(passports, p)
	}
	valid := 0
	for _, p := range passports {
		if isValidPassport(p) {
			valid++
		}
	}
	log.Println(valid)
}

func isValidPassport(p map[string]string) bool {
	for k, v := range p {
		if validFunc, ok := validationFuncs[k]; ok && !validFunc(v) {
			return false
		}
	}
	_, isCIDPresent := p["cid"]
	if len(p) == 8 || (len(p) == 7 && !isCIDPresent) {
		return true
	}
	return false
}
