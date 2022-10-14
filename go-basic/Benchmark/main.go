package main

import (
	"fmt"
	"testing"
)

var m = make(map[int]int, 0)

func quickFibonacci(n int) int {
	if n < 2 {
		return n
	}

	var f int
	if v, ok := m[n]; ok {
		f = v
	} else {
		f = fibonacci(n-2) + fibonacci(n-1)
		m[n] = f
	}

	return f
}

func fibonacci(n int) int {
	if n < 2 {
		return n
	}

	return fibonacci(n-1) + fibonacci(n-2)
}

// fb(0) = 0
// fb(1) = 1
// fb(n) = fib(n-1) + fib(n-2)

// 0 1 1 2 3 5 8 13 ....
// 0 1 2 3 4 5 6 7

func TestFibonacci(t *testing.T) {
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

func BenchmarkFibonacci(b *testing.B) {
	seqs := []int{10, 20, 30, 40}
	for _, seq := range seqs {
		b.Run(fmt.Sprintf("benchmark-seq-%d", seq), func(b *testing.B) {
			for i := 0; i < b.N; i++ {
				fibonacci(seq)
			}
		})
	}
}

func BenchmarkQuickFibonacci(b *testing.B) {
	seqs := []int{10, 20, 30, 40}
	for _, seq := range seqs {
		b.Run(fmt.Sprintf("benchmark-seq-%d", seq), func(b *testing.B) {
			for i := 0; i < b.N; i++ {
				quickFibonacci(seq)
			}
		})
	}
}

// go test -run=xxx -v -bench=. -benchtime 3s
