from __future__ import print_function
import re

start_file = open('../res/aoc_day_10_input.txt')
instructions = start_file.read().strip().splitlines()

bots = {}
outputs = {}
reg1 = r'value (\d+) goes to bot (\d+)'
reg2 = r'bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)'

i = 0
while len(instructions) > 0:
    if i >= len(instructions):
        i = 0
    instruction = instructions[i]
    if re.match(reg1, instruction):
        val, bot = map(int, re.findall(reg1, instruction)[0])
        if bot not in bots:
            bots[bot] = []
        bots[bot].append(val)
        del instructions[i]
    else:
        bot, which1, to1, which2, to2 = re.findall(reg2, instruction)[0]
        bot, to1, to2 = int(bot), int(to1), int(to2)
        if bot in bots and len(bots[bot]) == 2:
            val1 = min(bots[bot])
            val2 = max(bots[bot])
            if val1 == 17 and val2 == 61:
                print('Answer to Part 1:',bot)
            bots[bot].remove(val1)
            bots[bot].remove(val2)
            if which1 == 'bot':
                if to1 not in bots:
                    bots[to1] = []
                bots[to1].append(val1)
            else:
                if to1 not in outputs:
                    outputs[to1] = []
                outputs[to1].append(val1)
            if which2 == 'bot':
                if to2 not in bots:
                    bots[to2] = []
                bots[to2].append(val2)
            else:
                if to2 not in outputs:
                    outputs[to2] = []
                outputs[to2].append(val2)
            del instructions[i]
        else:
            i = (i + 1) % len(instructions)

print('Answer to Part 2:', outputs[0][0] * outputs[1][0] * outputs[2][0])

