from __future__ import print_function
import re
import time

start_file = open('./aoc_day_10_input.txt')
instructions = start_file.read().strip().splitlines()

start = time.time()
bins = {'bot':{}, 'output':{}}

reg1 = r'value (\d+) goes to bot (\d+)'
reg2 = r'bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)'

i = 0
while len(instructions) > 0:
    i %= len(instructions)
    instruction = instructions[i]
    if re.match(reg1, instruction):
        val, bot = map(int, re.findall(reg1, instruction)[0])
        if bot not in bins['bot']:
            bins['bot'][bot] = []
        bins['bot'][bot].append(val)
        if len(bins['bot'][bot]) == 2:
            print(bot)
        del instructions[i]
    else:
        bot, which1, to1, which2, to2 = re.findall(reg2, instruction)[0]
        bot, to1, to2 = map(int, (bot, to1, to2))
        if bot in bins['bot'] and len(bins['bot'][bot]) == 2:
            val1 = min(bins['bot'][bot])
            val2 = max(bins['bot'][bot])
            if val1 == 17 and val2 == 61:
                print('Answer to Part 1:', bot)
            bins['bot'][bot].remove(val1)
            bins['bot'][bot].remove(val2)
            if to1 not in bins[which1]:
                bins[which1][to1] = []
            bins[which1][to1].append(val1)
            if to2 not in bins[which2]:
                bins[which2][to2] = []
            bins[which2][to2].append(val2)
            del instructions[i]
        else:
            i = (i + 1) % len(instructions)
print(time.time() - start)
print('Answer to Part 2:', bins['output'][0][0] * bins['output'][1][0] * bins['output'][2][0])

