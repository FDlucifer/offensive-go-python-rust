package main

import "fmt"

// we want to build a custom in memory database
// we are trying to aggregate weather data

// {"date" : "2020-01-01", "sensor_type": "temp", "value": 20.12}
// {"date" : "2020-01-02", "sensor_type": "temp", "value": 20.12}
// {"date" : "2020-01-02", "sensor_type": "hum", "value": 20.12}
// {"date" : "2020-01-02", "sensor_type": "hum", "value": 20.12}

type AggregationKey struct {
	Date, SensorType string
}

func main() {
	// map[KeyType]ValueType
	// func, slice, map
	m := make(map[string][]string)

	// add Key, Value
	m["fruits"] = []string{"apple", "pear", "peach", "cherry"}
	m["vegs"] = []string{"celery", "cucumber"}

	fmt.Println(m)

	// get Key
	fruits := m["fruits"]
	fmt.Println("got fruits from map: ", fruits)

	// delete Key
	//delete(m, "fruits")
	//fmt.Println("map after delete: ", m)

	fmt.Println(len(m))

	for key, value := range m {
		fmt.Println("key: ", key, "value: ", value)
	}

	weatherData := map[AggregationKey]float64{}

	weatherData[AggregationKey{Date: "2020-01-01", SensorType: "Temperature"}] = 20.01
	weatherData[AggregationKey{Date: "2020-01-01", SensorType: "Humidity"}] = 0.65

	fmt.Println(weatherData)
}
