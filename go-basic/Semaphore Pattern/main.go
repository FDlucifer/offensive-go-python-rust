package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"runtime"
	"sync"

	"golang.org/x/sync/errgroup"
	"golang.org/x/sync/semaphore"
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
	sem := semaphore.NewWeighted(10)
	errGroup, ctx := errgroup.WithContext(context.Background())
	for i := 0; i < 100; i++ {
		fmt.Println(runtime.NumGoroutine())
		if err := sem.Acquire(ctx, 1); err != nil {
			log.Fatal(err)
		}
		i := i
		errGroup.Go(func() error {
			defer wg.Done()
			defer sem.Release(1)
			res, err := http.Get(fmt.Sprintf("https://jsonplaceholder.typicode.com/todos/%d", i))
			if err != nil {
				return err
			}
			defer res.Body.Close()
			if err := json.NewDecoder(res.Body).Decode(&t); err != nil {
				return err
			}
			fmt.Println(t.Title)
			return nil
		})
	}
	if err := errGroup.Wait(); err != nil {
		log.Fatal(err)
	}
}
