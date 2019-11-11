import hashlib


def findHashWithStartingString(startingStringToFind):
    key = "iwrupvqb"
    n = 1
    while True:
        x = key + str(n)
        result = hashlib.md5(x.encode())
        if not result.hexdigest().startswith(startingStringToFind):
            n +=1
            continue
        
        print(result.hexdigest())
        print(n)
        break

def part1():
    findHashWithStartingString("00000")

def part2():
    findHashWithStartingString("000000")

part1()
part2()
