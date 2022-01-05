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

	list := []pair{}

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		list = append(list, parse(scanner.Text()))
	}

	fmt.Println(part1(list))
	fmt.Println(part2(list))
}

func part1(arr []pair) int {
	p := arr[0]
	for _, q := range arr[1:] {
		p = p.add(&q)
	}
	return p.magnitude()
}

func part2(arr []pair) int {
	max := 0
	for i, p := range arr {
		for j, q := range arr {
			if i != j {
				r := p.add(&q)
				if mag := r.magnitude(); mag > max {
					max = mag
				}
			}
		}
	}
	return max
}

type pair struct {
	leaf        bool
	value       int
	left, right *pair
}

func parse(s string) pair {
	if s[0] != '[' {
		v, _ := strconv.Atoi(s)
		return pair{leaf: true, value: v}
	} else {
		sep := 0
		for cnt := 0; s[sep] != ',' || cnt != 1; sep++ {
			if c := s[sep]; c == '[' {
				cnt++
			} else if c == ']' {
				cnt--
			}
		}
		left := parse(s[1:sep])
		right := parse(s[sep+1 : len(s)-1])
		return pair{leaf: false, left: &left, right: &right}
	}
}

func (p *pair) add(q *pair) pair {
	r := pair{leaf: false, left: p.Copy(), right: q.Copy()}
	r.reduce()
	return r
}

func (p *pair) reduce() {
	for ok := true; ok; ok = p.split() {
		for p.explode() {
		}
	}
}

func (p *pair) explode() bool {
	done, expld := p.explodesub(0, false, nil)
	if done && expld != nil {
		expld.leaf = true
		expld.value = 0
	}
	return done
}

func (p *pair) explodesub(depth int, done bool, left *pair) (bool, *pair) {
	if p.leaf {
		if done {
			p.value += left.right.value
			left.leaf = true
			left.value = 0
			return true, nil
		} else {
			return false, p
		}
	} else if !done && depth == 4 {
		if left != nil {
			left.value += p.left.value
		}
		return true, p
	} else {
		done, left = p.left.explodesub(depth+1, done, left)
		if !done || left != nil {
			done, left = p.right.explodesub(depth+1, done, left)
		}
		return done, left
	}
}

func (p *pair) split() bool {
	if p.leaf {
		if p.value > 9 {
			p.leaf = false
			p.left = &pair{leaf: true, value: p.value / 2}
			p.right = &pair{leaf: true, value: p.value - p.left.value}
		}
		return !p.leaf
	} else {
		return p.left.split() || p.right.split()
	}
}

func (p *pair) magnitude() int {
	if p.leaf {
		return p.value
	} else {
		return 3*p.left.magnitude() + 2*p.right.magnitude()
	}
}

func (p *pair) Copy() *pair {
	if p.leaf {
		return &pair{leaf: p.leaf, value: p.value}
	} else {
		return &pair{leaf: p.leaf, left: p.left.Copy(), right: p.right.Copy()}
	}
}

func (p pair) String() string {
	if p.leaf {
		return fmt.Sprintf("%d", p.value)
	} else {
		return fmt.Sprintf("[%s,%s]", p.left, p.right)
	}
}
