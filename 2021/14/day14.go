package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
)

type duo struct {
	left, right int
}

type state struct {
	pair  duo
	steps int
}

type record = [26]int

func main() {
	file, _ := os.Open("input.txt")
	defer file.Close()
	scanner := bufio.NewScanner(file)

	scanner.Scan()
	template := []int{}
	for _, c := range scanner.Text() {
		template = append(template, int(c-'A'))
	}

	rules := map[duo]int{}
	re := regexp.MustCompile(`([A-Z]{2}) -> ([A-Z])`)
	scanner.Scan()
	for scanner.Scan() {
		pair := re.FindStringSubmatch(scanner.Text())
		l, r := int(pair[1][0]-'A'), int(pair[1][1]-'A')
		rules[duo{l, r}] = int(pair[2][0] - 'A')
	}

	fmt.Println(process(rules, template, 10))
	fmt.Println(process(rules, template, 40))
}

func process(rules map[duo]int, input []int, steps int) int {
	cnt, memo := record{}, map[state]record{}
	for i := range input[1:] {
		tot := expand(memo, rules, state{duo{input[i], input[i+1]}, steps})

		for i, t := range tot {
			cnt[i] += t
		}
		cnt[input[i]]--
	}
	cnt[input[0]]++

	min, max := minmax(cnt[:])
	return max - min
}

func expand(memo map[state]record, rules map[duo]int, target state) record {
	if val, ok := memo[target]; ok {
		return val
	}

	cnt := record{}
	if target.steps == 0 {
		cnt[target.pair.left]++
		cnt[target.pair.right]++
	} else {
		mid := rules[target.pair]

		L := expand(memo, rules, state{duo{target.pair.left, mid}, target.steps - 1})
		R := expand(memo, rules, state{duo{mid, target.pair.right}, target.steps - 1})
		for i := range cnt {
			cnt[i] = L[i] + R[i]
		}
		cnt[mid]--
	}

	memo[target] = cnt
	return cnt
}

func minmax(arr []int) (int, int) {
	min, max := int(^uint(0)>>1), 0
	for _, v := range arr {
		if v > 0 && v < min {
			min = v
		}
		if v > max {
			max = v
		}
	}
	return min, max
}
