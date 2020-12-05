package main

import (
	"aoc/lib"
	"fmt"
)

func main() {
	expenses := lib.ReadLinesAsInt("input")
	part2(expenses)
}

func part1(expenses []int64) {
	for i := 0; i < len(expenses); i++ {
		for j := i + 1; j < len(expenses); j++ {
			if expenses[i]+expenses[j] == 2020 {
				fmt.Println(expenses[i])
				fmt.Println(expenses[j])
				fmt.Println(expenses[i] * expenses[j])
			}
		}
	}
}

func part2(expenses []int64) {
	for i := 0; i < len(expenses); i++ {
		for j := i + 1; j < len(expenses); j++ {
			for l := j + i; l < len(expenses); l++ {
				if expenses[i]+expenses[j]+expenses[l] == 2020 {
					fmt.Println(expenses[i])
					fmt.Println(expenses[j])
					fmt.Println(expenses[l])
					fmt.Println(expenses[i] * expenses[j] * expenses[l])
				}
			}
		}
	}
}
