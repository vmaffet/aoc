package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	hex, _ := os.ReadFile("input.txt")

	bit := []bool{}
	for _, h := range hex {
		bit = append(bit, HexToBin(h)...)
	}

	_, p1, p2 := read(bit)

	fmt.Println(p1)
	fmt.Println(p2)
}

func read(packet []bool) (int, int, int) {
	e, n := 0, 0

	v := BinToInt(packet[:3])
	t := BinToInt(packet[3:6])

	if t == 4 {
		for e = 11; packet[e-5]; e += 5 {
			n = n<<4 + BinToInt(packet[e-4:e])
		}
		n = n<<4 + BinToInt(packet[e-4:e])
	} else {
		vals := []int{}
		if packet[6] {
			e = 18
			for i := 0; i < BinToInt(packet[7:18]); i++ {
				esub, vsub, nsub := read(packet[e:])
				vals = append(vals, nsub)
				v += vsub
				e += esub
			}
		} else {
			e = 22 + BinToInt(packet[7:22])
			for i := 22; i < e; i += 0 {
				esub, vsub, nsub := read(packet[i:e])
				vals = append(vals, nsub)
				v += vsub
				i += esub
			}
		}

		o := func(a, b int) int {
			switch t {
			case 0:
				return a + b
			case 1:
				return a * b
			case 2:
				if a < b {
					return a
				} else {
					return b
				}
			case 3:
				if a > b {
					return a
				} else {
					return b
				}
			case 5:
				if a > b {
					return 1
				} else {
					return 0
				}
			case 6:
				if a < b {
					return 1
				} else {
					return 0
				}
			case 7:
				if a == b {
					return 1
				} else {
					return 0
				}
			}
			return -1
		}

		n = vals[0]
		for _, x := range vals[1:] {
			n = o(n, x)
		}
	}

	return e, v, n
}

func HexToBin(hex byte) []bool {
	n, err := strconv.ParseUint(string(hex), 16, 4)
	if err != nil {
		panic(err)
	}

	bin := [4]bool{}
	for i := 3; i >= 0; i, n = i-1, n>>1 {
		bin[i] = n%2 == 1
	}
	return bin[:]
}

func BinToInt(bin []bool) int {
	i := 0
	for _, b := range bin {
		i = i << 1
		if b {
			i = i + 1
		}
	}
	return i
}
