package main

import (
	"fmt"
	"net"
	"os"
	"sort"
	"strconv"
	"strings"
)

func worker(ports, results chan int) {
	for p := range ports {
		conn, err := net.Dial("tcp", os.Args[3]+":"+strconv.Itoa(p))
		if err != nil {
			results <- 0
			continue
		}
		conn.Close()
		results <- p
	}
}

func main() {
	if len(os.Args) != 4 {
		fmt.Println("please give all the required arguments!")
		os.Exit(1)
	}

	numOfWorkers, _ := strconv.Atoi(os.Args[1])
	portRange := strings.Split(os.Args[2], ":")
	startPort, _ := strconv.Atoi(portRange[0])
	endPort, _ := strconv.Atoi(portRange[1])

	ports := make(chan int, numOfWorkers)
	results := make(chan int)

	var openPorts []int

	for i := 0; i <= cap(ports); i++ {
		go worker(ports, results)
	}

	go func() {
		for i := startPort; i <= endPort; i++ {
			ports <- i
		}
	}()

	for i := startPort; i <= endPort; i++ {
		port := <-results
		if port != 0 {
			fmt.Printf("%d port is open\n", port)
			openPorts = append(openPorts, port)
		}
	}
	close(ports)
	close(results)

	sort.Ints(openPorts)
	fmt.Printf("list of open ports -> ")
	fmt.Println(openPorts)
}
