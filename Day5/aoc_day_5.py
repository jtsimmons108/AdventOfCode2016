from __future__ import print_function
from hashlib import md5

pass_ = 'cxdnnyjw'
result = ''
i = 10**6
letters = ['_']*8
while '_' in letters:
    hash_ = md5(pass_+str(i)).hexdigest()
    if hash_[0:5] == '00000':
        #Part One
        if len(result) < 8:
            result += hash_[5]
        #Part Two
        if hash_[5] in '01234567' and letters[int(hash_[5])] == '_':
            letters[int(hash_[5])] = hash_[6]
            print(''.join(letters))

    i += 1
print('Part one: ', result)
print('Part two: ', ''.join(letters))

