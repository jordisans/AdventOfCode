package main

import (
	"aoc/lib"
	"fmt"
	"strconv"
	"strings"
)

func main() {
	lines := lib.ReadLines("input")
	validPasswords := part2(lines)
	fmt.Println(validPasswords)
}

func part1(lines []string) int {
	validPasswords := 0
	for _, line := range lines {
		splittedLine := strings.Split(line, " ")
		nRange, letter, password := splittedLine[0], []rune(splittedLine[1])[0], splittedLine[2]
		splittedNRange := strings.Split(nRange, "-")
		lowerBound, _ := strconv.Atoi(splittedNRange[0])
		upperBound, _ := strconv.Atoi(splittedNRange[1])

		letterAppearences := 0
		for _, l := range password {
			if l == letter {
				letterAppearences++
			}
		}

		if lowerBound <= letterAppearences && letterAppearences <= upperBound {
			validPasswords++
		}
	}

	return validPasswords
}

func part2(lines []string) int {
	validPasswords := 0
	for _, line := range lines {
		splittedLine := strings.Split(line, " ")
		nRange, letter, password := splittedLine[0], []rune(splittedLine[1])[0], []rune(splittedLine[2])
		splittedNRange := strings.Split(nRange, "-")
		firstPosition, _ := strconv.Atoi(splittedNRange[0])
		secondPosition, _ := strconv.Atoi(splittedNRange[1])

		letterAppearsInFirstPosition := password[firstPosition-1] == letter
		letterAppearsInSecondPosition := password[secondPosition-1] == letter

		if letterAppearsInFirstPosition != letterAppearsInSecondPosition {
			validPasswords++
		}
	}

	return validPasswords
}
