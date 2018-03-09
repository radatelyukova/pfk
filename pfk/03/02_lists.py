#!/usr/bin/env python3
################################################################################
#   lists.py
#
#   Python for Kids, Ch. 3: Lists
#
#   06.06.2017  Created by:  rada
################################################################################

# List of numbers

numbs = [2, -33, 4, 26, 100, -7, 3, 30]
#index:  0    1  2   3    4   5  6   7
print(len(numbs))

print(numbs)
print(numbs[2])
print(numbs[2:5]) # i=5 is excluded
print(numbs[-1])
print(numbs[-1:-4]) # nothing

# List of strings

greetings = ['Hello', 'Привет', 'hi', 'здорова']
print('\n')
print(greetings[-1])
print(greetings)

# Concatenation

mix = numbs + greetings
print(mix)
print(mix[6:10])

new = [numbs, greetings]
print('\n')
print(new)
print(len(new))
print(new[0])
print(new[0][1])

more_numbs = [103, -9, 22]
print(more_numbs)

numbs.append(more_numbs)
print(numbs)
print(numbs[-1][1])

del numbs[3]
print(numbs)

list1 = [1,2,3]
list2 = ['Rada','Evgeny']
list3 = list1 + list2
print(list3)
print(list1 * 3)
print(list2 * 3)

season1 = ['a1',  'a2',  'a3',  'a4']
season2 = ['b1',  'b2',  'b3',  'b4']
season3 = ['c1',  'c2',  'c3',  'c4']
serial  = [season1, season2, season3]
print('\n')
print(serial)
print(serial[1][2])
