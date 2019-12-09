def IntCodeComputer(noun, verb, initialMemoryState):
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

def GetIntCodeProgramFromFile():
    f = open("input.txt", "r")
    _input = f.read().strip()
    intCodeProgram = list(map(lambda x: int(x), _input.split(",")))
    return intCodeProgram

def Part1():
    intCodeProgram = GetIntCodeProgramFromFile()
    output = IntCodeComputer(12, 2, intCodeProgram)
    print(output)

def Part2():
    intCodeProgram = GetIntCodeProgramFromFile()
    for noun in range(0, 100):
        for verb in range(0, 100):
            print(f"Noun {noun} Verb {verb}")
            output = IntCodeComputer(noun, verb, intCodeProgram)
            if output == 19690720:
                print("Output found")
                print(f"Result {100 * noun + verb}")
                return


Part1()
Part2()