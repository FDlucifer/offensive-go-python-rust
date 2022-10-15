package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"

	"golang.cafe/protobuf/model"

	"github.com/golang/protobuf/proto"
)

// Protocol Buffers Doc
//
// https://developers.google.com/protocol-buffers/docs/proto3
//
// SETUP protoc compiler
//
// export GO111MODULE=on
// go get google.golang.org/protobuf/cmd/protoc-gen-go
// export PATH="$PATH:$(go env GOPATH)/bin"

func main() {
	book := &model.Book{
		Id:    1,
		Title: "the road to wigan pier",
		Authors: []*model.Author{
			{Id: 1, Name: "oscar wilde"},
		},
		Category: model.Category_Novel,
	}
	data, err := proto.Marshal(book)
	if err != nil {
		log.Fatal(err)
	}
	ioutil.WriteFile("book.protobuf", data, 0600)
	data, err = json.Marshal(book)
	if err != nil {
		log.Fatal(err)
	}
	ioutil.WriteFile("book.json", data, 0600)

	// decode the data from protobuf bytes
	data, err = ioutil.ReadFile("book.protobuf")
	if err != nil {
		log.Fatal(err)
	}
	bookFromFile := model.Book{}
	if err := proto.Unmarshal(data, &bookFromFile); err != nil {
		log.Fatal(err)
	}
	fmt.Printf("book from protobuf file %+v\n", bookFromFile)
}
