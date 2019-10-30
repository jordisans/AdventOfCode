f = open("input.txt", "r")

data = f.read()

floor = 0
for movement in data:
    floor = floor + 1 if movement == "(" else floor - 1

print(floor)