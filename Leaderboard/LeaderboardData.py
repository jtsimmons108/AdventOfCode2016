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
for i in range(1, 26):
    inpt = [line.strip().replace(' (AoC++)', '') for line in open('./Day' + str(i) + 'Leaderboard.txt').read().strip().splitlines()]
    part1_users = []
    part2_users = []
    part1 = True
    for person in inpt:
            if lead_entry.match(person):
                all += 1
                place, user = lead_entry.findall(person.replace(' (AoC++)', ''))[0]
                entries.setdefault(user, [])
                entries[user].append(int(place))
    #             if part1:
    #                 part1_users.append(user)
    #             else:
    #                 part2_users.append(user)
    #         else:
    #             part1 = False
    # star_one_only = [user for user in part1_users if user not in part2_users]
    # star_two_only = [user for user in part2_users if user not in part1_users]
    # star_both = [user for user in part1_users if user in part2_users]
    # day_string = str(i) if i >= 10 else ' ' + str(i)
    # print('Day', day_string, 'Star 1 only:', len(star_one_only), '\tBoth Stars:', len(star_both), '\tNumber of people on leaderboard:', len(entries))

print(len(entries))
print(all)
people = sorted(entries.items(), key = lambda person: -sum([101 - x for x in person[1]]))
for i in range(len(people)):
    print(("" + str(i + 1)).center(5, ' '), (people[i][0].strip()).center(25, ' '), '' +  str(sum([101 - x for x in people[i][1]])).center(7, ' ') + '\n')


