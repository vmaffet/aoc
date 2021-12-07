package main

import (
	"fmt"
	"os"
)

func main() {
	data, _ := os.ReadFile("input.txt")

	timer := [9]int{}
	for i := 0; i < len(data); i += 2 {
		timer[data[i]-'0']++
	}

	fmt.Println(sim(timer, 80))
	fmt.Println(sim(timer, 256))
}

func sim(arr [9]int, iter int) int {
	for i := 0; i < iter; i++ {
		arr[(i+7)%9] += arr[i%9]
	}

	cnt := 0
	for _, x := range arr {
		cnt += x
	}
	return cnt
}
