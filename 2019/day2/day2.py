def intCodeComputer(noun, verb, initialMemoryState):
    intCodeProgram = initialMemoryState.copy()
    intCodeProgram[1] = noun
    intCodeProgram[2] = verb
    intructionPointer = 0
    haltNotReached = True
    while haltNotReached:
        opCode = intCodeProgram[intructionPointer]
        if opCode == 1:
            firstOperandIndex = intCodeProgram[intructionPointer + 1]
            secondOperandIndex = intCodeProgram[intructionPointer + 2]
            resultIndex = intCodeProgram[intructionPointer + 3]
            intCodeProgram[resultIndex] = intCodeProgram[firstOperandIndex] + intCodeProgram[secondOperandIndex]
            
            intructionPointer += 4
        elif opCode == 2:
            firstOperandIndex = intCodeProgram[intructionPointer + 1]
            secondOperandIndex = intCodeProgram[intructionPointer + 2]
            resultIndex = intCodeProgram[intructionPointer + 3]
            intCodeProgram[resultIndex] = intCodeProgram[firstOperandIndex] * intCodeProgram[secondOperandIndex]
            
            intructionPointer += 4
        elif opCode == 99:
            haltNotReached = False
        else:
            print(f"Invalid opcode {opCode}")
    return intCodeProgram[0]

def getIntCodeProgramFromFile():
    f = open("input.txt", "r")
    _input = f.read().strip()
    intCodeProgram = list(map(lambda x: int(x), _input.split(",")))
    return intCodeProgram

def part1():
    intCodeProgram = getIntCodeProgramFromFile()
    output = intCodeComputer(12, 2, intCodeProgram)
    print(output)

def part2():
    intCodeProgram = getIntCodeProgramFromFile()
    for noun in range(0, 100):
        for verb in range(0, 100):
            print(f"Noun {noun} Verb {verb}")
            output = intCodeComputer(noun, verb, intCodeProgram)
            if output == 19690720:
                print("Output found")
                print(f"Result {100 * noun + verb}")
                return


part1()
part2()