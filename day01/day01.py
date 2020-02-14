import os
import math
from functools import reduce

filepath = os.path.join('.', 'input.txt')
answer = 0

with open(filepath, 'r') as file_handler:
    values = file_handler.read()
    lines = values.split('\n')
    for line in lines:
        current = int(line)
        answer = answer + math.floor(current / 3) - 2
print(answer)

with open(filepath, 'r') as file_handler:
    values = file_handler.read()
    lines = values.splitlines()


    def getFuel(mass):
        fuel = math.floor(mass / 3) - 2
        return fuel + getFuel(fuel) if fuel > 0 else 0


    answer = reduce(lambda accum, element: accum + getFuel(int(element)), lines, 0)
    print(answer)
