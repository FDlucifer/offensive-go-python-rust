package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

type Direction struct {
	East  int
	North int
}

var Directions = []Direction{
	Direction{0, 1},  // east
	Direction{1, 0},  // north
	Direction{0, -1}, // west
	Direction{-1, 0}, // south
}

type Position struct {
	Northing int
	Easting  int
}

type State struct {
	Position
	Facing int
}

func (s State) Turn(steps int) State {
	s.Facing = (s.Facing + steps + len(Directions)) % len(Directions)
	return s
}

func (s State) Walk() State {
	s.Northing += Directions[s.Facing].North
	s.Easting += Directions[s.Facing].East
	return s
}

func (s State) Distance() int {
	return Abs(s.Northing) + Abs(s.Easting)
}

func main() {
	s := State{}
	visits := make(map[Position]int)
	visits[s.Position] += 1

	buf, _ := ioutil.ReadFile("input.txt")
	for _, instruction := range strings.Split(strings.TrimSpace(string(buf)), ", ") {
		//fmt.Println(string(instruction[0]))
		rotation := string(instruction[0])
		blocks, _ := strconv.Atoi(instruction[1:])
		//fmt.Println(blocks)
		if rotation == "L" {
			s = s.Turn(1)
		} else if rotation == "R" {
			s = s.Turn(-1)
		}
		for i := 0; i < blocks; i++ {
			s = s.Walk()
			visits[s.Position] += 1
			if visits[s.Position] == 2 {
				fmt.Printf("Part2: Visited twice distance ==> %v\n", s.Distance())
			}
		}
	}
	fmt.Printf("Part1: %v\n", s.Distance())
}

func Abs(n int) int {
	if n >= 0 {
		return n
	} else {
		return -n
	}
}
