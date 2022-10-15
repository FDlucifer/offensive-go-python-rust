package main

import (
	"encoding/gob"
	"log"
	"os"
	"time"
)

// gob encoding
type User struct {
	Name      string
	Age       int
	CreatedAt time.Time
}

func (u User) ID() string {
	return u.Name
}

type Identifiable interface {
	ID() string
}

func main() {
	users := []Identifiable{
		User{Name: "bob", Age: 20, CreatedAt: time.Now()},
		User{Name: "joe", Age: 21, CreatedAt: time.Now()},
	}
	f, err := os.Create("user.gob")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()
	gob.Register(User{})
	enc := gob.NewEncoder(f)
	if err := enc.Encode(users); err != nil {
		log.Fatal(err)
	}
}
