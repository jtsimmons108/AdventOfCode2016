from __future__ import print_function
import itertools
import re
from collections import deque, Counter


start_file = open('./aoc_day_24_input.txt')
grid = [list(line) for line in start_file.read().strip().splitlines()]
locs = {}
lengths = {}
distances1 = []
distances2 = []

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c].isdigit():
            locs[int(grid[r][c])] = (r, c)


def can_move(r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and (grid[r][c] == '.' or grid[r][c] in '01234567')


for place, loc in locs.items():
    paths = deque([[loc]])
    seen = set()
    seen.add(loc)
    while paths:
        curr_path = paths.popleft()
        r, c = curr_path[-1]
        if (r, c) in locs.values() and len(curr_path) > 1:
            lengths[(place, int(grid[r][c]))] = len(curr_path) - 1
            continue
        if can_move(r + 1, c) and (r + 1, c) not in seen:
            paths.append(curr_path + [(r+1, c)])
            seen.add((r + 1, c))
        if can_move(r -1, c) and (r - 1, c) not in seen:
            paths.append(curr_path + [(r - 1, c)])
            seen.add((r - 1, c))
        if can_move(r, c + 1) and (r, c + 1) not in seen:
            paths.append(curr_path + [(r, c + 1)])
            seen.add((r, c + 1))
        if can_move(r, c - 1) and (r, c - 1) not in seen:
            paths.append(curr_path + [(r, c - 1)])
            seen.add((r, c-1))


for path in itertools.permutations(range(1, 8)):
    path = (0,) + path + (0,)
    distance = 0
    for i in range(len(path) - 2):
        distance += lengths[(path[i], path[i+1])]
    distances1.append(distance)
    distances2.append(distance + lengths[(path[-2], path[-1])])

print('Part1:', min(distances1))
print('Part2:', min(distances2))
