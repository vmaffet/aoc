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

	depths := []int{}

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		n, _ := strconv.Atoi(scanner.Text())
		depths = append(depths, n)
	}

	fmt.Println(task1(depths))
	fmt.Println(task2(depths))
}

func task1(depths []int) int {
	return inccount(depths, 1)
}

func task2(depths []int) int {
	return inccount(depths, 3)
}

func inccount(arr []int, offset int) int {
	count := 0

	for i, d := range arr[offset:] {
		if d > arr[i] {
			count++
		}
	}

	return count
}
