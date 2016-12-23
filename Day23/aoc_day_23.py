from __future__ import print_function
import itertools
import re
from collections import deque, Counter


start_file = open('./aoc_day_23_input.txt')
instructions = start_file.read().strip().splitlines()


#Change c to 1 for part 2
registers = {'a' : 12, 'b' : 0, 'c' : 1, 'd' : 0}


cpy = re.compile(r'cpy (-?\d+|[a-d]) (.)')
inc = re.compile(r'inc (.)')
dec = re.compile(r'dec (.)')
jump = re.compile(r'jnz (.) (.+)')
toggle = re.compile(r'tgl (.)')

i = 0
while i < len(instructions):
    line = instructions[i]
    if i == 4:
        registers['a'] += registers['b'] * registers['d']
        registers['c'] = 0
        registers['d'] = 0
        i = 10
    elif jump.match(line):
        reg, amt = jump.findall(line)[0]
        val = int(reg) if reg.isdigit() else registers[reg]
        amt = int(amt) if amt.isdigit() or amt[0] == '-' else registers[amt]
        delta = 1 if val == 0 else amt
        i += delta
    else:
        if cpy.match(line):
            val, reg = cpy.findall(line)[0]
            if not reg.isdigit():
                registers[reg] = int(val) if val.isdigit() or val[0] == '-' else registers[val]
        elif toggle.match(line):
            amt = toggle.findall(line)[0]
            if amt.isdigit():
                amt = int(amt)
            else:
                amt = registers[amt]
            if i + amt < len(instructions):
                past_instruct = instructions[i + amt]
                info = past_instruct.split()
                if len(info) == 2:
                    instructions[i + amt] = ('dec' if info[0] == 'inc' else 'inc') + ' ' + info[1]
                elif len(info) == 3:
                    instructions[i + amt] = ('cpy' if info[0] == 'jnz' else 'jnz') + ' ' + info[1] + ' ' + info[2]
        elif inc.match(line):
            registers[inc.findall(line)[0]] += 1
        elif dec.match(line):
            registers[dec.findall(line)[0]] -= 1
        else:
            print('this shouldn\'t happen', line)
        i += 1

print(registers['a'])
