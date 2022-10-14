package main

import (
	"context"
	"fmt"
	"math/rand"
	"os"
	"os/signal"
	"syscall"
	"time"
)

const (
	minLatency = 10
	maxLatency = 5000
	timeout    = 3000
)

func main() {
	// little program that searches flights routes
	// we are going to use a mock/backend database

	// the purpose of this is to show how the context can be used to propagate cancellation signals across
	// different go routines/ "processes" (abstract processes)

	rootCtx := context.Background()

	ctxWithTimeout, cancel := context.WithTimeout(rootCtx, time.Duration(timeout)*time.Millisecond)
	defer cancel()

	// listen for interrupt signal
	sig := make(chan os.Signal)
	signal.Notify(sig, os.Interrupt, syscall.SIGTERM)
	go func() {
		<-sig
		// NOW cancel
		fmt.Println("aborting due to interrupt...")
		cancel()
	}()
	res, err := Search(ctxWithTimeout, "nyc", "london")
	if err != nil {
		fmt.Println("got error: ", err)
		return
	}
	fmt.Println("got result: ", res)
}

func Search(ctx context.Context, from, to string) ([]string, error) {
	// we need to watch for when ctx.Done() is closed
	res := make(chan []string)
	go func() {
		res <- slowSearch(from, to)
		close(res)
	}()

	// wait for 2 events: either of one will be the result
	for {
		select {
		case dst := <-res:
			return dst, nil
		case <-ctx.Done():
			return []string{}, ctx.Err()
		}
	}
}

// is a very slow function that goes through a series of ooperations and returns a slice of strings
func slowSearch(from, to string) []string {
	// sleep for a random period between 10 and 5000 ms

	rand.Seed(time.Now().Unix())
	latency := rand.Intn(maxLatency-minLatency+1) - minLatency
	fmt.Printf("started to search for %s-%s takes %dms...", from, to, latency)
	time.Sleep(time.Duration(latency) * time.Millisecond)

	return []string{from + "-" + to + "-british airways-11am", from + "-" + to + "-delta airlines-12am"}
}
