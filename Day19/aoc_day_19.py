from __future__ import print_function
import matplotlib.pyplot as plt
from collections import deque

num = 3014387

def part_one(num):
    elves = range(1, num + 1)
    while len(elves) > 1:
        if len(elves) % 2 != 0:
            elves = elves[::2]
            elves = elves[-1:] + elves[:-1]
        else:
            elves = elves[::2]
    return elves[0]

# Modified after reading /r/adventofcode
# originally solved by looking at patterns of smaller values of n
def part_two(num):
    elves = range(1, num + 1)
    left = deque(elves[:len(elves)/2])
    right = deque(elves[len(elves)/2:])
    while left:
        right.popleft()
        if len(left) == len(right):
            left.append(right.popleft())
        right.append(left.popleft())

    return right[0]

print('Part one:', part_one(3014387))
print('Part two:', part_two(3014387))
