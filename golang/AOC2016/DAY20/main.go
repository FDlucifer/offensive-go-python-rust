package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"math"
	"path"
	"runtime"
	"sort"
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

	ans := firewall(ReadFile("./input.txt"), part)
	fmt.Println("Output:", ans)
}

func MaxInt(nums ...int) int {
	maxNum := nums[0]
	for _, v := range nums {
		if v > maxNum {
			maxNum = v
		}
	}
	return maxNum
}

func firewall(input string, part int) int {
	var allBlockedRanges [][2]int
	for _, line := range strings.Split(input, "\n") {
		var r [2]int
		fmt.Sscanf(line, "%d-%d", &r[0], &r[1])
		allBlockedRanges = append(allBlockedRanges, r)
	}
	sort.Slice(allBlockedRanges, func(i, j int) bool {
		if allBlockedRanges[i][0] != allBlockedRanges[j][0] {
			return allBlockedRanges[i][0] < allBlockedRanges[j][0]
		}
		return allBlockedRanges[i][1] < allBlockedRanges[j][1]
	})

	// merge allBlockedRanges
	merged := [][2]int{[2]int{}}
	for _, r := range allBlockedRanges {
		endOfLastRange := merged[len(merged)-1][1]
		if endOfLastRange >= r[0]-1 {
			merged[len(merged)-1][1] = MaxInt(endOfLastRange, r[1])
		} else {
			merged = append(merged, r)
		}
	}

	if part == 1 {
		return merged[0][1] + 1
	}

	if merged[len(merged)-1][1] != math.MaxUint32 {
		merged = append(merged, [2]int{math.MaxUint32, 0})
	}

	var totalAllowed int
	for i := 1; i < len(merged); i++ {
		totalAllowed += merged[i][0] - merged[i-1][1] - 1
	}

	return totalAllowed
}
