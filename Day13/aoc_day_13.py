from __future__ import print_function
import re
import string
import itertools
from collections import Counter
import time

num = 1364
target_x, target_y = 31, 39

def get_value(x, y):
    if bin((x*x + 3 * x + 2 * x * y + y + y * y) + num)[2:].count('1') % 2 == 0:
        return '.'

    return '#'


values = [['']*40 for _ in range(45)]

for r in range(len(values)):
    for c in range(len(values[0])):
        values[r][c] = get_value(c, r)

values[target_y][target_x] = 'X'


def is_valid(x, y):
    return y in range(len(values)) and x in range(len(values[0])) and values[y][x] in '.X'

for row in values:
    for val in row:
        print(val, end = "  ")
    print()

start_x, start_y = (1, 1)
distances = []
visited = set()
path = []
nodes = 0
def find_path(x, y, seen, day1):
    global nodes
    nodes += 1
    seen.append((x, y))
    visited.add((x,y))
    if day1 and (x, y) == (target_x, target_y):
        distances.append(len(seen))
        if len(seen) == min(distances):
            global path
            path = seen

    if day1 and (len(distances ) == 0 or len(seen) < min(distances)) or len(seen) <= 50 and not day1:
        if is_valid(x + 1, y) and (x + 1, y) not in seen:
            find_path(x + 1, y, seen[::], day1)

        if is_valid(x - 1, y) and (x - 1, y) not in seen:
            find_path(x - 1, y, seen[::], day1)

        if is_valid(x, y + 1) and (x, y + 1) not in seen:
            find_path(x, y + 1, seen[::], day1)

        if is_valid(x, y - 1) and (x, y- 1) not in seen:
            find_path(x, y - 1, seen[::], day1)




day1 = True
find_path(1, 1, [], day1)

if day1:
    print(min(distances))
    for x, y in path:
        values[y][x] = 'O'
else:
    print(len(visited))


for row in values:
    for val in row:
        print(val, end = "  ")
    print()

print(nodes)
