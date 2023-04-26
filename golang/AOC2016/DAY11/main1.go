package main

import (
	"bytes"
	"fmt"
	"sort"
	"strconv"
)

type pair struct {
	mcLoc int
	gnLoc int
}

type pairList []pair

func (p pairList) Len() int      { return len(p) }
func (p pairList) Swap(i, j int) { p[i], p[j] = p[j], p[i] }
func (p pairList) Less(i, j int) bool {
	if p[i].mcLoc < p[j].mcLoc {
		return true
	}
	if p[i].mcLoc > p[j].mcLoc {
		return false
	}
	return p[i].gnLoc < p[j].gnLoc
}

type state struct {
	elLoc int
	pairs pairList
}

func (s *state) hash() string {
	buf := new(bytes.Buffer)
	buf.WriteString(strconv.Itoa(s.elLoc))
	for _, p := range s.pairs {
		buf.WriteString(strconv.Itoa(p.mcLoc))
		buf.WriteString(strconv.Itoa(p.gnLoc))
	}
	return buf.String()
}

func (s *state) copy() (new state) {
	new = state{
		elLoc: s.elLoc,
		pairs: make([]pair, len(s.pairs), len(s.pairs)),
	}
	copy(new.pairs, s.pairs)
	return
}

func (s *state) isValid() bool {
	for i := 1; i <= 4; i++ {
		if len(s.getGeneratorIndexesForFloor(i)) > 0 {
			for _, p := range s.pairs {
				if p.mcLoc == i && p.gnLoc != p.mcLoc {
					return false
				}
			}
		}
	}
	return true
}

func (s *state) getGeneratorIndexesForFloor(floor int) (ixs []int) {
	for i, p := range s.pairs {
		if p.gnLoc == floor {
			ixs = append(ixs, i)
		}
	}
	return
}

func (s *state) getMicrochipIndexesForFloor(floor int) (ixs []int) {
	for i, p := range s.pairs {
		if p.mcLoc == floor {
			ixs = append(ixs, i)
		}
	}
	return
}

func (s *state) isFinal() bool {
	for _, p := range s.pairs {
		if p.gnLoc != 4 || p.mcLoc != 4 {
			return false
		}
	}
	return true
}

func (s *state) moveElevator(direction int, microchipindexes, generatorindexes []int) {
	for _, m := range microchipindexes {
		s.pairs[m].mcLoc += direction
	}
	for _, g := range generatorindexes {
		s.pairs[g].gnLoc += direction
	}
	sort.Sort(s.pairs)
	s.elLoc += direction
}

func (s *state) getPossibleNextStates() (states []state) {

	mIxs, gIxs := s.getMicrochipIndexesForFloor(s.elLoc), s.getGeneratorIndexesForFloor(s.elLoc)

	mIxsToMove, gIxsToMove := [][]int{}, [][]int{}

	for i, mIx := range mIxs {
		// move alone first, then combine with other objects
		mIxsToMove, gIxsToMove = append(mIxsToMove, []int{mIx}), append(gIxsToMove, []int{})
		for _, mIx2 := range mIxs[i+1:] {
			mIxsToMove, gIxsToMove = append(mIxsToMove, []int{mIx, mIx2}), append(gIxsToMove, []int{})
		}
	}

	for i, gIx := range gIxs {
		// move alone first, then combine with other objects
		mIxsToMove, gIxsToMove = append(mIxsToMove, []int{}), append(gIxsToMove, []int{gIx})
		for _, gIx2 := range gIxs[i+1:] {
			mIxsToMove, gIxsToMove = append(mIxsToMove, []int{}), append(gIxsToMove, []int{gIx, gIx2})
		}
	}

	// if microchip and generator are both on this floor, they can be moved together
	for i, p := range s.pairs {
		if p.mcLoc == s.elLoc && p.gnLoc == s.elLoc {
			mIxsToMove, gIxsToMove = append(mIxsToMove, []int{i}), append(gIxsToMove, []int{i})
		}
	}

	// execute the moves and check if the results are valid
	for _, dir := range []int{-1, 1} {
		if s.elLoc+dir > 0 && s.elLoc+dir <= 4 {
			for i := range mIxsToMove {
				new := s.copy()
				new.moveElevator(dir, mIxsToMove[i], gIxsToMove[i])
				if new.isValid() {
					states = append(states, new)
				}
			}
		}
	}
	return
}

func (s state) getMinimumStepsToSolution() (steps int) {
	currentStates := []state{s}
	previousStateHashes := map[string]bool{s.hash(): true}

	for {
		steps++
		nextStates := []state{}
		for _, cs := range currentStates {
			for _, ns := range cs.getPossibleNextStates() {
				if ns.isFinal() {
					return
				}
				nsHash := ns.hash()
				if !previousStateHashes[nsHash] {
					nextStates = append(nextStates, ns)
					previousStateHashes[nsHash] = true
				}
			}
		}
		currentStates = nextStates
	}
}

func main() {
	s := state{
		elLoc: 1,
		pairs: pairList{
			pair{1, 1}, //strontium
			pair{1, 1}, //plutonium
			pair{3, 2}, //strontium
			pair{2, 2}, //curium
			pair{2, 2}, //rhutenium
		},
	}
	sort.Sort(s.pairs)

	s2 := state{
		elLoc: 1,
		pairs: pairList{
			pair{1, 1}, //strontium
			pair{1, 1}, //plutonium
			pair{1, 1}, //elerium
			pair{1, 1}, //dilithium
			pair{3, 2}, //strontium
			pair{2, 2}, //curium
			pair{2, 2}, //rhutenium
		},
	}
	sort.Sort(s2.pairs)

	fmt.Println("The minimum number of steps required is", s.getMinimumStepsToSolution())
	fmt.Println("The minimum number of steps required with the unexpected parts is", s2.getMinimumStepsToSolution())
}
