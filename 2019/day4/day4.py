def HasRepeatedNumberPart1(password):
    compareTo = "-1"
    for digit in password:
        if compareTo == digit:
            return True
        else:
            compareTo = digit
    return False

def HasRepeatedNumberPart2(password):
    compareTo = "-1"
    repeatedNumInstances = 1
    for digit in password:
        if compareTo == digit:
            repeatedNumInstances += 1
        else:
            if repeatedNumInstances == 2:
                return True
            repeatedNumInstances = 1
            compareTo = digit
    
    return True if repeatedNumInstances == 2 else False

def NeverDecreases(password):
    compareTo = "0"
    for digit in password:
        if compareTo > digit:
            return False
        compareTo = digit
    return True

def Part1Rules(password):
    return HasRepeatedNumberPart1(password) and NeverDecreases(password)

def Part2Rules(password):
    return HasRepeatedNumberPart2(password) and NeverDecreases(password)

def Part1():
    startRange = 248345
    endRange = 746315 
    validPasswords = 0

    for password in range(startRange, endRange + 1):
        password = str(password)
        if Part1Rules(password):
            validPasswords += 1

    print(validPasswords)

def Part2():
    startRange = 248345
    endRange = 746315 
    validPasswords = 0

    for password in range(startRange, endRange + 1):
        password = str(password)
        if Part2Rules(password):
            validPasswords += 1

    print(validPasswords)

Part1()
Part2()
