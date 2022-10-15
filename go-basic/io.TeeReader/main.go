package main

import (
	"compress/gzip"
	"fmt"
	"io"
	"io/ioutil"
	"net/http"
	"os"
)

// http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-5gram-20120701-0.gz

// r: download the file
// w: progress counter: measure in real time the number of mb downloaded
// w: write the file into our local filesystem
// w: write the file into our archive

type counter struct {
	total uint64
}

// Write
func (c *counter) Write(b []byte) (int, error) {
	c.total += uint64(len(b)) // 32kb at a time
	progress := float64(c.total) / (1024 * 1024)
	fmt.Printf("\rDownloading %f MB...", progress)
	return len(b), nil
}

// r1: <filefrom the internet>
// w1: <progress counter>
// r2 := TeeReader(r1, w1)
// r2.Read()
//
//    -- TeeReader
//       r1.Read(b)
//       w1.Write(b
//	return
func main() {
	res, err := http.Get("http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-5gram-20120701-0.gz")
	if err != nil {
		panic(err)
	}
	// download the file into our local fs
	local, err := os.OpenFile("download-5gram.txt", os.O_CREATE|os.O_WRONLY, 0600)
	if err != nil {
		panic(err)
	}
	defer local.Close()
	dec, err := gzip.NewReader(res.Body)
	if err != nil {
		panic(err)
	}
	// copy res.Body into local
	if _, err := io.Copy(ioutil.Discard, io.TeeReader(dec, &counter{})); err != nil {
		panic(err)
	}
}
