from __future__ import print_function
import re


start_file = open('./aoc_day_12_input.txt')
instructions = start_file.read().strip().splitlines()

#Change c to 1 for part 2



cpy = re.compile(r'cpy (\d+|[a-d]) (.)')
inc = re.compile(r'inc (.)')
dec = re.compile(r'dec (.)')
jump = re.compile(r'jnz (.) (-?\d+)')

for c in [0, 1]:
    registers = {'a': 0, 'b': 0, 'c': c, 'd': 0}
    i = 0
    while i < len(instructions):
        line = instructions[i]
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
                if dec.match(instructions[i + 1]) and jump.match(instructions[i + 2]):
                    if dec.match(instructions[i + 3]) and jump.match(instructions[i+4]):
                        reg_one = inc.findall(line)[0]
                        reg_two = dec.findall(instructions[i + 1])[0]
                        reg_three = dec.findall(instructions[i + 3])[0]
                        registers[reg_one] += registers[reg_two] * registers[reg_three]
                        registers[reg_two] = 0
                        registers[reg_three] = 0
                        i += 5
                        continue
                    else:
                        reg_one = inc.findall(line)[0]
                        reg_two = dec.findall(instructions[i+1])[0]
                        registers[reg_one] += registers[reg_two]
                        registers[reg_two] = 0
                        i += 3
                        continue
                else:
                    registers[inc.findall(line)[0]] += 1
            else:
                registers[dec.findall(line)[0]] -= 1
            i += 1

    print('Part' + str(c+1) + ':', registers['a'])
