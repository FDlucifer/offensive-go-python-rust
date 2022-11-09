package main

import (
	"crypto/md5"
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
	"strings"
)

func ToInt(arg interface{}) int {
	var val int
	switch arg.(type) {
	case string:
		var err error
		val, err = strconv.Atoi(arg.(string))
		if err != nil {
			panic("error converting string to int " + err.Error())
		}
	default:
		panic(fmt.Sprintf("unhandled type for int casting %T", arg))
	}
	return val
}

func main() {
	buf, _ := ioutil.ReadFile("input.txt")

	ans := md5Chess(string(buf), 1)
	fmt.Println("Part1: ", ans)

	ans1 := md5Chess(string(buf), 2)
	fmt.Println("Part2: ", ans1)
}

func md5Chess(input string, part int) string {
	passwordParts := map[int]string{}
	var part1Index int

	for i := 0; len(passwordParts) < 8; i++ {
		in := fmt.Sprintf("%s%d", input, i)
		hash := fmt.Sprintf("%x", md5.Sum([]byte(in)))

		if strings.HasPrefix(hash, "00000") {
			if part == 1 {
				passwordParts[part1Index] = hash[5:6]
				part1Index++
			} else {
				if regexp.MustCompile("[0-7]").MatchString(hash[5:6]) {
					index := ToInt(hash[5:6])
					if _, ok := passwordParts[index]; !ok {
						value := hash[6:7]
						passwordParts[index] = value
					}
				}
			}
		}
	}

	var password string
	for i := 0; i < 8; i++ {
		password += passwordParts[i]
	}

	return password
}
