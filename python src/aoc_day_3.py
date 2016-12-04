from __future__ import print_function
import time

start_file = open('../res/aoc_day_3_input.txt')
instructions = [line for line in start_file.read().strip().splitlines()]


def part_one():
    total = 0
    for instruction in instructions:
        sides = sorted([int(x) for x in instruction.split()])
        if sides[0] + sides[1] > sides[2]:
            total += 1
    return total


def part_two():
    total = 0
    for i in range(0, len(instructions), 3):
        first = [int(x) for x in instructions[i].split()]
        second = [int(x) for x in instructions[i + 1].split()]
        third = [int(x) for x in instructions[i + 2].split()]
        for i in range(3):
            sides = sorted([first[i], second[i], third[i]])
            if sides[0] + sides[1] > sides[2]:
                total += 1

    return total


print('Part one:', part_one())
print('Part two:', part_two())

