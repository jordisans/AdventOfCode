with open("input.txt", "r") as file:
    x, y = 0, 0
    frontPanel = { (x, y): 0 }
    minDistance = 9999
    wireId = 0
    for wirePath in file:
        x, y = 0, 0
        wireSteps = wirePath.strip().split(",")
        for wireStepDefinition in wireSteps:
            direction = wireStepDefinition[0] 
            distance = int(wireStepDefinition[1:])
            for _ in range(0, distance):
                if direction == "U":
                    x += 1
                elif direction == "D":
                    x -= 1
                elif direction == "R":
                    y += 1
                else:
                    y -= 1
            
                if  (x, y) in frontPanel and frontPanel[(x, y)] != wireId and (x, y) != (0, 0):
                    frontPanel[(x, y)] = "X"
                    distance = abs(x) + abs(y)
                    if distance < minDistance:
                        minDistance = distance
                else:
                    frontPanel[(x, y)] = wireId
        wireId += 1

    print(minDistance)
