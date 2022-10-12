package main

import (
	"bytes"
	"io/ioutil"
	"log"
	"regexp"
	"strconv"
	"strings"
)

var validationFuncs = map[string]func(string) bool{
	"byr": func(v string) bool {
		intVal, err := strconv.Atoi(v)
		if err != nil {
			return false
		}
		return 1920 <= intVal && intVal <= 2002
	},
	"iyr": func(v string) bool {
		intVal, err := strconv.Atoi(v)
		if err != nil {
			return false
		}
		return 2010 <= intVal && intVal <= 2020
	},
	"eyr": func(v string) bool {
		intVal, err := strconv.Atoi(v)
		if err != nil {
			return false
		}
		return 2020 <= intVal && intVal <= 2030
	},
	"hgt": func(v string) bool {
		heightRe := regexp.MustCompile("^(\\d+)(cm|in)$")
		matches := heightRe.FindStringSubmatch(v)
		if len(matches) < 3 {
			return false
		}
		intVal, err := strconv.Atoi(matches[1])
		if err != nil {
			return false
		}
		if matches[2] == "cm" && 150 <= intVal && intVal <= 193 {
			return true
		}
		if matches[2] == "in" && 59 <= intVal && intVal <= 76 {
			return true
		}
		return false
	},
	"hcl": func(v string) bool {
		hclRe := regexp.MustCompile("^\\#[0-9a-f]{6}$")
		return hclRe.MatchString(v)
	},
	"ecl": func(v string) bool {
		valid := []string{"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
		for _, c := range valid {
			if v == c {
				return true
			}
		}
		return false
	},
	"pid": func(v string) bool {
		pidRe := regexp.MustCompile("^[0-9]{9}$")
		return pidRe.MatchString(v)
	},
	"cid": func(v string) bool {
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
