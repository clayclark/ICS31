#
#
#Part 1
#
#
print('\n')
print('----------- Part 1 -----------')
print()

def abbreviate(m: str) -> str:
    ''' Return first 3 numbers of argument'''
    return m[0:3]
assert abbreviate('January') == 'Jan'
assert abbreviate('May') == 'May'

#
#
#Part 2
#
#
print('\n')
print('----------- Part 2 -----------')
print()

def find_area_square(l: int) -> int:
    ''' Return area using length'''
    return l**2
assert find_area_square(4) == 16
assert find_area_square(5) == 25

