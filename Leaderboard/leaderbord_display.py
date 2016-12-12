from __future__ import print_function
import json, dateutil.parser

data = json.load(open('./leaderboard.json'))
print('Leaderboard for:', data['event'],'\n')
members = data['members']
for member, stars, local_score in sorted([(name, int(members[name]['stars']), int(members[name]['local_score'])) for name in members.keys()], key = lambda x: (-x[1], -x[2])):
    user = members[member]
    print(user['name'], ':', stars, '*', '\t\tscore:', local_score)
    daily_info = members[member]['completion_day_level']
    for day in sorted(daily_info.keys(), key = lambda x: int(x)):
        part_one_time_string, part_two_time_string = '',''
        if '1' in daily_info[day].keys():
            part_one_time_string = dateutil.parser.parse(daily_info[day]['1']['get_star_ts']).strftime('%I:%M:%S %p %m/%d/%y')
        if '2' in daily_info[day].keys():
            part_two_time_string = dateutil.parser.parse(daily_info[day]['2']['get_star_ts']).strftime('%I:%M:%S %p %m/%d/%y')
        if len(day) == 1:
            day = '0' + day
        print('Day', day, ':  Part 1: ', part_one_time_string, '\tPart 2:', part_two_time_string)
    print('\n')


