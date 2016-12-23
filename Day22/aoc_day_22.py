from __future__ import print_function
import itertools
import re
from collections import deque, Counter


class Node(object):
    def __init__(self, x, y, size, avail, used, percent):
        self.x = x
        self.y = y
        self.size = size
        self.avail = avail
        self.used = used
        self.percent = percent


    def __str__(self):
        return '{}T / {}T'.format(self.used, self.size)

    def is_viable_with(self, other):
        return self.used > 0 and self.used <= other.avail



def get_open_path(start_x, start_y, data_x, data_y):
    paths = deque([[(start_x, start_y)]])
    while paths:
        curr_path = paths.popleft()
        c_x, c_y = curr_path[-1]
        neighbors = [loc for loc in grid[c_y][c_x].get_neighbor_locations() if loc != (data_x, data_y)]
        for n in neighbors:
            if grid[c_y][c_x].is_viable_with(grid[n[1]][n[0]]):
                return curr_path + [n]
            elif grid[c_y][c_x].used <= grid[n[1]][n[0]].size and n not in curr_path:
                paths.append(curr_path + [n])

def print_grid():
    for row in grid:
        for n in row:
            if (n.x, n.y) == (0, 0):
                ch = 'G'
            elif (n.x, n.y) == (31, 0):
                ch = 'D'
            elif n.used == 0:
                ch = 'E'
            elif n.size < 100:
                ch = '.'
            else:
                ch = 'x'
            print(ch + '  ', end = '')
        print()
    print()

start_file = open('./aoc_day_22_input.txt')
instructions = start_file.read().strip().splitlines()
grid = []
#/dev/grid/node-x0-y0     88T   67T    21T   76%
node = re.compile(r'/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)\%')
nodes = []
for instruction in instructions:
    if len(node.findall(instruction)) > 0:
        x, y, s, u, a, p = map(int, node.findall(instruction)[0])
        if y == len(grid):
            grid.append([])
        grid[y].append(Node(x, y, s, a, u, p))

#Solve By Hand
print_grid()





