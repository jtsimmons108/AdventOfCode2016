from __future__ import print_function
start_file = open('/Users/jeremiahsimmons/Desktop/AOC_2016/res/aoc_day_1_input.txt')
instructions = start_file.read().split(", ")
movements = {0:(0,1), 90: (1, 0), 180: (0, -1), 270: (-1, 0)}

def part_one():
    location = [0,0]
    direction = 0
    for instruction in instructions:
        if instruction[0] == 'R':
            direction += 90
        else:
            direction -= 90
        direction %= 360
        distance = int(instruction[1:])
        location[0] += movements[direction][0] * distance
        location[1] += movements[direction][1] * distance
    return abs(location[0]) + abs(location[1])

def part_two():
    direction = 0
    location = [0,0]
    locations = []
    found = False
    index = 0
    while not found:
        instruction = instructions[index]
        if instruction[0] == 'R':
            direction += 90
        else:
            direction -= 90
        direction %= 360
        distance = int(instruction[1:])
        for i in range(distance):
            location[0] += movements[direction][0]
            location[1] += movements[direction][1]
            if location in locations:
                found = True
                break
            else:
                locations += [location[::]]
        index += 1
    return abs(location[0]) + abs(location[1])

print('Part one answer: ', part_one())
print('Part two answer: ', part_two())
