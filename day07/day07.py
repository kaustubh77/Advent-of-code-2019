import itertools
import queue
import threading

with open('input.txt') as file:
    data = list(file)

for line in data:
    a = [int(x) for x in line.split(',')]


def get_value(a, index, param_num):
    mode = a[index] // (10 * 10 ** param_num)
    val = a[index + param_num]
    if mode % 10 == 0:
        return a[val]
    if mode % 10 == 1:
        return val



def process_program(amplifier_number, a, inqueue, outqueue):
    a = list(a)
    index = 0
    while True:
        opcode = a[index] % 100
        # print(opcode, index)
        if opcode == 1:
            v1 = get_value(a, index, 1)
            v2 = get_value(a, index, 2)
            a[a[index + 3]] = v1 + v2
            index += 4
        elif opcode == 2:
            v1 = get_value(a, index, 1)
            v2 = get_value(a, index, 2)
            a[a[index + 3]] = v1 * v2
            index += 4
        elif opcode == 3:
            x = inqueue.get(True)
            # print(x)
            a[a[index + 1]] = x
            index += 2
        elif opcode == 4:
            # print(get_value(a,index,1))
            outqueue.put(get_value(a, index, 1))
            index += 2
        elif opcode == 5:
            v1 = get_value(a, index, 1)
            if v1:
                index = get_value(a, index, 2)
            else:
                index += 3
        elif opcode == 6:
            v1 = get_value(a, index, 1)
            if not v1:
                index = get_value(a, index, 2)
            else:
                index += 3
        elif a[index] % 100 == 7:
            v1 = get_value(a, index, 1)
            v2 = get_value(a, index, 2)
            a[a[index + 3]] = 1 if v1 < v2 else 0
            index += 4
        elif opcode == 8:
            v1 = get_value(a, index, 1)
            v2 = get_value(a, index, 2)
            a[a[index + 3]] = 1 if v1 == v2 else 0
            index += 4
        elif opcode == 99:
            # print("reached")
            index += 1
            break
    return


def getAnswer(arr):
    max_output = -1000
    for ordering in itertools.permutations(arr):
        # print(ordering)
        queues = [queue.Queue() for i in range(6)]
        for (curr_queue, order) in zip(queues, ordering):
            # print(order)
            curr_queue.put(order)
        queues[0].put(0)
        threads = []
        for index in range(5):
            threads.append(threading.Thread(

                target=process_program, args=(index, a, queues[index], queues[(index + 1) % 5])))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        output = queues[0].get()
        # print(output)
        max_output = max(max_output, output)

    return max_output


# PART 1
print(getAnswer([0, 1, 2, 3, 4]))

# PART 2
print(getAnswer([5, 6, 7, 8, 9]))
