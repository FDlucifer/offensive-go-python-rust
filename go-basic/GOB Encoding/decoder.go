package main

import (
	"encoding/gob"
	"log"
	"os"
	"time"
)

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
	f, err := os.Open("user.gob")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()
	var users []Identifiable
	gob.Register(User{})
	dec := gob.NewDecoder(f)
	if err := dec.Decode(&users); err != nil {
		log.Fatal(err)
	}
	for _, u := range users {
		log.Println(u)
	}
}
