package lib

import (
	"bufio"
	"os"
	"strconv"
)

// ReadLines reads the file described in path and returns each line as a string
func ReadLines(path string) []string {
	file, err := os.Open(path)
	defer file.Close()
	check(err)

	scanner := bufio.NewScanner(file)
	var lines []string

	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	return lines
}

// ReadLinesAsInt reads the file described in path and returns each line as an int
func ReadLinesAsInt(path string) []int64 {
	file, err := os.Open(path)
	defer file.Close()
	check(err)

	scanner := bufio.NewScanner(file)
	var lines []int64

	for scanner.Scan() {
		parsedInt, err := strconv.ParseInt(scanner.Text(), 10, 64)
		check(err)
		lines = append(lines, parsedInt)
	}

	return lines

}

func check(e error) {
	if e != nil {
		panic(e)
	}
}
