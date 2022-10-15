package main

import (
	"fmt"
	"io"
	"io/ioutil"
	"net/http"
	"os"
	"time"
)

// - logging
// - retrying
// - auth
// - caching
// - headers manipulation
// - testing

func main() {
	c := &http.Client{
		Transport: &authRoundTripper{
			next: &retryRoundTripper{
				next: &loggingRoundTripper{
					next:   http.DefaultTransport,
					logger: os.Stdout,
				},
				maxRetries: 3,
				delay:      time.Duration(1 * time.Second),
			},
			user: "bob",
			pwd:  "pwd",
		},
	}
	req, err := http.NewRequest(http.MethodGet, "http://httpbin.org/basic-auth/bob/pwd", nil)
	if err != nil {
		panic(err)
	}
	res, err := c.Do(req)
	if err != nil {
		panic(err)
	}
	body, err := ioutil.ReadAll(res.Body)
	if err != nil {
		panic(err)
	}
	defer res.Body.Close()
	fmt.Println("\n--- RESPONSE ---\n")
	fmt.Println("STATUS CODE: ", res.StatusCode)
	fmt.Println("BODY: ", string(body))

	req, err = http.NewRequest(http.MethodGet, "http://httpbin.org/status/500", nil)
	if err != nil {
		panic(err)
	}
	res, err = c.Do(req)
	if err != nil {
		panic(err)
	}
	body, err = ioutil.ReadAll(res.Body)
	if err != nil {
		panic(err)
	}
	defer res.Body.Close()
	fmt.Println("\n--- RESPONSE ---\n")
	fmt.Println("STATUS CODE: ", res.StatusCode)
	fmt.Println("BODY: ", string(body))
}

type authRoundTripper struct {
	next      http.RoundTripper
	user, pwd string
}

func (a authRoundTripper) RoundTrip(r *http.Request) (*http.Response, error) {
	r.SetBasicAuth(a.user, a.pwd)
	return a.next.RoundTrip(r)
}

type retryRoundTripper struct {
	next       http.RoundTripper
	maxRetries int
	delay      time.Duration // delay between each retry
}

func (rr retryRoundTripper) RoundTrip(r *http.Request) (*http.Response, error) {
	var attempts int
	for {
		res, err := rr.next.RoundTrip(r)
		attempts++

		// max retries exceeded
		if attempts == rr.maxRetries {
			return res, err
		}

		// good outcome
		if err == nil && res.StatusCode < http.StatusInternalServerError {
			return res, err
		}

		// delay and retry
		select {
		case <-r.Context().Done():
			return res, r.Context().Err()
		case <-time.After(rr.delay):
		}
	}
}

type loggingRoundTripper struct {
	next   http.RoundTripper
	logger io.Writer
}

// RoundTrip is a decorator on top of the default roundtripper
func (l loggingRoundTripper) RoundTrip(r *http.Request) (*http.Response, error) {
	// here we can log our message and info
	fmt.Fprintf(l.logger, "[%s] %s %s\n", time.Now().Format(time.ANSIC), r.Method, r.URL.String())
	return l.next.RoundTrip(r)
}
