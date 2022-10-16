package main

import (
	"archive/zip"
	"fmt"
	"io"
	"os"
)

func main() {
	fmt.Println("creating zip archive...")
	archive, err := os.Create("archive.zip")
	if err != nil {
		panic(err)
	}
	defer archive.Close()

	zipWriter := zip.NewWriter(archive)

	fmt.Println("opening first file...")
	f1, err := os.Open("test.csv")
	if err != nil {
		panic(err)
	}
	defer f1.Close()

	fmt.Println("adding file to archive..")
	// create entry in the zip archive
	w1, err := zipWriter.Create("csv/test.csv")
	if err != nil {
		panic(err)
	}
	// copy uncompressed file to archive
	if _, err := io.Copy(w1, f1); err != nil {
		panic(err)
	}

	fmt.Println("open second file...")
	f2, err := os.Open("test.txt")
	if err != nil {
		panic(err)
	}
	defer f2.Close()

	fmt.Println("adding second file to archive...")
	// create entry in the zip archive
	w2, err := zipWriter.Create("txt/test.txt")
	if err != nil {
		panic(err)
	}
	// copy uncompressed file to archive
	if _, err := io.Copy(w2, f2); err != nil {
		panic(err)
	}

	fmt.Println("closing archive...")
	zipWriter.Close()

}
