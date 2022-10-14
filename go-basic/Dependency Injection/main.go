package main

import (
	"bufio"
	"bytes"
	"fmt"
	"io"
	"os"
	"strings"
	"testing"

	"errors"
)

// Dependency injection involves four roles:

// - the service object(s) to be used - also known as "dependency"
// - the client object that is depending on the service(s) it uses
// - the interfaces that define how the client may use the services
// - the injector, which is responsible for constructing the services
//   and injecting them into the client

// As an analogy,

// service - an electric, gas, hybrid, or diesel car
// client - a driver who uses the car the same way regardless of the engine
// interface - automatic, ensures driver does not have to understand engine details like gears
// injector - the parent who bought the kid the car and decided which kind

var (
	errUsage = errors.New(`usage:
	set <key> <value>  Set specified key and value
	get <key>	   Get specified key`)
)

// main is the injector
func main() {
	runner := newRunner(newFileDatabase("database.txt"))
	if err := runner.run(os.Stdout, os.Args); err != nil {
		fmt.Println(err)
	}
}

// storage is the interface
type storage interface {
	Set(string, string) error
	Get(string) (string, error)
}

// runner is the client
type runner struct {
	database storage
}

func newRunner(db storage) runner {
	return runner{db}
}

func (r runner) run(output io.StringWriter, args []string) error {
	if len(args) < 3 {
		return errUsage
	}
	switch args[1] {
	case "set":
		if len(args) < 4 {
			return errUsage
		}
		if err := r.database.Set(args[2], args[3]); err != nil {
			return err
		}
	case "get":
		v, err := r.database.Get(args[2])
		if err != nil {
			return err
		}
		output.WriteString(v + "\n")
	default:
		return errUsage
	}

	return nil
}

// fileDatabase is the service
type fileDatabase struct {
	file string
}

func newFileDatabase(path string) fileDatabase {
	return fileDatabase{path}
}

func (db fileDatabase) Set(key, value string) error {
	f, err := os.OpenFile(db.file, os.O_WRONLY|os.O_CREATE|os.O_APPEND, 0600)
	if err != nil {
		return err
	}
	defer f.Close()
	if _, err := f.WriteString(fmt.Sprintf("%s:%s\n", key, value)); err != nil {
		return err
	}

	return nil
}

func (db fileDatabase) Get(key string) (string, error) {
	f, err := os.OpenFile(db.file, os.O_RDONLY, 0600)
	if err != nil {
		return "", err
	}
	defer f.Close()
	scanner := bufio.NewScanner(f)
	var last string
	for scanner.Scan() {
		row := scanner.Text()
		parts := strings.Split(row, ":")
		if len(parts) < 2 {
			return "", errors.New("invalid record")
		}
		if parts[0] == key {
			last = parts[1]
		}
	}

	if err := scanner.Err(); err != nil {
		return "", errors.New("scanner.Err")
	}

	if last != "" {
		return last, nil
	}

	return "", errors.New("not found")
}

type mockDatabase struct {
	setErr error

	getErr error
	getStr string
}

func (m mockDatabase) Get(string) (string, error) {
	return m.getStr, m.getErr
}

func (m mockDatabase) Set(string, string) error {
	return m.setErr
}

func TestRunnerArgsErr(t *testing.T) {
	r := newRunner(mockDatabase{})
	if err := r.run(&bytes.Buffer{}, []string{}); err == nil {
		t.Error("expected err on empty slice for args, got nil")
	}
}

func TestRunnerUsageErr(t *testing.T) {
	r := newRunner(mockDatabase{})
	if err := r.run(&bytes.Buffer{}, []string{"./kv", "help", "123"}); err == nil {
		t.Error("expected err on empty slice for args, got nil")
	}
}

func TestRunnerSetMisingArgErr(t *testing.T) {
	r := newRunner(mockDatabase{})
	if err := r.run(&bytes.Buffer{}, []string{"./kv", "set", "bob"}); err == nil {
		t.Error("expected err on empty slice for args, got nil")
	}
}

func TestRunnerReturnsErrOnSet(t *testing.T) {
	setErr := errors.New("set err")
	r := newRunner(mockDatabase{setErr: setErr})
	err := r.run(&bytes.Buffer{}, []string{"./kv", "set", "bob", "10"})
	if err == nil {
		t.Error("expected err on empty slice for args, got nil")
	}
	if err.Error() != setErr.Error() {
		t.Errorf("expected err to be %v got %v", setErr, err)
	}
}

func TestRunnerReturnsErrOnGet(t *testing.T) {
	getErr := errors.New("get err")
	r := newRunner(mockDatabase{getErr: getErr, getStr: "10"})
	err := r.run(&bytes.Buffer{}, []string{"./kv", "get", "bob"})
	if err == nil {
		t.Error("expected err on empty slice for args, got nil")
	}
	if err.Error() != getErr.Error() {
		t.Errorf("expected err to be %v got %v", getErr, err)
	}
}

func TestRunnerExpectedOutput(t *testing.T) {
	r := newRunner(mockDatabase{getStr: "10"})
	buf := &bytes.Buffer{}
	err := r.run(buf, []string{"./kv", "get", "bob"})
	if err != nil {
		t.Error("expected err to be nil on mock db get returning strings")
	}
	if buf.String() != "10\n" {
		t.Errorf("expected buffer to be 10 got %s", buf.String())
	}
}
