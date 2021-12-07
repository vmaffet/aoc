package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

type point struct {
	x, y int
}

func main() {
	file, _ := os.Open("input.txt")
	defer file.Close()

	lines := [][2]point{}
	re := regexp.MustCompile(`(\d+),(\d+) -> (\d+),(\d+)`)

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		coords := re.FindStringSubmatch(scanner.Text())

		x1, _ := strconv.Atoi(coords[1])
		y1, _ := strconv.Atoi(coords[2])
		x2, _ := strconv.Atoi(coords[3])
		y2, _ := strconv.Atoi(coords[4])
		lines = append(lines, [2]point{{x1, y1}, {x2, y2}})
	}

	fmt.Println(task1(lines))
	fmt.Println(task2(lines))
}

func task1(lines [][2]point) int {
	return overlap(lines, false)
}

func task2(lines [][2]point) int {
	return overlap(lines, true)
}

func overlap(lines [][2]point, diag bool) int {
	graph := map[point]int{}
	for _, line := range lines {
		from, to := line[0], line[1]
		if from.x == to.x || from.y == to.y || diag {
			for _, p := range draw(from, to) {
				graph[p]++
			}
		}
	}

	cnt := 0
	for _, c := range graph {
		if c > 1 {
			cnt++
		}
	}
	return cnt
}

func draw(start, end point) []point {
	line := []point{}
	dx, dy := dir(start.x, end.x), dir(start.y, end.y)
	for p := start; p != end; p.x, p.y = p.x+dx, p.y+dy {
		line = append(line, p)
	}
	line = append(line, end)
	return line
}

func minmax(a, b int) (int, int) {
	if a < b {
		return a, b
	} else {
		return b, a
	}
}

func dir(a, b int) int {
	switch {
	case a < b:
		return 1
	case a > b:
		return -1
	default:
		return 0
	}
}
