import math
import functools 

def part1():
    print("Part 1")
    with open("input.txt", "r") as f:
        orderSqFeet = 0
        for line in f:
            strl, strw, strh = line.strip().split("x")
            l, w, h = int(strl), int(strw), int(strh)
            paperForSide = [l*w, l*h, w*h]
            orderSqFeet += sum(map(lambda x: x * 2, paperForSide)) + min(paperForSide)
        print(orderSqFeet)


def part2():
    print("Part 2")
    with open("input.txt", "r") as f:
        feetOfRibbon = 0
        for line in f:
            strl, strw, strh = line.strip().split("x")
            sides = [int(strl), int(strw), int(strh)]
            sides.sort()
            shortestSide, secondShortestSide = sides[:2]
            # feetOfRibbon += shortestSide * 2 + secondShortestSide * 2 + functools.reduce(lambda a,b: a*b, sides) alternative to math.prod with reduce
            feetOfRibbon += shortestSide * 2 + secondShortestSide * 2 + math.prod(sides)
        print(feetOfRibbon)

part1()
part2()

