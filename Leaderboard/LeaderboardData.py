from __future__ import print_function
import re


def average(lst):
    return sum(lst) / float(len(lst))
lead_entry = re.compile(r'(\d+)\)\s+Dec\s+\d+\s+\d{2}:\d{2}:\d{2}\s+(.+)')
global_entry = re.compile(r'\d+\)\s+\d+\s+(.+)')
global_leaderboard_info = [line.strip().replace(' (AoC++)', '') for line in open('./GlobalLeaderboard.txt').read().strip().splitlines()]
leaders = [global_entry.findall(person.replace(' (AoC++)', ''))[0] for person in global_leaderboard_info if global_entry.match(person)]

entries = {}
all = 0
for i in range(1, 23):
    inpt = [line.strip().replace(' (AoC++)', '') for line in open('./Day' + str(i) + 'Leaderboard.txt').read().strip().splitlines()]
    for person in inpt:
            if lead_entry.match(person):
                all += 1
                place, user = lead_entry.findall(person.replace(' (AoC++)', ''))[0]
                entries.setdefault(user, [])
                entries[user].append(int(place))

print(len(entries))
print(all)
people = sorted(entries.items(), key = lambda person: -len(filter(lambda num: num < 10, person[1])))

for i in range(len(people)):
    score = sum([101 - x for x in people[i][1]])
    #print(' '* (3 - len(str(i + 1))), i + 1, ': ', people[i][0], '\t', len(people[i][1]), '  score: ', score, '   average:  ', average(people[i][1]), sep = '')
    print(person[i][0], len(filter(lambda num: num < 10, person[i][1])))
print(filter(lambda x: x[0] in leaders, people ))
print(filter(lambda x: x[0] not in leaders, people ))
first_places = sorted(filter(lambda x: 1 in x[1], people), key = lambda x: -x[1].count(1))
print (len(first_places))
for person in first_places:
    print(person[0], person[1].count(1))
