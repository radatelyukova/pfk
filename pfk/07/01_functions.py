#!/usr/bin/env python3
################################################################################
#   01_functions.py
#
#   <Executable Module Purpose>
#
#   18.07.2017  Created by:  rada
################################################################################

def show_name(name):
    print("hello %s" % name)

show_name('Renesma')
show_name('Evgeny')

def full_name(first_name, last_name):
    print("hello %s %s" % (first_name, last_name))

full_name('Rada', 'Telyukova')

f_name = 'Evgeny'
l_name = 'Telyukov'
full_name(f_name, l_name )

def my_sum(x, y):
    return x + y

result = my_sum(17, 50)
print('\n')
print(result)
print(my_sum(17, 12))

if (result > 0):
    print('LOL')

def new_sum(x, y):
    print(x + y)

new_sum(4,39)

def my_mult(a, b):
    print('my_mult: a = %i' % a)
    return a * b 

def my_sub(x, y):
    return x - y

print('\n')
print(my_sub(10, 30))

def my_div(w, q):
    if(q == 0):
        return "Ты Вася"
    return w / q

print('\n')
print(my_div(45, 3))
print(my_div(45, 33))
print(my_div(45, 33.0))
print(my_div(45, 0))


a = 100
print('\nScope')
print('main: a = %i' % a)
print(my_mult(10, 2))
print('main again: a = %i' % a)

# Error
#def my_mult(a, b):
#    return a * x
#print(my_mult(10, 43))