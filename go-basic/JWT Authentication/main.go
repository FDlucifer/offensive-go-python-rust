package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"regexp"
	"sync"
	"time"

	jwt "github.com/dgrijalva/jwt-go"
)

// JWT: <header>.<payload>.<signature> (base64 URL encoded)
// Eg.  eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c

// Header (decoded)
// {
//  "alg": "HS256",
//  "typ": "JWT"
// }

// Payload (decoded)
// {
//  "sub": "1234567890",
//  "name": "Bob",
//  "iat": 1516239022,
//  "nbf": 1517000000,
//  "exp": 1600000000
// }

var (
	listUserRe   = regexp.MustCompile(`^\/users[\/]*$`)
	getUserRe    = regexp.MustCompile(`^\/users\/(\d+)$`)
	createUserRe = regexp.MustCompile(`^\/users[\/]*$`)

	headerTokenRe = regexp.MustCompile(`^Bearer\s([a-zA-Z0-9\.\-_]+)$`)
)

type user struct {
	ID   string `json:"id"`
	Name string `json:"name"`
}

type datastore struct {
	m map[string]user
	*sync.RWMutex
}

type userHandler struct {
	key   []byte
	store *datastore
}

func (h *userHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("content-type", "application/json")
	switch {
	case r.Method == http.MethodGet && listUserRe.MatchString(r.URL.Path):
		h.List(w, r)
		return
	case r.Method == http.MethodGet && getUserRe.MatchString(r.URL.Path):
		h.Get(w, r)
		return
	case r.Method == http.MethodPost && createUserRe.MatchString(r.URL.Path):
		h.Create(w, r)
		return
	default:
		notFound(w, r)
		return
	}
}

func (h *userHandler) List(w http.ResponseWriter, r *http.Request) {
	h.store.RLock()
	users := make([]user, 0, len(h.store.m))
	for _, v := range h.store.m {
		users = append(users, v)
	}
	h.store.RUnlock()
	jsonBytes, err := json.Marshal(users)
	if err != nil {
		internalServerError(w, r)
		return
	}
	w.WriteHeader(http.StatusOK)
	w.Write(jsonBytes)
}

func (h *userHandler) Get(w http.ResponseWriter, r *http.Request) {
	matches := getUserRe.FindStringSubmatch(r.URL.Path)
	if len(matches) < 2 {
		notFound(w, r)
		return
	}
	h.store.RLock()
	u, ok := h.store.m[matches[1]]
	h.store.RUnlock()
	if !ok {
		w.WriteHeader(http.StatusNotFound)
		w.Write([]byte("user not found"))
		return
	}
	jsonBytes, err := json.Marshal(u)
	if err != nil {
		internalServerError(w, r)
		return
	}
	w.WriteHeader(http.StatusOK)
	w.Write(jsonBytes)
}

func (h *userHandler) Create(w http.ResponseWriter, r *http.Request) {
	if !authorizer(h.key)(w, r) {
		unauthorized(w, r)
		return
	}
	var u user
	if err := json.NewDecoder(r.Body).Decode(&u); err != nil {
		internalServerError(w, r)
		return
	}
	h.store.Lock()
	h.store.m[u.ID] = u
	h.store.Unlock()
	jsonBytes, err := json.Marshal(u)
	if err != nil {
		internalServerError(w, r)
		return
	}
	w.WriteHeader(http.StatusOK)
	w.Write(jsonBytes)
}

func internalServerError(w http.ResponseWriter, r *http.Request) {
	w.WriteHeader(http.StatusInternalServerError)
	w.Write([]byte("internal server error"))
}

func notFound(w http.ResponseWriter, r *http.Request) {
	w.WriteHeader(http.StatusNotFound)
	w.Write([]byte("not found"))
}

func unauthorized(w http.ResponseWriter, r *http.Request) {
	w.WriteHeader(http.StatusUnauthorized)
	w.Write([]byte("unauthorized"))
}

type authHandler struct {
	key []byte
}

func (h *authHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("content-type", "application/json")
	switch {
	case r.Method == http.MethodPost:
		h.Token(w, r)
		return
	default:
		notFound(w, r)
		return
	}
}

type CustomClaims struct {
	Username string
	jwt.StandardClaims
}

func (h *authHandler) Token(w http.ResponseWriter, r *http.Request) {
	// check user credentials
	// issue a token
	req := struct {
		User, Pwd string
	}{}
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		internalServerError(w, r)
		return
	}
	if !checkCredentials(req.User, req.Pwd) {
		unauthorized(w, r)
		return
	}
	token := jwt.NewWithClaims(jwt.SigningMethodHS256, CustomClaims{
		Username: req.User,
		StandardClaims: jwt.StandardClaims{
			ExpiresAt: time.Now().AddDate(0, 0, 1).Unix(),
			Issuer:    "https://golang.cafe",
		},
	})
	tkn, err := token.SignedString(h.key)
	if err != nil {
		unauthorized(w, r)
		return
	}
	jsonBytes, err := json.Marshal(struct{ JWT string }{JWT: tkn})
	if err != nil {
		unauthorized(w, r)
		return
	}
	w.WriteHeader(http.StatusOK)
	w.Write(jsonBytes)
}

func authorizer(key []byte) func(w http.ResponseWriter, r *http.Request) bool {
	return func(w http.ResponseWriter, r *http.Request) bool {
		// Header
		// Authorization: Bearer <jwt-token>
		matches := headerTokenRe.FindStringSubmatch(r.Header.Get("Authorization"))
		if len(matches) < 2 {
			return false
		}
		token, err := jwt.ParseWithClaims(matches[1], &CustomClaims{}, func(t *jwt.Token) (interface{}, error) {
			// check if alg is hs256
			// if alg RSA
			// retrieve key from t
			return key, nil
		})
		if err != nil {
			return false
		}
		tkn, ok := token.Claims.(*CustomClaims)
		if !ok {
			return false
		}
		if err := tkn.Valid(); err != nil {
			return false
		}
		fmt.Printf("%+v", tkn)

		return true
	}
}

func checkCredentials(user, pwd string) bool {
	return user == "admin" && pwd == "secret"
}

var secretKey = []byte("029b937dab2b4e79e24757d5c316b785397b30b6938c71f7ff6d4e7665d0a046")

func main() {
	mux := http.NewServeMux()
	userH := &userHandler{
		store: &datastore{
			m: map[string]user{
				"1": user{ID: "1", Name: "bob"},
			},
			RWMutex: &sync.RWMutex{},
		},
		key: secretKey,
	}
	authH := &authHandler{key: secretKey}
	mux.Handle("/users", userH)
	mux.Handle("/users/", userH)
	mux.Handle("/auth", authH)

	http.ListenAndServe("localhost:8080", mux)
}
