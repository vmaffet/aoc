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

	east := map[point]bool{}
	south := map[point]bool{}

	height, width := 0, 0
	scanner := bufio.NewScanner(file)
	for i := 0; scanner.Scan(); i++ {
		line := scanner.Text()
		for j, c := range line {
			switch c {
			case '>':
				east[point{j, i}] = true
			case 'v':
				south[point{j, i}] = true
			}
		}
		height, width = i+1, len(line)
	}

	fmt.Println(part1(east, south, height, width))
}

func part1(east, south map[point]bool, height, width int) int {

	var i int
	var change bool
	for i, change = 0, true; change; i++ {
		change = false
		neweast := map[point]bool{}
		for p := range east {
			d := point{(p.x + 1) % width, p.y}
			_, oke := east[d]
			_, oks := south[d]
			if !oke && !oks {
				neweast[d] = true
				change = true
			} else {
				neweast[p] = true
			}
		}
		east = neweast
		newsouth := map[point]bool{}
		for p := range south {
			d := point{p.x, (p.y + 1) % height}
			_, oke := east[d]
			_, oks := south[d]
			if !oke && !oks {
				newsouth[d] = true
				change = true
			} else {
				newsouth[p] = true
			}
		}
		south = newsouth
	}

	return i
}
