with open('./input.txt', 'r') as _file:
    strInputs = _file.read().split(',')

arr = list(map(lambda str: int(str), strInputs))


def get_mode(first):
    opcode = first % 100
    modes = [int(d) for d in str(int(first / 100))]
    modes = [0] * (3 - len(modes)) + modes
    return opcode, modes[::-1]


def get_value(program, index, immediate):
    if immediate:
        return program[index]
    else:
        return program[program[index]]


def process_program(program, inputValue):
    index = 0
    opcode = 0
    while program[index] != 99:
        opcode, modes = get_mode(program[index])

        if opcode == 99:
            print(program[0])
            break
        elif opcode == 1:
            v1 = get_value(program, index + 1, modes[0])
            v2 = get_value(program, index + 2, modes[1])
            destination = program[index + 3]
            program[destination] = v1 + v2
            index += 4
        elif opcode == 2:
            v1 = get_value(program, index + 1, modes[0])
            v2 = get_value(program, index + 2, modes[1])
            destination = program[index + 3]
            program[destination] = v1 * v2
            index += 4
        elif opcode == 3:
            destination = program[index + 1]
            program[destination] = inputValue
            index += 2
        elif opcode == 4:
            v1 = get_value(program, index + 1, modes[0])
            print(v1)
            index += 2
        elif opcode == 5:
            v1 = get_value(program, index + 1, modes[0])
            v2 = get_value(program, index + 2, modes[1])
            if v1 != 0:
                index = v2
            else:
                index += 3
        elif opcode == 6:
            v1 = get_value(program, index + 1, modes[0])
            v2 = get_value(program, index + 2, modes[1])
            if v1 == 0:
                index = v2
            else:
                index += 3
        elif opcode == 7:
            v1 = get_value(program, index + 1, modes[0])
            v2 = get_value(program, index + 2, modes[1])
            destination = program[index + 3]
            program[destination] = int(v1 < v2)
            index += 4
        elif opcode == 8:
            v1 = get_value(program, index + 1, modes[0])
            v2 = get_value(program, index + 2, modes[1])
            destination = program[index + 3]
            program[destination] = int(v1 == v2)
            index += 4


# PART 1
process_program(arr.copy(), 1)

# PART 2
process_program(arr.copy(), 5)
