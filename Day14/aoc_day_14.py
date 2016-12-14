from __future__ import print_function
from hashlib import md5
import re
import time

hashes = {}
found = []
has_three = re.compile(r'(.)\1\1')

part1 = False

def stretched_key(string):
    for i in range(2017):
        string = md5(string).hexdigest()
    return string

start_time = time.time()
start = 'ihaygndm'
i = 0
while len(found) < 64:
    if i not in hashes:
        hashes[i] = md5(start + str(i)).hexdigest() if part1 else stretched_key(start + str(i))
    hash_ = hashes[i]
    if has_three.search(hash_):
        letter = has_three.search(hash_).group(1)
        for j in range(1, 1001):
            if i + j not in hashes:
                hashes[i+j] = md5(start + str(i + j)).hexdigest() if part1 else stretched_key(start + str(i + j))
            hash_2 = hashes[i+j]
            if letter * 5 in hash_2:
                found.append(i)

    i += 1

print(time.time() - start_time)
print(len(hashes)*2017)
print(found[-1])