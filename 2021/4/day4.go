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

	scanner := bufio.NewScanner(file)

	scanner.Scan()
	order := strings.Split(scanner.Text(), ",")

	cards := [][][]string{}
	for scanner.Scan() {
		text := scanner.Text()
		if text == "" {
			cards = append(cards, [][]string{})
		} else {
			cur := len(cards) - 1
			cards[cur] = append(cards[cur], strings.Fields(text))
		}
	}

	fmt.Println(task1(order, cards))
	fmt.Println(task2(order, cards))
}

func task1(order []string, cards [][][]string) int {
	return score(order, cards, 1)
}

func task2(order []string, cards [][][]string) int {
	return score(order, cards, len(cards))
}

func score(order []string, cards [][][]string, rank int) int {
	marked := make([][5][5]bool, len(cards))
	won := make([]bool, len(cards))
	for _, n := range order {
		for i, card := range cards {
			if won[i] {
				continue
			}

			f, j, k := find(card, n)
			if f {
				marked[i][j][k] = true
				if check(marked[i]) {
					won[i] = true
					rank--
					if rank < 1 {
						v, _ := strconv.Atoi(n)
						return v * sum(card, marked[i])
					}
				}
			}
		}
	}
	return -1
}

func find(arr [][]string, s string) (bool, int, int) {
	for i, row := range arr {
		for j, el := range row {
			if el == s {
				return true, i, j
			}
		}
	}
	return false, 0, 0
}

func check(arr [5][5]bool) bool {
	for i := 0; i < 5; i++ {
		hor, ver := true, true
		for j := 0; j < 5; j++ {
			hor = hor && arr[i][j]
			ver = ver && arr[j][i]
			if !(hor || ver) {
				break
			}
		}
		if hor || ver {
			return true
		}
	}
	return false
}

func sum(arr [][]string, mask [5][5]bool) int {
	sum := 0
	for i := 0; i < 5; i++ {
		for j := 0; j < 5; j++ {
			if !mask[i][j] {
				v, _ := strconv.Atoi(arr[i][j])
				sum += v
			}
		}
	}
	return sum
}
