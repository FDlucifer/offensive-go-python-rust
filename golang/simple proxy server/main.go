package main

import (
	"io"
	"log"
	"net"
)

func main() {
	listener, err := net.Listen("tcp", ":1111")
	if err != nil {
		log.Fatalln("unable to bind on port")
	}

	for {
		conn, err := listener.Accept()
		if err != nil {
			log.Fatalln("unable to accept connection")
		}
		go handleConn((conn))
	}
}

func handleConn(src net.Conn) {
	dst, err := net.Dial("tcp", "http://www.google.com:80")
	if err != nil {
		log.Fatalln("unable to connect to target server")
	}
	defer dst.Close()

	go func() {
		if _, err := io.Copy(dst, src); err != nil {
			log.Fatalln(err)
		}
	}()
	if _, err := io.Copy(src, dst); err != nil {
		log.Fatalln(err)
	}
}
