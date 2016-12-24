from __future__ import print_function
import itertools
from collections import deque


start_file = open('./aoc_day_24_input.txt')
grid = [list(line) for line in start_file.read().strip().splitlines()]
locations = {}
lengths = {}
distances1 = []
distances2 = []
moves  = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c].isdigit():
            locations[int(grid[r][c])] = (r, c)


def can_move(r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] in '.01234567'


for place, loc in locations.items():
    paths = deque([[loc]])
    seen = set()
    seen.add(loc)
    while paths:
        curr_path = paths.popleft()
        r, c = curr_path[-1]
        if (r, c) in locations.values() and len(curr_path) > 1:
            lengths[(place, int(grid[r][c]))] = len(curr_path) - 1
            continue
        for dr, dc in moves:
            if can_move(r + dr, c + dc) and (r + dr, c + dc) not in seen:
                paths.append(curr_path + [(r + dr, c + dc)])
                seen.add((r + dr, c + dc))


for path in itertools.permutations(range(1, 8)):
    path = (0,) + path + (0,)
    distance = 0
    for i in range(len(path) - 2):
        distance += lengths[(path[i], path[i+1])]
    distances1.append(distance)
    distances2.append(distance + lengths[(path[-2], path[-1])])

print('Part1:', min(distances1))
print('Part2:', min(distances2))
