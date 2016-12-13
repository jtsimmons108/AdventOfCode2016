from __future__ import print_function
import re


start_file = open('./aoc_day_12_input.txt')
instructions = start_file.read().strip().splitlines()

#Change c to 1 for part 2
registers = {'a' : 0, 'b' : 0, 'c' : 1, 'd' : 0}


cpy = re.compile(r'cpy (\d+|[a-d]) (.)')
inc = re.compile(r'inc (.)')
dec = re.compile(r'dec (.)')
jump = re.compile(r'jnz (.) (-?\d+)')

i = 0
while i < len(instructions):
    line = instructions[i]
    print(line, registers)
    if jump.match(line):
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
        else:
            registers[dec.findall(line)[0]] -= 1
        i += 1

print(registers['a'])
