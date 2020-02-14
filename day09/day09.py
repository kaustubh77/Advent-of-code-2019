def get_opcode(num):
    digits = [0, 0, 0, 0, 0]
    pos = len(digits) - 1
    while num > 0 and pos >= 0:
        digits[pos] = num % 10
        num //= 10
        pos -= 1
    return digits


def get_value(input, index, mode, offset, rel_base):
    if mode == 0:
        return input[index + offset]
    if mode == 1:
        return index + offset
    if mode == 2:
        return rel_base + input[index + offset]


with open('input.txt') as f:
    a = list(map(int, f.read().split(',')))


def run(input, input_id):
    answer = 0
    index = 0
    rel_base = 0
    a = [0] * 100000
    for pos, intcode in enumerate(input):
        a[pos] = intcode
    while index < len(input):
        opcode_obj = get_opcode(a[index])
        opcode = opcode_obj[3] * 10 + opcode_obj[4]
        op1_mode = opcode_obj[2]
        op2_mode = opcode_obj[1]
        op3_mode = opcode_obj[0]

        if opcode == 1:
            v1 = a[get_value(a, index, op1_mode, 1, rel_base)]
            v2 = a[get_value(a, index, op2_mode, 2, rel_base)]
            a[get_value(a, index, op3_mode, 3, rel_base)] = v1 + v2
            index += 4
        elif opcode == 2:
            v1 = a[get_value(a, index, op1_mode, 1, rel_base)]
            v2 = a[get_value(a, index, op2_mode, 2, rel_base)]
            a[get_value(a, index, op3_mode, 3, rel_base)] = v1 * v2
            index += 4
        elif opcode == 3:
            a[get_value(a, index, op1_mode, 1, rel_base)] = input_id
            index += 2
        elif opcode == 4:
            v1 = a[get_value(a, index, op1_mode, 1, rel_base)]
            answer = v1
            index += 2
        elif opcode == 5:
            v1 = a[get_value(a, index, op1_mode, 1, rel_base)]
            v2 = a[get_value(a, index, op2_mode, 2, rel_base)]
            index = v2 if (v1 != 0) else index + 3
        elif opcode == 6:
            v1 = a[get_value(a, index, op1_mode, 1, rel_base)]
            v2 = a[get_value(a, index, op2_mode, 2, rel_base)]
            index = v2 if (v1 == 0) else index + 3
        elif opcode == 7:
            v1 = a[get_value(a, index, op1_mode, 1, rel_base)]
            v2 = a[get_value(a, index, op2_mode, 2, rel_base)]
            a[get_value(a, index, op3_mode, 3, rel_base)] = 1 if v1 < v2 else 0
            index += 4
        elif opcode == 8:
            v1 = a[get_value(a, index, op1_mode, 1, rel_base)]
            v2 = a[get_value(a, index, op2_mode, 2, rel_base)]
            a[get_value(a, index, op3_mode, 3, rel_base)] = 1 if v1 == v2 else 0
            index += 4
        elif opcode == 9:
            rel_base += a[get_value(a, index, op1_mode, 1, rel_base)]
            index += 2
        elif opcode == 99:
            break
    return answer


# PART 1
print(run(a, 1))

# PART 2
print(run(a, 2))
