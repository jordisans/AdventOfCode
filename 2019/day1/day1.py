import math

def Part1():
    print("Part 1")
    with open("input.txt", "r") as f:
        fuelNeeded = 0
        for moduleMass in f:
            fuelNeeded += math.trunc(int(moduleMass) / 3) - 2
        print(fuelNeeded)

def Part2():
    print("Part 2")
    with open("input.txt", "r") as f:
        fuelNeeded = 0
        for moduleMass in f:
            fuelForModule = math.trunc(int(moduleMass) / 3) - 2 
            while fuelForModule > 0:
                fuelNeeded += fuelForModule
                fuelForModule = math.trunc(fuelForModule / 3) - 2
        print(fuelNeeded)

Part1()
Part2()