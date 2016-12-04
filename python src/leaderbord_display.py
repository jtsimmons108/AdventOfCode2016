from __future__ import print_function
import json, dateutil.parser

data = json.load(open('../res/leaderboard.json'))
print('Leaderboard for:', data['event'],'\n')
members = data['members']
for member, stars in sorted([(name, int(members[name]['stars'])) for name in members.keys()], key = lambda x: -x[1]):
    user = members[member]
    print(user['name'], ':', stars, '*')
    daily_info = members[member]['completion_day_level']
    for day in sorted(daily_info.keys()):
        part_one_time_string, part_two_time_string = '',''
        if '1' in daily_info[day].keys():
            part_one_time_string = dateutil.parser.parse(daily_info[day]['1']['get_star_ts']).strftime('%I:%M %p %m/%d/%y')
        if '2' in daily_info[day].keys():
            part_two_time_string = dateutil.parser.parse(daily_info[day]['2']['get_star_ts']).strftime('%I:%M %p %m/%d/%y')
        print('Day', day, ':  Part 1: ', part_one_time_string, '\tPart 2:', part_two_time_string)
    print('\n')


