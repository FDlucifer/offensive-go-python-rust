package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
)

func main() {
	customsComputation()
}

//Add a # after the last line of the input
func customsComputation() {
	scanner := bufio.NewScanner(os.Stdin)
	unionAnswers := uint32(0)
	intersectionAnswers := ^uint32(0)
	sumOfIntersectionAnswers := 0
	sumOfUnionAnswers := 0

	for scanner.Scan() {
		line := scanner.Text()
		if line == "" || line == "#" {
			sumOfUnionAnswers += bits.OnesCount32(unionAnswers)
			sumOfIntersectionAnswers += bits.OnesCount32(intersectionAnswers)
			unionAnswers = uint32(0)
			intersectionAnswers = ^uint32(0)
		} else {
			lineAnswers := uint32(0)
			for _, question := range line {
				lineAnswers |= 1 << uint32(int(question)-int(rune('a')))
			}
			unionAnswers |= lineAnswers
			intersectionAnswers &= lineAnswers
		}
		if line == "#" {
			break
		}
	}

	fmt.Println(sumOfUnionAnswers)
	fmt.Println(sumOfIntersectionAnswers)
}
