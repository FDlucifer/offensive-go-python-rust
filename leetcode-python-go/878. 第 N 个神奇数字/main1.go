package main

import (
	"fmt"
)

const mod int = 1e9 + 7

func nthMagicalNumber(n, a, b int) int {
	c := a / gcd(a, b) * b
	m := c/a + c/b - 1
	r := n % m
	res := c * (n / m) % mod
	if r == 0 {
		return res
	}
	addA := a
	addB := b
	for i := 0; i < r-1; i++ {
		if addA < addB {
			addA += a
		} else {
			addB += b
		}
	}
	return (res + min(addA, addB)%mod) % mod
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}

func gcd(a, b int) int {
	if b != 0 {
		return gcd(b, a%b)
	}
	return a
}

func main() {
	n := 4
	a := 2
	b := 3
	results := nthMagicalNumber(n, a, b)
	fmt.Println(results)
}
