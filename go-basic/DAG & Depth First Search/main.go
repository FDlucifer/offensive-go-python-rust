package main

import (
	"bytes"
	"io/ioutil"
	"log"
	"regexp"
	"strings"
)

type bag struct {
	name     string
	children []*bag
	parents  []*bag
}

func main() {
	c, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	bags := make(map[string]*bag)
	// parse the input into graph structure
	for _, line := range bytes.Split(c, []byte("\n")) {
		if len(line) == 0 {
			continue
		}
		parts := strings.Split(string(line), " bags contain ")
		parent := &bag{name: parts[0]}
		for _, child := range strings.Split(parts[1], ",") {
			childRe := regexp.MustCompile("(\\d+)\\s([a-z\\s]+)\\sbag[s]*[\\.]*")
			matches := childRe.FindStringSubmatch(child)
			if len(matches) < 3 {
				continue
			}
			childBag := &bag{name: matches[2]}
			parent.children = append(parent.children, childBag)
		}
		bags[parent.name] = parent
	}
	// add the parents to the nodes
	for k, _ := range bags {
		for idx, _ := range bags[k].children {
			child, ok := bags[bags[k].children[idx].name]
			if !ok {
				log.Println("not found")
				continue
			}
			child.parents = append(child.parents, bags[k])
			bags[k].children[idx] = child
		}
	}

	// dfs
	start := bags["shiny gold"]
	next := []*bag{start}
	visited := make(map[string]struct{})
	for len(next) > 0 {
		n := next[0]
		next = next[1:]
		for _, v := range n.parents {
			next = append(next, v)
		}
		visited[n.name] = struct{}{}
	}
	log.Println(len(visited) - 1)
}
