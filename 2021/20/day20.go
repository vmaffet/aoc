package main

import (
	"bufio"
	"fmt"
	"os"
)

type Point struct {
	x, y int
}

func main() {
	file, _ := os.Open("input.txt")
	defer file.Close()

	iea := make([]bool, 512)
	img := map[Point]bool{}
	fill := false
	var br Point

	scanner := bufio.NewScanner(file)
	for i := 0; scanner.Scan(); i++ {
		s := scanner.Text()
		switch i {
		case 0:
			for j, c := range s {
				iea[j] = c == '#'
			}
		case 1:
			continue
		default:
			for j, c := range s {
				br = Point{j, i - 2}
				img[br] = c == '#'
			}
		}
	}

	fmt.Println(part(2, br, img, fill, iea))
	fmt.Println(part(50, br, img, fill, iea))
}

func part(n int, br Point, img map[Point]bool, fill bool, iea []bool) int {
	tl := Point{0, 0}
	for i := 0; i < n; i++ {
		img, fill = enhance(tl, br, img, fill, iea)
		tl.x, tl.y = tl.x-1, tl.y-1
		br.x, br.y = br.x+1, br.y+1
	}
	return count(img)
}

func enhance(tl, br Point, img map[Point]bool, fill bool, iea []bool) (map[Point]bool, bool) {
	enh := map[Point]bool{}
	q := Point{}
	for q.y = tl.y - 1; q.y <= br.y+1; q.y++ {
		for q.x = tl.x - 1; q.x <= br.x+1; q.x++ {
			i := index(q, img, fill)
			enh[q] = iea[i]
		}
	}
	if fill {
		fill = iea[511]
	} else {
		fill = iea[0]
	}
	return enh, fill
}

func index(p Point, img map[Point]bool, fill bool) int {
	n, q := 0, Point{}
	for q.y = p.y - 1; q.y <= p.y+1; q.y++ {
		for q.x = p.x - 1; q.x <= p.x+1; q.x++ {
			n <<= 1
			if v, ok := img[q]; (ok && v) || (!ok && fill) {
				n |= 1
			}
		}
	}
	return n
}

func count(img map[Point]bool) int {
	n := 0
	for _, v := range img {
		if v {
			n++
		}
	}
	return n
}
