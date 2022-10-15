package main

import "fmt"

func main() {
	// var a, b, c int8
	// a := 10
	joe := person{Name: "joe"}
	p := &joe
	// b := 20
	// c := a + b
	// var p *int
	fmt.Printf("main.go: addr: %p val: %v\n", p, joe)
	changeName(p)
	fmt.Printf("main.go: addr: %p val: %v\n", p, joe)
}

type person struct{ Name string }

func changeNumber(pointerToANumber *int) {
	*pointerToANumber = 42
}

func changePerson(pointerToPerson *person) {
	jane := &person{Name: "jane"}
	pointerToPerson = jane
}

func changeName(p *person) {
	(*p).Name = "bob"
}
