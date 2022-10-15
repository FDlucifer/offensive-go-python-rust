package main

import (
	"fmt"
	"io"
	"log"
	"os"
)

func main() {
	f, err := os.Open("text.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	// read with an offset from the start of the file
	cur, err := f.Seek(16, io.SeekStart)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("current loc from start", cur)
	buf := make([]byte, 3)
	n, err := f.Read(buf)
	if err == io.EOF {
		log.Println("we reached EOF")
	} else if err != nil {
		log.Fatal(err)
	}
	fmt.Println(string(buf[:n]))

	// read with an offset from the end of the file
	cur, err = f.Seek(-4, io.SeekEnd)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("current loc from start", cur)
	buf = make([]byte, 4)
	n, err = f.Read(buf)
	if err == io.EOF {
		log.Println("reached eof")
	} else if err != nil {
		log.Fatal(err)
	}
	fmt.Println(string(buf[:n]))

	// read a file twice or more
	cur, err = f.Seek(0, io.SeekStart)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("current loc from start", cur)
	buf = make([]byte, 1024)
	for {
		n, err = f.Read(buf)
		if err == io.EOF {
			break
		}
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(string(buf[:n]))
	}
}
