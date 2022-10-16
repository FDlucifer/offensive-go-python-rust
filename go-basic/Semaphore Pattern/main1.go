package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"runtime"
	"sync"
)

type Task struct {
	ID        int    `json:"id"`
	UserID    int    `json:"user_id"`
	Title     string `json:"title"`
	Completed bool   `json:"completed"`
}

func main() {
	var t Task
	wg := &sync.WaitGroup{}
	wg.Add(100)
	sem := make(chan bool, 10)
	for i := 0; i < 100; i++ {
		fmt.Println(runtime.NumGoroutine())
		i := i
		sem <- true
		go func() {
			defer wg.Done()
			defer func() { <-sem }()
			res, err := http.Get(fmt.Sprintf("https://jsonplaceholder.typicode.com/todos/%d", i))
			if err != nil {
				log.Fatal(err)
			}
			defer res.Body.Close()
			if err := json.NewDecoder(res.Body).Decode(&t); err != nil {
				log.Fatal(err)
			}
			fmt.Println(t.Title)
		}()
	}
	wg.Wait()
}
