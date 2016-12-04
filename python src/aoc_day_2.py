from __future__ import print_function
start_file = open('/Users/jeremiahsimmons/Desktop/AOC_2016/res/aoc_day_2_input.txt')
instructions = start_file.read().strip().splitlines()

directions = {'D': (1,0), 'U': (-1, 0), 'L':(0, -1), 'R':(0, 1)}

def part_one():
    r, c = 1,1
    result = ''
    keypad = [[1,2,3], [4,5,6], [7,8,9]]
    for instruction in instructions:
        for letter in instruction:
            temp_r = r + directions[letter][0]
            temp_c = c + directions[letter][1]
            if temp_r in range(3) and temp_c in range(3):
                 r, c = temp_r, temp_c
        result += str(keypad[r][c])
    return result

def part_two():
    r, c = 2,0
    result = ''
    keypad = [[0,0,1,0,0], [0,2,3,4,0], [5,6,7,8,9], [0,'A', 'B', 'C', 0], [0,0,'D',0,0]]
    for instruction in instructions:
        for letter in instruction:
            temp_r = r + directions[letter][0]
            temp_c = c + directions[letter][1]
            if temp_r in range(5) and temp_c in range(5) and keypad[temp_r][temp_c] != 0:
                 r, c = temp_r, temp_c
        result += str(keypad[r][c])
    return result



print('Part one --> ', part_one())
print('Part two --> ', part_two())
