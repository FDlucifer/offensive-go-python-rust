package main

import (
	"fmt"

	"errors"
	"math"
)

func main() {
	fmt.Println(math.Max(1, 2))
	fmt.Println(errors.New("testing new error"))
}
