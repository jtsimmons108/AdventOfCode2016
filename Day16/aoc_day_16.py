from __future__ import print_function

def generate_data(a):
    b = a[::-1]
    b = b.replace('1', 'x').replace('0', '1').replace('x', '0')
    return a + '0' + b

def generate_checksum(data):
    result = ''
    for i in range(0, len(data), 2):
        if data[i] == data[i + 1]:
            result += '1'
        else:
            result += '0'
    return result

part1 = 272
part2 = 35651584
data = '10111011111001111'

while len(data) < part2:
    data = generate_data(data)

checksum = generate_checksum(data[:part2])
while len(checksum) % 2 == 0:
    checksum = generate_checksum(checksum)

print(checksum)
