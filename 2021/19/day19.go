package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, _ := os.Open("input.txt")
	defer file.Close()

	var n int
	scanners := []Scanner{}

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		s := scanner.Text()
		if strings.HasPrefix(s, "--- scanner") {
			scanners = append(scanners, Scanner{})
			n = len(scanners) - 1
			scanners[n].id = n
		} else if s != "" {
			ls := strings.Split(s, ",")
			x, _ := strconv.Atoi(ls[0])
			y, _ := strconv.Atoi(ls[1])
			z, _ := strconv.Atoi(ls[2])
			b := Point{x, y, z}
			scanners[n].beacons = append(scanners[n].beacons, b)
		}
	}

	NormalizeScanners(scanners, 12)

	fmt.Println(part1(scanners))
	fmt.Println(part2(scanners))
}

func part1(scanners []Scanner) int {
	beaconSet := map[Point]bool{}
	for _, s := range scanners {
		for _, b := range s.beacons {
			if _, ok := beaconSet[b]; !ok {
				beaconSet[b] = true
			}
		}
	}
	return len(beaconSet)
}

func part2(scanners []Scanner) int {
	best := 0
	for i, s := range scanners {
		for _, t := range scanners[i+1:] {
			d := s.pos.Sub(t.pos).Manhattan()
			if d > best {
				best = d
			}
		}
	}
	return best
}

func NormalizeScanners(scanners []Scanner, threshold int) {
	scanners[0].pos = Point{0, 0, 0}
	scanners[0].fixed = true

	var i int
	queue := []int{0}
	for len(queue) > 0 {
		i, queue = queue[0], queue[1:]

		ref := scanners[i]
		for j, s := range scanners {
			if s.fixed {
				continue
			}

			p, r, e := ref.Overlaps(s, threshold)
			if e == nil {
				scanners[j].Normalize(p, r)
				scanners[j].fixed = true
				queue = append(queue, j)
			}
		}
	}
}

// --- POINT --- //

type Point [3]int

func (p Point) Rotate(r Rotation) Point {
	x := p[r.axis[0]] * r.dir[0]
	y := p[r.axis[1]] * r.dir[1]
	z := p[r.axis[2]] * r.dir[2]
	return Point{x, y, z}
}

func (p Point) Sub(q Point) Point {
	return Point{p[0] - q[0], p[1] - q[1], p[2] - q[2]}
}

func (p Point) Add(q Point) Point {
	return Point{p[0] + q[0], p[1] + q[1], p[2] + q[2]}
}

func (p Point) Manhattan() int {
	return Abs(p[0]) + Abs(p[1]) + Abs(p[2])
}

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

// --- ROTATION --- //

type Rotation struct {
	axis, dir [3]int
}

const (
	X   = 0
	Y   = 1
	Z   = 2
	POS = 1
	NEG = -1
)

var ROTATIONS = [24]Rotation{
	{[3]int{X, Y, Z}, [3]int{POS, POS, POS}},
	{[3]int{X, Z, Y}, [3]int{POS, POS, NEG}},
	{[3]int{X, Y, Z}, [3]int{POS, NEG, NEG}},
	{[3]int{X, Z, Y}, [3]int{POS, NEG, POS}},
	{[3]int{X, Y, Z}, [3]int{NEG, POS, NEG}},
	{[3]int{X, Z, Y}, [3]int{NEG, NEG, NEG}},
	{[3]int{X, Y, Z}, [3]int{NEG, NEG, POS}},
	{[3]int{X, Z, Y}, [3]int{NEG, POS, POS}},
	{[3]int{Y, X, Z}, [3]int{POS, POS, NEG}},
	{[3]int{Y, Z, X}, [3]int{POS, NEG, NEG}},
	{[3]int{Y, X, Z}, [3]int{POS, NEG, POS}},
	{[3]int{Y, Z, X}, [3]int{POS, POS, POS}},
	{[3]int{Y, X, Z}, [3]int{NEG, POS, POS}},
	{[3]int{Y, Z, X}, [3]int{NEG, POS, NEG}},
	{[3]int{Y, X, Z}, [3]int{NEG, NEG, NEG}},
	{[3]int{Y, Z, X}, [3]int{NEG, NEG, POS}},
	{[3]int{Z, X, Y}, [3]int{POS, POS, POS}},
	{[3]int{Z, Y, X}, [3]int{POS, POS, NEG}},
	{[3]int{Z, X, Y}, [3]int{POS, NEG, NEG}},
	{[3]int{Z, Y, X}, [3]int{POS, NEG, POS}},
	{[3]int{Z, X, Y}, [3]int{NEG, POS, NEG}},
	{[3]int{Z, Y, X}, [3]int{NEG, NEG, NEG}},
	{[3]int{Z, X, Y}, [3]int{NEG, NEG, POS}},
	{[3]int{Z, Y, X}, [3]int{NEG, POS, POS}},
}

// --- SCANNER --- //

type Scanner struct {
	id      int
	beacons []Point
	pos     Point
	fixed   bool
}

func (s Scanner) Overlaps(o Scanner, t int) (Point, Rotation, error) {
	for _, r := range ROTATIONS {
		cnt := map[Point]int{}
		for _, sb := range s.beacons {
			for _, ob := range o.beacons {
				cnt[sb.Sub(ob.Rotate(r))]++
			}
		}

		for p, n := range cnt {
			if n >= t {
				return p, r, nil
			}
		}
	}
	return Point{}, Rotation{}, errors.New("Scanners do not overlap.")
}

func (s *Scanner) Normalize(p Point, r Rotation) {
	for i, b := range s.beacons {
		s.beacons[i] = b.Rotate(r).Add(p)
	}
	s.pos = p
}
