#!/usr/bin/env python3
################################################################################
#   built_in_functions.py
#
#   <Executable Module Purpose>
#
#   21.07.2017  Created by:  rada
################################################################################

print('\nabs()')
print(abs(55))      # 55
print(abs(-409))    # 409
print(abs(0))       # 0

print('\nbool()')
print(bool(0))      # False
print(bool(None))   # False
print(bool(1))      # True
print(bool(-1))     # True
print(bool(36.6))   # True
print(bool('Rada')) # True
print(bool(True))   # True
print(bool(False))  # False

print('\neval()')
print(eval('5 * (23 - 3)'))

#calc = input('Введите математическую операцию: ')
#print(eval(calc))

print('\nexec()')
my_prog = '''
print('Hello!')
print('Goodbye!')
'''
exec(my_prog)

print('\nint()')
print(int(36.6))
print(int(2))

print('\nfloat()')
print(float(2))
print(float(-2))
print(float(2.60))

print('\nlen()')
print(len('abcdefg hi'))
print(len([1, 3, 5, 7]))
print(len({'ru': 'rub', 'us': '$'}))

print('\nmin / max')
numbs = [1, 45, -90, 3567, 3568, 0]
print(max(numbs))
print(min(numbs))

strings = ['abc', 'Abc', 'abC', 'ABC']
print(max(strings))
print(min(strings))

