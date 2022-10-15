package main

import (
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"net/http"
	"net/http/httptrace"
	"time"
)

func main() {
	req, err := http.NewRequest(http.MethodGet, "http://example.com", nil)
	if err != nil {
		log.Fatal(err)
	}
	t0 := time.Now()
	var getConn, dnsStart, dnsDone, gotConn, gotFirstResByte time.Time

	// Create Trace Info
	trace := &httptrace.ClientTrace{
		GetConn: func(hostPort string) {
			getConn = time.Now()
			fmt.Printf("GetConn(%s) %d ms\n", hostPort, getConn.Sub(t0).Milliseconds())
		},
		DNSStart: func(info httptrace.DNSStartInfo) {
			dnsStart = time.Now()
			fmt.Printf("DNSStart(%+v) %d ms\n", info, dnsStart.Sub(t0).Milliseconds())
		},
		DNSDone: func(info httptrace.DNSDoneInfo) {
			dnsDone = time.Now()
			fmt.Printf("DNSDone(%+v) %d ms\n", info, dnsDone.Sub(t0).Milliseconds())
		},
		ConnectStart: func(network, addr string) {
			fmt.Printf("ConnectStart(%s, %s)\n", network, addr)
		},
		ConnectDone: func(network, addr string, err error) {
			fmt.Printf("ConnectDone(%s, %s, %v)\n", network, addr, err)
		},
		GotConn: func(info httptrace.GotConnInfo) {
			gotConn = time.Now()
			fmt.Printf("GotConn(%+v) %d ms\n", info, gotConn.Sub(t0).Milliseconds())
		},
		GotFirstResponseByte: func() {
			gotFirstResByte = time.Now()
			fmt.Printf("GotFirstResponseByte %d ms\n", gotFirstResByte.Sub(t0).Milliseconds())
		},
		PutIdleConn: func(err error) {
			fmt.Printf("PutIdleConn(%+v)\n", err)
		},
	}

	// Create Trace context
	ctx := httptrace.WithClientTrace(req.Context(), trace)

	// Attach Trace context to request
	req = req.WithContext(ctx)

	fmt.Println("# Request to example.com")
	fmt.Println("")

	// HTTP Request/Response - Trace Events
	//  DNS Request - DNSStart
	//  DNS Response - DNSDone
	//  TCP Create Connection - ConnectStart/ConnectDone
	//  Write to the TCP connection - WroteHeaders/WroteRequest
	//  Read from TCP Connection - GotFirstResponseByte
	//  Close TCP Connection

	// HTTP Persitent Connections
	//
	// HTTP Request/Response - Trace Events
	//  If TCP Connection already exists use it
	//  Write to the TCP connection - WroteHeaders/WroteRequest
	//  Read from TCP Connection - GotFirstResponseByte
	//  Keep Connection alive for later use - PutIdleConn

	t0 = time.Now()
	res, err := http.DefaultClient.Do(req)
	if err != nil {
		log.Fatal(err)
	}

	// read the whole body and close so that the underlying TCP conn is re-used
	io.Copy(ioutil.Discard, res.Body)
	res.Body.Close()

	fmt.Println("")
	fmt.Println("# Request to example.com")
	fmt.Println("")

	t0 = time.Now()
	_, err = http.DefaultClient.Do(req)
	if err != nil {
		log.Fatal(err)
	}
}
