from __future__ import print_function
import string
import re
from collections import Counter

start_file = open('../res/aoc_day_4_input.txt')
instructions = start_file.read().strip().splitlines()
pattern = r'([a-z-]+)-(\d+)\[([a-z]+)\]'
def part_one():
    total = 0
    for line in instructions:
        data, sector, check = re.findall(pattern, line)[0]
        data = data.replace('-','')
        counts = sorted(Counter(data).most_common(), key = lambda x: (-x[1], x[0]))[:5]
        result = ''.join([l for (l,c) in counts])
        if result == check:
            total += int(sector)
    return total


def part_two():
    for line in instructions:
        data, sector, check = re.findall(pattern, line)[0]
        data = data.replace('-', ' ')
        name = ''
        for letter in data:
            if letter != ' ':
                name += string.lowercase[(string.lowercase.index(letter) + int(sector)) % 26]
            else:
                name += ' '
        if 'north' in name and 'pole' in name:
            return sector

print('Part one:', part_one())
print('Part two:', part_two())
