#!/usr/bin/env python3
################################################################################
#   condition.py
#
#   <Executable Module Purpose>
#
#   14.07.2017  Created by:  rada
################################################################################
'''
answer = input('enter 2 numbers: ').split(' ')
print(answer)
a, b   = map(int, answer)
print(a, b)

if (a == b):
    print('=')

if (a != b):
    print(':(')


if (a < b):
    print('<')
elif (a > b):
    print('>')
else:
    print('=')
'''

age = int(input('enter age: '))

if (age < 7):
    print('детский сад')
elif (age >= 7 and age < 11):
    print('началка')
elif (age >= 11 and age < 15):
    print('среднечок')
elif (age >= 15 and age <= 17):
    print('старшина')
else:
    print('НЕТ ШКОЛЫ, УРА!!!!!!!!')
    
if (age < 7 or age > 17):
    print('НЕТ ШКОЛЫ, ХАХАХАХА!!!!!!!!')


