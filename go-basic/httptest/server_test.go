package main

import (
	"io/ioutil"
	"net/http"
	"net/http/httptest"
	"testing"
)

func TestUpperCaseHandler(t *testing.T) {
	req := httptest.NewRequest(http.MethodGet, "/upper?word=abc", nil)
	w := httptest.NewRecorder()
	upperCaseHandler(w, req)
	res := w.Result()
	defer res.Body.Close()
	data, err := ioutil.ReadAll(res.Body)
	if err != nil {
		t.Errorf("expected error to be nil got %v", err)
	}
	if string(data) != "ABC" {
		t.Errorf("expected ABC got %v", string(data))
	}
}
