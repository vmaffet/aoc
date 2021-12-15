package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
)

type point struct {
	x, y int
}

func main() {
	file, _ := os.Open("input.txt")
	defer file.Close()

	risk := map[point]int{}
	start, end := point{}, point{}

	scanner := bufio.NewScanner(file)
	for end.y = 0; scanner.Scan(); end.y++ {
		var c rune
		for end.x, c = range scanner.Text() {
			risk[end] = int(c - '0')
		}
	}
	end.y--

	fmt.Println(visit(risk, start, end))

	risk5 := expand(risk, end.y+1, end.x+1, 5)
	fmt.Println(visit(risk5, start, point{end.x*5 + 4, end.y*5 + 4}))
}

func expand(org map[point]int, h, w, n int) map[point]int {
	res := map[point]int{}
	for iy := 0; iy < n; iy++ {
		for ix := 0; ix < n; ix++ {
			for p, v := range org {
				np := point{p.x + ix*w, p.y + iy*h}
				res[np] = (v+ix+iy-1)%9 + 1
			}
		}
	}
	return res
}

func visit(node map[point]int, start, end point) int {
	dist := map[point]int{start: 0}

	pq := &PriorityQueue{}
	heap.Init(pq)
	heap.Push(pq, &Item{pos: start, dist: 0})
	for pq.Len() > 0 {
		cur := heap.Pop(pq).(*Item).pos

		if cur == end {
			break
		}

		for _, p := range neighbors(cur) {
			if n, nok := node[p]; nok {
				nt := dist[cur] + n
				if t, tok := dist[p]; !tok || nt < t {
					dist[p] = nt
					heap.Push(pq, &Item{pos: p, dist: nt})
				}
			}
		}
	}

	return dist[end]
}

func neighbors(p point) []point {
	n := point{p.x, p.y - 1}
	e := point{p.x + 1, p.y}
	s := point{p.x, p.y + 1}
	w := point{p.x - 1, p.y}
	return []point{n, e, s, w}
}

type Item struct {
	pos   point
	dist  int
	index int
}

type PriorityQueue []*Item

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool { return pq[i].dist < pq[j].dist }

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *PriorityQueue) Push(x interface{}) {
	n := len(*pq)
	item := x.(*Item)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	old[n-1] = nil
	item.index = -1
	*pq = old[0 : n-1]
	return item
}
