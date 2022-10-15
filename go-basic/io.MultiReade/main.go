package main

import (
	"encoding/csv"
	"fmt"
	"io"
	"log"
	"os"
)

func main() {
	italy, err := os.Open("italy.csv")
	if err != nil {
		log.Fatal(err)
	}
	defer italy.Close()
	spain, err := os.Open("spain.csv")
	if err != nil {
		log.Fatal(err)
	}
	defer spain.Close()
	france, err := os.Open("france.csv")
	if err != nil {
		log.Fatal(err)
	}
	defer france.Close()

	// create a multi reader from 3 io.Reader
	cities := io.MultiReader(italy, spain, france)
	if err := parseCities(cities, os.Stdout); err != nil {
		log.Fatal(err)
	}
}

func parseCities(r io.Reader, w io.Writer) error {
	reader := csv.NewReader(r)
	for {
		line, err := reader.Read()
		if err == io.EOF {
			return nil
		}
		if err != nil {
			return err
		}
		w.Write([]byte(fmt.Sprintf("%s - %s\n", line[0], line[9])))
	}
	return nil
}
