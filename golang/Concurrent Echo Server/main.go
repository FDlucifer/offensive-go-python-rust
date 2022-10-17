package main

import (
	"io"
	"log"
	"net"
)

func echo(conn net.Conn) {
	defer conn.Close()
	if _, err := io.Copy(conn, conn); err != nil {
		log.Fatalln("unable to read/write data...")
	}
}

func main() {
	listener, err := net.Listen("tcp", ":2000")
	if err != nil {
		log.Fatalln("unable to bind to port...")
	}

	log.Println("listening on 0.0.0.0:2000")

	for {
		conn, err := listener.Accept()
		log.Println("recieved a connection!")
		if err != nil {
			log.Fatalln("unable to accept connection")
		}
		echo(conn)
	}
}
