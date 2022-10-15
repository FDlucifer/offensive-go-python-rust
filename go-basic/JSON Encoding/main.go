package main

import (
	"encoding/json"
	"fmt"
	"time"
)

type City struct {
	Name       string `json:"city_name"`
	GDP        int    `json:"-"`
	Population int    `json:"city_pop"`
}

type User struct {
	Name      string     `json:"name"`
	Age       int        `json:"age"`
	City      City       `json:"city"`
	CreatedAt time.Time  `json:"created_at"`
	DeletedAt *time.Time `json:"deleted_at"`
}

func main() {
	t := time.Now()
	u := User{
		Name: "bob",
		Age:  20,
		City: City{
			Name:       "london",
			GDP:        500,
			Population: 8000000},
		CreatedAt: time.Now(),
		DeletedAt: &t,
	}
	out, err := json.Marshal(u)
	if err != nil {
		panic(err)
	}
	fmt.Println(string(out))
}
