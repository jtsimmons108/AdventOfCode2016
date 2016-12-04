from __future__ import print_function
import itertools
import string

start_file = open('../res/aoc_day_4_input.txt')
instructions = start_file.read().strip().splitlines()

def part_one():
    total = 0
    for line in instructions:
        data = line[:line.rfind('-')].replace('-', '')
        sector = int(line[line.rfind('-') + 1:line.index('[')])
        check = line[line.index('[') + 1:-1]
        counts = []
        for letter in string.lowercase:
            if data.count(letter) > 0:
                counts += [(letter, data.count(letter))]
        counts = sorted(counts, key = lambda x: (-x[1], x[0]))
        result = ''
        for i in range(5):
            result += counts[i][0]
        if result == check:
            total += int(sector)
    return total


def part_two():
    for line in instructions:
        data = line[:line.rfind('-')].replace('-', ' ')
        sector = int(line[line.rfind('-') + 1:line.index('[')])
        shift = sector % 26
        name = ''
        for letter in data:
            if letter != ' ':
                index = (string.lowercase.index(letter) + shift) % 26
                name += string.lowercase[index]
            else:
                name += ' '
        if 'north' in name and 'pole' in name:
            return sector

print('Part one:', part_one())
print('Part two:', part_two())
