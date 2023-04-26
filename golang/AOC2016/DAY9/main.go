package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"path"
	"runtime"
	"strings"
)

func ReadFile(pathFromCaller string) string {
	// Docs: https://golang.org/pkg/runtime/#Caller
	_, filename, _, ok := runtime.Caller(1)
	if !ok {
		panic("Could not find Caller of util.ReadFile")
	}

	// parse directory with pathFromCaller (which could be relative to Directory)
	absolutePath := path.Join(path.Dir(filename), pathFromCaller)

	// read the entire file & return the byte slice as a string
	content, err := ioutil.ReadFile(absolutePath)
	if err != nil {
		panic(err)
	}
	// trim off new lines and tabs at end of input files
	strContent := string(content)
	return strings.TrimRight(strContent, "\n")
}

func main() {
	var part int
	flag.IntVar(&part, "part", 1, "part 1 or 2")
	flag.Parse()
	fmt.Println("Running part", part)

	ans := decompressLength(ReadFile("./input.txt"), part)
	fmt.Println("Output:", ans)
}

// well...... this is gross.......
func decompressLength(in string, part int) int {
	var decompressedLen int
	for i := 0; i < len(in); {
		switch in[i] {
		case '(':
			// find index of closing paren, then find total length of substring
			relativeCloseIndex := strings.Index(in[i:], ")")
			closeIndex := relativeCloseIndex + i

			var copyLen, repeat int
			fmt.Sscanf(in[i:closeIndex+1], "(%dx%d)", &copyLen, &repeat)

			substring := in[closeIndex+1 : closeIndex+1+copyLen]
			patternLength := len(substring)
			if part == 2 {
				patternLength = decompressLength(substring, 2)
			}
			decompressedLen += patternLength * repeat
			// jump the closed paren (+1) the length of the substring from THIS
			// function call
			i = closeIndex + 1 + len(substring)
		default:
			decompressedLen++
			i++
		}
	}
	return decompressedLen
}
