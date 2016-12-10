from __future__ import print_function
import time
import re

start_file = open('../res/aoc_day_9_input.txt')
instruction = start_file.read().strip()


def split_pieces(input):
    pieces = []
    start = 0
    while input.find('(', start) > -1:
        op, end = input.find('(', start), input.find(')', start)
        if op != start:
            pieces.append(input[start:op])
        length = int(input[op+1:input.find('x', op)])
        pieces.append(input[op:end + length + 1])
        start = end + length + 1
    if start != len(input):
        pieces.append(input[start:])
    return pieces


def get_decompressed_length(piece):
    if '(' not in piece:
        return len(piece)
    return int(piece[piece.find('x') + 1:piece.find(')')]) * sum(map(get_decompressed_length, split_pieces(piece[piece.index(')') +1:])))


def decompress_part_one(val):
    vals = split_pieces(val)
    total = 0
    for piece in vals:
        if '(' not in piece:
            total += len(piece)
        else:
            m = re.match('\((\d+)x(\d+)\)', piece)
            total += int(m.group(1)) * int(m.group(2))
    return total


def decompress_part_two(instruction):
    return sum(map(get_decompressed_length, split_pieces(instruction)))


print('Part One', decompress_part_one(instruction))
print('Part Two', decompress_part_two(instruction))
