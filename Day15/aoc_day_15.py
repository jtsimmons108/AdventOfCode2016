from __future__ import print_function
import re


start_file = open('./aoc_day_15_input.txt')
instructions = start_file.read().strip().splitlines()
reg = r'\d+'
discs = [0] * len(instructions)

def rotate(lst, amt):
    if amt != 0:
        amt %= len(lst)
    return lst[amt:] + lst[:amt]

for instruction in instructions:
    disc, num_positions, time, start = re.findall(reg, instruction)
    discs[int(disc) - 1] = rotate([i for i in range(int(num_positions))], int(start))

found = False
i = 0
while not found:
    passed = True
    for j in range(len(instructions)):
        if rotate(discs[j], i + j + 1)[0] != 0:
            passed = False
    if passed:
        print(i)
        found = True
    i += 1






