import itertools

with open('input.txt') as file:
    data = list(file)

for line in data:
    prog = [int(x) for x in line.split(',')]


def get_value(prog, index, param_num):
    mode = prog[index] // (10 * 10 ** param_num)
    val = prog[index + param_num]
    if mode % 10 == 0:
        return prog[val]
    if mode % 10 == 1:
        return val


def process_program2(amplifier_number, prog, x):
    prog = list(prog)
    index = 0
    while True:
        opcode = prog[index] % 100
        if opcode == 1:
            v1 = get_value(prog, index, 1)
            v2 = get_value(prog, index, 2)
            prog[prog[index + 3]] = v1 + v2
            index += 4
        elif opcode == 2:
            v1 = get_value(prog, index, 1)
            v2 = get_value(prog, index, 2)
            prog[prog[index + 3]] = v1 * v2
            index += 4
        elif opcode == 3:
            prog[prog[index + 1]] = x
            index += 2
        elif opcode == 4:
            x = get_value(prog, index, 1)
            index += 2
        elif opcode == 5:
            v1 = get_value(prog, index, 1)
            if v1:
                index = get_value(prog, index, 2)
            else:
                index += 3
        elif opcode == 6:
            v1 = get_value(prog, index, 1)
            if not v1:
                index = get_value(prog, index, 2)
            else:
                index += 3
        elif prog[index] % 100 == 7:
            v1 = get_value(prog, index, 1)
            v2 = get_value(prog, index, 2)
            prog[prog[index + 3]] = 1 if v1 < v2 else 0
            index += 4
        elif opcode == 8:
            v1 = get_value(prog, index, 1)
            v2 = get_value(prog, index, 2)
            prog[prog[index + 3]] = 1 if v1 == v2 else 0
            index += 4
        elif opcode == 99:
            index += 1
            break
        else:
            break
    return x


def getAnswer2(arr):
    max_output = -1000
    for ordering in itertools.permutations(arr):
        x = 0
        for i in range(5):
            x = process_program2(0, prog, ordering[i])
        max_output = max(max_output, x)
    return max_output


# PART 1
print(getAnswer2([0, 1, 2, 3, 4]))

# PART 2
print(getAnswer2([5, 6, 7, 8, 9]))
