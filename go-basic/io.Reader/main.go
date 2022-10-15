package main

import (
	"fmt"
	"io"
	"net"
	"os"
	"strings"
)

func main() {
	stringsReader()
}

func connReader() {
	conn, err := net.Dial("tcp", "google.com:80")
	if err != nil {
		panic(err)
	}
	defer conn.Close()

	fmt.Fprint(conn, "GET HTTP 1.0\r\n\r\n")
	readerToStdout(conn, 25)
}

func stringsReader() {
	s := strings.NewReader("very short but interesting string")
	readerToStdout(s, 2)
}

func fileReader() {
	f, err := os.Open("small.txt")
	if err != nil {
		panic(err)
	}
	defer f.Close()
	readerToStdout(f, 3)
}

func readerToStdout(r io.Reader, bufSize int) {
	buf := make([]byte, bufSize)
	for {
		n, err := r.Read(buf)
		if err == io.EOF {
			break
		}
		if err != nil {
			fmt.Println(err)
			break
		}
		if n > 0 {
			fmt.Println(string(buf[:n]))
		}
	}
}
