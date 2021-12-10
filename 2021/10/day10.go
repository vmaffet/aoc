package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	file, _ := os.Open("input.txt")
	defer file.Close()

	nav := []string{}

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		nav = append(nav, scanner.Text())
	}

	fmt.Println(task1(nav))
	fmt.Println(task2(nav))
}

func task1(nav []string) int {
	pts := map[rune]int{')': 3, ']': 57, '}': 1197, '>': 25137}

	cnt := 0
	for _, line := range nav {
		ill, _ := check(line)
		if p, ok := pts[ill]; ok {
			cnt += p
		}
	}
	return cnt
}

func task2(nav []string) int {
	pts := map[rune]int{')': 1, ']': 2, '}': 3, '>': 4}

	scores := []int{}
	for _, line := range nav {
		_, mis := check(line)
		if n := len(mis); n > 0 {
			scr := 0
			for i := n - 1; i >= 0; i-- {
				scr = scr*5 + pts[mis[i]]
			}
			scores = append(scores, scr)
		}
	}
	sort.Ints(scores)
	return scores[len(scores)/2]
}

func check(line string) (rune, []rune) {
	dual := map[rune]rune{'(': ')', '[': ']', '{': '}', '<': '>'}

	next := []rune{}
	for _, c := range line {
		switch c {
		case '(', '[', '{', '<':
			next = append(next, dual[c])
		case ')', ']', '}', '>':
			if n := len(next); n > 0 && c == next[n-1] {
				next = next[:n-1]
			} else {
				return c, nil
			}
		}
	}
	return 0, next
}
