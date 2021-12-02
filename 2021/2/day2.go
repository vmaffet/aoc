package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type command struct {
	dir   string
	units int
}

func main() {
	file, _ := os.Open("input.txt")
	defer file.Close()

	cmds := []command{}

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		words := strings.Split(scanner.Text(), " ")

		dir := words[0]
		units, _ := strconv.Atoi(words[1])
		cmds = append(cmds, command{dir, units})
	}

	x, y, z := course(cmds)

	fmt.Println(x * y)
	fmt.Println(x * z)
}

func course(cmds []command) (int, int, int) {
	x, y, z := 0, 0, 0

	for _, cmd := range cmds {
		switch cmd.dir {
		case "up":
			y -= cmd.units
		case "down":
			y += cmd.units
		case "forward":
			x += cmd.units
			z += cmd.units * y
		}
	}

	return x, y, z
}
