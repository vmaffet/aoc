package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	data, _ := os.ReadFile("input.txt")

	pos := []int{}
	for _, ps := range strings.Split(string(data), ",") {
		p, _ := strconv.Atoi(ps)
		pos = append(pos, p)
	}
	sort.Ints(pos)

	fmt.Println(task1(pos))
	fmt.Println(task2(pos))
}

func task1(arr []int) int {
	med := arr[len(arr)/2]

	cost := 0
	for _, x := range arr {
		cost += abs(x - med)
	}

	return cost
}

func task2(arr []int) int {
	best := int(^uint(0) >> 1)
	for t := arr[0]; t <= arr[len(arr)-1]; t++ {
		cost := 0
		for _, x := range arr {
			cost += ((x-t)*(x-t) + abs(x-t)) / 2
		}
		if cost < best {
			best = cost
		}
	}

	return best
}

func abs(a int) int {
	if a >= 0 {
		return a
	} else {
		return -a
	}
}
