package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func main() {
	buf, _ := ioutil.ReadFile("input.txt")

	ans := part1(string(buf))
	fmt.Println("Part1: ", ans)

	ans1 := part2(string(buf))
	fmt.Println("Part2: ", ans1)
}

func part1(input string) int {
	insideBraces, outsideBraces := parseInput(input)

	var count int
	for i := range insideBraces {
		inside, outside := insideBraces[i], outsideBraces[i]
		var insidesHaveABBA bool
		for _, str := range inside {
			if hasABBA(str) {
				insidesHaveABBA = true
				break
			}
		}
		if !insidesHaveABBA {
			var outsidesHaveABBA bool
			for _, str := range outside {
				if hasABBA(str) {
					outsidesHaveABBA = true
				}
			}
			if outsidesHaveABBA {
				count++
			}
		}
	}

	return count
}

func hasABBA(str string) bool {
	for i := 3; i < len(str); i++ {
		// match outsides, match insides, ensure insides and outsides are different
		if str[i-3] == str[i] && str[i-2] == str[i-1] && str[i] != str[i-1] {
			return true
		}
	}
	return false
}

func part2(input string) int {
	insideBraces, outsideBraces := parseInput(input)

	var count int
	for i := range insideBraces {
		inside, outside := insideBraces[i], outsideBraces[i]

		insideABAs := findABAs(inside)
		outsideABAs := findABAs(outside)

		for aba := range insideABAs {
			// make new string in pattern BAB and see if it's in the outside hashmap
			bab := fmt.Sprintf("%s%s%s", aba[1:2], aba[0:1], aba[1:2])
			if outsideABAs[bab] {
				count++
				break
			}
		}
	}

	return count
}

func findABAs(strs []string) map[string]bool {
	found := map[string]bool{}
	for _, str := range strs {
		for i := 2; i < len(str); i++ {
			if str[i-2] == str[i] && str[i] != str[i-1] {
				found[str[i-2:i+1]] = true
			}
		}
	}
	return found
}

func parseInput(input string) (insides, outsides [][]string) {
	for _, line := range strings.Split(input, "\n") {
		var collectChars string
		var insideBraces, outsideBraces []string

		// lazy, add an open bracket at the end to add the last collected string
		// to the slice. A tricky input could've broken this logic
		for _, rn := range line + "[" {
			switch char := string(rn); char {
			case "[":
				outsideBraces = append(outsideBraces, collectChars)
				collectChars = ""
			case "]":
				insideBraces = append(insideBraces, collectChars)
				collectChars = ""
			default:
				collectChars += char
			}
		}
		insides = append(insides, insideBraces)
		outsides = append(outsides, outsideBraces)
	}
	return insides, outsides
}
