package main

import (
	"fmt"
	"testing"
)

func fibonacci(n int) int {
	if n < 2 {
		return n
	}

	return fibonacci(n-1) + fibonacci(n-2)
}

func TestFibonacci1(t *testing.T) {
	testCases := []struct{ seqNo, expected int }{
		{0, 0},
		{1, 1},
		{2, 1},
		{3, 2},
		{5, 5},
		{10, 55},
	}
	for n, tc := range testCases {
		testCase := tc
		t.Run(fmt.Sprintf("test-case-%d", n), func(t *testing.T) {
			t.Parallel()
			out := fibonacci(testCase.seqNo)
			if out != testCase.expected {
				t.Errorf("fibonacci(%d) = %d; got %d", testCase.seqNo, testCase.expected, out)
			}
		})
	}
}

// fb(0) = 0
// fb(1) = 1
// fb(2) = 1
// fb(n) = fib(n-1) + fib(n-2)

// 0 1 1 2 3 5 8 13 ....

// val: 0 1 1 2 3 5 8 13 21 34 55
// pos: 0 1 2 3 4 5 6 7  8  9  10
