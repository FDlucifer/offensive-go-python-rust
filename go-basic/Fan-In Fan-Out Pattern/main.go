package main

import (
	"encoding/csv"
	"io"
	"log"
	"os"
	"strconv"
	"strings"
	"sync"
)

type City struct {
	Name       string
	Population int
}

func main() {
	f, err := os.Open("cities.csv")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	rows := genRows(f)
	filterSmallCity := filterByMinPopulation(40000)

	// fan out pattern
	// more than one worker competing to consume the same channel

	//       __ worker1
	// rows /__ worker2
	//      \__ worker3
	//       __ workern...
	ur1 := upperCityName(filterSmallCity(rows))
	ur2 := upperCityName(filterSmallCity(rows))
	ur3 := upperCityName(filterSmallCity(rows))

	// fan in pattern consolidates the outputs from multiple channels into one
	//
	// worker1 ___
	// worker2 ___\ output
	// worker3 ___/

	for c := range fanIn(ur1, ur2, ur3) {
		log.Println(c)
	}
}

func upperCityName(cities <-chan City) <-chan City {
	out := make(chan City)
	go func() {
		for c := range cities {
			out <- City{Name: strings.ToUpper(c.Name), Population: c.Population}
		}
		close(out)
	}()
	return out
}

func filterByMinPopulation(min int) func(<-chan City) <-chan City {
	return func(cities <-chan City) <-chan City {
		out := make(chan City)
		go func() {
			for c := range cities {
				if c.Population > min {
					out <- City{Name: c.Name, Population: c.Population}
				}
			}
			close(out)
		}()
		return out
	}
}

func genRows(r io.Reader) chan City {
	out := make(chan City)
	go func() {
		reader := csv.NewReader(r)
		_, err := reader.Read()
		if err != nil {
			log.Fatal(err)
		}
		for {
			row, err := reader.Read()
			if err == io.EOF {
				break
			}
			if err != nil {
				log.Fatal(err)
			}
			populationInt, err := strconv.Atoi(row[9])
			if err != nil {
				continue
			}
			out <- City{
				Name:       row[1],
				Population: populationInt,
			}
		}
		close(out)
	}()
	return out
}

func fanIn(chans ...<-chan City) <-chan City {
	out := make(chan City)
	wg := &sync.WaitGroup{}
	wg.Add(len(chans))
	for _, c := range chans {
		go func(city <-chan City) {
			for r := range city {
				out <- r
			}
			wg.Done()
		}(c)
	}
	go func() {
		wg.Wait()
		close(out)
	}()
	return out
}
