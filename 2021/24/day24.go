package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	file, _ := os.Open("input.txt")
	defer file.Close()

	program := []string{}

	scanner := bufio.NewScanner(file)
	for i := 0; scanner.Scan(); i++ {
		program = append(program, scanner.Text())
	}

	ABC := [14][3]int{}
	for i := range ABC {
		part := program[18*i:]
		A, _ := strconv.Atoi(part[4][6:])
		B, _ := strconv.Atoi(part[5][6:])
		C, _ := strconv.Atoi(part[15][6:])
		ABC[i] = [3]int{A, B, C}
	}

	fmt.Println(part1(ABC))
	fmt.Println(part2(ABC))
}

func execute(program []string, input [14]int) [4]int {

	ii := 0
	vars := [4]int{0, 0, 0, 0}

	for _, inst := range program {
		i := inst[:3]
		a := inst[4] - 'w'
		if i == "inp" {
			vars[a] = input[ii]
			ii++
		} else {
			var b int
			if ib := inst[6] - 'w'; 0 <= ib && ib < 4 {
				b = vars[ib]
			} else {
				b, _ = strconv.Atoi(inst[6:])
			}
			switch i {
			case "add":
				vars[a] += b
			case "mul":
				vars[a] *= b
			case "div":
				vars[a] /= b
			case "mod":
				vars[a] %= b
			case "eql":
				if vars[a] == b {
					vars[a] = 1
				} else {
					vars[a] = 0
				}
			}
		}
	}

	return vars
}

func analized(ABC [14][3]int, input [14]int) int {

	var z int

	for i, w := range input {
		A, B, C := ABC[i][0], ABC[i][1], ABC[i][2]

		x := (z % 26) + B
		z /= A
		if w != x {
			z *= 26
			z += w + C
		}
	}

	return z
}

func part1(ABC [14][3]int) int {

	input := [14]int{}
	stack := [][2]int{}
	for i := range ABC {
		A, B, C := ABC[i][0], ABC[i][1], ABC[i][2]
		if A == 1 {
			stack = append(stack, [2]int{i, C})
		} else {
			pop := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			diff := pop[1] + B
			if diff > 0 {
				input[i] = 9
				input[pop[0]] = 9 - diff
			} else {
				input[i] = 9 + diff
				input[pop[0]] = 9
			}
		}
	}

	res := 0
	for _, v := range input {
		res = 10*res + v
	}

	return res
}

func part2(ABC [14][3]int) int {

	input := [14]int{}
	stack := [][2]int{}
	for i := range ABC {
		A, B, C := ABC[i][0], ABC[i][1], ABC[i][2]
		if A == 1 {
			stack = append(stack, [2]int{i, C})
		} else {
			pop := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			diff := pop[1] + B
			if diff > 0 {
				input[i] = 1 + diff
				input[pop[0]] = 1
			} else {
				input[i] = 1
				input[pop[0]] = 1 - diff
			}
		}
	}

	res := 0
	for _, v := range input {
		res = 10*res + v
	}

	return res
}
