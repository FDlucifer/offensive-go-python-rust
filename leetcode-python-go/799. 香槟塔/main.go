package main

import (
	"fmt"
	"math"
)

func champagneTower(poured, queryRow, queryGlass int) float64 {
	row := []float64{float64(poured)}
	for i := 1; i <= queryRow; i++ {
		nextRow := make([]float64, i+1)
		for j, volume := range row {
			if volume > 1 {
				nextRow[j] += (volume - 1) / 2
				nextRow[j+1] += (volume - 1) / 2
			}
		}
		row = nextRow
	}
	return math.Min(1, row[queryGlass])
}

func main() {
	poured := 2
	query_glass := 1
	query_row := 1
	results := champagneTower(poured, query_glass, query_row)
	fmt.Println(results)
}
