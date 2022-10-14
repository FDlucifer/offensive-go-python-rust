package main

import (
	"bufio"
	"encoding/csv"
	"encoding/json"
	"fmt"
	"io"
	"log"
	"os"
	"strconv"
)

type City struct {
	Name       string `json:"city_name"`
	Lat, Long  float64
	Country    string
	Population int
}

const (
	name int = iota
	nameAscii
	lat
	lon
	country
	iso2
	iso3
	adminName
	capital
	population
	id
)

func main() {
	f, err := os.Open("cities.csv")
	if err != nil {
		log.Fatal(err)
	}
	reader := csv.NewReader(bufio.NewReader(f))
	// discard the header
	_, err = reader.Read()
	if err != nil {
		log.Fatal(err)
	}
	rowNo := 0
	for {
		rowNo++
		row, err := reader.Read()
		if err == io.EOF {
			break
		}
		if err != nil {
			log.Fatal(err)
		}
		pop, err := strconv.Atoi(row[population])
		if err != nil {
			fmt.Fprintf(os.Stderr, "%d:%d strconv.Atoi(%s): %+v\n", rowNo, population, row[population], err)
			continue
		}
		latFloat, err := strconv.ParseFloat(row[lat], 64)
		if err != nil {
			fmt.Fprintf(os.Stderr, "%d:%d strconv.ParseFloat(%s): %+v\n", rowNo, lat, row[lat], err)
			continue
		}
		lonFloat, err := strconv.ParseFloat(row[lon], 64)
		if err != nil {
			fmt.Fprintf(os.Stderr, "%d:%d strconv.ParseFloat(%s): %+v\n", rowNo, lon, row[lon], err)
			continue
		}
		jsonB, err := json.Marshal(City{
			Name:       row[nameAscii],
			Population: pop,
			Country:    row[country],
			Lat:        latFloat,
			Long:       lonFloat,
		})
		if err != nil {
			log.Fatal(err)
		}
		fmt.Fprintf(os.Stdout, "%s\n", jsonB)
	}
}
