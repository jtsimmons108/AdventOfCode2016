from __future__ import print_function
import itertools

start_file = open('./aoc_day_21_input.txt')
instructions = start_file.read().strip().splitlines()

def swap(x, y, word):
    word = list(word)
    temp = word[x]
    word[x] = word[y]
    word[y] = temp
    return ''.join(word)

def swap_letters(x, y, word):
    return word.replace(x, '?').replace(y, x).replace('?', y)

def rotate(direction, distance, word):
    distance %= len(word)
    if direction == 'right':
        return word[-distance:] + word[:-distance]
    else:
        return word[distance:] + word[:distance]

def rotate_position(letter, word):
    index = word.find(letter)
    distance = index + 2 if index >= 4 else index + 1
    return rotate('right', distance, word)

def reverse_positions(x, y, word):
    return word[:x] + word[x:y+1][::-1] + word[y+1:]

def move_position(x, y, word):
    letter = word[x]
    word = word[:x] + word[x+1:]
    return word[:y] + letter + word[y:]

first = 'abcdefgh'

for start in itertools.permutations(first):
    begin = ''.join(start)
    start = ''.join(start)
    for instruction in instructions:
        info = instruction.split()
        if info[0] == 'swap':
            if info[1] == 'position':
                start = swap(int(info[2]), int(info[-1]), start)
            else:
                start = swap_letters(info[2], info[-1], start)
        elif info[0] == 'rotate':
            if info[1] == 'based':
                start = rotate_position(info[-1], start)
            else:
                start = rotate(info[1], int(info[2]), start)
        elif info[0] == 'reverse':
            start = reverse_positions(int(info[2]), int(info[-1]), start)
        elif info[0] == 'move':
            start = move_position(int(info[2]), int(info[-1]), start)
        else:
            print('this shouldn\'t happen')
    if begin == first:
        print('Part 1:', start)
    if start == 'fbgdceah':
        print('Part 2:', begin)
        exit()
