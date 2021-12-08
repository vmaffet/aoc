package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"sort"
	"strings"
)

func main() {
	file, _ := os.Open("input.txt")
	defer file.Close()

	re := regexp.MustCompile(`([\w ]+) \| ([\w ]+)`)

	patterns, outputs := [][]string{}, [][]string{}

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		entry := re.FindStringSubmatch(scanner.Text())
		pat := strings.Split(entry[1], " ")
		out := strings.Split(entry[2], " ")

		sort.Slice(pat, func(i, j int) bool { return len(pat[i]) < len(pat[j]) })
		for i, s := range pat {
			r := []rune(s)
			sort.Slice(r, func(i int, j int) bool { return r[i] < r[j] })
			pat[i] = string(r)
		}

		for i, s := range out {
			r := []rune(s)
			sort.Slice(r, func(i int, j int) bool { return r[i] < r[j] })
			out[i] = string(r)
		}

		patterns = append(patterns, pat)
		outputs = append(outputs, out)
	}

	fmt.Println(task1(outputs))
	fmt.Println(task2(patterns, outputs))
}

func task1(arr [][]string) int {
	cnt := 0
	for _, line := range arr {
		for _, s := range line {
			switch len(s) {
			case 2, 3, 4, 7:
				cnt++
			}
		}
	}
	return cnt
}

func task2(patterns, outputs [][]string) int {
	cnt := 0
	for i, pat := range patterns {
		mapping := identify(pat)
		out := 0
		for _, enc := range outputs[i] {
			out = 10*out + mapping[enc]
		}
		cnt += out
	}
	return cnt
}

func identify(enc []string) map[string]int {
	one := enc[0]
	four := enc[2]

	dec := map[string]int{enc[0]: 1, enc[1]: 7, enc[2]: 4, enc[9]: 8}

	for _, s := range enc[3:6] {
		if ContainsAll(s, one) {
			dec[s] = 3
		} else if CountCommon(s, four) == 2 {
			dec[s] = 2
		} else {
			dec[s] = 5
		}
	}

	for _, s := range enc[6:9] {
		if ContainsAll(s, four) {
			dec[s] = 9
		} else if ContainsAll(s, one) {
			dec[s] = 0
		} else {
			dec[s] = 6
		}
	}

	return dec
}

func ContainsAll(s, chars string) bool {
	return CountCommon(s, chars) == len(chars)
}

func CountCommon(s, chars string) int {
	cnt := 0
	for _, c := range chars {
		if strings.ContainsRune(s, c) {
			cnt++
		}
	}
	return cnt
}
