from __future__ import print_function

num = 1364
target_x, target_y = 31, 39
moves = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def get_value(x, y):
    if bin((x*x + 3 * x + 2 * x * y + y + y * y) + num)[2:].count('1') % 2 == 0:
        return '.'

    return '#'


values = [['']*40 for _ in range(45)]

for r in range(len(values)):
    for c in range(len(values[0])):
        values[r][c] = get_value(c, r)

values[target_y][target_x] = 'X'


def is_valid(x, y):
    return y in range(len(values)) and x in range(len(values[0])) and values[y][x] in '.X'


def find_path(x, y, seen, part1):
    seen.append((x, y))
    visited.add((x,y))
    if part1 and (x, y) == (target_x, target_y):
        distances.append(len(seen) - 1)
    if part1 and (len(distances) == 0 or len(seen) < min(distances)) or len(seen) <= 50 and not part1:
        for dx, dy in moves:
            if is_valid(x + dx, y + dy) and (x + dx, y + dy) not in seen:
                find_path(x + dx, y + dy, seen[::], part1)

for part1 in [True, False]:
    start_x, start_y = (1, 1)
    distances = []
    visited = set()
    find_path(start_x, start_y, [], part1)
    if part1:
        print('Part 1:', min(distances))
    else:
        print('Part 2:', len(visited))



