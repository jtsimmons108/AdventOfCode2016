from __future__ import print_function
from collections import Counter
import time

start_file = open('./aoc_day_6_input.txt')
instructions = start_file.read().strip().splitlines()

words = {}
for line in instructions:
    for i in range(len(line)):
        words.setdefault(i, [])
        words[i].append(line[i])

result1 = ''
result2 = ''
for i in words.keys():
    result1 += Counter(words[i]).most_common()[0][0]
    result2 += Counter(words[i]).most_common()[-1][0]

print('Part 1:', result1)
print('Part 2:', result2)
