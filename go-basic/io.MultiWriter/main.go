package main

import (
	"encoding/json"
	"io"
	"log"
	"os"
)

type Company struct {
	Name string
	ID   int
}

func main() {
	companies := []Company{
		{Name: "apple", ID: 1},
		{Name: "google", ID: 2},
		{Name: "microsoft", ID: 3},
		{Name: "golang cafe", ID: 4},
	}
	// data coming in

	// save data into a file
	f, err := os.Create("companies.json")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()
	// save data into a backup
	fb, err := os.Create("companies.backup")
	if err != nil {
		log.Fatal(err)
	}
	defer fb.Close()
	// write data to stdout as well
	w := io.MultiWriter(f, fb, os.Stdout)
	enc := json.NewEncoder(w)
	for _, c := range companies {
		if err := enc.Encode(c); err != nil {
			log.Fatal(err)
		}
	}
}
