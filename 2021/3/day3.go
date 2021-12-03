package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	file, _ := os.Open("input.txt")
	defer file.Close()

	report := []string{}

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		report = append(report, scanner.Text())
	}

	fmt.Println(task1(report))
	fmt.Println(2)
}

func task1(arr []string) int {
	n, m := len(arr), len(arr[0])
	cnt := make([]int, m)

	for _, s := range arr {
		for i, c := range s {
			if c == '1' {
				cnt[i]++
			}
		}
	}

	gamma, epsilon := 0, 0
	for _, c := range cnt {
		gamma *= 2
		epsilon *= 2
		if 2*c > n {
			gamma++
		} else {
			epsilon++
		}
	}

	return gamma * epsilon
}
