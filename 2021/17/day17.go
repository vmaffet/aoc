package main

import (
	"fmt"
	"math"
	"os"
	"regexp"
	"strconv"
)

func main() {
	raw, _ := os.ReadFile("input.txt")

	re := regexp.MustCompile(`target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)`)
	target := re.FindStringSubmatch(string(raw))

	left, _ := strconv.Atoi(target[1])
	right, _ := strconv.Atoi(target[2])
	bot, _ := strconv.Atoi(target[3])
	top, _ := strconv.Atoi(target[4])

	fmt.Println(part1(bot))
	fmt.Println(part2(left, right, bot, top))
}

func part1(ymax int) int {
	v := -(ymax + 1)
	return v * (v + 1) / 2
}

func part2(xmin, xmax, ymin, ymax int) int {
	vymin := ymin
	vymax := -(ymin + 1)
	vxmin := int(math.Ceil((math.Sqrt(1+8*float64(xmin)) - 1) / 2))
	vxmax := xmax

	cnt := 0
	for vx := vxmin; vx <= vxmax; vx++ {
		for vy := vymin; vy <= vymax; vy++ {
			cnt += simulate(vx, vy, xmin, xmax, ymin, ymax)
		}
	}
	return cnt
}

func simulate(vx, vy, xmin, xmax, ymin, ymax int) int {
	x, y := 0, 0
	for x <= xmax && y >= ymin {
		x, y = x+vx, y+vy
		if xmin <= x && x <= xmax && ymin <= y && y <= ymax {
			return 1
		}
		vy -= 1
		if vx > 0 {
			vx -= 1
		}

	}
	return 0
}
