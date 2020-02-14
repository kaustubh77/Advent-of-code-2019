with open('./input.txt', 'r') as _file:
    strInputs = _file.read().split(',')

arr = list(map(lambda str: int(str), strInputs))


def get_mode(first):
    opcode = first % 100
    modes = [int(d) for d in str(int(first / 100))]
    modes = [0] * (3 - len(modes)) + modes
    return opcode, modes[::-1]


def get_value(a, index, immediate):
    if immediate:
        return a[index]
    else:
        return a[a[index]]


def process_program(a, inputValue):
    index = 0
    opcode = 0
    while a[index] != 99:
        opcode, modes = get_mode(a[index])

        if opcode == 99:
            print(a[0])
            break
        elif opcode == 1:
            v1 = get_value(a, index + 1, modes[0])
            v2 = get_value(a, index + 2, modes[1])
            destination = a[index + 3]
            a[destination] = v1 + v2
            index += 4
        elif opcode == 2:
            v1 = get_value(a, index + 1, modes[0])
            v2 = get_value(a, index + 2, modes[1])
            destination = a[index + 3]
            a[destination] = v1 * v2
            index += 4
        elif opcode == 3:
            destination = a[index + 1]
            a[destination] = inputValue
            index += 2
        elif opcode == 4:
            v1 = get_value(a, index + 1, modes[0])
            print(v1)
            index += 2
        elif opcode == 5:
            v1 = get_value(a, index + 1, modes[0])
            v2 = get_value(a, index + 2, modes[1])
            if v1 != 0:
                index = v2
            else:
                index += 3
        elif opcode == 6:
            v1 = get_value(a, index + 1, modes[0])
            v2 = get_value(a, index + 2, modes[1])
            if v1 == 0:
                index = v2
            else:
                index += 3
        elif opcode == 7:
            v1 = get_value(a, index + 1, modes[0])
            v2 = get_value(a, index + 2, modes[1])
            destination = a[index + 3]
            a[destination] = int(v1 < v2)
            index += 4
        elif opcode == 8:
            v1 = get_value(a, index + 1, modes[0])
            v2 = get_value(a, index + 2, modes[1])
            destination = a[index + 3]
            a[destination] = int(v1 == v2)
            index += 4


# PART 1
process_program(arr.copy(), 1)

# PART 2
process_program(arr.copy(), 5)

