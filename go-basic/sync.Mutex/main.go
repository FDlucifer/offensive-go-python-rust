package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

type cache struct {
	mu sync.RWMutex
	m  map[string]int
}

var inMemoryCache = &cache{m: make(map[string]int)}

func main() {
	rand.Seed(time.Now().UnixNano())
	wg := &sync.WaitGroup{}
	wg.Add(100)
	for i := 0; i < 100; i++ {
		go save(fmt.Sprintf("user_id_%d", rand.Intn(100)), rand.Intn(100), wg)
	}

	wg.Add(100)
	for i := 0; i < 100; i++ {
		go func() {
			inMemoryCache.mu.RLock()
			fmt.Println(inMemoryCache.m)
			inMemoryCache.mu.RUnlock()
			wg.Done()
		}()
	}
	wg.Wait()

	fmt.Println(inMemoryCache.m)
}

func save(k string, v int, wg *sync.WaitGroup) {
	inMemoryCache.mu.Lock()
	inMemoryCache.m[k] = v
	inMemoryCache.mu.Unlock()
	wg.Done()
}

func saveSlow(k string, v int) {
	inMemoryCache.m[k] = v
}
