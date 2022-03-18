package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, _ := os.Open("input.txt")
	defer file.Close()

	var p1, p2 int

	scanner := bufio.NewScanner(file)
	for i := 0; scanner.Scan(); i++ {
		s := scanner.Text()
		switch i {
		case 0:
			p1, _ = strconv.Atoi(strings.TrimPrefix(s, "Player 1 starting position: "))
		case 1:
			p2, _ = strconv.Atoi(strings.TrimPrefix(s, "Player 2 starting position: "))
		}
	}

	fmt.Println(part1(p1, p2))
	fmt.Println(part2(p1, p2))
}

func part1(p1, p2 int) int {
	s1, s2 := 0, 0
	for n := 0; true; n++ {
		s1 += ((p1 + (9*n+6)*(n+1) - 1) % 10) + 1
		if s1 >= 1000 {
			return (6*n + 3) * s2
		}
		s2 += ((p2 + (9*n+15)*(n+1) - 1) % 10) + 1
		if s2 >= 1000 {
			return (6*n + 6) * s1
		}
	}
	panic("unreachable")
}

func part2(p1, p2 int) uint64 {
	us1 := make([][10]uint64, 31)
	us2 := make([][10]uint64, 31)

	us1[0][p1] = 1
	us2[0][p2] = 1

	var uw1, uw2 uint64
	for count(us1[:21]) > 0 && count(us2[:21]) > 0 {
		us1 = split(us1[:21])
		uw1 += count(us2[:21]) * count(us1[21:])

		us2 = split(us2[:21])
		uw2 += count(us1[:21]) * count(us2[21:])
	}

	if uw1 > uw2 {
		return uw1
	} else {
		return uw2
	}
}

func split(us [][10]uint64) [][10]uint64 {
	dice := map[int]uint64{3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

	nus := make([][10]uint64, 31)
	for s, up := range us {
		for p, cu := range up {
			for d, nu := range dice {
				nus[s+(p+d-1)%10+1][(p+d)%10] += cu * nu
			}
		}
	}
	return nus
}

func count(us [][10]uint64) uint64 {
	var n uint64
	for _, up := range us {
		for _, nu := range up {
			n += nu
		}
	}
	return n
}
