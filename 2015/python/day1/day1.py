def part1(data):
    floor = 0
    for movement in data:
        floor = floor + 1 if movement == "(" else floor - 1

    print(floor)

def part2(data):
    floor = 0
    for index, movement in enumerate(data):
        floor = floor + 1 if movement == "(" else floor - 1
        if (floor == -1):
            print(index + 1)
            return

f = open("input.txt", "r")

data = f.read()
part1(data)
part2(data)