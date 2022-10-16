package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/BHG", func(rw http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(rw, "greeting from %s\n", r.URL.Query().Get("name"))
	})
	http.ListenAndServe(":8000", nil)
}
