def part1(data):
    print("Part 1")

def part2(data):
    print("Part 2")

# part1(data)
# part2(data)

with open("input.txt", "r") as f:
    orderSqFeet = 0
    for line in f:
        strl, strw, strh = line.strip().split("x")
        l, w, h = int(strl), int(strw), int(strh)
        paperForSide = [l*w, l*h, w*h]
        orderSqFeet += sum(map(lambda x: x * 2, paperForSide)) + min(paperForSide)
    print(orderSqFeet)
        