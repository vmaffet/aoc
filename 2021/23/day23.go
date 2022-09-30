package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
)

func main() {
	file, _ := os.Open("input.txt")
	defer file.Close()

	c := Config{}
	for i := range c.rooms {
		c.rooms[i] = make([]int, 2)
	}

	scanner := bufio.NewScanner(file)
	for i := 0; scanner.Scan(); i++ {
		line := scanner.Text()
		switch i {
		case 2, 3:
			for j := range c.rooms {
				c.rooms[j][i-2] = int(line[3+2*j] - 'A' + 1)
			}
		}
	}

	t := Config{}
	for i := range t.rooms {
		t.rooms[i] = make([]int, 2)
		for j := range t.rooms[i] {
			t.rooms[i][j] = i + 1
		}
	}

	fmt.Println(part(c.ToHash(), t.ToHash(), 2))

	c.rooms[0] = []int{c.rooms[0][0], 4, 4, c.rooms[0][1]}
	c.rooms[1] = []int{c.rooms[1][0], 3, 2, c.rooms[1][1]}
	c.rooms[2] = []int{c.rooms[2][0], 2, 1, c.rooms[2][1]}
	c.rooms[3] = []int{c.rooms[3][0], 1, 3, c.rooms[3][1]}

	for i := range t.rooms {
		t.rooms[i] = make([]int, 4)
		for j := range t.rooms[i] {
			t.rooms[i][j] = i + 1
		}
	}

	fmt.Println(part(c.ToHash(), t.ToHash(), 4))
}

func part(sh, th ConfigHash, l int) int {

	dist := map[ConfigHash]*Item{
		sh: {
			value:    sh,
			priority: 0,
			index:    0,
		},
	}

	pq := make(PriorityQueue, 1)
	pq[0] = dist[sh]
	heap.Init(&pq)

	for pq.Len() > 0 {
		top := heap.Pop(&pq).(*Item)
		if th == top.value {
			return -top.priority
		}

		current := top.value.FromHash(l)
		for ch, p := range current.FindMoves() {
			if item, ok := dist[ch]; ok {
				if top.priority-p > item.priority {
					pq.update(item, item.value, top.priority-p)
				}
			} else {
				dist[ch] = &Item{
					value:    ch,
					priority: top.priority - p,
				}
				heap.Push(&pq, dist[ch])
			}
		}
	}

	return -1
}

type Config struct {
	hallway [11]int
	rooms   [4][]int
}

type ConfigHash uint64

func (c Config) ToHash() ConfigHash {
	h := ConfigHash(0)
	for _, v := range c.hallway {
		h *= 5
		h += ConfigHash(v)
	}
	for _, r := range c.rooms {
		for _, s := range r {
			h *= 5
			h += ConfigHash(s)
		}
	}
	return h
}

func (h ConfigHash) FromHash(nr int) Config {
	c := Config{}
	for i := len(c.rooms) - 1; i >= 0; i-- {
		c.rooms[i] = make([]int, nr)
		for j := len(c.rooms[i]) - 1; j >= 0; j-- {
			c.rooms[i][j], h = int(h%5), h/5
		}
	}
	for i := len(c.hallway) - 1; i >= 0; i-- {
		c.hallway[i], h = int(h%5), h/5
	}
	return c
}

func (c Config) Copy() Config {
	d := Config{}
	d.hallway = c.hallway
	for i := range d.rooms {
		d.rooms[i] = make([]int, len(c.rooms[i]))
		copy(d.rooms[i], c.rooms[i])
	}
	return d
}

func (c Config) ToString() string {
	conv := map[int]string{0: ".", 1: "A", 2: "B", 3: "C", 4: "D"}
	s := "#############\n#"
	for _, v := range c.hallway {
		s += conv[v]
	}
	s += "#\n###"
	for i := range c.rooms[0] {
		for _, r := range c.rooms {
			s += conv[r[i]]
			s += "#"
		}
		s += "##\n###"
	}
	s += "##########"
	return s
}

func (c Config) FindMoves() map[ConfigHash]int {
	moves := map[ConfigHash]int{}

	mul := [5]int{0, 1, 10, 100, 1000}
	for ir, r := range c.rooms {
		ok := true
		for is := len(r) - 1; is >= 0; is-- {
			s := r[is]
			ok = ok && s == ir+1
			if s == 0 {
				continue
			} else if ok {
				continue
			} else if is > 0 && r[is-1] != 0 {
				continue
			}
			cost := (is + 1)
			irh := 2 * (ir + 1)
			for ih := irh - 1; ih >= 0; ih-- {
				if c.hallway[ih] != 0 {
					break
				} else if ih > 0 && ih%2 == 0 {
					continue
				}
				d := c.Copy()
				d.rooms[ir][is] = 0
				d.hallway[ih] = s
				moves[d.ToHash()] = mul[s] * (cost + irh - ih)
			}
			for ih := irh + 1; ih < len(c.hallway); ih++ {
				if c.hallway[ih] != 0 {
					break
				} else if ih < len(c.hallway)-1 && ih%2 == 0 {
					continue
				}
				d := c.Copy()
				d.rooms[ir][is] = 0
				d.hallway[ih] = s
				moves[d.ToHash()] = mul[s] * (cost + ih - irh)
			}
		}
	}
	for ih, h := range c.hallway {
		if h == 0 {
			continue
		}
		ir := h - 1
		isd := 0
		for is, s := range c.rooms[ir] {
			if s == 0 {
				isd = is
			} else if s != h {
				isd = -1
				break
			}
		}
		if isd < 0 {
			continue
		}
		irh := 2 * (ir + 1)
		a, b := irh+1, ih
		if ih < irh {
			a, b = ih+1, irh
		}
		ok := true
		for _, v := range c.hallway[a:b] {
			if v != 0 {
				ok = false
				break
			}
		}
		if !ok {
			continue
		}
		d := c.Copy()
		d.hallway[ih] = 0
		d.rooms[ir][isd] = h
		moves[d.ToHash()] = mul[h] * (isd + 1 + b - a + 1)
	}
	return moves
}

/////////////////////////////////////////////////////
//                  PriorityQueue                  //
/////////////////////////////////////////////////////

// An Item is something we manage in a priority queue.
type Item struct {
	value    ConfigHash // The value of the item; arbitrary.
	priority int        // The priority of the item in the queue.
	// The index is needed by update and is maintained by the heap.Interface methods.
	index int // The index of the item in the heap.
}

// A PriorityQueue implements heap.Interface and holds Items.
type PriorityQueue []*Item

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	// We want Pop to give us the highest, not lowest, priority so we use greater than here.
	return pq[i].priority > pq[j].priority
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *PriorityQueue) Push(x any) {
	n := len(*pq)
	item := x.(*Item)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() any {
	old := *pq
	n := len(old)
	item := old[n-1]
	old[n-1] = nil  // avoid memory leak
	item.index = -1 // for safety
	*pq = old[0 : n-1]
	return item
}

// update modifies the priority and value of an Item in the queue.
func (pq *PriorityQueue) update(item *Item, value ConfigHash, priority int) {
	item.value = value
	item.priority = priority
	heap.Fix(pq, item.index)
}
