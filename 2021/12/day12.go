package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
)

func main() {
	file, _ := os.Open("input.txt")
	defer file.Close()

	caves := map[string][]string{}
	re := regexp.MustCompile(`(\w+)-(\w+)`)

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		conn := re.FindStringSubmatch(scanner.Text())
		node1, node2 := conn[1], conn[2]

		if node2 != "start" && node1 != "end" {
			caves[node1] = append(caves[node1], node2)
		}
		if node1 != "start" && node2 != "end" {
			caves[node2] = append(caves[node2], node1)
		}
	}

	fmt.Println(task1(caves))
	fmt.Println(task2(caves))
}

func task1(net map[string][]string) int {
	return explore(net, "start", map[string]int{}, false)
}

func task2(net map[string][]string) int {
	return explore(net, "start", map[string]int{}, true)
}

func explore(graph map[string][]string, node string, hit map[string]int, doublable bool) int {
	routes := 0
	for _, neigh := range graph[node] {
		if neigh == "end" {
			routes++
		} else if IsBig(neigh) || hit[neigh] < 1 {
			hit[neigh]++
			routes += explore(graph, neigh, hit, doublable)
			hit[neigh]--
		} else if doublable {
			doublable = false
			routes += explore(graph, neigh, hit, doublable)
			doublable = true
		}
	}
	return routes
}

func IsBig(s string) bool {
	return 'A' <= s[0] && s[0] <= 'Z'
}
