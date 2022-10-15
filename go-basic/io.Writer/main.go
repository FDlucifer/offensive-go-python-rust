package main

import (
	"bytes"
	"encoding/json"
	"os"
)

type user struct {
	Name string `json:"name"`
	Age  int    `json:"age"`
}

func main() {
	f, err := os.OpenFile("file.txt", os.O_WRONLY|os.O_CREATE|os.O_TRUNC, 0600)
	if err != nil {
		panic(err)
	}
	defer f.Close()
	buf := new(bytes.Buffer)
	enc := json.NewEncoder(buf)
	u := user{Name: "bob", Age: 10}
	if err := enc.Encode(u); err != nil {
		panic(err)
	}
	f.Write(buf.Bytes())
}
