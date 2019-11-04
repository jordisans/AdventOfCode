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
            if move == "^":
                santaY -= 1
            elif move == "v":
                santaY += 1
            elif move == "<":
                santaX -= 1
            else:
                santaX += 1
            location = (santaX, santaY)
            if location not in houses:
                houses[location] = 1
            else:
                houses[location] += 1
            santasTurn = False
        else:
            if move == "^":
                roboSantaY -= 1
            elif move == "v":
                roboSantaY += 1
            elif move == "<":
                roboSantaX -= 1
            else:
                roboSantaX += 1
            location = (roboSantaX, roboSantaY)
            if location not in houses:
                houses[location] = 1
            else:
                houses[location] += 1
            santasTurn = True
    print(len(houses))


f = open("input.txt", "r")

data = f.read()

part1(data)
part2(data)
