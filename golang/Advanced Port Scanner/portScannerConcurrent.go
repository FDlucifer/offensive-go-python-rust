package main

import (
	"fmt"
	"net"
	"sync"
)

func main() {
	var wg sync.WaitGroup
	for i := 1; i <= 1024; i++ {
		wg.Add(1)
		go func(j int) {
			defer wg.Done()
			address := fmt.Sprintf("scanme.nmap.org:%d", j)
			_, err := net.Dial("tcp", address)
			if err != nil {
				//continue
			}
			//conn.Close()
			fmt.Printf("port opened: %d\n", j)
		}(i)
	}
	wg.Wait()
}
