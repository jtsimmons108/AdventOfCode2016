from __future__ import print_function


start_file = open('./aoc_day_18_input.txt')
row0 = start_file.read().strip()
cols = len(row0)
grid = [row0]
count = row0.count('.')

for r in range(1, 400000):
    new_row = []
    for c in range(cols):
        left = grid[r-1][c-1] if 0 <= c - 1 < cols else '.'
        right = grid[r-1][c+1] if 0 <= c + 1 < cols  else '.'
        ch = '.'
        if left != right:
            ch = '^'
        new_row.append(ch)
    new_row = ''.join(new_row)
    count += new_row.count('.')
    grid.append(new_row)



print(count)