from __future__ import print_function
import re

start_file = open('./aoc_day_25_input.txt')
instructions = start_file.read().strip().splitlines()


cpy = re.compile(r'cpy (\d+|[a-d]) (.)')
inc = re.compile(r'inc (.)')
dec = re.compile(r'dec (.)')
jump = re.compile(r'jnz (.) (-?\d+)')
out = re.compile(r'out (.)')

a = 2
found = False
while not found:
    registers = {'a' : a, 'b' : 0, 'c' : 0, 'd' : 0}
    output = ''
    i = 0
    while len(output) < 40:
        line = instructions[i]
        if i == 3:
            registers['d'] += registers['b'] * registers['c']
            registers['b'] = 0
            registers['c'] = 0
            i = 8
        elif i == 10:
            registers['b'] = registers['a'] % 2
            registers['a'] /= 2
            i = 19
        elif jump.match(line):
            reg, amt = jump.findall(line)[0]
            val = int(reg) if reg.isdigit() else registers[reg]
            delta = 1 if val == 0 else int(amt)
            i += delta
        else:
            if cpy.match(line):
                val, reg = cpy.findall(line)[0]
                registers[reg] = int(val) if val.isdigit() else registers[val]
            elif inc.match(line):
                registers[inc.findall(line)[0]] += 1
            elif dec.match(line):
                registers[dec.findall(line)[0]] -= 1
            elif out.match(line):
                output += str(registers[out.findall(line)[0]])
                if len(output) >= 2 and output[-1] == output[-2]:
                    a += 2
                    output = ''
                    break
            else:
                print("This shouldn't happen")
            i += 1
    if len(output) == 40:
        found = True

print('Part 1:', a)
