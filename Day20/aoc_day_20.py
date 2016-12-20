from __future__ import print_function
import re


start_file = open('./aoc_day_20_input.txt')
instructions = start_file.read().strip().splitlines()

nums = re.compile(r'(\d+)-(\d+)')
all_nums = []
for instruction in instructions:
    all_nums.append(map(int, nums.findall(instruction)[0]))

all_nums = sorted(all_nums, key = lambda x: x[0])
low, high = all_nums[0]
allowed = 0
first = True
for l, h in all_nums:
    if l <= high + 1:
        if h > high:
            high = h
    else:
         if first:
             print('Part1:', high + 1)
             first = False
         allowed += (l - (high + 1))
         low, high = l, h

print('Part 2:', allowed)