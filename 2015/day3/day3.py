def part1(data):
    print("Part 1")
    x = 0
    y = 0
    houses = { (x, y) : 1 }

    for move in data:
        if move == "^":
            y -= 1
        elif move == "v":
            y += 1
        elif move == "<":
            x -= 1
        else:
            x += 1
        location = (x, y)
        if location not in houses:
            houses[location] = 1
        else:
            houses[location] += 1

    print(len(houses))

def moveSanta(move, x, y, houses):
    if move == "^":
        y -= 1
    elif move == "v":
        y += 1
    elif move == "<":
        x -= 1
    else:
        x += 1
    location = (x, y)
    if location not in houses:
        houses[location] = 1
    else:
        houses[location] += 1
    return x, y

def part2(data):
    print("Part 2")
    santaX = 0
    santaY = 0
    roboSantaX = 0
    roboSantaY = 0
    houses = { (0, 0) : 2 }
    santasTurn = True
    for move in data:
        if santasTurn:
            santaX, santaY = moveSanta(move, santaX, santaY, houses)
            santasTurn = False
        else:
            roboSantaX, roboSantaY = moveSanta(move, roboSantaX, roboSantaY, houses)
            santasTurn = True
    print(len(houses))


f = open("input.txt", "r")

data = f.read()

part1(data)
part2(data)
