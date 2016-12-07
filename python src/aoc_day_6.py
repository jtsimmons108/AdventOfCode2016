from __future__ import print_function
from collections import Counter
import time

start = time.time()
start_file = open('../res/aoc_day_6_input.txt')
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

print(time.time() - start)
print(result1)
print(result2)
