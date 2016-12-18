from __future__ import print_function
from collections import deque
from hashlib import md5

start = 'qzthpkfp'
open_doors = 'bcdef'
moves = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}


class Maze(object):

    def __init__(self, r, c, path):
        self.r, self.c = r, c
        self.path = path

    def get_possible_moves(self):
        up, down, left, right = md5(start + ''.join(self.path)).hexdigest()[:4]
        possible_moves = []
        if up in open_doors:
            possible_moves.append('U')
        if down in open_doors:
            possible_moves.append('D')
        if left in open_doors:
            possible_moves.append('L')
        if right in open_doors:
            possible_moves.append('R')
        return possible_moves

    def is_valid(self):
        return self.r in range(4) and self.c in range(4)


states = deque([Maze(0, 0, [])])
paths = []

while states:
    curr_maze = states.popleft()
    if curr_maze.r == 3 and curr_maze.c == 3:
        if len(paths) == 0:
            print(''.join(curr_maze.path))
        paths.append(''.join(curr_maze.path))
        continue
    for move in curr_maze.get_possible_moves():
        new_r, new_c = map(sum, zip((curr_maze.r, curr_maze.c), moves[move]))
        new_maze = Maze(new_r, new_c, curr_maze.path + [move])
        if new_maze.is_valid():
            states.append(Maze(new_r, new_c, curr_maze.path + [move]))

print(max(map(len, paths)))