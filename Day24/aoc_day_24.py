from __future__ import print_function
import itertools
from collections import deque
import os
import time

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
    return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != '#'

def print_grid(steps):
    for row in grid:
        print(''.join(row))
    print('Steps:', steps)

for place, loc in locations.items():
    paths = deque([[loc]])
    seen = set()
    seen.add(loc)
    while paths:
        curr_path = paths.popleft()
        r, c = curr_path[-1]
        if (r, c) in locations.values() and len(curr_path) > 1:
            lengths[(place, int(grid[r][c]))] = (len(curr_path) - 1, curr_path)
            continue
        for dr, dc in moves:
            if can_move(r + dr, c + dc) and (r + dr, c + dc) not in seen:
                paths.append(curr_path + [(r + dr, c + dc)])
                seen.add((r + dr, c + dc))

for path in itertools.permutations(range(1, 8)):
    path = (0,) + path + (0,)
    distance = 0
    for i in range(len(path) - 2):
        distance += lengths[(path[i], path[i+1])][0]
    distances1.append((distance, path[:-1]))
    distances2.append((distance + lengths[(path[-2], path[-1])][0], path))

print('Part1:', min(distances1))
print('Part2:', min(distances2))

#Visualization
# for r, c in locations.values():
#     grid[r][c] = '\033[31m' + grid[r][c] + '\033[37m'
# steps = 0
# path = min(distances1)[1]
# for i in range(len(path)-1):
#     one, two = path[i], path[i+1]
#     curr_path = lengths[(one, two)][1][1:-1]
#     r, c = locations[one]
#     grid[r][c] = '\033[32m' + str(one) + '\033[37m'
#     for i in range(len(curr_path)):
#         steps += 1
#         cr, cc = curr_path[i]
#         grid[cr][cc] = '\033[32m' + '@' + '\033[37m'
#         if i > 0:
#             pr, pc = curr_path[i - 1]
#             grid[pr][pc] = '.'
#         os.system('clear')
#         print_grid(steps)
#         time.sleep(.05)
#         if i == len(curr_path) - 1:
#             steps += 1
#             grid[cr][cc] = '.'
#             os.system('clear')
#             print_grid(steps)
#     r, c = locations[two]
#     grid[r][c] = '\033[32m' + str(two) + '\033[37m'
#     os.system('clear')
#     print_grid(steps)
