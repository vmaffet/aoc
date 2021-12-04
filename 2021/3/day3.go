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
	fmt.Println(task2(report))
}

func task1(arr []string) int {
	gamma, epsilon := 0, 0
	for _, c := range common(arr) {
		gamma *= 2
		epsilon *= 2
		if c > 0 {
			gamma++
		} else {
			epsilon++
		}
	}

	return gamma * epsilon
}

func task2(arr []string) int {
	var ogr_bc bitcriteria = func(c int, b byte) bool {
		return (c >= 0) == (b == '1')
	}
	ogr := process(arr, ogr_bc)

	var csr_bc bitcriteria = func(c int, b byte) bool {
		return (c >= 0) == (b == '0')
	}
	csr := process(arr, csr_bc)

	return ogr * csr
}

func common(arr []string) []int {
	n, m := len(arr), len(arr[0])
	cnt := make([]int, m)

	for _, s := range arr {
		for i, c := range s {
			if c == '1' {
				cnt[i]++
			}
		}
	}

	cmmn := make([]int, m)
	for i, x := range cnt {
		cmmn[i] = 2*x - n
	}

	return cmmn
}

type bitcriteria func(c int, b byte) bool

func process(arr []string, fn bitcriteria) int {
	for i := 0; len(arr) > 1; i++ {
		cmmn := common(arr)
		j := 0
		for k, s := range arr {
			if fn(cmmn[i], s[i]) {
				arr[k] = arr[j]
				arr[j] = s
				j++
			}
		}
		arr = arr[:j]
	}

	res := 0
	for _, b := range arr[0] {
		res *= 2
		if b == '1' {
			res++
		}
	}

	return res
}
