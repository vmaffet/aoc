package main

import (
	"bufio"
	"fmt"
	"os"
)

type point struct {
	x, y int
}

func main() {
	file, _ := os.Open("input.txt")
	defer file.Close()

	energy := map[point]int{}

	scanner := bufio.NewScanner(file)
	for i := 0; scanner.Scan(); i++ {
		for j, r := range scanner.Text() {
			energy[point{j, i}] = int(r - '0')
		}
	}

	fmt.Println(task1(copy(energy), 100))
	fmt.Println(task2(copy(energy)))
}

func task1(level map[point]int, steps int) int {
	cnt := 0
	for i := 0; i < steps; i++ {
		cnt += step(level)
	}
	return cnt
}

func task2(level map[point]int) int {
	i := 0
	for n := len(level); true; i++ {
		if step(level) == n {
			break
		}
	}
	return i + 1
}

func step(octopus map[point]int) int {
	for p, e := range octopus {
		octopus[p]++
		if e == 9 {
			flash(octopus, p)
		}
	}

	cnt := 0
	for p, e := range octopus {
		if e > 9 {
			octopus[p] = 0
			cnt++
		}
	}
	return cnt
}

func flash(lvl map[point]int, cur point) {
	n := point{cur.x, cur.y - 1}
	e := point{cur.x + 1, cur.y}
	s := point{cur.x, cur.y + 1}
	w := point{cur.x - 1, cur.y}
	ne := point{cur.x + 1, cur.y - 1}
	se := point{cur.x + 1, cur.y + 1}
	sw := point{cur.x - 1, cur.y + 1}
	nw := point{cur.x - 1, cur.y - 1}
	for _, p := range [8]point{n, ne, e, se, s, sw, w, nw} {
		if val, ok := lvl[p]; ok {
			lvl[p]++
			if val == 9 {
				flash(lvl, p)
			}
		}
	}
}

func copy(src map[point]int) map[point]int {
	dst := map[point]int{}
	for k, v := range src {
		dst[k] = v
	}
	return dst
}
