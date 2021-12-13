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

	heightmap := map[point]int{}

	scanner := bufio.NewScanner(file)
	for i := 0; scanner.Scan(); i++ {
		for j, r := range scanner.Text() {
			heightmap[point{j, i}] = int(r - '0')
		}
	}

	fmt.Println(task1(heightmap))
	fmt.Println(task2(heightmap))
}

func task1(heights map[point]int) int {
	cnt := 0
	for p, h := range heights {
		u, su := heights[point{p.x, p.y - 1}]
		d, sd := heights[point{p.x, p.y + 1}]
		l, sl := heights[point{p.x - 1, p.y}]
		r, sr := heights[point{p.x + 1, p.y}]
		if (!su || u > h) && (!sd || d > h) && (!sl || l > h) && (!sr || r > h) {
			cnt += h + 1
		}
	}
	return cnt
}

func task2(heights map[point]int) int {
	A, B, C := 0, 0, 0

	bassin := map[point]bool{}
	for p, h := range heights {
		if h != 9 && !bassin[p] {
			size := fill(bassin, heights, p)
			switch {
			case size > A:
				A, B, C = size, A, B
			case size > B:
				B, C = size, B
			case size > C:
				C = size
			}
		}
	}

	return A * B * C
}

func fill(id map[point]bool, arr map[point]int, start point) int {
	cnt := 0

	id[start] = true
	tovisit := []point{start}
	for last := 0; last >= 0; last = len(tovisit) - 1 {
		cur := tovisit[last]
		tovisit = tovisit[:last]

		up := point{cur.x, cur.y - 1}
		down := point{cur.x, cur.y + 1}
		left := point{cur.x - 1, cur.y}
		right := point{cur.x + 1, cur.y}
		for _, p := range [4]point{up, down, left, right} {
			if val, ok := arr[p]; ok && (val != 9 && !id[p]) {
				id[p] = true
				tovisit = append(tovisit, p)
			}
		}

		cnt++
	}

	return cnt
}
