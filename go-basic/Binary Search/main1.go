package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	var puzzleInput []string = getPuzzleInput()
	var seatNumbers []int

	for i := 0; i < len(puzzleInput); i++ {
		seatNumbers = append(seatNumbers, getSeatNumber(puzzleInput[i]))
	}
	sort.Ints(seatNumbers)
	fmt.Println(seatNumbers[len(seatNumbers)-1])
	fmt.Println(getMissingSeat(seatNumbers))
}

func getPuzzleInput() []string {
	scanner := bufio.NewScanner(os.Stdin)
	var puzzleInput []string
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			break
		}
		puzzleInput = append(puzzleInput, line)
	}
	return puzzleInput
}

func getSeatNumber(seatData string) int {
	minRowNumber := 0
	maxRowNumber := 127
	minColNumber := 0
	maxColNumber := 7
	for i := 0; i < len(seatData); i++ {
		if i <= 6 {
			if seatData[i] == 'F' {
				maxRowNumber = (minRowNumber + maxRowNumber) / 2
			} else {
				minRowNumber = (minRowNumber+maxRowNumber)/2 + 1
			}
		} else {
			if seatData[i] == 'L' {
				maxColNumber = (minColNumber + maxColNumber) / 2
			} else {
				minColNumber = (minColNumber+maxColNumber)/2 + 1
			}
		}
	}
	var seatNumber int = minRowNumber*8 + minColNumber
	return seatNumber
}

func getMissingSeat(seatNumbers []int) int {
	for i := 0; i < len(seatNumbers)-1; i++ {
		if seatNumbers[i+1]-seatNumbers[i] != 1 {
			return seatNumbers[i] + 1
		}
	}
	return -1
}
