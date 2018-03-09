#!/usr/bin/env python3
################################################################################
#   strings.py
#
#   Python for Kids, Ch. 3: Strings
#
#   04.06.2017  Created by:  rada
#   05.06.2017  Update
#   06.06.2017  Update
################################################################################

# Single string

question = "How are you?"
print(question)

print("\n")
triple_single_quote_str = '''He said, "Aren't Can't Wouldn't"'''
print(triple_single_quote_str)

single_quote_str = 'He said, "Aren\'t Can\'t Wouldn\'t"'
print(single_quote_str)

double_quote_str = "He said, \"Aren't Can't Wouldn't\""
print(double_quote_str)

# Multiple strings
text = '''
Буря мглою небо кроет,
Вихри снежные крутя'''
print("\n")
print(text)

# Embended values in string
age = 9
print("\n")
print('Мне ' + str(age) + ' лет')
print('Мне', age, 'лет')
print('I am %s years old' % age)

name = 'Rada'
print('My name is %s. I am %s years old' % (name, age))

# Multiplying strings
print("\n")
print('2'*5, ' '*10, 'stop'*2)

print("\n")
for i in range(0,10):
    print(' '*i + '\\')
for i in range(9,-1,-1): 
    print(' '*i + '/')