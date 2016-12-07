from __future__ import print_function
import re

start_file = open('../res/aoc_day_7_input.txt')
instructions = start_file.read().strip().splitlines()


def get_aba_set(string):
    lst = set()
    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            lst.add(string[i:i+3])
    return lst


def make_bab(aba):
    return aba[1] + aba[0] + aba[1]


def contains_abba(string):
    for i in range(len(string)-3):
        if string[i] == string[i + 3] and string[i+1] == string[i+2] and string[i+0] != string[i+1]:
            return True
    return False

TLS = 0
SSL = 0


for line in instructions:
    hypernet = re.findall(r'\[\w+\]', line)
    supernet = re.split(r'\[\w+\]', line)

    #Part 1
    if any(map(contains_abba, supernet)) and not any(map(contains_abba, hypernet)):
        TLS += 1

    #Part 2
    abas = set()
    for part in supernet:
        abas |= get_aba_set(part)
    if len(filter(lambda x: any(make_bab(aba) in x for aba in abas), hypernet)) > 0:
        SSL += 1




print('Part one:', TLS)
print('Part two:', SSL)