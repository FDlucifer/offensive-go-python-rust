package main

import "fmt"

func main() {
	// array definition
	var a [3]int
	b := [3]int{1, 2, 3}
	c := [...]int{1, 2, 3, 4}
	fmt.Println("a", a)
	fmt.Println("b", b)
	fmt.Println("c", c)

	// direct addressing
	a[2] = 31
	fmt.Println("a", a)

	// slice definition
	s1 := []int{1, 2, 3}    // underlying array: [3]int{1, 2, 3}
	s2 := make([]int, 3, 6) // underlying array: [6]int{0, 0, 0, 0, 0, 0}
	fmt.Println("s1", s1, "cap", cap(s1), "len", len(s1))
	fmt.Println("s2", s2, "cap", cap(s2), "len", len(s2))

	// slicing operator
	b1 := s1[1:3]
	fmt.Println("b1", b1, "cap", cap(b1), "len", len(b1))

	// when using the slicing operator
	// all the subsequent slices use the same underlying array under the hood!
	s1[2] = 42
	fmt.Println("b1", b1, "cap", cap(b1), "len", len(b1))

	// convert static array to slice
	key := [32]byte{}
	keyS := key[:] // converts array to slice
	fmt.Println("keyS", keyS, "cap", cap(keyS), "len", len(keyS))

	// to avoid side effects instead of using slicing operator which shares the underlying array
	// just copy the entire slice to a new one
	s1 = []int{1, 2, 3}
	b2 := make([]int, len(s1))
	//for i, _ := range s1 {
	//	b2[i] = s1[i]
	//}
	// same as "copy" func see doc at: go doc builtin.copy
	copyInt(b2, s1)

	fmt.Println("b2", b2, "cap", cap(b2), "len", len(b2))
	s1[2] = 41
	fmt.Println("b2", b2, "cap", cap(b2), "len", len(b2))

	s2 = make([]int, 3, 10)
	fmt.Println("s2", s2, "cap", cap(s2), "len", len(s2))
	// increase the length of s2 just use the slicing operator
	// works up until the cap(s2)
	s2 = s2[:5]
	fmt.Println("s2", s2, "cap", cap(s2), "len", len(s2))
	s1 = []int{1, 2, 3}
	fmt.Println("s1", s1, "cap", cap(s1), "len", len(s1))
	s1 = appendInt(s1, 31)
	fmt.Println("s1", s1, "cap", cap(s1), "len", len(s1))

}

func copyInt(dst, src []int) int {
	var n int
	for i, _ := range src {
		dst[i] = src[i]
		n++
	}
	return n
}

func appendInt(s []int, e int) []int {
	expLen := len(s) + 1
	if cap(s) < expLen {
		// grow the slice
		// new allocation create new slice from scratch
		newS := make([]int, expLen, (cap(s)+1)*2)
		// copy the data from old to new
		copyInt(newS, s)
		// assign new to old
		s = newS
	}
	// grow len
	s = s[:expLen]
	// assign the element
	s[expLen-1] = e
	return s
}
