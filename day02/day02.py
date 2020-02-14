with open('./input.txt', 'r') as file:
    str_input = file.read().split(',')

arr = [int(x) for x in str_input]


# PART 1
def intcode(a, index=0):
    opcode = a[index]
    if opcode == 99:
        return a[0]
    num1_index = a[index + 1]
    num2_index = a[index + 2]
    answer_index = a[index + 3]
    if opcode == 1:
        a[answer_index] = a[num1_index] + a[num2_index]
    elif opcode == 2:
        a[answer_index] = a[num1_index] * a[num2_index]
    index += 4
    return intcode(a, index)


arr[1] = 12
arr[2] = 2
print(intcode(arr))

# PART 2
arr2 = [int(x) for x in str_input]
answer = 0
for i in range(100):
    for j in range(100):
        arr3 = arr2.copy()
        arr3[1] = i
        arr3[2] = j
        if intcode(arr3) == 19690720:
            answer = 100 * i + j
            break
    if answer != 0:
        break
print(answer)
