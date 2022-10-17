package main

import (
	"fmt"
	"io"
	"log"
	"os"
)

type demoRead struct{}

func (d *demoRead) Read(b []byte) (int, error) {
	fmt.Println("in> ")
	return os.Stdin.Read(b)
}

type demoWrite struct{}

func (d *demoRead) Write(b []byte) (int, error) {
	fmt.Println("out> ")
	return os.Stdin.Write(b)
}

func main() {
	var (
		reader demoRead
		writer demoWrite
	)

	input := make([]byte, 4096)

	s, err := reader.Read(input)
	if err != nil {
		log.Fatalln("unable to read data!")
	}
	fmt.Printf("read %d bytes", s)

	w, err := writer.Write(input)
	if err != nil {
		log.Fatalln("unable to Write data!")
	}
	fmt.Printf("Write %d bytes", w)

	_, err := io.Copy(&writer, &reader)
	if err != nil {
		log.Fatalln("unable to read/write data")
	}
}
