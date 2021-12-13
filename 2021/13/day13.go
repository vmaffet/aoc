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

type inst struct {
	axis  string
	coord int
}

func main() {
	file, _ := os.Open("input.txt")
	defer file.Close()
	scanner := bufio.NewScanner(file)

	paper := map[point]bool{}
	re := regexp.MustCompile(`(\d+),(\d+)`)
	for scanner.Scan() {
		pos := re.FindStringSubmatch(scanner.Text())

		if len(pos) == 3 {
			x, _ := strconv.Atoi(pos[1])
			y, _ := strconv.Atoi(pos[2])
			paper[point{x, y}] = true
		} else {
			break
		}
	}

	folds := []inst{}
	re = regexp.MustCompile(`fold along ([xy])=(\d+)`)
	for scanner.Scan() {
		cmd := re.FindStringSubmatch(scanner.Text())

		a := cmd[1]
		c, _ := strconv.Atoi(cmd[2])
		folds = append(folds, inst{a, c})
	}

	fold(paper, folds[:1])
	fmt.Println(len(paper))

	fold(paper, folds[1:])
	fmt.Print(disp(paper))
}

func fold(dots map[point]bool, rules []inst) {
	for _, i := range rules {
		for p := range dots {
			switch i.axis {
			case "x":
				if dlt := p.x - i.coord; dlt > 0 {
					delete(dots, p)
					dots[point{p.x - 2*dlt, p.y}] = true
				}
			case "y":
				if dlt := p.y - i.coord; dlt > 0 {
					delete(dots, p)
					dots[point{p.x, p.y - 2*dlt}] = true
				}
			}
		}
	}
}

func disp(locs map[point]bool) string {
	max := point{0, 0}
	for p := range locs {
		if p.x > max.x {
			max.x = p.x
		}
		if p.y > max.y {
			max.y = p.y
		}
	}

	out := ""
	for y := 0; y <= max.y; y++ {
		for x := 0; x <= max.x; x++ {
			if locs[point{x, y}] {
				out += "█"
			} else {
				out += " "
			}
		}
		out += "\n"
	}
	return out
}
