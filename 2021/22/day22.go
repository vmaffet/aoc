package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

type Zone struct {
	state                  bool
	x0, x1, y0, y1, z0, z1 int
}

type Point struct {
	x, y, z int
}

func main() {
	file, _ := os.Open("input.txt")
	defer file.Close()

	re := regexp.MustCompile(`(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)`)
	steps := []Zone{}

	scanner := bufio.NewScanner(file)
	for i := 0; scanner.Scan(); i++ {
		match := re.FindStringSubmatch(scanner.Text())
		state := match[1] == "on"
		x0, _ := strconv.Atoi(match[2])
		x1, _ := strconv.Atoi(match[3])
		y0, _ := strconv.Atoi(match[4])
		y1, _ := strconv.Atoi(match[5])
		z0, _ := strconv.Atoi(match[6])
		z1, _ := strconv.Atoi(match[7])
		steps = append(steps, Zone{state, x0, x1, y0, y1, z0, z1})
	}

	fmt.Println(part1(steps))
	fmt.Println(part2(steps))
}

func part1(steps []Zone) int {
	cuboids := map[Point]bool{}
	for _, s := range steps {
		x0, x1 := max(s.x0, -50), min(s.x1, 50)
		y0, y1 := max(s.y0, -50), min(s.y1, 50)
		z0, z1 := max(s.z0, -50), min(s.z1, 50)
		for x := x0; x <= x1; x++ {
			for y := y0; y <= y1; y++ {
				for z := z0; z <= z1; z++ {
					p := Point{x, y, z}
					if s.state {
						cuboids[p] = true
					} else {
						delete(cuboids, p)
					}
				}
			}
		}
	}

	return len(cuboids)
}

func part2(steps []Zone) int {
	grid := []Zone{}
	for _, s := range steps {
		for _, z := range grid {
			if ok, i := intersects(s, z); ok {
				grid = append(grid, i)
			}
		}
		if s.state {
			grid = append(grid, s)
		}
	}
	n := 0
	for _, z := range grid {
		if z.state {
			n += size(z)
		} else {
			n -= size(z)
		}
	}
	return n
}

func size(a Zone) int {
	return (a.x1 - a.x0 + 1) * (a.y1 - a.y0 + 1) * (a.z1 - a.z0 + 1)
}

func intersects(a, b Zone) (bool, Zone) {
	xok := a.x0 <= b.x1 && b.x0 <= a.x1
	yok := a.y0 <= b.y1 && b.y0 <= a.y1
	zok := a.z0 <= b.z1 && b.z0 <= a.z1
	if xok && yok && zok {
		state := !b.state
		x0, x1 := max(a.x0, b.x0), min(a.x1, b.x1)
		y0, y1 := max(a.y0, b.y0), min(a.y1, b.y1)
		z0, z1 := max(a.z0, b.z0), min(a.z1, b.z1)
		return true, Zone{state, x0, x1, y0, y1, z0, z1}
	}
	return false, Zone{}
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
