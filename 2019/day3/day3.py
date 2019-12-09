def GetWiresCoordinates(wireDescription):
    x, y = 0, 0
    wireCoordinates = [(x,y)]
    for wireStep in wireDescription:
        direction = wireStep[0]
        distance = int(wireStep[1:])
        for _ in range(0, distance):
            if direction == "U":
                x += 1
            elif direction == "D":
                x -= 1
            elif direction == "R":
                y += 1
            else:
                y -= 1
            wireCoordinates.append((x, y))
    return wireCoordinates

def GetFrontPanelLayout():
    with open("input.txt", "r") as f:
        firstWire = f.readline().strip().split(",")
        secondWire = f.readline().strip().split(",")

        firstWireCoordinates =  GetWiresCoordinates(firstWire)
        secondWireCoordinates = GetWiresCoordinates(secondWire)
        intersections =  set(firstWireCoordinates) & set(secondWireCoordinates)
        intersections.remove((0,0))

        return firstWireCoordinates, secondWireCoordinates, intersections

def part1():
    _, _, intersections = GetFrontPanelLayout()
    minDistance = 9999

    for intersection in intersections:
        distance = abs(intersection[0]) + abs(intersection[1])
        if distance < minDistance:
            minDistance = distance
    print(minDistance)

def part2():
    firstWireCoordinates, secondWireCoordinates, intersections = GetFrontPanelLayout()
    minSteps = 999999
    for intersection in intersections:
        stepsUntilIntersection = firstWireCoordinates.index(intersection) + secondWireCoordinates.index(intersection)
        if stepsUntilIntersection < minSteps:
            minSteps = stepsUntilIntersection
    print(minSteps)

part1()
part2()