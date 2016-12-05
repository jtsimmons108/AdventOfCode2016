from __future__ import print_function
import md5

pass_ = 'cxdnnyjw'
result = ''
i = 10**6
letters = []
while len(letters) < 8:
    hash_ = md5.new(pass_+str(i)).hexdigest()
    if hash_[0:5] == '00000':
        #Part One
        if len(result) < 8:
            result += hash_[5]
        #Part Two
        if hash_[5] in '01234567' and hash_[5] not in [x[0] for x in letters]:
            letters += [(hash_[5], hash_[6])]
    i += 1
print('Part one: ', result)
print('Part two: ', ''.join([ch for pl, ch in sorted(letters, key=lambda x: x[0])]))
